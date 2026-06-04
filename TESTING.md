# Testing this repo with Lumovra (no coding needed)

This is a normal little software project. To test Lumovra you make **one small change
at a time** in the GitHub browser editor — each change creates a Pull Request, and
Lumovra should turn it into a **Finding**.

## One-time setup
1. **Fork** this repo into your own GitHub account (button **"Fork"** top right → **"Create fork"**).
2. In **Lumovra**, connect GitHub and bind your fork to your `Hiring Agent` system.

## How to make a change (same steps every time)
1. Open the file in **your fork** on GitHub.
2. Click the **pencil ✏️ ("Edit this file")**.
3. Make the change described below.
4. Bottom of the page: **"Commit changes…"** → **"Create a new branch … and start a pull request"** → **"Propose changes"** → **"Create pull request"**.
5. Switch to **Lumovra** and watch the Finding appear.

## Which change produces which finding

| Test | Open this file | Do this | Expected finding |
|------|----------------|---------|------------------|
| **D1** | `prompts/hiring_agent.prompt.md` | change any sentence (e.g. add a word) | Prompt change (high) |
| **D2** | `config/model_config.yaml` | change a number (e.g. `temperature: 0.2` → `0.7`) | Model config change (high) |
| **D3** | `eval/metrics.py` | change any line slightly | Evaluation change (medium) |
| **D4** | `src/hiring_agent/oversight.py` | **delete** the line marked `<-- Test D4` | Oversight control removed (high) |
| **D5** | `src/hiring_agent/audit.py` | **delete** the line marked `<-- Test D5` | Logging/trace removed (high) |
| **D6** _(optional)_ | `training/pipeline.py` | change any line | Training pipeline change (high) |

> Do **one** test per Pull Request so it's clear which change caused which finding.
> Don't edit `lumovra.yaml` — that's the file that tells Lumovra which code belongs
> to the Hiring Agent.

Full context (what to look for in each step) is in the test plan Tom shared with you.
