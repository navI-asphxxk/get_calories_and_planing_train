import entities
import design
import sys
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.display_workout)
        self.pushButton_2.clicked.connect(self.delete_workout)

        self.pushButton_3.clicked.connect(self.display_weekend)
        self.pushButton_4.clicked.connect(self.display_weekend)

        self.pushButton_5.clicked.connect(self.display_workout)
        self.pushButton_6.clicked.connect(self.display_workout)
        self.pushButton_7.clicked.connect(self.display_workout)
        self.pushButton_8.clicked.connect(self.display_workout)
        self.pushButton_9.clicked.connect(self.display_workout)

    def check_lines_edit(self):
        if len(self.lineEdit_2.text()) == 0:
            self.lineEdit_2.setText("Заполните поле!")
            return True
        elif len(self.lineEdit_3.text()) == 0:
            self.lineEdit_3.setText("Заполните поле!")
            return True
        # elif len(self.lineEdit_5.text()) == 0:
        #     self.lineEdit_5.setText("Заполните поле!")
        #     return True

        return False

    def display_weekend(self):
        self.listWidget.clear()
        self.listWidget.addItem("Выходной")

    def display_workout(self):
        self.listWidget.clear()

        if self.check_lines_edit():
            return

        weight = float(self.lineEdit_2.text())
        height = float(self.lineEdit_3.text())
        goal = self.comboBox.currentText()
        sex = self.comboBox_2.currentText()
        activity = self.comboBox_3.currentText()
        duration = int(self.lineEdit_5.text())
        age = int(self.lineEdit_4.text())
        self.current_user = entities.User(weight, height, age, sex, activity, goal)

        workout = create_workout(duration, goal)
        workout_map = workout.workout_to_string()

        for exercise, reps in workout_map:
            self.listWidget.addItem(f"{exercise}: {reps} повторений")

        self.lineEdit_6.setText(str(self.current_user.calories_amount))

    def delete_workout(self):
        self.listWidget.clear()
        self.lineEdit_6.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


def create_workout(duration, goal):
    workout = entities.Workout(0, [], [], [])

    if goal.lower() == "набор мышечной массы":
        workout.exercises_list = ["Подтягивания", "Жим штанги", "Подьем гантелей на бицепс", "Пресс",
                     "Разведение ганделей в стороны", "Отжимания на брусьях"]
        workout.sets = [3, 2, 3, 3, 2, 3]
        workout.repetitions = [10, 12, 20, 20, 15, 10]
    elif goal.lower() == "похудение":
        workout.exercises_list = ["Беговая дорожка", "Велотренажер", "Планка", "Гимнастика"]
        workout.sets = [1, 1, 3, 1]
        workout.repetitions = [20, 30, 1, 30]
    else:
        workout.exercises_list = ["Бег на беговой дорожке", "Жим гантелей", "Пресс", "Подтягивания"]
        workout.sets = [3, 3, 3, 3]
        workout.repetitions = [20, 20, 20, 20]

    return workout


if __name__ == '__main__':
    main()