import copy
import random
import unittest

from reservations import ReservationBook


class ReservationTests(unittest.TestCase):
    def test_overlap_shapes_and_adjacency(self):
        book = ReservationBook()
        original = book.reserve("r", 0, 10)
        for start, end in [(0, 10), (2, 3), (-1, 11), (-1, 1), (9, 11)]:
            with self.subTest(start=start, end=end):
                self.assertFalse(book.available("r", start, end))
                with self.assertRaises(ValueError):
                    book.reserve("r", start, end)
        self.assertTrue(book.available("r", -2, 0))
        self.assertTrue(book.available("r", 10, 12))
        book.reserve("r", -2, 0)
        book.reserve("r", 10, 12)
        book.reserve("s", 0, 10)
        self.assertTrue(book.cancel(original))
        self.assertTrue(book.available("r", 0, 10))

    def test_invalid_and_query_calls_do_not_mutate(self):
        for occupied in (False, True):
            book = ReservationBook()
            if occupied:
                book.reserve("r", -5, 5)
            before = copy.deepcopy(vars(book))
            serial = ReservationBook._next_id
            for args in [("", 0, 1), ("r", 2, 2), ("r", 3, 2)]:
                for operation in (book.reserve, book.available):
                    with self.assertRaises(ValueError):
                        operation(*args)
                    self.assertEqual(vars(book), before)
                    self.assertEqual(ReservationBook._next_id, serial)
            for _ in range(3):
                self.assertTrue(book.available("new", -10, -9))
                book.available("r", -1, 1)
            self.assertFalse(book.cancel("never-issued"))
            if occupied:
                with self.assertRaises(ValueError):
                    book.reserve("r", -1, 1)
            self.assertEqual(vars(book), before)
            self.assertEqual(ReservationBook._next_id, serial)

    def test_cancellation_and_nonreuse(self):
        book = ReservationBook()
        seen = set()
        for _ in range(100):
            rid = book.reserve("r", -2, -1)
            self.assertIsInstance(rid, str)
            self.assertNotIn(rid, seen)
            seen.add(rid)
            self.assertTrue(book.cancel(rid))
            self.assertFalse(book.cancel(rid))
            self.assertTrue(book.available("r", -2, -1))
        replacement = book.reserve("r", -2, -1)
        self.assertNotIn(replacement, seen)
        for rid in seen:
            self.assertFalse(book.cancel(rid))
        self.assertFalse(book.available("r", -2, -1))

    def test_books_are_independent_and_ids_distinct(self):
        a, b = ReservationBook(), ReservationBook()
        aid = a.reserve("r", 0, 1)
        bid = b.reserve("r", 0, 1)
        self.assertNotEqual(aid, bid)
        self.assertFalse(a.cancel(bid))
        self.assertFalse(b.cancel(aid))
        self.assertTrue(a.cancel(aid))
        self.assertFalse(b.available("r", 0, 1))

    def test_large_negative_endpoints_and_literal_resources(self):
        book = ReservationBook()
        start = -(10 ** 100)
        book.reserve(" ", start, start + 1)
        self.assertTrue(book.available(" ", start + 1, 10 ** 100))
        book.reserve("R", start, 0)
        book.reserve("r", start, 0)

    def test_seeded_operation_sequences_against_discrete_oracle(self):
        rng = random.Random(491)
        book = ReservationBook()
        live = {}
        issued = []
        for _ in range(2000):
            operation = rng.choice(("reserve", "available", "cancel"))
            if operation == "cancel":
                rid = rng.choice(issued + ["unknown"])
                self.assertEqual(book.cancel(rid), rid in live)
                live.pop(rid, None)
                continue
            resource = rng.choice(("a", "b", "c"))
            start = rng.randrange(-10, 10)
            end = rng.randrange(start + 1, 12)
            cells = set(range(start, end))
            conflict = any(resource == r and bool(cells & occupied)
                           for r, occupied in live.values())
            if operation == "available":
                self.assertEqual(book.available(resource, start, end), not conflict)
            elif conflict:
                with self.assertRaises(ValueError):
                    book.reserve(resource, start, end)
            else:
                rid = book.reserve(resource, start, end)
                self.assertNotIn(rid, issued)
                issued.append(rid)
                live[rid] = (resource, cells)
        for rid in live:
            self.assertTrue(book.cancel(rid))
        for resource in ("a", "b", "c"):
            self.assertTrue(book.available(resource, -20, 20))


if __name__ == "__main__":
    unittest.main()
