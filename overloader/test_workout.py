import unittest
import os
import json
from overloader import exercise, workout

class TestExercise(unittest.TestCase):

    def test_add_set(self):
        exercise = exercise.Exercise.BENCH_PRESS
        exercise.add_set(5, 100)
        self.assertEqual(exercise.total, 500)