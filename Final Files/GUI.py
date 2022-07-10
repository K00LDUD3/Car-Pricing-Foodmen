from ctypes.wintypes import HGDIOBJ
from tkinter import *
from tkinter import ttk
import tkinter.font as font

import GenFunctions as gf

#Creating window
root = Tk()
root.title('Used Car Pricing')

#FRAMES
sign_frame = LabelFrame(root)
signIn_frame = LabelFrame(root)
signUp_frame = LabelFrame(root)

home_frame = LabelFrame(root)

#CATEGORICAL input frames
iManufacturer_frame = LabelFrame(root)
iModel_frame = LabelFrame(root)
iCategory_frame = LabelFrame(root)
iFuelType_frame = LabelFrame(root)
iGearBox_frame = LabelFrame(root)
iDriveWheels_frame = LabelFrame(root)
iColor_frame = LabelFrame(root)

iLRWheel_frame = LabelFrame(root)

#NUMERICAL input frames
iNumericInp_frame = LabelFrame(root)

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
label_dict = {
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


def home(frame):
    '''
    Homescreen to display available options(sign out, start pricing)
    '''
    hideFrame(frame=frame)
    h_gd = gd
    h_bd = button_dict
    h_gd['ipady'] = 5
    h_bd['master'] = home_frame
    h_bd['w'] = 20
    
    placements = [[0,],
                  [0,]]

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    start_b = gf.GenFunc('button', h_bd, 'Start', h_gd)

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', h_bd, 'Sign Out', h_gd)

    home_frame.pack()
    return

#ALL FRAMES for taking CATEGORICAL input
def iManufacturer(frame):
    hideFrame(frame=frame)

    im_bd = button_dict
    im_ld = label_dict
    im_bd['master'] = iManufacturer_frame
    im_ld['master'] = iManufacturer_frame
    im_gd = gd

    placements = [[0,0],
                  [0,0]
                  [0,0]]

    #0,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', im_ld, 'Manufacturer:', im_ld)

    #1,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)

home(frame=None)
root.mainloop()
