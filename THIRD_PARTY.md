# Third-party material

Each copied file keeps its original license. Full license texts are in `licenses/`.

## From blader/humanizer (MIT, Copyright (c) 2025 Siqi Chen)

Source: https://github.com/blader/humanizer, commit `8c307f367c91bd974002f10f2be2965d642c13df` (2026-10-16), skill version 3.1.0. License: `licenses/humanizer.LICENSE`.

- `skills/humanizer/references/patterns.md`: sections A to F (patterns §1 to §26) and the source note, copied unchanged under a new header.
- `skills/humanizer/SKILL.md`: rewritten as a short core around humanizer's method, voice rule, return modes, "When not to act" section and a condensed pattern index. Changes:
  - Voice section now puts a writing sample first, then the reetish-voice-content skill, then another writer's brand guide, then text type.
  - "You may add a reaction where the writer would" removed; replaced with "never add an opinion, reaction or stance the writer did not express".
  - File mode keeps the original (git or a `.orig` copy) before overwriting.
  - Added a check-only mode, drafting from scratch, and the optional checker.
  - Description widened to cover drafting as well as editing.
- The upstream README's benchmark claim ("16 out of 16") is not repeated here.

## From ItsssssJack/SlopMonster (MIT, Copyright (c) 2026 Jack Roberts)

Source: https://github.com/ItsssssJack/SlopMonster, commit `3fc9787d9337b57c599a80afbefbbb3be5a8eb0b` (2026-09-26). License: `licenses/slopmonster.LICENSE`.

- `skills/humanizer/tools/deslop.py`: advisory by default (weighted per-match density, exit 0; `--strict` for CI) instead of a 5-point score that failed below 5; skips short double-quoted phrases (`--keep-quotes` to score them); three-item lists weigh 0.5; `--voice NAME` loads `voice-NAME-phrases.txt` and flags every em dash; `.txt` files read as prose; curly double quotes normalised.
- `skills/humanizer/tools/test_deslop.py`: two CLI tests now pass `--strict` and check the new output line; added tests for the new behaviour.
- Not included: `tools/cleanse.sh` (sends drafts to another vendor's model), `SKILL.md`, `references/`, `prompts/`, `examples/`, `docs/`.

## Original to this repo

- `skills/humanizer/references/voice-reetish.md`: copy of Reetish's own reetish-voice-content skill (fallback when that skill is not loaded).
- `skills/humanizer/tools/voice-reetish-phrases.txt`, `scripts/sync_voice.py`, `scripts/build_zips.py`.
