"""In-memory half-open resource reservations, without concurrency support."""

__all__ = ["ReservationBook"]


class ReservationBook:
    """Own live bookings; issued IDs are never reused during module lifetime."""

    _next_id = 0

    def __init__(self) -> None:
        self._live: dict[str, tuple[str, int, int]] = {}

    @staticmethod
    def _validate(resource: str, start: int, end: int) -> None:
        if resource == "" or end <= start:
            raise ValueError("resource must be nonempty and start must precede end")

    def _conflicts(self, resource: str, start: int, end: int) -> bool:
        return any(
            resource == existing_resource and start < existing_end and existing_start < end
            for existing_resource, existing_start, existing_end in self._live.values()
        )

    def reserve(self, resource: str, start: int, end: int) -> str:
        """Reserve [start, end), raising ValueError for invalid input or overlap."""
        self._validate(resource, start, end)
        if self._conflicts(resource, start, end):
            raise ValueError("reservation overlaps an existing booking")
        reservation_id = str(ReservationBook._next_id)
        next_id = ReservationBook._next_id + 1
        self._live[reservation_id] = (resource, start, end)
        ReservationBook._next_id = next_id
        return reservation_id

    def available(self, resource: str, start: int, end: int) -> bool:
        """Report whether a valid interval is free, without changing any state."""
        self._validate(resource, start, end)
        return not self._conflicts(resource, start, end)

    def cancel(self, id: str) -> bool:
        """Remove a live booking, returning False for unknown or cancelled IDs."""
        return self._live.pop(id, None) is not None
