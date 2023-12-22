from exercise import Exercise
import json

class Workout:

    def __init__(self):
        self.exercises = {}

    def add_exercise(self, exercise: Exercise):
        self.exercises[str(exercise.name)] = exercise.total

    def write_to_json(self):
        with open("log.json", "a") as f:
            json.dump(self.exercises, f)