"""
camzpt/router.py

Routes an instruction through the correct pipeline based on its layer.

  protoss → down_translate → terran task list
  terran  → pass through (already executable)
  zerg    → normalise → cleaner task list
"""

from __future__ import annotations
from dataclasses import dataclass, field

from .layers import Layer, LayerResult, detect_layer
from .translator import down_translate, up_translate, normalise_zerg


@dataclass
class RouteResult:
    input: str
    layer: Layer
    confidence: float
    signals: list[str]
    tasks: list[str]
    summary: str = ""

    def __str__(self) -> str:
        lines = [
            f'INPUT:      "{self.input}"',
            f"LAYER:      {self.layer.value}  (confidence: {self.confidence:.0%})",
            "",
            "OUTPUT:",
        ]
        for task in self.tasks:
            lines.append(f"  → {task}")
        if self.summary:
            lines.append(f"\nSUMMARY:    {self.summary}")
        return "\n".join(lines)


def route(text: str) -> RouteResult:
    """
    Detect the layer of an instruction and route it to the correct translator.

    Returns a RouteResult with the detected layer and translated task list.
    """
    detection: LayerResult = detect_layer(text)
    layer = detection.layer
    tasks: list[str] = []
    summary: str = ""

    if layer == Layer.PROTOSS:
        # High abstraction → break down into executable tasks
        tasks = down_translate(text)
        summary = text  # The protoss text IS the summary

    elif layer == Layer.TERRAN:
        # Already concrete → pass through as single task
        tasks = [text]
        summary = up_translate(text)

    elif layer == Layer.ZERG:
        # Simplified → normalise into cleaner task list
        tasks = normalise_zerg(text)
        summary = f"normalised: {text}"

    return RouteResult(
        input=text,
        layer=layer,
        confidence=detection.confidence,
        signals=detection.signals,
        tasks=tasks,
        summary=summary,
    )
