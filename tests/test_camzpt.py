"""
tests/test_camzpt.py

Basic tests. Run: pytest
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from camzpt import process, detect
from camzpt.layers import Layer


def test_detect_protoss():
    result = detect("optimise onboarding experience")
    assert result.layer == Layer.PROTOSS

def test_detect_terran():
    result = detect("send a confirmation email")
    assert result.layer == Layer.TERRAN

def test_detect_zerg():
    result = detect("make it easier")
    assert result.layer == Layer.ZERG

def test_protoss_produces_tasks():
    result = process("optimise onboarding experience")
    assert result.layer == Layer.PROTOSS
    assert len(result.tasks) >= 2
    assert all(isinstance(t, str) for t in result.tasks)

def test_terran_passes_through():
    result = process("send a confirmation email")
    assert result.layer == Layer.TERRAN
    assert result.tasks[0] == "send a confirmation email"

def test_zerg_normalises():
    result = process("make it easier for users")
    assert result.layer == Layer.ZERG
    assert len(result.tasks) >= 1

def test_unknown_instruction_fallback():
    result = process("optimise the blorglewump")
    assert result.layer == Layer.PROTOSS
    assert len(result.tasks) >= 1
