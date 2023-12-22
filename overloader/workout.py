from exercise import Exercise
import json
from json import JSONDecodeError

class Workout:

    def __init__(self):
        self.exercises = {}

    def add_exercise(self, exercise: Exercise):
        self.exercises[str(exercise.name)] = exercise.total

    def write_to_json(self, jsonfile: str):
        with open(jsonfile, 'r') as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                data = []
            data.append(self.exercises)

        with open(jsonfile, "w") as f:
            json.dump(data, f)