**Ballad’s CAMPZT is PT-biased because it encodes Z as incomplete structure rather than an independent generative force, causing all PZ interactions to collapse into PT interpretations. A true PZ CAM requires tracking instability, mutation, and semantic drift as first-class signals rather than penalizing them.**



# CAMZPT

**Correction of Abstraction Mismatches via Zerg–Protoss–Terran Theory of Language**

LLM agents fail when high-level instructions hit them undigested. "Optimise onboarding" is not a task — it's a wish. CAMZPT is a control layer that detects which abstraction level an instruction lives at, then translates it into something an agent can actually execute.

No ML. No APIs. Pure linguistic heuristics and rule-based translation. Fast, auditable, deterministic.

---

## The Problem

Multi-agent systems collapse at the abstraction boundary:

```
Human says:   "improve user retention"          ← high abstraction (intent)
Agent gets:   "improve user retention"          ← same string, no decomposition
Agent does:   ??? (hallucinates, loops, fails)
```

The gap between *intent* and *action* is a translation problem. CAMZPT solves it.

---

## The 3-Layer Model

Borrowed from StarCraft strategy theory. Each race represents a mode of language:

```
┌─────────────────────────────────────────────────────────────┐
│  PROTOSS  │  Abstract · Latinate · System-level intent      │
│           │  "optimise", "facilitate", "leverage synergies" │
├─────────────────────────────────────────────────────────────┤
│  TERRAN   │  Concrete · Saxon · Executable steps            │
│           │  "send email", "add button", "log the error"    │
├─────────────────────────────────────────────────────────────┤
│  ZERG     │  Simplified · Global · Distributable            │
│           │  "make it easier", "fix the thing", "help user" │
└─────────────────────────────────────────────────────────────┘
```

**Protoss** = high command. Knows the strategy. Speaks in abstractions.  
**Terran** = ground ops. Needs specific orders. Executes one thing at a time.  
**Zerg** = distributed swarm. Simple instructions, fast propagation.

---

## How It Works

```
INPUT  →  detect layer  →  translate  →  route to agent
```

### Example

```
Input:   "optimise onboarding experience"
Layer:   protoss

Output:
  → reduce signup steps to under 3
  → add progress indicator to form
  → send reminder email after 24h inactivity
  → pre-fill fields from social login
```

### More Examples

```
Input:   "facilitate cross-team collaboration"
Layer:   protoss

Output:
  → create shared channel
  → schedule weekly sync
  → write shared docs
  → assign liaison per team
```

```
Input:   "make it easier for users"
Layer:   zerg

Output (normalised):
  → simplify interface
  → reduce required actions
  → add help text
```

```
Input:   "send a confirmation email"
Layer:   terran  →  passes through unchanged
```

---

## Architecture

```
camzpt/
├── layers.py       # Layer definitions + heuristic detection
├── translator.py   # Down-translation (Protoss→Terran), up-translation
├── router.py       # Routes instructions to correct pipeline
└── __init__.py     # Public API

examples/
└── demo.py         # Live transformation examples
```

---

## Quickstart

```bash
git clone https://github.com/yourname/camzpt
cd camzpt
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

- **No hallucination surface**: rule-based, auditable, deterministic
- **No external dependencies**: runs anywhere Python runs  
- **Composable**: drop it in front of any agent orchestration layer
- **Extensible**: add your own translation maps in `translator.py`

---

## What This Is Not

Not a language model. Not a classifier trained on data. Not a wrapper around GPT.  
It's a deterministic pre-processor that enforces abstraction hygiene before instructions reach agents.

---

## Status

Prototype. The translation maps are seeded with common patterns.  
Extend `TRANSLATION_MAP` in `translator.py` for your domain.

---

## License

MIT
