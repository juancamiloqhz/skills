"""Independent public-contract checks; pass the generated project directory."""
import importlib.util
from pathlib import Path
import sys
import unittest

project = Path(sys.argv.pop(1))
spec = importlib.util.spec_from_file_location("evaluated_reservations", project / "reservations.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class ReservationContract(unittest.TestCase):
    def setUp(self):
        self.book = module.ReservationBook()

    def test_overlap_and_half_open_boundaries(self):
        self.book.reserve("room", 10, 20)
        for start, end in [(10, 20), (11, 19), (0, 30), (5, 11), (19, 21)]:
            with self.subTest(start=start, end=end):
                self.assertFalse(self.book.available("room", start, end))
                with self.assertRaises(ValueError):
                    self.book.reserve("room", start, end)
        self.book.reserve("room", 0, 10)
        self.book.reserve("room", 20, 30)
        self.assertTrue(self.book.available("other", 10, 20))
        self.book.reserve("other", 10, 20)

    def test_cancel_is_once_and_releases_only_its_reservation(self):
        first = self.book.reserve("room", 1, 3)
        second = self.book.reserve("room", 3, 5)
        self.assertFalse(self.book.cancel("unknown"))
        self.assertIs(self.book.cancel(first), True)
        self.assertIs(self.book.cancel(first), False)
        self.assertTrue(self.book.available("room", 1, 3))
        self.assertFalse(self.book.available("room", 3, 5))
        self.assertIs(self.book.cancel(second), True)

    def test_ids_are_strings_and_never_reused_within_book(self):
        seen = set()
        for _ in range(50):
            identifier = self.book.reserve("room", 0, 1)
            self.assertIsInstance(identifier, str)
            self.assertNotIn(identifier, seen)
            seen.add(identifier)
            self.assertTrue(self.book.cancel(identifier))

    def test_invalid_operations_do_not_change_existing_state(self):
        held = self.book.reserve("room", -10, -2)
        for resource, start, end in [("", 1, 2), ("room", 2, 2), ("room", 3, 2)]:
            for method in [self.book.reserve, self.book.available]:
                with self.subTest(method=method.__name__, values=(resource, start, end)):
                    with self.assertRaises(ValueError):
                        method(resource, start, end)
        self.assertFalse(self.book.available("room", -8, -3))
        self.assertTrue(self.book.available("room", -2, 0))
        self.assertTrue(self.book.cancel(held))
        self.assertTrue(self.book.available("room", -10, -2))

    def test_queries_do_not_reserve(self):
        for _ in range(3):
            self.assertIs(self.book.available("room", -100, 100), True)
        identifier = self.book.reserve("room", -100, 100)
        for _ in range(3):
            self.assertIs(self.book.available("room", 0, 1), False)
        self.assertTrue(self.book.cancel(identifier))
        self.assertTrue(self.book.available("room", 0, 1))

    def test_books_have_independent_state(self):
        other = module.ReservationBook()
        self.book.reserve("room", 1, 2)
        self.assertTrue(other.available("room", 1, 2))
        other.reserve("room", 1, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
