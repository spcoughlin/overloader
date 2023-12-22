import unittest
import os
import json
from exercise import Exercise
from workout import Workout

class TestExercise(unittest.TestCase):

    def test_add_set(self):
        exercise = Exercise.BENCH_PRESS
        exercise.add_set(5, 100)
        self.assertEqual(exercise.total, 500)

class TestWorkout(unittest.TestCase):

    def setUp(self):
        self.workout = Workout()
        self.jsonfile = 'test_workout.json'

    def tearDown(self):
        if os.path.exists(self.jsonfile):
            os.remove(self.jsonfile)

    def test_add_exercise(self):
        exercise = Exercise.SQUAT
        exercise.add_set(10, 200)
        self.workout.add_exercise(exercise)
        self.assertIn('SQUAT', self.workout.exercises)
        self.assertEqual(self.workout.exercises['SQUAT'], 2000)

    def test_write_to_json(self):
        exercise = Exercise.DEADLIFT
        exercise.add_set(3, 300)
        self.workout.add_exercise(exercise)
        self.workout.write_to_json(self.jsonfile)
        self.assertTrue(os.path.exists(self.jsonfile))

        # Verify file content
        with open(self.jsonfile, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, {'DEADLIFT': 900})

if __name__ == '__main__':
    unittest.main()