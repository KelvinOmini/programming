import tkinter
import turtle
import random
import time
import math

class Point(turtle.RawTurtle):
    def __init__(self, canvas, x, y):
        super().__init__(canvas)
        canvas.register_shape("dot", ((3,0), (2,2), (0,3), (-2,-2), (0,-3), (2, -2)))
        self.shape("dot")
        self.speed(0)
        self.penup()
        self.goto(x, y)

    def __str__(self):
        return f"({self.xcor()}, {self.ycor()})"
    
    def __lt__(self, other):
        return self.ycor() < other.ycor()

# This class defines the animation.
class SortAnimation(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.paused = False
        self.paused = False
        self.should_stop = False
        self.running = False
        self.theTurtle = None
        self.screen = None
        self.canvas = None
        self.buildWindow()
        
    def buildWindow(self):
        def partition(seq, start, stop):
            pivotIndex = start
            pivot = seq[pivotIndex]

            self.theTurtle.color("red")
            self.theTurtle.penup()
            self.theTurtle.goto(start, pivot.ycor())
            self.theTurtle.pendown()
            self.theTurtle.goto(stop, pivot.ycor())
            self.screen.update()

            i = start + 1
            j = stop - 1

            while i <= j:
                while i <= j and not pivot < seq[i]:
                    i += 1
                while i <= j and pivot < seq[j]:
                    j -= 1

                if i < j:
                    seq[i], seq[j] = seq[j], seq[i]
                    seq[i].goto(i, seq[i].ycor())
                    seq[j].goto(j, seq[j].ycor())
                    self.screen.update()
                    i += 1
                    j -= 1

            seq[pivotIndex], seq[j] = seq[j], seq[pivotIndex]
            seq[pivotIndex].goto(pivotIndex, seq[pivotIndex].ycor())
            seq[j].goto(j, seq[j].ycor())
            seq[j].color("green")
            self.screen.update()

            self.theTurtle.color("white")
            self.theTurtle.penup()
            self.theTurtle.goto(0, pivot.ycor())
            self.theTurtle.pendown()
            self.theTurtle.goto(len(seq), pivot.ycor())
            self.screen.update()

            return j
        
        def quicksortRecursively(seq, start, stop):
            if start >= stop:
                return
            if self.should_stop:
                return
            pivotIndex = partition(seq, start, stop)

            if self.should_stop:
                return
            
            quicksortRecursively(seq, start, pivotIndex)

            if self.should_stop:
                return
            
            quicksortRecursively(seq, pivotIndex + 1, stop)
            
        def quicksort(seq):
            quicksortRecursively(seq, 0, len(seq))

        def merge(seq, start, mid, stop):
            length = stop - start
            log = math.log(length, 2)

            self.theTurtle.color("blue")
            self.theTurtle.penup()
            self.theTurtle.goto(start, -3*log)
            self.theTurtle.pendown()
            self.theTurtle.forward(length)
            self.screen.update()

            lst = []
            i = start
            j = mid

            while i < mid and j < stop:
                if seq[i] < seq[j]:
                    lst.append(seq[i])
                    i += 1
                else:
                    lst.append(seq[j])
                    j += 1

            while i < mid:
                lst.append(seq[i])
                i += 1

            while j < stop:
                lst.append(seq[j])
                j += 1

            for i in range(len(lst)):
                seq[start + i] = lst[i]
                lst[i].goto(start + i, lst[i].ycor())
                lst[i].color("green")
                self.screen.update()

        def mergeSortRecursively(seq, start, stop):
            if start >= stop - 1:
                return
            mid = (start + stop) // 2

            if self.should_stop:
                return
            length = stop - start
            log = math.log(length, 2)

            self.theTurtle.color("red")
            self.theTurtle.penup()
            self.theTurtle.goto(start, -3*log)
            self.theTurtle.pendown()
            self.theTurtle.forward(length)
            self.screen.update()

            mergeSortRecursively(seq, start, mid)

            if self.should_stop:
                return
            
            mergeSortRecursively(seq, mid, stop)

            merge(seq, start, mid, stop)

        def mergeSort():
            seq = []
            for i in range(200):
                x = i
                y = random.randint(0, 199)
                p = Point(self.screen, x, y)
                p.color("black")
                seq.append(p)
                
            mergeSortRecursively(seq, 0, len(seq))

        def select(seq, start):
            minIndex = start
            seq[minIndex].color("green")

            for i in range(start, len(seq)):
                if seq[minIndex] > seq[i]:
                    seq[minIndex].color("black")
                    minIndex = i
                    seq[minIndex].color("green")

            return minIndex
        
        def selectionSort(seq):
            for i in range(len(seq)):
                minIndex = select(seq, i)
                if self.should_stop:
                    return

                seq[i], seq[minIndex] = seq[minIndex], seq[i]
                seq[i].goto(i, seq[i].ycor())
                seq[minIndex].goto(minIndex, seq[minIndex].ycor())
                seq[i].color("green")

        def pause():
            while self.paused:
                time.sleep(1)
                self.screen.update()
                self.screen.listen()

        def stop():
            if self.paused:
                pause()

            if self.should_stop:
                self.paused = False
                self.running = False
                self.screen.update()
                self.screen.listen()
                return True
            return False
        
        self.master.title("KELVIN SORT ANIMATION")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        def clear():
            self.screen.clear()
            self.screen.update()
            self.screen.listen()

        def newWindow():
            clear()
            if self.running:
                self.should_stop = True
            self.initTurtle()

        fileMenu.add_command(label="Clear", command=newWindow)
        fileMenu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=fileMenu)
        self.master.configure(menu=bar)

        self.initTurtle()
            
        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        speedLabel = tkinter.Label(sideBar, text="Animation Speed")
        speedLabel.pack()
        speed = tkinter.StringVar()
        speedEntry = tkinter.Entry(sideBar, textvariable=speed)
        speedEntry.pack()
        speed.set("10")

        def selSortHandler():
            self.running = True
            clear()
            self.screen.setworldcoordinates(0, 0, 200, 200)
            self.screen.tracer(0)
            self.master.title("Selection Sort Algorithm")
            seq = []
            for i in range(200):
                if stop():
                    return
                
                p = Point(self.screen, i, i)
                p.color("green")
                seq.append(p)

            for i in range(200):
                if self.should_stop:
                    return
                
                j = random.randint(0, 199)
                
                seq[i], seq[j] = seq[j], seq[i]
                seq[i].goto(i, seq[i].ycor())
                seq[j].goto(j, seq[j].ycor())
                seq[i].color("black")
                seq[j].color("black")

            selectionSort(seq)
            self.running = False
            self.should_stop = False

        button = tkinter.Button(sideBar, text="Selection Sort", command=selSortHandler)
        button.pack(fill=tkinter.BOTH)

        def quickSortHandler():
            self.running = True
            clear()
            self.screen.setworldcoordinates(0, 0, 200, 200)
            self.theTurtle.width(5)
            self.screen.tracer(0)
            self.master.title("Quicksort Animation")
            seq = []
            for i in range(200):
                if stop():
                    return
                
                p = Point(self.screen, i, i)
                p.color("green")
                seq.append(p)

            self.screen.update()
            self.screen.tracer(1)
            for i in range(200):
                if self.should_stop:
                    return
                j = random.randint(0, 199)
                
                seq[i], seq[j] = seq[j], seq[i]
                seq[i].goto(i, seq[i].ycor())
                seq[j].goto(j, seq[j].ycor())
                seq[i].color("black")
                seq[j].color("black")

            self.screen.tracer(1)
            quicksort(seq)
            self.running = False
            self.should_stop = False

        button = tkinter.Button(sideBar, text="Quicksort", command=quickSortHandler)
        button.pack(fill=tkinter.BOTH)

        def pauseHandler():
            self.paused = not self.paused

        button = tkinter.Button(sideBar, text="Pause", command=pauseHandler)
        button.pack(fill=tkinter.BOTH)

        def stopHandler():
            if not self.paused and self.running:
                self.should_stop = True

        button = tkinter.Button(sideBar, text="Stop", command=stopHandler)
        button.pack(fill=tkinter.BOTH)

        self.screen.listen()
    
    def initTurtle(self):
        if self.canvas:
            self.canvas.destroy()

        self.canvas = tkinter.Canvas(self, width=600, height=600)
        self.canvas.pack(side=tkinter.LEFT)

        self.theTurtle = turtle.RawTurtle(self.canvas)
        self.theTurtle.ht()
        self.theTurtle.speed(0)
        self.screen =self.theTurtle.getscreen()
        self.screen.tracer(0)

def main():
    root = tkinter.Tk()
    anime = SortAnimation(root)
    anime.mainloop()

if __name__ == "__main__":
    main()