from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont



app = QApplication([])

# Define the colors for the dark theme
background_color = QColor(53, 53, 53)
text_color = QColor(255, 255, 255)
button_color = QColor(255, 255, 255)
button_hover_color = QColor(35, 35, 35)

# Create a QMessageBox
msgBox = QMessageBox()

# Set the font size
font = QFont()
font.setPointSize(50)  # Change the number to adjust the font size
msgBox.setFont(font)

msgBox.setText("This is a QMessageBox!")

# Set the background color, text color, and button color using Qt Style Sheet syntax
msgBox.setStyleSheet('''
QToolTip {
    background-color: #444444;
    color: white;
    border: none;
    padding: 5px;
    opacity: 200;
}

QWidget {
    background-color: #2b2b2b;
    color: white;
    selection-background-color: #4a4a4a;
    selection-color: white;
    font-family: Arial;
    font-size: 12px;
}

QMenuBar {
    background-color: #2b2b2b;
    color: white;
}

QMenuBar::item {
    padding: 2px 10px 2px 10px;
    background-color: #2b2b2b;
    color: white;
    border-radius: 2px;
}

QMenuBar::item:selected {
    background-color: #3d3d3d;
}

QMenu {
    background-color: #2b2b2b;
    color: white;
    border: 1px solid #444444;
}

QMenu::item {
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected {
    background-color: #3d3d3d;
}

QPushButton {
    background-color: #555555;
    color: white;
    border: none;
    padding: 5px 10px 5px 10px;
    border-radius: 5px;
}

QPushButton:hover {
    background-color: #4a4a4a;
}

QLineEdit {
    background-color: #444444;
    color: white;
    border: none;
    padding: 5px;
    border-radius: 2px;
}

QGroupBox {
    border: 1px solid #444444;
    border-radius: 5px;
    margin-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 5px;
    color: white;
}
''')

# Show the QMessageBox
msgBox.exec_()
