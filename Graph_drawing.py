from distutils.command import build
import turtle
import tkinter
import tkinter as tk

gui = tk.Tk() #creating the gui window
#configuring the gui
gui.geometry("700x650")
gui.title("Oh boy oh no")
gui.configure(bg="#19181D")
#canvas for the turtle
canvas = tkinter.Canvas(gui,width=500,height=500,bg="#25242A",highlightbackground="#1B1A1F")
canvas.pack()
#create the turtle
turt = turtle.RawTurtle(canvas)

def coeff(gui): #creates input box for the x coefficient
    global coefficient
    coefficient = tk.Entry(gui,width=2,fg="white",bg="#46444C",font=16)
    coefficient.pack(side=tk.LEFT,padx=0,pady=5)

def exponent(gui): #creates input box for the power
    power = tk.Entry(gui,width=1,fg="white",bg="#46444C",font=14)
    power.pack(side=tk.LEFT,padx=0,pady=5)

def printx(gui): #prints the letter x to the gui
    xval = tk.Label(gui,text="x",fg="white",bg="#19181D",font=16)
    xval.pack(side=tk.LEFT,padx=0,pady=5)
    
def printy(gui): #prints "y = " to the gui
    yval = tk.Label(gui,text="      y = ",fg="white",bg="#19181D",font=16)
    yval.pack(side=tk.LEFT,padx=2,pady=2)
    
def printplus(gui): #prints + symbol
    plus = tk.Label(gui,text="+",fg="white",bg="#19181D",font=16)
    plus.pack(side=tk.LEFT,padx=2,pady=5)
    
def y_interc(gui):
    printplus(gui)
    cval = tk.Entry(gui,width=2,fg="white",bg="#46444C",font=16)
    cval.pack(side=tk.LEFT,padx=2,pady=5)
    
def graph(gui,turt): #draws the graph axis
    #y axis
    turt.width(3)
    turt.speed(10)
    turt.penup()
    turt.goto(0,250)
    turt.setheading(270)
    turt.pendown()
    turt.forward(500)
    turt.penup()
    #x axis
    turt.goto(-250,0)
    turt.setheading(0)
    turt.pendown()
    turt.forward(500)
    turt.penup()
    turt.hideturtle()
graph(gui,turt)

def first_term(gui):
    printy(gui) #prints "y = " at the start of the equation
    coeff(gui)
    printx(gui)
    exponent(gui)
    new_term(gui) 
    
def extra_terms(gui):
    printplus(gui)
    coeff(gui)
    printx(gui)
    exponent(gui)

def new_term(gui):
    more = tk.Button(gui,text="Add term",fg="white",bg="#46444C",command=lambda: extra_terms(gui),height=1,width=10)
    #button to add a new term to the equation
    more.place(x=315,y=610) #button to add a term to the equation
    
def plus_c(gui):
    c_btn = tk.Button(gui,text="+ c",fg="white",bg="#464446",command=lambda: y_interc(gui),height=1,width=4)
    #c_btn.pack(side=tk.BOTTOM,padx=3,pady=5) #button to add +c to the equation
    c_btn.place(x=410,y=610) #button to add +c to the equation
plus_c(gui)

first_term(gui)

#the graph's equation
global equation
equation = ""

def end_btn(gui):
    end = tk.Button(gui,text="Draw graph",fg="white",bg="#464446",command=lambda: stop_entry(gui),height=1,width=11)
    end.place(x=460,y=610)
end_btn(gui)
    
def stop_entry(gui):
    coefficient.config(state="readonly")
    power.config(state="readonly")
    
    

gui.mainloop() 

