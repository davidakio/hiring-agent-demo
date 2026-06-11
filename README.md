# Hiring Agent

An AI assistant that screens job applications: it summarizes each candidate's CV,
scores their fit for a role, and ranks candidates. High-impact decisions (such as
auto-rejections) pass through a **human-oversight gate**, and every decision is written
to an **audit log** with a trace id.  

Is this just a readme file that will still generate a recording?  I will commit the changes...

## Architecture

```
src/hiring_agent/
  api.py         FastAPI service — POST /screen
  llm.py         builds the prompt + calls the model
  config.py      loads config/model_config.yaml
  oversight.py   human-in-the-loop approval gate
  audit.py       decision audit log (trace ids)
prompts/         the system prompt(s)
config/          model + inference configuration
eval/            offline evaluation (precision@k, recall@k)
training/        fine-tuning pipeline
tests/           unit tests
```

## Run locally

```bash
pip install -e ".[dev]"
export OPENAI_API_KEY=sk-...
uvicorn hiring_agent.api:app --reload   # http://localhost:8000/screen
pytest
```

## Governance

This repository is governed by **Lumovra** (see `lumovra.yaml`). AI-relevant changes
in pull requests — prompts, model configuration, evaluation, training, and the
oversight/audit code — are detected automatically and tracked as evidence.

> **Testers:** follow [`TESTING.md`](./TESTING.md) — it tells you exactly which file
> to change to produce each type of finding, all from the GitHub browser (no coding).
