from tkinter import * 
from settings import *
import c_func as cf
import time
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
  
# plot function is created for  
# plotting the graph in  
# tkinter window 
def squares_plot(bottom_range, top_range):
  
    # the figure that will contain the plot 
    fig = Figure(figsize = (10, 5), 
                 dpi = 100) 
  
    # list of squares 
    start = time.perf_counter()
    y = cf.getRangeSquares(bottom_range, top_range)
    end = time.perf_counter()
  
    # adding the subplot 
    plot1 = fig.add_subplot(111) 
  
    # plotting the graph 
    plot1.plot(y) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 
    print(end-start)
  
# the main Tkinter window 
window = Tk() 
  
# setting the title  
window.title("Suppy & Demand Simulator") 

# dimensions of the main window 
window.geometry(f"{WIDTH}x{HEIGHT}") 

my_spinner = Spinbox(window, from_=1, to=9999998, font=("Helvetica", 20))

# button that displays the plot 
plot_button = Button(master = window,  
                     command = lambda x=0: squares_plot(int(my_spinner.get()), 99999999), 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 
  
# place the button  
# in main window 
plot_button.pack() 
my_spinner.pack(pady=20)
  
# run the gui 
window.mainloop() 