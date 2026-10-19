# writing-editor

Write and edit prose without AI tells, in your own voice. Private plugin, installed through [reetish-marketplace](https://github.com/nofomojustfafo/reetish-marketplace).

## What's inside

One skill, `humanizer`, that fires when you draft or edit posts, captions, scripts, emails, DMs, proposals, web copy or docs, or ask to "humanize", "de-slop" or check a draft.

- **Voice first.** A writing sample in the chat wins. For your own content it uses the `reetish-voice-content` skill (or the copy in `references/voice-reetish.md`), whose rules override the generic patterns. For a client or brand it uses their sample or guide, never your voice.
- **26 patterns**, strongest first, from humanizer. A short index loads on every use; the full rules and examples in `references/patterns.md` load only for long texts, file edits or unclear cases.
- **Never invents** facts, stories, credentials, outcomes or opinions.
- **File edits keep the original** (git, or a `.orig` copy).
- **Optional checker** `tools/deslop.py` lists AI tells with a weighted density. It's advisory: it reports, it doesn't block.

## Install and update (Claude Code)

```bash
claude plugin marketplace add nofomojustfafo/reetish-marketplace
claude plugin install writing-editor@reetish-marketplace
```

After pushing changes:

```bash
claude plugin marketplace update
claude plugin update writing-editor@reetish-marketplace
```

## Claude Desktop

Every push to `main` that touches `skills/` builds `humanizer.zip` (GitHub > Actions > skill-zips > Artifacts). Upload it in Settings > Capabilities > Skills. In chat, the checker runs only if code execution is on; the skill works without it.

## Checker

```bash
python skills/humanizer/tools/deslop.py draft.md
python skills/humanizer/tools/deslop.py --text "copy to check"
python skills/humanizer/tools/deslop.py post.txt --voice reetish
python skills/humanizer/tools/test_deslop.py
```

Options: `--voice NAME`, `--keep-quotes`, `--allow-proof`, `--strict` (exit 1 on any flag, for CI).

To add a voice for another writer or brand, create `skills/humanizer/tools/voice-<name>-phrases.txt` (one phrase per line) and pass `--voice <name>`.

## When your voice skill changes

The `reetish-voice-content` skill in Claude is the source of truth. After editing it, save its `SKILL.md` locally and run:

```bash
python scripts/sync_voice.py path/to/reetish-voice-content/SKILL.md
```

Update `tools/voice-reetish-phrases.txt` by hand if the banned-phrase list changed, bump the version in `.claude-plugin/plugin.json`, commit and push.

`references/voice-reetish.md` holds your positioning notes. Keep this repo private.
