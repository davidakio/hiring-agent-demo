# Hiring Agent — Lumovra Demo Repo

This is a **demo repository** for testing Lumovra. It pretends to be the codebase of a
"Hiring Agent" — an AI that pre-sorts job applications. You don't need to understand the
code. You only make tiny text changes in the browser to see Lumovra detect them.

## What you'll do (no coding!)

1. **Fork** this repo into your own GitHub account (button "Fork" top right → "Create fork").
2. In **Lumovra**, connect GitHub and bind your fork to your `Hiring Agent` system.
3. Make a small change to one of the files below **in the GitHub browser editor**:
   - Open the file → click the **pencil ✏️ ("Edit this file")**
   - Change the text as instructed
   - Bottom: **"Commit changes…"** → **"Create a new branch … and start a pull request"** → **"Propose changes"** → **"Create pull request"**
4. Switch back to **Lumovra** and watch a **Finding** appear.

## Which file to change for which test

| Test | File | Change to make | What Lumovra should detect |
|------|------|----------------|----------------------------|
| D1 | `prompts/hiring_agent.prompt.md` | change any sentence | Prompt change (high) |
| D2 | `config/model_config.yaml` | change a number (e.g. `temperature`) | Model config change (high) |
| D3 | `eval/metrics.py` | change any line slightly | Evaluation change (medium) |
| D4 | `src/oversight.py` | **delete** the line marked `<-- DELETE THIS LINE` | Oversight control removed (high) |
| D5 | `src/audit.py` | **delete** the line marked `<-- DELETE THIS LINE` | Logging/trace removed (high) |

The full step-by-step is in the test plan Tom shared with you (Sets C–D).

> `lumovra.yaml` in this repo tells Lumovra which files belong to the `Hiring Agent`
> system. Don't edit it — just leave it as is.
