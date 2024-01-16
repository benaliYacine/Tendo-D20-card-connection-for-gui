"""

a code in py and using pyqtgraph and minimalmodbus that draw GRAPH OF VALUES - Voltage_S1, Voltage_S2, Voltage_S3, Voltage_S4
over time
Y axis: MIN 0, MAX 12
X axis: the 4 values plotted over 30 seconds (continuously updates)
UPDATES AT A SMOOTH RATE (10 HZ)
and the values ofVoltage_S1, Voltage_S2, Voltage_S3, Voltage_S4 are been readed by minimal modbus ,here is the line that let you read the value of for example VALUES - Voltage_S1 : val1=instr.read_float(34, functioncode=4) and the adresses of Voltage_S2, Voltage_S3, Voltage_S4 are 36 , 38 ,40 

"""
import sys
import minimalmodbus
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import argparse
# Set up minimalmodbus
def comUpdate():#hadi lfct lwahida li sta3melna fiha minimalmodbus
    print('*************************************************************************************\n')
    global instr
    minimalmodbus._print_out( 'Port: ' +  str(args.port) + ', Address: ' + str(args.adr) )
    instr = minimalmodbus.Instrument(args.port, args.adr)#esah ga3 fi l'Instrument instr biha te9der tmed l registre mo3ayan valeur /te9ra lvaleur li fi registre etc..
    # Setup serial port
    instr.serial.parity=minimalmodbus.serial.PARITY_NONE
    instr.serial.baudrate=115200
    instr.serial.bytesize=8
    instr.serial.stopbits=1
    instr.serial.timeout=1
    instr.handle_local_echo = False
    instr.debug = False
    instr.serial.timeout = 1.0
    instr.mode= minimalmodbus.MODE_RTU
    instr.clear_buffers_before_each_transaction=True
    print('*************************************************************************************\n')
    print(instr)

def update():
    comUpdate()
    global curve_s1, curve_s2, curve_s3, curve_s4, time_data, voltage_s1_data, voltage_s2_data, voltage_s3_data, voltage_s4_data
    
    # Read voltage values
    voltage_s1 = instr.read_float(34, functioncode=4)
    voltage_s2 = instr.read_float(36, functioncode=4)
    voltage_s3 = instr.read_float(38, functioncode=4)
    voltage_s4 = instr.read_float(40, functioncode=4)
    
    # Shift voltage data arrays to the left by one element
    voltage_s1_data = np.roll(voltage_s1_data, -1)
    voltage_s2_data = np.roll(voltage_s2_data, -1)
    voltage_s3_data = np.roll(voltage_s3_data, -1)
    voltage_s4_data = np.roll(voltage_s4_data, -1)

    # Replace the last element of each voltage data array with the corresponding value
    voltage_s1_data[-1] = voltage_s1
    voltage_s2_data[-1] = voltage_s2
    voltage_s3_data[-1] = voltage_s3
    voltage_s4_data[-1] = voltage_s4
    
    # Update time data
    time_data = np.roll(time_data, -1)
    time_data[-1] = time_data[-2] + 0.1
    
    curve_s1.setData(time_data, voltage_s1_data)
    curve_s2.setData(time_data, voltage_s2_data)
    curve_s3.setData(time_data, voltage_s3_data)
    curve_s4.setData(time_data, voltage_s4_data)


version='v1.5'
#ex ki truni l code dir python myscript.py --port /dev/ttyUSB1 --adr 2 --file /path/to/database.csv koun madirhomch yeb9aw bel valeur deafault ta3hom
parser = argparse.ArgumentParser(description=f"Dynamic GUI {version} (paul@mcnab.se)")
parser.add_argument('--port', default='/dev/ttyUSB0', help='Serial port')
parser.add_argument('--adr', type=int, default=1, help='Modbus address')
parser.add_argument('--file', default='Database.csv', help='Patch to database cvs file')
args = parser.parse_args()

instr = None


# Set up pyqtgraph
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Voltage Plot")
win.resize(800, 600)
win.setWindowTitle("Voltage Plot")
pg.setConfigOptions(antialias=True)

plot = win.addPlot(title="Signal Graph")
legend = plot.addLegend()
grid = pg.GridItem()

plot.addItem(grid)
plot.showGrid(x=True, y=True)
curve_s1 = plot.plot(pen="r", name="Voltage_S1")
curve_s2 = plot.plot(pen="g", name="Voltage_S2")
curve_s3 = plot.plot(pen="b", name="Voltage_S3")
curve_s4 = plot.plot(pen="y", name="Voltage_S4")
plot.setLabel("left", "Voltage", units="V")
plot.setLabel("bottom", "Time", units="s")
plot.setYRange(0, 12)
plot.setXRange(0, 30)
# Initialize data arrays
time_data = np.zeros(300)
j = 0
for index, _ in enumerate(time_data):
    time_data[index] = j
    j += 0.1

voltage_s1_data = np.ones(300) * 1
voltage_s2_data = np.ones(300) * 2
voltage_s3_data = np.ones(300) * 3
voltage_s4_data = np.ones(300) * 4

curve_s1.setData(time_data, voltage_s1_data)
curve_s2.setData(time_data, voltage_s2_data)
curve_s3.setData(time_data, voltage_s3_data)
curve_s4.setData(time_data, voltage_s4_data)


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)  # Update at 10Hz (100ms interval)

if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()