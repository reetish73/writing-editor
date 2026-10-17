"""Refresh skills/humanizer/references/voice-reetish.md from the reetish-voice-content skill.

Usage: python scripts/sync_voice.py <path to reetish-voice-content/SKILL.md>
Run it after editing the voice skill, then commit. Update tools/voice-reetish-phrases.txt
by hand if the banned-phrase list changed.
"""
import pathlib
import sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
body = text.split("---", 2)[2].lstrip() if text.startswith("---") else text
head = ("<!-- Copy of the reetish-voice-content skill, used when that skill is not loaded.\n"
        "     Source of truth: the reetish-voice-content skill in Claude. When you change it, copy the\n"
        "     new text here too (python scripts/sync_voice.py <path-to-SKILL.md>). -->\n\n")
out = pathlib.Path(__file__).resolve().parent.parent / "skills/humanizer/references/voice-reetish.md"
out.write_text(head + body, encoding="utf-8", newline="\n")
print(f"updated {out} ({len(body.split())} words)")
