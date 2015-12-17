from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QCheckBox, QComboBox,
                             QDial, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QScrollBar,
                             QSlider, QSpinBox, QStackedWidget, QWidget)
import algorithm_test

import sys


class GuiController:
    def __init__(self, algorithm):
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.signals = None
        self.horizontal_sliders = self.window.horizontalSliders

        for item in algorithm.integer_sliders:
            slider = self.horizontal_sliders.add_slider(item.default, item.lower, item.upper)
            SlidersGroup("test")
            slot = item.set_value
            signal = pyqtSignal()
            # slider.connect(signal)

        self.window.show()
        sys.exit(self.app.exec_())
        print
        "test"


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup("test")

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)

        layout = QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.setWindowTitle("Sliders")


class SlidersGroup(QGroupBox):
    valueChanged = pyqtSignal(int)

    def __init__(self, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)
        self.slidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.slidersLayout)

    def add_slider(self, default, lower, upper):
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setRange(lower, upper)
        slider.setValue(default)
        slider.setTickInterval(10)
        slider.setSingleStep(1)
        self.slidersLayout.addWidget(slider)
        return slider


def createControls(self, title):
    self.controlsGroup = QGroupBox(title)

    valueLabel = QLabel("Current value:")

    self.valueSpinBox = QSpinBox()
    self.valueSpinBox.setRange(-100, 100)
    self.valueSpinBox.setSingleStep(1)

    controlsLayout = QGridLayout()
    controlsLayout.addWidget(valueLabel, 2, 0)
    controlsLayout.addWidget(self.valueSpinBox, 2, 1)
    self.controlsGroup.setLayout(controlsLayout)


MyAlgorithm = algorithm_test.MyAlgorithm
Slider1 = algorithm_test.Slider1
Slider2 = algorithm_test.Slider2
Slider3 = algorithm_test.Slider3
CheckBox1 = algorithm_test.CheckBox1

Controller = GuiController(MyAlgorithm)
