import json
from json import JSONDecodeError
from exercise import Exercise
from workout import Workout


def main():
    print("Welcome to Overloader! What would you like to do?\n"
          "E - Enter new workout\n"
          "V - View workout suggestions\n"
          "X - Exit")
    user_input = input()
    if user_input == "E":
        workout = Workout()
        workout = enter_exercise(1, workout)
        workout.write_to_json("log.json")
        main()
    elif user_input == "V":
        view_suggestion()
        main()
    elif user_input == "X":
        pass
    else:
        print("Enter a valid choice!")
        print("---------------------")
        main()


def enter_exercise(exercise_number, workout):
    print(f"Exercise {exercise_number}. Enter exercise you want (BENCH_PRESS, SQUAT, DEADLIFT) or X to go back:")
    user_input = input()
    if user_input == "X":
        main()
    if user_input == "BENCH_PRESS":
        exercise = Exercise.BENCH_PRESS
    elif user_input == "SQUAT":
        exercise = Exercise.SQUAT
    elif user_input == "DEADLIFT":
        exercise = Exercise.DEADLIFT
    else:
        print("Enter a valid choice!")
        print("---------------------")
        enter_exercise(exercise_number, workout)

    while True:
        print("Enter reps and weight, separated by a space ([reps] [weight]). Don't include warmup sets. : ")
        user_input = input().split(" ")
        try:
            reps, weight = int(user_input[0]), float(user_input[1])
        except ValueError:
            print("Enter a valid input!")
            reps, weight = None, None
        if reps and weight:
            exercise.add_set(reps, weight)
        print("Add another set? (Y/N)")
        user_input = input()
        if user_input == "Y":
            pass
        elif user_input == "N":
            break
        else:
            print("I'm gonna assume you meant yes. If not, enter '0 0' and get it right.")

    workout.add_exercise(exercise)

    print("Would you like to add another exercise? (Y/N):")
    user_input = input()
    if user_input == "Y":
        enter_exercise(exercise_number + 1, workout)
    elif user_input == "N":
        pass
    else:
        print("I'm gonna assume you meant yes. If not, enter your last exercise and '0 0' and get it right.")
        enter_exercise(exercise_number + 1, workout)

    return workout


def view_suggestion():
    print("What exercise would you like to get your next workout for? (BENCH_PRESS, SQUAT, DEADLIFT) or X to go back:")
    user_input = input()
    if user_input == "X":
        main()
    elif user_input not in ["BENCH_PRESS", "SQUAT", "DEADLIFT"]:
        print("Enter a valid choice!")
        print("---------------------")
        view_suggestion()

    with open("log.json", 'r') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            data = []

    times_exercise_performed = 0
    max_volume_exercise = 0
    for workout in data:
        if workout[f"{user_input}"]:
            times_exercise_performed += 1
            if workout[f"{user_input}"] > max_volume_exercise:
                max_volume_exercise = workout[f"{user_input}"]

    weeks_of_experience = times_exercise_performed // 2  # assuming doing this exercise 2 times/week
    if weeks_of_experience <= 4:
        overload = 0.05
    elif 4 < weeks_of_experience <= 12:
        overload = 0.035
    else:
        overload = 0.02

    next_lift = max_volume_exercise + max_volume_exercise * overload
    print(f"Your best time on {user_input}, you did {max_volume_exercise}lbs of volume.\n"
          f"For your next workout, you should aim for {next_lift}lbs of volume.")
    print("How many reps and sets would you like to do on this exercise? ([sets] [reps]), integers only: ")

    user_input = input().split(" ")
    sets, reps = int(user_input[0]), int(user_input[1])
    next_weight = round((next_lift / (sets * reps)) / 5) * 5

    print(f"Your next time with this exercise should be {sets}x{reps} @ {next_weight}lbs.")
    print("Get advice for another exercise? (Y/N): ")
    user_input = input()
    if user_input == "Y":
        view_suggestion()
    elif user_input == "N":
        pass
    else:
        print("I'm gonna assume you meant yes.")
        view_suggestion()


if __name__ == "__main__":
    main()
