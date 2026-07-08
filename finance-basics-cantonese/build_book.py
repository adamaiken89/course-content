"""Regenerate book.md by concatenating each module's lesson.md + rendered quiz.yaml.

Module order = sorted modules/ subdirectory names. book.md contains no front
matter, no cloze.yaml, and no cumulative quizzes — just the 28 module sections.
"""
from pathlib import Path

import yaml

COURSE = Path(__file__).resolve().parent
LETTERS = "abcd"


def render_quiz(quiz_path: Path) -> str:
    items = yaml.safe_load(quiz_path.read_text())
    parts = []
    for q in items:
        lines = [f"### {q['question']}", ""]
        for letter in LETTERS:
            if letter not in q.get("options", {}):
                continue
            mark = "✓" if letter == q["answer"] else " "
            lines.append(f"[{mark}] {letter}: {q['options'][letter]}")
            lines.append("")
        lines.append("")
        lines.append(f"**Answer:** {q['answer']}")
        lines.append("")
        lines.append(q["explanation"])
        parts.append("\n".join(lines))
    return "\n\n\n".join(parts)


def main():
    sections = []
    for mod_dir in sorted((COURSE / "modules").iterdir()):
        if not mod_dir.is_dir():
            continue
        lesson = (mod_dir / "lesson.md").read_text().rstrip("\n")
        quiz_md = render_quiz(mod_dir / "quiz.yaml")
        sections.append(f"{lesson}\n\n---\n\n## Quiz: {mod_dir.name}\n\n\n{quiz_md}")
    (COURSE / "book.md").write_text("\n\n\n---\n\n\n".join(sections) + "\n")


if __name__ == "__main__":
    main()
