"""
camzpt/translator.py

Translation logic between abstraction layers.

Down-translation: Protoss → Terran (abstract intent → executable tasks)
Up-translation:   Terran  → Protoss (concrete steps → abstract summary)
Normalise:        Zerg    → Terran  (vague directive → cleaner instruction)
"""

from __future__ import annotations
import re
from typing import Optional


# ─────────────────────────────────────────────
# PRIMARY TRANSLATION MAP
# key:   abstract Protoss phrase / keyword
# value: list of concrete Terran tasks
# ─────────────────────────────────────────────

TRANSLATION_MAP: dict[str, list[str]] = {
    # Onboarding / UX
    "optimise onboarding":          ["reduce signup steps to under 3",
                                     "add progress indicator to form",
                                     "send reminder email after 24h inactivity",
                                     "pre-fill fields from social login"],
    "improve onboarding":           ["reduce signup steps",
                                     "add progress bar",
                                     "send welcome email on signup"],
    "optimise onboarding experience": ["reduce signup steps to under 3",
                                       "add progress indicator to form",
                                       "send reminder email after 24h inactivity",
                                       "pre-fill fields from social login"],

    # Retention / engagement
    "improve user retention":       ["add re-engagement email sequence",
                                     "add in-app nudges for inactive users",
                                     "surface key features on dashboard",
                                     "track churn signals in analytics"],
    "increase engagement":          ["add notification triggers",
                                     "personalise homepage content",
                                     "run A/B test on CTA copy"],

    # Collaboration
    "facilitate collaboration":     ["create shared channel",
                                     "schedule weekly sync",
                                     "write shared docs",
                                     "assign liaison per team"],
    "facilitate cross-team collaboration": ["create shared Slack channel",
                                            "schedule bi-weekly cross-team sync",
                                            "set up shared documentation space",
                                            "assign a liaison from each team"],
    "improve team communication":   ["set up shared channel",
                                     "document decisions in shared notes",
                                     "send weekly status update"],

    # Performance
    "optimise performance":         ["profile slow queries",
                                     "add caching layer",
                                     "lazy load non-critical assets",
                                     "compress static files"],
    "improve performance":          ["run performance audit",
                                     "cache frequent requests",
                                     "minify JS and CSS"],
    "enhance system performance":   ["profile bottlenecks",
                                     "add Redis caching",
                                     "optimise database indexes",
                                     "enable CDN for static assets"],

    # Checkout / conversion
    "optimise checkout flow":       ["reduce checkout steps",
                                     "add guest checkout option",
                                     "pre-fill saved addresses",
                                     "add progress indicator"],
    "improve conversion":           ["simplify form fields",
                                     "add social proof near CTA",
                                     "run A/B test on headline"],

    # Generic high-abstraction verbs (fallback patterns)
    "optimise":                     ["identify bottleneck",
                                     "measure current state",
                                     "reduce unnecessary steps",
                                     "test and iterate"],
    "facilitate":                   ["help", "enable action", "remove blocker"],
    "leverage":                     ["use", "apply", "activate"],
    "streamline":                   ["remove unnecessary steps",
                                     "automate repetitive tasks",
                                     "simplify the process"],
    "maximise":                     ["increase to maximum",
                                     "remove constraints",
                                     "measure and push limit"],
    "enhance":                      ["improve quality",
                                     "add missing feature",
                                     "fix rough edges"],
    "consolidate":                  ["merge duplicates",
                                     "centralise into one place",
                                     "remove redundancy"],
    "transform":                    ["define target state",
                                     "map current to target",
                                     "migrate in stages"],
    "develop strategy":             ["define goal",
                                     "list constraints",
                                     "identify options",
                                     "pick best path",
                                     "write action plan"],
}


# ─────────────────────────────────────────────
# UP-TRANSLATION MAP (Terran → Protoss summary)
# ─────────────────────────────────────────────

UP_TRANSLATION_MAP: dict[str, str] = {
    "send email":             "facilitate communication",
    "add button":             "enhance interface",
    "fix bug":                "improve system reliability",
    "write tests":            "ensure quality assurance",
    "update database":        "maintain data integrity",
    "add caching":            "optimise performance",
    "reduce steps":           "streamline user journey",
    "create docs":            "establish knowledge base",
    "schedule meeting":       "coordinate team alignment",
    "log error":              "implement error monitoring",
}


# ─────────────────────────────────────────────
# ZERG NORMALISATION MAP
# ─────────────────────────────────────────────

ZERG_NORMALISE_MAP: dict[str, list[str]] = {
    "make it easier":         ["simplify interface",
                               "reduce required actions",
                               "add help text"],
    "fix the thing":          ["identify broken component",
                               "reproduce the issue",
                               "apply fix",
                               "verify and deploy"],
    "help users":             ["add onboarding guide",
                               "add tooltip hints",
                               "create FAQ page"],
    "make it better":         ["run user feedback survey",
                               "identify top complaints",
                               "prioritise and fix top 3"],
    "make it faster":         ["profile current speed",
                               "remove bottleneck",
                               "measure improvement"],
    "make it simpler":        ["remove unnecessary fields",
                               "reduce menu depth",
                               "use plain language in UI"],
}


def down_translate(text: str) -> list[str]:
    """
    Translate an abstract (Protoss) instruction into concrete (Terran) tasks.

    Tries exact match first, then partial match on key phrases,
    then word-level fallback on known abstract verbs.
    """
    normalised = text.lower().strip().rstrip(".")

    # 1. Exact match
    if normalised in TRANSLATION_MAP:
        return TRANSLATION_MAP[normalised]

    # 2. Partial match — find longest key that appears in the input
    best_match: Optional[str] = None
    best_len = 0
    for key in TRANSLATION_MAP:
        if key in normalised and len(key) > best_len:
            best_match = key
            best_len = len(key)

    if best_match:
        return TRANSLATION_MAP[best_match]

    # 3. Word-level fallback — find any abstract verb in the text
    words = re.findall(r"\b\w+\b", normalised)
    for word in words:
        if word in TRANSLATION_MAP:
            return TRANSLATION_MAP[word]

    # 4. Generic fallback
    return [
        f"define what '{text}' means concretely",
        "identify measurable outcome",
        "list 3 specific actions to achieve it",
        "assign owner and deadline",
    ]


def up_translate(text: str) -> str:
    """
    Translate a concrete (Terran) instruction into an abstract (Protoss) summary.
    """
    normalised = text.lower().strip()

    for key, abstract in UP_TRANSLATION_MAP.items():
        if key in normalised:
            return abstract

    # Generic up-translation
    words = normalised.split()
    if words:
        return f"enhance {' '.join(words[-2:])}"
    return "improve system capability"


def normalise_zerg(text: str) -> list[str]:
    """
    Normalise a vague Zerg directive into cleaner Terran tasks.
    """
    normalised = text.lower().strip().rstrip(".")

    # Exact match
    if normalised in ZERG_NORMALISE_MAP:
        return ZERG_NORMALISE_MAP[normalised]

    # Partial match
    for key, tasks in ZERG_NORMALISE_MAP.items():
        if key in normalised:
            return tasks

    # Fallback: pass through with minimal clean-up
    return [f"clarify: '{text}'", "define specific action", "assign to owner"]
