from tkinter import *
from tkinter import ttk
import tkinter.font as font

import GenFunctions as gf

#Creating window
root = Tk()
root.title('Used Car Pricing')

#FRAMES


#WIDGET DICTIONARIES (GLOBAL to access anytime)
#Button features
button_dict = {
            'master':None,
            'act_bg':None, #Color
            'act_fg':None, #Color
            'bg':None, #Color
            'fg':None, #Color
            'border':None,
            'font':None, #Font
            'height':None, #Number
            'highl_color':None, #Color
            'image':None, #Img
            'justify':None,
            'padx':None, #Number
            'pady':None, #Number
            'relief':None,
            'underline':None,
            'w':None, #Number WIDTH
            'wraplength':None
        }
#for label features
lab_dict = {
            'master':None,
            'anchor':None,
            'bg':None,
            'bitmap':None,
            'bd':None,
            'font':None,
            'fg':None,
            'height':None,
            'image':None,
            'justify':None,
            'padx':None,
            'pady':None,
            'relief':None,
            'text':None,
            'textvar':None,
            'underline':None,
            'w':None,
            'wraplength':None
        }   
#Entry features
entry_dict = {
            'master':None,
            'bd':None,
            'height':None,
            'width':None,
            'bg':None,
            'fg':None,
            'font':None,
            'insertofftime':None,
            'insertontime':None,
            'padx':None,
            'pady':None,
            'highthick':None,
            'charwidth':None,
            'relief':None,
            'yscrollcommand':None,
            'xscrollcommand':None,
        }
#GRID features
gd = {
            'column':0,
            'row':0,
            'cspan':1,
            'rspan':1,
            'padx':10,
            'pady':10,
            'ipadx':None,
            'ipady':None
        }

#Creating hide frame function
#Used to hide previous frame so that new frame can safely come on screen
def hideFrame(frame):
    try:
        frame.pack_forget()
        #print(f'Frame Hidden')
    except (TypeError, AttributeError):
        pass
    finally:
        return
#Getting next free coordinates starting from TOP LEFT
def GetFreeCoor(arr):
    taken = 1
    free = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == free:
                arr[i][j] = taken
                return (i, j, arr)
    return (None, None, arr)





root.mainloop()
