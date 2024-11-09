import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QRadioButton, \
    QPushButton, QButtonGroup, QTextEdit
from PyQt6.QtGui import QFont
import numpy as np
import sympy as sp

from iterationMethod import iterationMethodFunc
from bisectionMethod import bisection as bs1
from index4 import methodNewtons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculating methods")
        self.resize(600, 400)
        self.move(350, 160)

        fontIter = QFont("Arial", 10)

        self.label = QLabel("Чисельні методи", self)
        self.label.move(225, 10)
        self.label.setFixedSize(600, 50)

        font = QFont("Arial", 15)
        font.setBold(True)
        self.label.setFont(font)

        self.method = QLabel("Виберіть метод для обробки", self)
        self.method.move(30, 60)
        self.method.setFixedSize(175, 40)

        self.iteration = QRadioButton("Метод ітерації", self)
        self.iteration.move(30, 90)
        self.iteration.setFixedSize(175, 40)
        self.iteration.setChecked(True)
        
        self.bisection = QRadioButton("Метод дихотомії", self)
        self.bisection.move(30, 120)
        self.bisection.setFixedSize(175, 40)

        self.newthonsMethod = QRadioButton("Метод Ньютона", self)
        self.newthonsMethod.move(30, 150)
        self.newthonsMethod.setFixedSize(175, 40)

        self.methodGroup = QButtonGroup(self)
        self.methodGroup.addButton(self.iteration)
        self.methodGroup.addButton(self.bisection)
        self.methodGroup.addButton(self.newthonsMethod)

        self.equation = QLabel("Виберіть рівняння", self)
        self.equation.move(410, 60)
        self.equation.setFixedSize(130, 40)
        self.equation.setFont(fontIter)

        self.firstEq = QRadioButton("cos((x**2-2)/(3*x+1))-x**2+1.5", self)
        self.firstEq.move(410, 90)
        self.firstEq.setFixedSize(130, 40)
        self.firstEq.setChecked(True)

        self.secondEq = QRadioButton("sin(x)+tan((2-x)/(x**2+1))", self)
        self.secondEq.move(410, 120)
        self.secondEq.setFixedSize(130, 40)

        self.eqGroup = QButtonGroup(self)
        self.eqGroup.addButton(self.firstEq)
        self.eqGroup.addButton(self.secondEq)

        self.calculating = QPushButton("Розрахувати", self)
        self.calculating.move(240, 300)
        self.calculating.setFixedSize(130, 40)
        self.calculating.setFont(fontIter)
        self.calculating.clicked.connect(self.isCheckFunction)

        self.method.setFont(fontIter)
        
        self.title = QLabel("Виберіть межі та похибку", self)
        self.title.move(230, 200)
        self.title.setFixedSize(170, 40)
        self.title.setFont(fontIter)

        self.limitA = QTextEdit(self)
        self.limitA.move(130, 250)
        self.limitA.setFixedSize(100, 40)
        self.limitA.setPlaceholderText("Межа А: -2.5")
        self.limitA.setPlainText(str(-2.5))

        self.limitB = QTextEdit(self)
        self.limitB.move(250, 250)
        self.limitB.setFixedSize(100, 40)
        self.limitB.setPlaceholderText("Межа В: 2.5")
        self.limitB.setPlainText(str(2.5))

        self.epsilon = QTextEdit(self)
        self.epsilon.move(370, 250)
        self.epsilon.setFixedSize(100, 40)
        self.epsilon.setPlaceholderText("Похибка Е: 0.01")
        self.epsilon.setPlainText(str(0.01))

    def fx1(self, x):
        return sp.cos((x**2 - 2) / (3 * x + 1)) - x**2 + 1.5

    def fx2(self, x):
        return sp.sin(x) + sp.tan((2 - x) / (x**2 + 1))
        
    def fx3(self, x):
        return np.cos((x**2 - 2) / (3 * x + 1)) - x**2 + 1.5

    def fx4(self, x):
        return np.sin(x) + np.tan((2 - x) / (x**2 + 1))

    def isCheckFunction(self):
        try:
            a = float(self.limitA.toPlainText())
            b = float(self.limitB.toPlainText())
            epsilon = float(self.epsilon.toPlainText())
        except ValueError:
            print("Invalid input values. Please enter numeric values for limits and epsilon.")
            return

        if self.bisection.isChecked() and self.firstEq.isChecked():
            bs1(a, b, epsilon, self.fx3)
        elif self.bisection.isChecked() and self.secondEq.isChecked():
            bs1(a, b, epsilon, self.fx4)
        elif self.newthonsMethod.isChecked() and self.firstEq.isChecked():
            methodNewtons(a, self.fx1)
        elif self.newthonsMethod.isChecked() and self.secondEq.isChecked():
            methodNewtons(a, self.fx2)
        elif self.iteration.isChecked() and self.firstEq.isChecked():
            iterationMethodFunc(a, b, epsilon, self.fx3)
        elif self.iteration.isChecked() and self.secondEq.isChecked():
            iterationMethodFunc(a, b, epsilon, self.fx4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
