# 🧠 CAMZPT — Correction of Abstraction Mismatches

Control layer for multi-agent systems that translates high-level instructions into executable tasks.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![No ML](https://img.shields.io/badge/No-ML-brightgreen)
![Deterministic](https://img.shields.io/badge/Deterministic-100%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## What It Does

Multi-agent systems collapse when high-level instructions hit them undigested. "Optimise onboarding" is not a task — it's a wish.

**CAMZPT** detects which abstraction level an instruction lives at, then translates it down into concrete, executable steps that agents can actually do.

No ML. No APIs. Pure linguistic heuristics and rule-based translation. **Fast, auditable, deterministic.**

---

## The Problem

```
Human says:   "improve user retention"          ← high abstraction (intent)
Agent gets:   "improve user retention"          ← same string, no decomposition
Agent does:   ??? (hallucinates, loops, fails)
```

The gap between *intent* and *action* is a translation problem. CAMZPT solves it.

---

## The 3-Layer Model

Borrowed from **StarCraft strategy theory**. Each layer represents a mode of language:

| Layer | Style | Examples |
|-------|-------|----------|
| **Protoss** | Abstract · Latinate · System-level intent | "optimise", "facilitate", "leverage synergies" |
| **Terran** | Concrete · Saxon · Executable steps | "send email", "add button", "log the error" |
| **Zerg** | Simplified · Global · Distributable | "make it easier", "fix the thing", "help user" |

- **Protoss** = high command. Knows the strategy. Speaks in abstractions.
- **Terran** = ground ops. Needs specific orders. Executes one thing at a time.
- **Zerg** = distributed swarm. Simple instructions, fast propagation.

---

## Example

**Input:** "optimise onboarding experience"  
**Layer Detected:** protoss

**Output:**
- reduce signup steps to under 3
- add progress indicator to form
- send reminder email after 24h inactivity
- pre-fill fields from social login

---

## Architecture

```
camzpt/
├── layers.py       # Layer definitions + heuristic detection
├── translator.py   # Down-translation (Protoss→Terran)
├── router.py       # Routes instructions to correct pipeline
└── __init__.py     # Public API

examples/
└── demo.py         # Live transformation examples
```

---

## Quickstart

```bash
git clone https://github.com/balladwoodley/ZPT
cd ZPT
pip install -r requirements.txt

python examples/demo.py
```

Or use the CLI:

```bash
python -m camzpt "optimise the checkout flow"
```

---

## Python API

```python
from camzpt import process

result = process("optimise onboarding experience")
print(result.layer)    # 'protoss'
print(result.tasks)    # ['reduce signup steps', 'add progress bar', ...]
```

---

## Design Principles

- **No hallucination surface** — rule-based, auditable, deterministic
- **No external dependencies** — runs anywhere Python runs
- **Composable** — drop it in front of any agent orchestration layer
- **Extensible** — add your own translation maps in `translator.py`

---

## What This Is NOT

❌ Not a language model  
❌ Not a classifier trained on data  
❌ Not a wrapper around GPT

✅ A deterministic pre-processor that enforces abstraction hygiene before instructions reach agents.

---

## Status

**Prototype.** Translation maps are seeded with common patterns. Extend `TRANSLATION_MAP` in `translator.py` for your domain.

---

## Contributing

Bug reports and pull requests welcome. For major changes, open an issue first.

---

## License

MIT