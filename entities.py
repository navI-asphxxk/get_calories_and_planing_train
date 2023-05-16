class User:
    def __init__(self, weight, height, age, gender, activity_level, goal):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.activity_level = activity_level
        self.goal = goal
        self.age = age
        self.calories_amount = self.calculate_calories(weight, height, age, gender, activity_level, goal)

    def calculate_calories(self, weight, height, age, gender, activity_level, goal):
        if gender.lower() == "муж":
            metabolic_rate = weight * 10 + height * 6.25 - age * 5 + 5
        else:
            metabolic_rate = weight * 10 + height * 6.25 - age * 5 - 161

        if activity_level.lower() == "малая":
            activity_coefficient = 1.2
        elif activity_level.lower() == "средняя":
            activity_coefficient = 1.55
        elif activity_level.lower() == "высокая":
            activity_coefficient = 1.725
        else:
            activity_coefficient = 1.9

        if goal.lower() == "набор мышечной массы":
            calories_consuming_amount = metabolic_rate * activity_coefficient + 500
        elif goal.lower() == "похудение":
            calories_consuming_amount = metabolic_rate * activity_coefficient - 500
        else:
            calories_consuming_amount = metabolic_rate * activity_coefficient

        return calories_consuming_amount


class Workout:
    def __init__(self, duration, exercises_list, sets, repetitions):
        self.duration = duration
        self.exercises_list = exercises_list
        self.sets = sets
        self.repetitions = repetitions

    def count_calories(self):
        calories = 0
        for exercise in self.exercises_list:
            calories += exercise.calories_per_one

        return calories

    def workout_to_string(self):
        workout = []

        time_per_exercise = self.duration // len(self.exercises_list)

        for i in range(len(self.exercises_list)):
            for j in range(self.sets[i]):
                workout.append((self.exercises_list[i], self.repetitions[j]))

        return workout
