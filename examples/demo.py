"""
examples/demo.py

Live transformation examples showing CAMZPT in action.

Run: python examples/demo.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from camzpt import process

DIVIDER = "─" * 52

EXAMPLES = [
    # Protoss → Terran
    "optimise onboarding experience",
    "facilitate cross-team collaboration",
    "enhance system performance",
    "develop strategy for user retention",
    "streamline the checkout flow",

    # Terran → passes through
    "send a confirmation email",
    "add progress bar to signup form",

    # Zerg → normalise
    "make it easier for users",
    "make it faster",
]


def run_demo():
    print()
    print("CAMZPT — Abstraction Layer Translator")
    print("Correction of Abstraction Mismatches via Zerg–Protoss–Terran Theory")
    print(DIVIDER)

    for instruction in EXAMPLES:
        result = process(instruction)
        print()
        print(result)
        print(DIVIDER)

    print()
    print("Done. Extend TRANSLATION_MAP in camzpt/translator.py for your domain.")
    print()


if __name__ == "__main__":
    run_demo()
