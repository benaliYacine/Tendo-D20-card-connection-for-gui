import pyqtgraph as pg
from PyQt5 import QtWidgets

# Create some data
x = [1, 2, 3, 4, 5]
y = [1, 3, 2, 4, 5]

# Create the plot widget
app = QtWidgets.QApplication([])
win = pg.PlotWidget(title="Pyqtgraph example")

# Add the data to the plot
win.plot(x, y, pen='r')

# Show the plot
win.show()
app.exec_()
