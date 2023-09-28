# import the library
from appJar import gui
from numpy import sin, pi, arange
import time
import random
# create a GUI variable called app

students = ['Nixon','Wally','Kim','John','Steve']
majors = ['CS','DS','IMGD','IMGD','IMGD','IMGD','DS','DS','DS']
year = [1,2,3,4,2,4,3,4,2,3,3,1,2,1,2,3,1,1]
inp = [0,0,0,0]


app = gui()

app.addLabel("title", "Class Analysis")

app.addLabelEntry("File Name")

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        fname = app.getEntry("File Name")
        print("File Name:", fname)
        
app.addButtons(["Submit", "Cancel"], press)

def inBut(button):
    if button == "Cancel":
        app.stop()
    else:
        inp = app.getEntry("Input")
        print('Input: ', inp )
        glob = globals()
        inp = glob.get(inp)
        x = arange(len(inp)) + 0.5
        ax.bar(x,inp)
        app.refreshPlot("p1")

app.addLabelEntry("Input")
app.addButtons(["Enter", "End"], inBut)

x = arange(len(inp)) + 0.5

fig = app.addPlotFig("p1")
ax = fig.add_subplot(111)
ax.bar(x,inp)


app.go()
