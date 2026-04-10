"""
camzpt/__main__.py

CLI interface: python -m camzpt "your instruction here"
"""

import sys
from . import process


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m camzpt \"your instruction here\"")
        print("Example: python -m camzpt \"optimise onboarding experience\"")
        sys.exit(1)

    instruction = " ".join(sys.argv[1:])
    result = process(instruction)
    print()
    print(result)
    print()


if __name__ == "__main__":
    main()
