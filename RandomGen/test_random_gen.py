from collections import Counter
from unittest import TestCase

from RandomGen.random_number_generator import RandomGen
from RandomGen.exceptions import NotProbMassFuncException


class TestRandomGen(TestCase):
    def setUp(self):
        self.random_num = [-1, 0, 1, 2, 3]
        self.probs = [0.01, 0.3, 0.58, 0.1, 0.01]
        self.random_gen = RandomGen(self.random_num, self.probs)

    def test_validation(self):
        with self.assertRaises(NotProbMassFuncException):
            self.random_gen.reinit(
                [
                    1,
                ],
                [0.1, 0.3],
            )

        with self.assertRaises(NotProbMassFuncException):
            self.random_gen.reinit(
                [
                    1,
                ],
                [0.5, 0.5],
            )

    def test_random_gen(self):
        t = self.random_gen.next_num()
        self.assertIn(t, self.random_num)

    def test_cumulative_probs(self):
        accumulated = list(self.random_gen.get_cumulative_probs())
        expected = [0.01, 0.31, 0.89, 0.99, 1.00]
        self.assertEqual(accumulated, expected)

    def test_counter(self):
        counter = Counter[int]()
        for i in self.random_gen:
            counter[i] += 1
        c = self.random_gen.counter
        for num in self.random_num:
            self.assertEqual(counter[num], c[num])

    def test_refresh(self):
        self.random_gen.resize(1000000)
        self.assertEqual(self.random_gen._observation_size, 1000000)

    def test_reinit(self):
        self.random_gen.reinit(
            [
                1,
            ],
            [
                1,
            ],
        )
        self.assertEqual(
            self.random_gen._random_nums,
            [
                1,
            ],
        )
        self.assertEqual(
            self.random_gen._probabilities,
            [
                1,
            ],
        )

    def test_big_input(self):
        self.random_gen.resize(1000000)
        counter = Counter[int]()
        for i in self.random_gen:
            counter[i] += 1
        self.assertEqual(sum(counter.values()), 1000000)
        pmf = self.random_gen.pmf
        for expected, (_, calculated) in zip(self.probs, sorted(pmf.items())):
            self.assertAlmostEqual(expected, calculated, 2)
