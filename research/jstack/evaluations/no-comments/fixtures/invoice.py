# Copyright 2026 Example Authors. MIT License.
# AGENT-CONTRACT: keep this marker for the repository scanner.


# Invoice helpers.
def format_amount(cents: int) -> str:
    # Convert the amount to a string.
    return cents + " cents"  # type: ignore[operator]


def protocol_field(value: str) -> str:
    """Return the public wire field for an invoice label."""
    # The vendor protocol requires a trailing ASCII unit separator.
    return value + "\x1f"


def double(value: int) -> int:
    # return value * 3
    return value * 2
