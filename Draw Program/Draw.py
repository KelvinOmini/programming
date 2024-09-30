# The import includes turtle graphics and tkinter modules.
# The colorchooser and fileddialog modules let the user
# pick a color and a filename
import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom

# The following classes define the different commands that
# are supported by the drawing application
class GoToCommand:
    def __init__(self, x,y,width=1, color="black"):
        self.x =x
        self.y=y 
        self.width = width
        self.color = color

    # The draw method for each command draws the command
    # using the given turtle
    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)

    # The __str__ method is a special method that is 
    # called when a command is converted to string. The string
    # version of the command is how  it appears in the graphics file format

    def __str__(self):
        return '<Command x = ' + str(self.x) + " y = " + str(self.y) + " width = " + str(self.width) + " color = " + self.color + ">GoTo</Command>"

class CircleCommand:
    def __init__(self, radius, width =1, color = "black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        return "<Command radius = " + str(self.radius) + " width = " + str(self.width) + " color =" + self.color + ">Circle</Command>"
    

class BeginFillCommand:
    def __init__ (self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return "<Command color =" + self.color + ">BeginFill</Command>"
    
class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()

    def __str__(self):
        return "<Command>PenUp<Command>"

class PenUpCommand:
    def __init__(self):
        pass
    def draw(self, turtle):
        turtle.penup()
    def __str__(self):
        return "<Command>EndFill</Command>"
     
class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return "<Command>PenDown</Command>"
    
# This special method is called when iterating over the sequence.
# Each time yield is called another element of the sequence is returned
# to the iterator
class PyList:
    def __init__(self):
        self.gcList = []
    
    def append(self, item):
        self.gcList = self.gcList + [item]

    # To slice the sequence to remove the last item
    def removeLast(self):
        self.gcList = self.gcList[:-1]

    def __iter__(self):
        for c in self.gcList:
            yield c
    
    # This is called when the len function is called on the sequence.
    def __len__(self):
        return len(self.gcList)
    
    # This class defines the drawing application. The following line says that
    # the DrawingApplication class inherit from the frame class. This means
    # that a DrawingApplication is like a frame object except for the code
    # written here which redefines/extends the behavior of a Frame.

class DrawingApplication(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()

    # This method is called to create all widget, place them in the GUI,
    # and define the event handlers for the application.
    def buildWindow(self):
        # The master  is the root window. The title is set as below
        self.master.title("Draw")

        # Here is how to create a menu bar. The tearoff = 0 means that menus
        # can't be separated from the window which is a feature of tkinter.
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff = 0)

        # This code is called by "New" menu item below when it is selected
        # The same applies for loadfile, addToFile, and saveFile below.  The
        # "Exit" menu item below calls quit on the "master" or root window.
        def newWindow():
            self.theTurtle.clear()
            self.theTurtle.pendown()
            self.theTurtle.goto(0,0)
            self.theTurtle.pendown()
            self.screen.update()
            self.screen.listen()
            self.graphicsCommands = PyList()

        fileMenu.add_command(label = "New", command = newWindow)

        # The parse function adds the contents of an XML file to the sequence.
        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)

            graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommand")[0]
            graphicsCommands = graphicsCommandsElement.getElementsByTagName("Command")

            for commandElement in graphicsCommands:
                print(type(commandElement))
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x,y,width, color)

                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius, width, color)

                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)

                elif command == "EndFill":
                    cmd = EndFillCommand()

                elif command == "PenUp":
                    cmd = PenUpCommand()

                elif command == "PenDown":
                    cmd = PenDownCommand()

                else:
                    raise RuntimeError("Unknown Command: " + command)

                self.graphicsCommands.append(cmd)

        def loadFile():
            filename = tkinter.filedialog.askopenfilename(title = "Select a Graphics File")
            newWindow()
            self.graphicsCommands = PyList()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(self.theTurtle)
            self.screen.update()

        fileMenu.add_command(label = "Load...", command = loadFile)

        def addToFile():
            filename = tkinter.filedialog.askopenfilename(title = "Select a Graphics FIle")

            self.theTurtle.penup()
            self.theTurtle.goto(0,0)
            self.theTurtle.pendown()
            self.theTurtle.pencolor("#000000")
            self.theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0,0,1, "#000000")
            self.graphicsCommands.append(cmd)
            self.screen.update()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(self.theTurtle)
                self.screen.update()

        fileMenu.add_command(label = "Load into..", command =addToFile)
        
        def write(filename):
            file = open(filename, "w")
            file.write('<?xml version = "1.0" encoding = " UTF-8 " standalone = " no "?>\n')
            file.write('<GraphicsCommands>\n')
            for cmd in self.graphicsCommands:
                file.write('  '+ str(cmd)+"\n")
            file.write('</GraphicsCommands>\n')
            file.close()

        def savefile():
            filename = tkinter.filedialog.asksaveasfilename(title = "Save Picture As...")
            write(filename)
        
        fileMenu.add_command(label = "Save As...", command = savefile)

        fileMenu.add_command(label = "Exit", command = self.master.quit)
        bar.add_cascade(label = "File", menu = fileMenu)
        
        # This tells the root window to display the newly created menu bar.
        self.master.config(menu = bar)
        canvas = tkinter.Canvas(self, width= 600, height= 600)
        canvas.pack(side = tkinter.LEFT)
        self.theTurtle = turtle.RawTurtle(canvas)

        # This makes the sahpe of the turtle a circle
        self.theTurtle.shape("circle")
        self.screen = self.theTurtle.getscreen()
        self.screen.tracer(0)
        sideBar = tkinter.Frame(self, padx= 5, pady = 5)
        sideBar.pack(side= tkinter.RIGHT, fill= tkinter.BOTH)

        # This is a label widget. packingit puts it at the top of the sidebar
        pointLabel = tkinter.Label(sideBar, text = "width")
        pointLabel.pack()

        widthsize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar, textvariable= widthsize)
        widthEntry.pack()       
        widthsize.set(str(1))

        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar, textvariable= radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        def circleHanler():
            cmd = CircleCommand(float(radiusSize.get()), float(widthsize.get()), penColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)
            self.screen.update()
            self.screen.listen()

        # This creates the button widget in the sidebar. The fill= tkinter.BOTH causes the button
        # to expand to fill the entire width of the sidebar.
        circleButton = tkinter.Button(sideBar, text = "Draw_Circle", command = circleHanler)
        circleButton.pack(fill = tkinter.BOTH)

        self.screen.colormode(255)
        penlabel = tkinter.Label(sideBar, text = "penColor")
        penlabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar, textvariable = penColor)
        penEntry.pack()

        # This is the color black
        penColor.set("#000000")

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])

        penColorButton = tkinter.Button(sideBar, text = "Pick Pen Color", command= getPenColor)
        penColorButton.pack(fill = tkinter.BOTH) 
        
        fillLabel = tkinter.Label(sideBar, text = "Fill_Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar, textvariable= fillColor)
        fillEntry.pack()
        fillColor.set("#000000")

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(sideBar, text= "Begin Fill", command = beginFillHandler )
        beginFillButton.pack(fill = tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)

        endFillButton = tkinter.Button(sideBar, text = "End Fill", command = endFillHandler) 
        endFillButton.pack(fill = tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text = "Pen is Down")
        penLabel.pack()

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(self.theTurtle)
            penlabel.configure(text = "Pen is Down")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text = "Pen_Down", command=penDownHandler)
        penDownButton.pack(fill = tkinter.BOTH)

        # To handle mouse clicks on the screen
        def clickHander(x, y):
            # When a mouse clicks occurs, get the handles mouse clicks on the screen.
            # pen to the widthsize value. The float(widthSize.get()) is needed because
            # the width is a float, but the entry widget stores it as a string.
            
            cmd = GoToCommand(x, y, float(widthsize.get()), penColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)
            self.screen.update()
            self.screen.listen()

        # To tie the clickhandler to mouse clicks
        self.screen.onclick(clickHander)

        def dragHandler(x, y):
            cmd = GoToCommand(x, y, float(widthsize.get()), penColor.get())
            cmd.draw(self.theTurtle)
            self.graphicsCommands.append(cmd)
            self.screen.update()
            self.screen.listen()

        self.theTurtle.ondrag(dragHandler)

        # the undoHandler undoes the command by removing it from the
        # sequence and then redrawing the entire picture
        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                self.theTurtle.clear()
                self.theTurtle.penup()
                self.theTurtle.goto(0, 0)
                self.theTurtle.pendown()

                for cmd in self.graphicsCommands:
                    cmd.draw(self.theTurtle)
                self.screen.update()
                self.screen.listen()

        self.screen.onkeypress(undoHandler, "u")
        self.screen.listen()


def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()
    print("Program Execution Completed")

if __name__ == "__main__":
    main()
