#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#version 3.7.7 ta3 py w lekhra ta3 pyqt5 w numpy w minimalmodbus w 0.10.0 ta3 pyqtgraph
"""

.. moduleauthor:: Paul Bengtsson

Connect to Tendo D20 card and show live data as well as live graph of data.

"""
from os import name #not used 
from warnings import catch_warnings #not used 
from pyqtgraph.graphicsItems.ViewBox.ViewBox import ChildGroup#
import argparse
import os.path
import numpy as np#
import time#not used 
import struct#not used 
import pyqtgraph as pg#
import minimalmodbus
from pyqtgraph.dockarea import *#
import csv
import datetime
import io
from pyqtgraph.Qt import QtCore, QtGui#
import pyqtgraph.parametertree.parameterTypes as pTypes#
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType#
from PyQt5 import QtGui, QtCore, QtWidgets

#fonctions:
def updateCurveVals(s1, s2, s3, s4, s5, s6, s7):
    
    # use the global keyword to specify that the variables ct, curves, data1, data2, data3, data4, data5, and data6 
    # refer to global variables rather than local ones.
    global ct
    global curves, data1, data2, data3, data4, data5, data6, data7
    
    #update the values in the seven NumPy arrays (data1 through data7) with the values passed as arguments (s1 through s7).
    #  Specifically, each array is shifted to the left by one element 
    # (i.e., the first element is dropped and the remaining elements are shifted left), 
    # and the last element is replaced with the corresponding argument value.
    data1[:-1] = data1[1:]
    data1[-1] = s1
    data2[:-1] = data2[1:]
    data2[-1] = s2
    data3[:-1] = data3[1:]
    data3[-1] = s3
    data4[:-1] = data4[1:]
    data4[-1] = s4
    data5[:-1] = data5[1:]
    data5[-1] = s5
    data6[:-1] = data6[1:]
    data6[-1] = s6
    data7[:-1] = data7[1:]
    data7[-1] = s7

    if isinstance(file1, int) == False: #isinstance tchouf ida file1 tipe ta3o int 
        if file1.closed == False: #hna chefna ida rahou closed ida la :
            file1.writelines(f'{datetime.datetime.now().timestamp()}, {s1},{s2},{s3},{s4},{s5},{s6},{s7},\n')
#datetime.datetime.now() hadi treja3 ladate kamla ex 2023-04-04 15:30:00.123456 
# ki zedna .timestamp() returns the POSIX timestamp,
#  which is a floating-point value representing the number of seconds since the Unix epoch (January 1, 1970 at 00:00:00 UTC).
#writelines: ktebna hada estar men' lel ' w el f hadik bah thawel kamel les var l string / ex: 
# name = "Alice"
#age = 30
#print(f"My name is {name} and I'm {age} years old.")

def updatePlot():
    curves[0].setData(data1)
    curves[1].setData(data2)
    curves[2].setData(data3)
    curves[3].setData(data4)
    curves[4].setData(data5)
    curves[5].setData(data6)
    curves[6].setData(data7)
    QtGui.QApplication.processEvents()

def treeViewBuilder():
    line_count = 0
    index_cnt=0
    global csv_reader
    global paramsPB
    for row in csv_reader:
        print(row)
        regSize=1
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
            #exit()
        else:
            t='int'
            if row[11] == 'Float' or row[13] == '10' or row[13]=='100':
                t='float'
            if row[3]=='RI':
                paramsPB[1]["children"].append({'name': row[8], 'type': t, 'value': 0, 'decimals': 10, 'mb_addr': row[4], 'db_type': row[11], 'div': row[13], 'readonly': True})
            else:
                paramsPB[2]["children"].append({'name': row[8], 'type': t, 'value': 0, 'decimals': 10, 'mb_addr': row[4], 'db_type': row[11], 'div': row[13], 'readonly': False})

def updateCurvePlot():
    global plotLen
    try:

        #read_registers(registeraddress: int, number_of_registers: int, functioncode: int = 3) → List[int]
        val=instr.read_registers(27, 7, functioncode=4)
        updateCurveVals(val[0], val[1], val[2], val[3], val[4], val[5], val[6])
        if plotLen==10:
            updatePlot()
            plotLen=1
        plotLen=plotLen+1
    except (RuntimeError, TypeError, NameError, IOError, ValueError):
        print("RuntimeError RI: No value")


def updateRI():
#    print("updateRI")
    global doDelayRead
    if doDelayRead > 0:
        doDelayRead = doDelayRead - 1
        return
    try:
        d=[]

        #instr.write_register(2, 1) #write to debug level 1 indicating to fw that it can take next frame
        #updatePlot(np.array(d))

        for i in paramsPB[1]["children"]:
            #addr=paramsPB[0]["children"][i]['mb_addr'],  #print(i.get('mb_addr')) #print(i.get('db_type'))
            addr=i.get('mb_addr')
            dbtype=i.get('db_type')
            val=0
            if dbtype=='u16bit':
                val=instr.read_register((int(addr)), functioncode=4, signed=False)
            elif dbtype=='16bit':
                val=instr.read_register((int(addr)), functioncode=4, signed=True)
            elif dbtype=='32bit':
                val=instr.read_long(int(addr), functioncode=4)
            elif dbtype=='Float':
                val=instr.read_float(int(addr), functioncode=4)

            div=i.get('div')
            if div=='10':
                val=val/10
            if div=='100':
                val=val/100

            p.child(paramsPB[1]['name']).child(i.get('name')).setValue(val)
            QtGui.QApplication.processEvents()

    except (RuntimeError, TypeError, NameError, IOError, ValueError):
        print("RuntimeError RI: No value")
        doDelayRead = 5

def updateRH():
    global doDelayRead
    global doUpdateRH
    try:
        #print("RH-update")
        #only update RH that can change
        for i in paramsPB[2]["children"]:
            #addr=paramsPB[0]["children"][i]['mb_addr'],  #print(i.get('mb_addr')) #print(i.get('db_type'))
            addr=i.get('mb_addr')
            dbtype=i.get('db_type')
            val=0
            if dbtype=='u16bit':
                val=instr.read_register((int(addr)), functioncode=3, signed=False)
            elif dbtype=='16bit':
                val=instr.read_register(int(addr), functioncode=3, signed=True)
            elif dbtype=='32bit':
                val=instr.read_long(int(addr), functioncode=3, signed=True)
            elif dbtype=='u32bit':
                val=instr.read_long(int(addr), functioncode=3, signed=False)
            elif dbtype=='Float':
                val=instr.read_float(int(addr), functioncode=3)

            p.child(paramsPB[2]['name']).child(i.get('name')).setValue(val)
            QtGui.QApplication.processEvents()

        doUpdateRH = 0 #flag for indicating tree has populated and changes comes likly from enter data

    except (RuntimeError, TypeError, NameError, IOError, ValueError):
        print("RuntimeError RH: No value")
        doDelayRead = 5

def setRH(path, data):
    try:
        if path[0] != "Holding registers":
            return
        for i in paramsPB[2]["children"]:
            if i.get('name') == path[1]:
                addr=i.get('mb_addr')
                dbtype=i.get('db_type')
                if dbtype=='u16bit':
                    instr.write_register(int(addr), data)
                if dbtype=='16bit':
                    instr.write_register(int(addr), data)
                elif dbtype=='32bit':
                    instr.write_long(int(addr), data, signed=True)
                elif dbtype=='u32bit':
                    instr.write_long(int(addr), data, signed=False)
                elif dbtype=='Float':
                    instr.write_float(int(addr), data)
            QtGui.QApplication.processEvents()

    except (RuntimeError, TypeError, NameError, IOError, ValueError):
        print("RuntimeError Set RH")

## If anything changes in the tree, print a message
def change(param, changes):
    global doUpdateRH
    global app_run
    global file1
    global first
    #print("tree changes:")

    if first==True:
        first=False
        return

    for param, change, data in changes:
        path = p.childPath(param)
        if path is not None:
            childName = '.'.join(path)
        else:
            childName = param.name()
        #print('  parameter: %s'% childName)
        #print('  change:    %s'% change)
        #print('  data:      %s'% str(data))
        #print('  ----------')

        if childName == 'Command.Start':
            if app_run==False:
                comUpdate()#hadi hiya l fct li sta3melna fiha minimalmodbus sta3melnaha hna bark 
                timer.start(200)
                timer2.start(10)
            else:
                timer.stop()
                timer2.stop()
            app_run= not app_run

        if childName == "Command.Log":
            if data==True:
                fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")#tmed lel fileName la date b forma mohadada li hiya ex: 2023-04-04_16-45-30
                file1 = open(f"{fileName}.log","w") #hna ftahna file b ismo howa filename.log ex : 2023-04-04_16-45-30.log f mod <rite 
                file1.writelines(f'Time, Sensor 1, Sensor 2, Sensor 3, Sensor 4, Sensor 5, Sensor 6, Sensor 7 \n')#hna ktebna fiih 
            else:
                fileName = ""
                file1.close()

        if doUpdateRH == 1:
            """
            We are reading the values for the first time
            and would not like us to send out the data
            on the bus.
            """
            return;


        setRH(path, data)

        #if childName == 'Holding registers.Regulation.damper_regulation_config':
        #    writeRH(RH_DAMPER_REGULATION_CONFIG, data)

def save():
    global state
    state = p.saveState()

def restore():
    global state
    p.restoreState(state)

def comUpdate():#hadi lfct lwahida li sta3melna fiha minimalmodbus
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


#the main 

app = QtGui.QApplication([])
timer = QtCore.QTimer()
file1=io.TextIOBase()#hadi TextIOBase 3ibara 3an class dakhel module io tema file1 aw objet doka rah tel9a fi blayes khdokhrin 3ayatna l file. w kach methode men ta3 la class TextIOBase kima file1.closed
instr=0
app_run = False
doDelayRead = 0
doUpdateRH = 1
first=True

version='v1.5'
#ex ki truni l code dir python myscript.py --port /dev/ttyUSB1 --adr 2 --file /path/to/database.csv koun madirhomch yeb9aw bel valeur deafault ta3hom
parser = argparse.ArgumentParser(description=f"Dynamic GUI {version} (paul@mcnab.se)")
parser.add_argument('--port', default='/dev/ttyUSB0', help='Serial port')
parser.add_argument('--adr', type=int, default=1, help='Modbus address')
parser.add_argument('--file', default='Database.csv', help='Patch to database cvs file')
args = parser.parse_args()
infile = str(args.file)
if infile.find('.csv') < 0:
	infile = infile + '.csv'
if not os.path.isfile(infile):#os.path.isfile(infile) is a Python function that returns True if infile refers to a file that exists and is a regular file, and False otherwise.
	print('Error: file does not exist!')
	exit(-1)
csv_file=open(args.file, encoding='utf-8')#zedt , encoding='utf-8'
csv_reader = csv.reader(csv_file, delimiter=',')#csv.reader() te9ra kamel les fildes li fel file csv_file (rak dayerlou open)
#li yefsal biin koul field w deuxieme houwa ',' rana mhadinou fe l'arg zawj / csv_reader


#######################################
#Plot
#######################################

plotLen=1
#creates seven NumPy arrays, each with a length of 500 and all filled with zeros.
data1 = np.zeros(500)#np.zeros() function. This function creates an array of a specified length filled with zeros. In this case, each array is 500 elements long and is assigned to a variable named data1 through data7.
data2 = np.zeros(500)
data3 = np.zeros(500)
data4 = np.zeros(500)
data5 = np.zeros(500)
data6 = np.zeros(500)
data7 = np.zeros(500)

area = DockArea()
d1 = Dock("Tendo Plots")
area.addDock(d1, 'above')

p1 = pg.PlotWidget(title="Analog Plot")
p1.plotItem.showGrid(x=True,y=True,alpha=1)
p1.addLegend()
d1.addWidget(p1)

# add button to exit
exit_button = QtGui.QPushButton("Exit")
exit_button.setMaximumWidth(50)
exit_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
d1.addWidget(exit_button, 0, 1)



legends = ["CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7"]
#legends = ["CH1"]
nPlots = 7
curves = []
for i in range(nPlots):
    c = pg.PlotCurveItem(pen=(i,nPlots*1.3), name=legends[i])
    p1.addItem(c)
    curves.append(c)

#ADD general groups
paramsPB = [
    {'name': 'Command', 'type': 'group', 'expanded': True, 'children': [
        {'name': 'Start', 'type': 'bool'},
        {'name': 'Log', 'type': 'bool'},
    ]},
    {"name": "Input registers", "type": "group", "children": []},
    {'name': 'Holding registers', 'type': 'group', 'children': []},
];

treeViewBuilder()
p = Parameter.create(name='paramsPB', type='group', children=paramsPB)

p.sigTreeStateChanged.connect(change)

#p.param('Command','Update Input Registers').sigActivated.connect(updateInputRegisters)
#p.param('Command','Update Holding Registers').sigActivated.connect(updateHoldingRegisters)

t = ParameterTree()
t.setParameters(p, showTop=False)
t.setWindowTitle('GUI')


win = QtGui.QWidget()
hbox = QtGui.QHBoxLayout()
win.setLayout(hbox)
win.setWindowTitle(f'Dynamic GUI {version} (paul@mcnab.se)')
hbox.addWidget(t)
hbox.addWidget(area)


labels_pos = {'bottom': "Time [s]"}


win.show()
win.showFullScreen()
#win.resize(700,1000)

state = p.saveState()


timer.timeout.connect(updateRI)
timer.timeout.connect(updateRH)
#timer.start(200)

timer2 = QtCore.QTimer()
timer2.timeout.connect(updateCurvePlot)



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()