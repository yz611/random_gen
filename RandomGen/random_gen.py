import random
from abc import abstractmethod
from collections import Counter
from itertools import accumulate
from RandomGen.exceptions import NotProbMassFuncException

__all__ = ["RandomGenBase", "RandomGen"]


class RandomGenBase(object):
    """
    Generate a random number from a distribution
    """

    _random_nums: list[int] | None = None  # Values that may be returned by next_num()
    _probabilities: list[
        float
    ] | None = None  # Probability of the occurrence of random_nums

    @abstractmethod
    def __next__(self):
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def next_num(self) -> int:
        """
        Returns one of the randomNums.
        When this method is called multiple times over a long period,
        it should return the numbers roughly with the initialized probabilities.
        """
        raise NotImplementedError

    @staticmethod
    def validate_probs(probs: list[float]):
        if round(sum(probs), 2) != 1.00:
            raise NotProbMassFuncException("Not a probability mass function")

    @staticmethod
    def validate_random_nums(random_nums: list[int], probs: list[float]):
        if len(random_nums) < len(probs):
            raise NotProbMassFuncException("More numbers than probabilities")

    @abstractmethod
    def pmf(self):
        raise NotImplementedError


class RandomGen(RandomGenBase):
    """
    Implementation of a random number generator
    """

    def __init__(
        self, random_nums: list[int], probs: list[float], *, observation_size: int = 100
    ):
        self._random_nums = random_nums
        self._probabilities = probs
        self._observation_size = observation_size
        self._count = 0
        self._counter = Counter[int]()
        self.validate_probs(probs)  # validate if probabilities sum to 1
        self.validate_random_nums(
            random_nums, probs
        )  # validate if random_nums is shorter than probs

    @property
    def counter(self) -> Counter:
        return self._counter

    def resize(self, new_size: int):
        self._count = 0
        self._observation_size = new_size

    def refresh(self, random_nums: list[int], probs: list[float]):
        self.validate_probs(probs)
        self.validate_random_nums(random_nums, probs)
        self._count = 0

    def __iter__(self):
        self._count = 0
        return self

    def get_cumulative_probs(self):
        return (round(i, 2) for i in accumulate(self._probabilities))

    def __next__(self):
        if self._observation_size > self._count:
            self._count += 1
            return self.next_num()
        raise StopIteration

    def next_num(self) -> int:
        random_number = random.random()
        for i, prob in enumerate(self.get_cumulative_probs()):
            if prob > random_number:
                num = self._random_nums[i]
                self._counter[num] += 1
                return num

    @property
    def pmf(self):
        """probability mass function by Monte Carlo"""
        pmf = {}
        for value, count in self._counter.items():
            pmf[value] = count / float(self._observation_size)
        return dict(reversed(pmf.items()))
