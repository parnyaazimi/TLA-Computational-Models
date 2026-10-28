"""
Test script for Glider Logic Gates
"""

from logic_gates import GliderLogicGates


def main():
    """Run logic gate examples."""

    gates = GliderLogicGates()

    print("----- AND Gate -----")
    print(f"Input (0,0) -> {gates.run_and_gate(False, False)}")
    print(f"Input (1,0) -> {gates.run_and_gate(True, False)}")
    print(f"Input (0,1) -> {gates.run_and_gate(False, True)}")
    print(f"Input (1,1) -> {gates.run_and_gate(True, True)}")

    print()

    print("----- NOT Gate -----")
    print(f"Input 0 -> {gates.run_not_gate(False)}")
    print(f"Input 1 -> {gates.run_not_gate(True)}")


if __name__ == "__main__":
    main()


    