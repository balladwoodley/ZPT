"""
camzpt — Correction of Abstraction Mismatches via Zerg–Protoss–Terran Theory

Public API:

    from camzpt import process, detect, translate_down, translate_up

    result = process("optimise onboarding experience")
    print(result.layer)   # 'protoss'
    print(result.tasks)   # ['reduce signup steps', ...]
"""

from .layers import Layer, LayerResult, detect_layer
from .translator import down_translate, up_translate, normalise_zerg
from .router import RouteResult, route


def process(text: str) -> RouteResult:
    """Main entry point. Detect layer, translate, return structured result."""
    return route(text)


def detect(text: str) -> LayerResult:
    """Detect the abstraction layer of a text without translating."""
    return detect_layer(text)


def translate_down(text: str) -> list[str]:
    """Translate abstract instruction to concrete task list."""
    return down_translate(text)


def translate_up(text: str) -> str:
    """Translate concrete instruction to abstract summary."""
    return up_translate(text)


__all__ = [
    "process",
    "detect",
    "translate_down",
    "translate_up",
    "Layer",
    "LayerResult",
    "RouteResult",
    "route",
    "down_translate",
    "up_translate",
    "normalise_zerg",
]

__version__ = "0.1.0"
