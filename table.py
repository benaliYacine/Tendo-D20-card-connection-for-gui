from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtGui import QColor, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window title and size
        self.setWindowTitle("Table Example")
        self.setGeometry(100, 100, 500, 500)
        
        # Create title label and set font properties
        self.titleLabel = QLabel("My Table", self)
        self.titleLabel.setGeometry(50, 20, 400, 20)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)
        
        # Create table widget and set size
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 400, 400)
        
        # Set table row and column count
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        
        # Set table headers
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        
        # Fill in table with some data
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f"({row}, {col})")
                self.tableWidget.setItem(row, col, item)
                
        # Set dark stylesheet
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #424242;
                alternate-background-color: #3a3a3a;
                color: #f5f5f5;
                selection-background-color: #ff6600;
                selection-color: #f5f5f5;
            }
            
            QHeaderView::section {
                background-color: #222222;
                color: #f5f5f5;
                padding: 4px;
                border: none;
            }
            
            QTableCornerButton::section {
                background-color: #222222;
                border: none;
            }
        """)
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
