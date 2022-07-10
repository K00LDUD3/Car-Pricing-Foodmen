from ctypes.wintypes import HGDIOBJ
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.font as font

import GenFunctions as gf
import AlgoData as alg

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

#CLASS VARIABLES require
current_manufacturer = 'lexus' #First value is lexus

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
    
    placements = [[0],
                  [0]]

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    start_b = gf.GenFunc('button', h_bd, 'Start', h_gd)
    start_b.widg.config(command= lambda: iManufacturer(frame=home_frame))

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', h_bd, 'Sign Out', h_gd)

    home_frame.pack()
    return

# Changing current manufacturer to extract the models available
def UpdateManufacturer(choice):
    choice = choice.strip().split(' ')[1]
    current_manufacturer = choice
    print(current_manufacturer)
    return

#ALL FRAMES for taking CATEGORICAL input
def iManufacturer(frame):
    '''
    FRAME for taking manufacturer as input
    '''
    hideFrame(frame=frame)

    im_bd = button_dict
    im_ld = label_dict
    im_bd['master'] = iManufacturer_frame
    im_ld['master'] = iManufacturer_frame
    im_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0]]

    #0,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', im_ld, 'Manufacturer:', im_gd)

    #0,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    manufacturer_list = alg.ManufactUniqueModels(choice='m')
    manufacturer_list = ['   '+(str(i+1)+'. '+manufacturer_list[i]) for i in range(len(manufacturer_list))]
    s=ttk.Style(master=None)
    s.theme_use('xpnative')
    combo = ttk.Combobox(master=iManufacturer_frame, values=manufacturer_list, state='readonly', width=20, style='small.TButton')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateManufacturer(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=im_gd['row'], column=im_gd['column'])
    combo.current(0)

    #1,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', im_ld, 'OUTPUT', im_gd)
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 1

    #2,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    cancel_b =  gf.GenFunc('button', im_bd, 'Cancel', im_gd)

    #2,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', im_bd, 'Next', im_gd)
    go_b.widg.config(command= lambda: iModel(frame=iManufacturer_frame))
    iManufacturer_frame.pack()

def iModel(frame):
    hideFrame(frame=frame)

    im_bd = button_dict
    im_ld = label_dict
    im_bd['master'] = iModel_frame
    im_ld['master'] = iModel_frame
    im_gd = gd
    
    placements = [[0,0],
                  [0,0],
                  [0,0]]

    #0,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', im_ld, 'Model:', im_gd)

    #0,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    models_list = alg.ManufactUniqueModels(choice='mm')[current_manufacturer]
    s=ttk.Style(master=None)
    s.theme_use('xpnative')
    combo = ttk.Combobox(master=iModel_frame, values=models_list, state='readonly')
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=im_gd['row'], column=im_gd['column'])
    combo.current(0)
    
    #1,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', im_ld, 'OUTPUT', im_gd)
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 1
    
    #2,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    back_b =  gf.GenFunc('button', im_bd, 'Cancel', im_gd)

    #2,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', im_bd, 'Next', im_gd)

    iModel_frame.pack()

home(frame=None)
root.mainloop()
