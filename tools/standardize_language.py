"""
Language Standardizer - scans world bible .md files and fixes mixed PL/EN to pure English.

Usage:
    python tools/standardize_language.py --scan               # scan only, show issues
    python tools/standardize_language.py --fix                 # fix all files (with confirmation)
    python tools/standardize_language.py --fix --file zpd.md   # fix specific file
    python tools/standardize_language.py --dry-run             # show fixes without applying
"""

import argparse
import sys
from pathlib import Path

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.syntax import Syntax

sys.path.insert(0, str(Path(__file__).parent))
from context_loader import ContextLoader, load_config


console = Console(force_terminal=True)

# Common Polish words/phrases that indicate mixed language
POLISH_MARKERS = [
    "może", "jest", "nie", "tak", "lub", "oraz", "ale", "dla", "jako",
    "który", "która", "które", "których", "którzy",
    "może", "mogą", "będzie", "można", "powinien",
    "wymaga", "potrzebuje", "zawiera", "używa",
    "nowe", "nowy", "nowa", "nowych",
    "wszystkie", "wszystko", "każdy", "każda",
    "bardzo", "tylko", "jeszcze", "już", "teraz",
    "między", "przez", "przed", "po", "do", "od",
    "opis", "uwaga", "uwagi", "notatka", "notatki",
    "zmiana", "zmiany", "aktualizacja",
    "dochodzić", "odłożone", "późniejszego",
]

# Words to SKIP (proper nouns, code, etc.)
SKIP_PATTERNS = ["---", "```", "||", "STATUS_TRACKER", "YAML"]


def scan_file_for_polish(filepath: Path) -> list[dict]:
    """Scan a file for lines containing Polish words."""
    issues = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    in_frontmatter = False
    in_code_block = False
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Track frontmatter
        if stripped == "---":
            in_frontmatter = not in_frontmatter
            continue
        # Track code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
            
        # Check for Polish markers
        lower_line = line.lower()
        found_markers = []
        for marker in POLISH_MARKERS:
            # Check as whole word (with word boundaries)
            import re
            if re.search(rf'\b{re.escape(marker)}\b', lower_line):
                found_markers.append(marker)
        
        if found_markers:
            issues.append({
                "line": i,
                "text": stripped,
                "markers": found_markers,
            })
    
    return issues


def fix_file_with_llm(filepath: Path, config: dict) -> str:
    """Send file to LLM for language standardization."""
    model = config["models"]["light"]["name"]
    
    # Load the standardizer prompt
    loader = ContextLoader(config)
    system_prompt = loader.load_prompt("standardizer")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Standardize this document to English:\n\n{content}"},
        ],
    )
    
    return response["message"]["content"]


def main():
    parser = argparse.ArgumentParser(description="Standardize world bible language to English")
    parser.add_argument("--scan", action="store_true", help="Scan files and report issues")
    parser.add_argument("--fix", action="store_true", help="Fix files using LLM")
    parser.add_argument("--dry-run", action="store_true", help="Show fixes without applying")
    parser.add_argument("--file", type=str, help="Target specific file (by name)")
    args = parser.parse_args()
    
    if not args.scan and not args.fix:
        args.scan = True  # default to scan
    
    config = load_config()
    loader = ContextLoader(config)
    bible_path = Path(__file__).parent.parent / config["paths"]["world_bible"]
    
    # Get files to process
    if args.file:
        files = [f for f in bible_path.rglob("*.md") if args.file.lower() in f.name.lower()]
        if not files:
            console.print(f"[red]File not found: {args.file}[/red]")
            return
    else:
        files = sorted(bible_path.rglob("*.md"))
    
    if args.scan:
        console.print(Panel("[bold]Language Scan - Polish markers in English documents[/bold]", border_style="yellow"))
        total_issues = 0
        
        for filepath in files:
            rel_path = filepath.relative_to(Path(__file__).parent.parent)
            issues = scan_file_for_polish(filepath)
            
            if issues:
                console.print(f"\n[bold red]{rel_path}[/bold red] - {len(issues)} lines with Polish")
                for issue in issues[:5]:  # show max 5 per file
                    markers_str = ", ".join(issue["markers"][:3])
                    safe_text = issue['text'][:80].encode('ascii', 'replace').decode('ascii')
                    console.print(f"  L{issue['line']}: [dim]{safe_text}[/dim]")
                    console.print(f"         markers: [yellow]{markers_str}[/yellow]")
                if len(issues) > 5:
                    console.print(f"  ... and {len(issues) - 5} more lines")
                total_issues += len(issues)
            else:
                console.print(f"[green]{rel_path}[/green] - OK")
        
        console.print(f"\n[bold]Total: {total_issues} lines with Polish markers across {len(files)} files[/bold]")
    
    if args.fix:
        console.print(Panel("[bold]Language Fix - Standardizing to English via LLM[/bold]", border_style="blue"))
        model = config["models"]["light"]["name"]
        console.print(f"[dim]Using model: {model}[/dim]\n")
        
        for filepath in files:
            rel_path = filepath.relative_to(Path(__file__).parent.parent)
            issues = scan_file_for_polish(filepath)
            
            if not issues:
                console.print(f"[green]{rel_path}[/green] - already clean, skipping")
                continue
            
            console.print(f"\n[yellow]{rel_path}[/yellow] - {len(issues)} issues found")
            
            if not args.dry_run:
                if not Confirm.ask(f"  Fix {rel_path}?"):
                    continue
            
            console.print("  [dim]Processing with LLM...[/dim]")
            try:
                fixed_content = fix_file_with_llm(filepath, config)
                
                if args.dry_run:
                    console.print(Panel(fixed_content[:500] + "...", title=f"Preview: {rel_path}"))
                else:
                    # Backup original
                    backup_path = filepath.with_suffix(".md.bak")
                    filepath.rename(backup_path)
                    
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(fixed_content)
                    
                    console.print(f"  [green]Fixed! Backup: {backup_path.name}[/green]")
                    
            except Exception as e:
                console.print(f"  [red]Error: {e}[/red]")


if __name__ == "__main__":
    main()
