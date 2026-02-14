"""
Brainstorm Tool - interactive brainstorming with Ollama + world bible context.

Usage:
    python tools/brainstorm.py                      # interactive mode, load all context
    python tools/brainstorm.py --folder characters   # load only characters
    python tools/brainstorm.py --light               # use phi3.5 instead of writer-32k
    python tools/brainstorm.py --no-context          # no world bible, just chat
    python tools/brainstorm.py --save                # save conversation to output/
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import ollama
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from context_loader import ContextLoader, load_config


console = Console()


def get_model(config: dict, light: bool = False) -> str:
    if light:
        return config["models"]["light"]["name"]
    return config["models"]["heavy"]["name"]


def build_system_prompt(loader: ContextLoader, context: str) -> str:
    """Build system prompt with brainstorm instructions + world bible context."""
    base_prompt = loader.load_prompt("brainstorm")
    if context:
        return f"{base_prompt}\n\n--- WORLD BIBLE CONTEXT ---\n\n{context}"
    return base_prompt


def save_conversation(messages: list[dict], output_dir: Path):
    """Save conversation history to a timestamped file."""
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = output_dir / f"brainstorm_{timestamp}.md"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Brainstorm Session - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        for msg in messages:
            if msg["role"] == "system":
                continue
            role = "**USER:**" if msg["role"] == "user" else "**ASSISTANT:**"
            f.write(f"{role}\n{msg['content']}\n\n---\n\n")
    
    console.print(f"\n[green]Saved to {filepath}[/green]")


def interactive_chat(model: str, system_prompt: str, save: bool = False):
    """Run interactive chat loop with Ollama."""
    messages = [{"role": "system", "content": system_prompt}]
    
    console.print(Panel(
        f"[bold]Brainstorm Mode[/bold]\n"
        f"Model: [cyan]{model}[/cyan]\n"
        f"Commands: [yellow]/quit[/yellow] [yellow]/save[/yellow] [yellow]/clear[/yellow] [yellow]/context[/yellow]",
        title="Creative Brainstorm",
        border_style="blue",
    ))
    
    output_dir = Path(__file__).parent.parent / "output"
    
    while True:
        try:
            user_input = Prompt.ask("\n[bold green]You[/bold green]")
        except (KeyboardInterrupt, EOFError):
            break
        
        if not user_input.strip():
            continue
            
        # Commands
        if user_input.strip().startswith("/"):
            cmd = user_input.strip().lower()
            if cmd == "/quit":
                if save:
                    save_conversation(messages, output_dir)
                break
            elif cmd == "/save":
                save_conversation(messages, output_dir)
                continue
            elif cmd == "/clear":
                messages = [messages[0]]  # keep system prompt
                console.print("[yellow]Conversation cleared.[/yellow]")
                continue
            elif cmd == "/context":
                # Show how much context is loaded
                sys_len = len(messages[0]["content"])
                console.print(f"[dim]System prompt: {sys_len} chars (~{sys_len // 4} tokens)[/dim]")
                continue
        
        messages.append({"role": "user", "content": user_input})
        
        # Stream response
        console.print("\n[bold blue]Assistant[/bold blue]")
        try:
            full_response = ""
            stream = ollama.chat(model=model, messages=messages, stream=True)
            for chunk in stream:
                token = chunk["message"]["content"]
                console.print(token, end="")
                full_response += token
            console.print()  # newline after stream
            
            messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            console.print(f"\n[red]Error: {e}[/red]")
            console.print("[dim]Is Ollama running? Try: ollama serve[/dim]")
            messages.pop()  # remove failed user message


def main():
    parser = argparse.ArgumentParser(description="Brainstorm with Ollama + World Bible")
    parser.add_argument("--folder", type=str, help="Load only specific world_bible subfolder")
    parser.add_argument("--files", nargs="+", help="Load specific files by name")
    parser.add_argument("--light", action="store_true", help="Use lighter model (phi3.5)")
    parser.add_argument("--no-context", action="store_true", help="Skip world bible context")
    parser.add_argument("--save", action="store_true", help="Auto-save conversation on exit")
    args = parser.parse_args()
    
    config = load_config()
    loader = ContextLoader(config)
    model = get_model(config, light=args.light)
    
    # Load context
    if args.no_context:
        context = ""
        console.print("[dim]No world bible context loaded.[/dim]")
    elif args.folder:
        context = loader.load_by_folder(args.folder)
        console.print(f"[dim]Loaded context from: {args.folder}/[/dim]")
    elif args.files:
        context = loader.load_files(args.files)
        console.print(f"[dim]Loaded files: {', '.join(args.files)}[/dim]")
    else:
        # Default: load core context (characters + organizations + canon)
        # Skip style/locations to save tokens
        parts = []
        for folder in ["characters", "organizations", "canon"]:
            parts.append(loader.load_by_folder(folder))
        context = "\n".join(parts)
        console.print("[dim]Loaded: characters + organizations + canon[/dim]")
    
    stats = loader.get_context_stats()
    console.print(f"[dim]Bible: {stats['files']} files, ~{stats['estimated_tokens']} tokens total[/dim]")
    
    system_prompt = build_system_prompt(loader, context)
    interactive_chat(model, system_prompt, save=args.save)


if __name__ == "__main__":
    main()
