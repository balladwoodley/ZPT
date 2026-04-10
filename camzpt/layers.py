"""
camzpt/layers.py

Layer definitions and heuristic detection.

Three abstraction layers:
  - protoss: high-abstraction, Latinate, intent-level language
  - terran:  low-abstraction, Saxon, executable action language
  - zerg:    simplified, global, distributable language
"""

from dataclasses import dataclass
from enum import Enum
import re


class Layer(str, Enum):
    PROTOSS = "protoss"
    TERRAN = "terran"
    ZERG = "zerg"


@dataclass
class LayerResult:
    layer: Layer
    confidence: float
    signals: list[str]


# Latinate suffixes that indicate abstraction
LATINATE_SUFFIXES = (
    "tion", "sion", "ise", "ize", "ment", "ance", "ence",
    "ity", "ous", "ive", "ify", "ate", "ual", "ial",
)

# Concrete Saxon action verbs — clear Terran signals
TERRAN_VERBS = {
    "send", "write", "add", "remove", "fix", "log", "get", "set",
    "run", "build", "test", "check", "call", "open", "close",
    "click", "load", "save", "delete", "create", "update", "show",
    "hide", "read", "push", "pull", "post", "fetch", "render",
    "print", "move", "copy", "clear", "reset", "start", "stop",
}

# High-abstraction Protoss keywords
PROTOSS_KEYWORDS = {
    "optimise", "optimize", "facilitate", "leverage", "synergise",
    "synergize", "enhance", "streamline", "maximise", "maximize",
    "minimise", "minimize", "consolidate", "strategise", "strategize",
    "implement", "develop", "establish", "utilise", "utilize",
    "orchestrate", "coordinate", "align", "prioritise", "prioritize",
    "transform", "revolutionise", "revolutionize", "operationalise",
    "operationalize", "conceptualise", "conceptualize",
}

# Zerg signals: simplified, often informal or broad directives
ZERG_INDICATORS = {
    "make", "help", "easier", "better", "faster", "simpler", "nicer",
    "cleaner", "good", "bad", "fix", "improve", "thing", "stuff",
    "get", "give", "let", "more", "less",
}


def detect_layer(text: str) -> LayerResult:
    """
    Detect the abstraction layer of an instruction.

    Returns a LayerResult with the detected layer, a confidence score,
    and the signals that drove the classification.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    signals = []
    scores = {Layer.PROTOSS: 0.0, Layer.TERRAN: 0.0, Layer.ZERG: 0.0}

    for word in words:
        # Latinate suffix check → Protoss signal
        if any(word.endswith(suffix) for suffix in LATINATE_SUFFIXES) and len(word) > 6:
            scores[Layer.PROTOSS] += 1.5
            signals.append(f"latinate suffix: '{word}'")

        # Explicit Protoss keywords
        if word in PROTOSS_KEYWORDS:
            scores[Layer.PROTOSS] += 3.0
            signals.append(f"protoss keyword: '{word}'")

        # Concrete action verb → Terran signal
        if word in TERRAN_VERBS:
            scores[Layer.TERRAN] += 2.0
            signals.append(f"terran verb: '{word}'")

        # Zerg signal
        if word in ZERG_INDICATORS:
            scores[Layer.ZERG] += 1.0
            signals.append(f"zerg indicator: '{word}'")

    # Long average word length → Protoss lean
    if words:
        avg_len = sum(len(w) for w in words) / len(words)
        if avg_len > 6.5:
            scores[Layer.PROTOSS] += 1.0
            signals.append(f"high avg word length: {avg_len:.1f}")
        elif avg_len < 4.5:
            scores[Layer.ZERG] += 0.5
            signals.append(f"low avg word length: {avg_len:.1f}")

    # Determine winner
    if max(scores.values()) == 0:
        # Default: if nothing fires, it reads as Terran (literal instruction)
        return LayerResult(layer=Layer.TERRAN, confidence=0.5, signals=["no strong signals — defaulting to terran"])

    winner = max(scores, key=lambda k: scores[k])
    total = sum(scores.values())
    confidence = scores[winner] / total if total > 0 else 0.5

    return LayerResult(layer=winner, confidence=round(confidence, 2), signals=signals)
