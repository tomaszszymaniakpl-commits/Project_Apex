"""
Context Loader - loads world bible files and builds context for LLM prompts.

Usage:
    from context_loader import ContextLoader
    
    loader = ContextLoader()
    context = loader.load_all()                    # all files
    context = loader.load_by_folder("characters")  # specific folder
    context = loader.load_files(["nick_wilde_voice.md", "zpd.md"])  # specific files
"""

import os
import glob
from pathlib import Path
from typing import Optional

import frontmatter
import yaml


# Project root = parent of tools/
PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_PATH = PROJECT_ROOT / "tools" / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class ContextLoader:
    def __init__(self, config: Optional[dict] = None):
        self.config = config or load_config()
        self.bible_path = PROJECT_ROOT / self.config["paths"]["world_bible"]
        self.prompts_path = PROJECT_ROOT / self.config["paths"]["prompts"]

    def _read_md_file(self, filepath: Path) -> dict:
        """Read a markdown file, parse frontmatter if present."""
        try:
            post = frontmatter.load(str(filepath))
            return {
                "path": str(filepath.relative_to(PROJECT_ROOT)),
                "metadata": dict(post.metadata) if post.metadata else {},
                "content": post.content,
                "filename": filepath.name,
            }
        except Exception as e:
            # Fallback: read as plain text
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            return {
                "path": str(filepath.relative_to(PROJECT_ROOT)),
                "metadata": {},
                "content": content,
                "filename": filepath.name,
            }

    def list_files(self) -> list[dict]:
        """List all .md files in world_bible with metadata."""
        files = []
        for md_file in sorted(self.bible_path.rglob("*.md")):
            info = self._read_md_file(md_file)
            files.append({
                "path": info["path"],
                "filename": info["filename"],
                "metadata": info["metadata"],
                "size": len(info["content"]),
            })
        return files

    def load_all(self) -> str:
        """Load all world bible files into a single context string."""
        return self._build_context(self.bible_path.rglob("*.md"))

    def load_by_folder(self, folder: str) -> str:
        """Load all .md files from a specific subfolder."""
        folder_path = self.bible_path / folder
        if not folder_path.exists():
            return f"[Folder not found: {folder}]"
        return self._build_context(folder_path.rglob("*.md"))

    def load_files(self, filenames: list[str]) -> str:
        """Load specific files by name (searches recursively)."""
        all_files = list(self.bible_path.rglob("*.md"))
        matched = []
        for fn in filenames:
            for f in all_files:
                if fn.lower() in f.name.lower():
                    matched.append(f)
                    break
        return self._build_context(matched)

    def load_by_type(self, file_type: str) -> str:
        """Load files filtered by YAML frontmatter 'type' field."""
        matched = []
        for md_file in self.bible_path.rglob("*.md"):
            info = self._read_md_file(md_file)
            if info["metadata"].get("type") == file_type:
                matched.append(md_file)
        return self._build_context(matched)

    def _build_context(self, files) -> str:
        """Build a formatted context string from file list."""
        parts = []
        for filepath in sorted(files):
            if isinstance(filepath, str):
                filepath = Path(filepath)
            info = self._read_md_file(filepath)
            header = f"=== {info['path']} ==="
            parts.append(f"{header}\n{info['content']}\n")
        return "\n".join(parts)

    def load_prompt(self, prompt_name: str) -> str:
        """Load a system prompt from prompts/ folder."""
        prompt_file = self.prompts_path / f"{prompt_name}.md"
        if not prompt_file.exists():
            return f"[Prompt not found: {prompt_name}]"
        with open(prompt_file, "r", encoding="utf-8") as f:
            return f.read()

    def get_context_stats(self) -> dict:
        """Get stats about loaded context (for token budgeting)."""
        total_chars = 0
        file_count = 0
        for md_file in self.bible_path.rglob("*.md"):
            info = self._read_md_file(md_file)
            total_chars += len(info["content"])
            file_count += 1
        # Rough token estimate: ~4 chars per token for English
        return {
            "files": file_count,
            "total_chars": total_chars,
            "estimated_tokens": total_chars // 4,
        }


if __name__ == "__main__":
    # Quick test
    loader = ContextLoader()
    stats = loader.get_context_stats()
    print(f"World Bible: {stats['files']} files, ~{stats['estimated_tokens']} tokens")
    print("\nFiles:")
    for f in loader.list_files():
        print(f"  {f['path']} ({f['size']} chars)")
