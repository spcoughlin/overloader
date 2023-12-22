from enum import Enum

class Exercise(Enum):

    BENCH_PRESS: 1
    SQUAT: 2
    DEADLIFT: 3

    def __init__(self):
        self.total = 0

    def add_set(self, reps: int, weight: float):
        self.total += reps * weight