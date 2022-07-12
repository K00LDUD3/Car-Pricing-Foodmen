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

#NUMERICAL input frames
iNumericInp_frame = LabelFrame(root)

#CLASS VARIABLES required
c_manufacturer = 'lexus' #First value is lexus
c_model = '' 
c_category = ''
c_gearbox = ''
c_fueltype = ''
c_drivewheels = ''
c_color = ''

c_leather = 0
c_turbo = 0
c_year = 0
c_wheelSide = ''

categorical_cols = alg.CategValsUnique() #CATEGORICAL options

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


def UpdateManufacturer(choice):
    global c_manufacturer
    choice = choice.strip().split(' ')[1]
    c_manufacturer = choice
    return

#ALL FRAMES for taking CATEGORICAL input (Chronological)
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
    combo = ttk.Combobox(master=iManufacturer_frame, values=manufacturer_list, state='readonly', width=20, style='small.TButton')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateManufacturer(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=im_gd['row'], column=im_gd['column'])
    combo.current(0)
    UpdateManufacturer(choice=combo.get())

    #1,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', im_ld, 'OUTPUT', im_gd)
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 1

    #2,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    cancel_b =  gf.GenFunc('button', im_bd, 'Cancel', im_gd)
    cancel_b.widg.config(command= lambda: home(frame=iManufacturer))
    
    #2,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', im_bd, 'Next', im_gd)
    go_b.widg.config(command= lambda: iModel(frame=iManufacturer_frame))

    iManufacturer_frame.pack()

def UpdateModel(choice):
    global c_model
    choice = choice.strip()
    choice = choice[choice.index(' ')+1::]
    c_model = choice
    return

def iModel(frame):
    '''
    FRAME for taking model as input
    '''
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
    models_dict = alg.ManufactUniqueModels(choice='mm')
    global c_manufacturer
    models_list = models_dict.get(c_manufacturer)
    models_list = ['   '+(str(i+1)+'. '+models_list[i]) for i in range(len(models_list))]
    s=ttk.Style(master=None)
    
    combo = ttk.Combobox(master=iModel_frame, values=list(models_list), state='readonly')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateModel(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=im_gd['row'], column=im_gd['column'])
    combo.current(0)
    UpdateModel(choice=combo.get())
    
    #1,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', im_ld, 'OUTPUT', im_gd)
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    im_gd['cspan'] = 1
    
    #2,0
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    back_b =  gf.GenFunc('button', im_bd, 'Back', im_gd)
    back_b.widg.config(command=lambda: iManufacturer(frame=iModel_frame))
    
    #2,1
    im_gd['row'], im_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', im_bd, 'Next', im_gd)
    go_b.widg.config(command= lambda: iCategory(frame=iModel_frame))
    iModel_frame.pack()

def UpdateCategory(choice):
    global c_category
    c_category = choice.strip()
def iCategory(frame):
    '''
    FRAME for taking category as input
    '''
    hideFrame(frame=frame)

    ic_bd = button_dict
    ic_ld = label_dict
    ic_bd['master'] = iCategory_frame
    ic_ld['master'] = iCategory_frame
    ic_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0]]
    
    #0,0
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', ic_ld, 'Category', ic_gd)

    #0,1
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    global c_model
    category_list = alg.FetchModelsCateg(model=c_model)
    UpdateCategory(choice=category_list[0])
    s=ttk.Style(master=None)
    combo = ttk.Combobox(master=iCategory_frame, values=list(category_list), state='readonly')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateCategory(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=ic_gd['row'], column=ic_gd['column'])
    combo.current(0)

    #1,0
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    ic_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', ic_ld, 'OUTPUT', ic_gd)
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    ic_gd['cspan'] = 1

    #2,0
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', ic_bd, 'Back', ic_gd)
    back_b.widg.config(command=lambda: iModel(frame=iCategory_frame))

    #2,1
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', ic_bd, 'Next', ic_gd)
    go_b.widg.config(command=lambda: iFuelType(frame=iCategory_frame))

    iCategory_frame.pack()
    return

def UpdateFuelType(choice):
    global c_fueltype
    c_fueltype = choice.strip()
    return

def iFuelType(frame):
    '''
    FRAME for taking fuel type as input
    '''
    hideFrame(frame=frame)

    if_bd = button_dict
    if_ld = label_dict
    if_bd['master'] = iFuelType_frame
    if_ld['master'] = iFuelType_frame
    if_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0]]
    
    #0,0
    if_gd['row'], if_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', if_ld, 'Fuel Type:', if_gd)

    #0,1
    if_gd['row'], if_gd['column'], placements = GetFreeCoor(placements)
    categories_list = categorical_cols['fuel_type']
    s=ttk.Style(master=None)
    combo = ttk.Combobox(master=iFuelType_frame, values=list(categories_list), state='readonly')
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=if_gd['row'], column=if_gd['column'])
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateFuelType(combo.get()))
    combo.current(0)
    UpdateFuelType(choice=combo.get())

    #1,0
    if_gd['row'], if_gd['column'], placements = GetFreeCoor(placements)
    if_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', if_ld, 'OUTPUT', if_gd)
    if_gd['row'], if_gd['column'], placements = GetFreeCoor(placements)
    if_gd['cspan'] = 1

    #2,0
    if_gd['row'], if_gd['column'], placements = GetFreeCoor(placements)
    back_b =  gf.GenFunc('button', if_bd, 'Back', if_gd)
    back_b.widg.config(command= lambda: iModel(frame=iFuelType_frame))

    #2,1
    if_gd['row'], if_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', if_bd, 'Next', if_gd)
    go_b.widg.config(command= lambda: iGearBox(frame=iFuelType_frame))

    iFuelType_frame.pack()

def UpdateGearboxType(choice):
    global c_gearbox
    c_gearbox = choice.strip()
    return

def iGearBox(frame):
    '''
    FRAME for taking gear box type as input
    '''
    hideFrame(frame=frame)

    igb_bd = button_dict
    igb_ld = label_dict
    igb_bd['master'] = iGearBox_frame
    igb_ld['master'] = iGearBox_frame
    igb_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0]]

    #0,0
    igb_gd['row'], igb_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', igb_ld, 'Gearbox: ', igb_gd)

    #0,1
    igb_gd['row'], igb_gd['column'], placements = GetFreeCoor(placements)
    gearbox_list = alg.CategValsUnique()['gear_box_type']
    s=ttk.Style(master=None)
    
    combo = ttk.Combobox(master=iGearBox_frame, values=list(gearbox_list), state='readonly')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateGearboxType(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=igb_gd['row'], column=igb_gd['column'])
    combo.current(0)
    UpdateGearboxType(choice=combo.get())

    #1,0
    igb_gd['row'], igb_gd['column'], placements = GetFreeCoor(placements)
    igb_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', igb_ld, 'OUTPUT', igb_gd)
    igb_gd['row'], igb_gd['column'], placements = GetFreeCoor(placements)
    igb_gd['cspan'] = 1

    #2,0
    igb_gd['row'], igb_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', igb_bd, 'Back', igb_gd)
    back_b.widg.config(command= lambda: iFuelType(frame=iGearBox_frame))
    #2,1
    igb_gd['row'], igb_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', igb_bd, 'Next', igb_gd)
    go_b.widg.config(command= lambda: iDriveWheels(frame=iGearBox_frame))

    iGearBox_frame.pack()
    return

def UpdateDriveWheels(choice):
    global c_drivewheels
    c_drivewheels = choice.strip()
def iDriveWheels(frame):
    '''
    FRAME for taking drive wheels as input
    '''
    hideFrame(frame=frame)

    id_bd = button_dict
    id_ld = label_dict
    id_bd['master'] = iDriveWheels_frame
    id_ld['master'] = iDriveWheels_frame
    id_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0]]

    #0,0
    id_gd['row'], id_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', id_ld, 'Drive Wheels: ', id_gd)

    #0,1
    id_gd['row'], id_gd['column'], placements = GetFreeCoor(placements)
    driveWheels_list = alg.CategValsUnique()['drive_wheels']
    s=ttk.Style(master=None)
    combo = ttk.Combobox(master=iDriveWheels_frame, values=list(driveWheels_list), state='readonly')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateDriveWheels(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=id_gd['row'], column=id_gd['column'])
    combo.current(0)
    UpdateDriveWheels(choice=combo.get())

    #1,0
    id_gd['row'], id_gd['column'], placements = GetFreeCoor(placements)
    id_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', id_ld, 'OUTPUT', id_gd)
    id_gd['row'], id_gd['column'], placements = GetFreeCoor(placements)
    id_gd['cspan'] = 1

    #2,0
    id_gd['row'], id_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', id_bd, 'Back', id_gd)
    back_b.widg.config(command= lambda: iGearBox(frame=iDriveWheels_frame))

    #2,1
    id_gd['row'], id_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', id_bd, 'Next', id_gd)
    go_b.widg.config(command= lambda: iColor(frame=iDriveWheels_frame))

    iDriveWheels_frame.pack()
    return

def UpdateColor(choice):
    global c_color
    c_color = choice.strip()
    return

def iColor(frame):
    '''
    FRAME for taking color as input
    '''
    hideFrame(frame=frame)

    ic_bd = button_dict
    ic_ld = label_dict
    ic_bd['master'] = iColor_frame
    ic_ld['master'] = iColor_frame
    ic_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0]]
    
    #0,0
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', ic_ld, 'Color: ', ic_gd)

    #0,1
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    input_l = gf.GenFunc('label', ic_ld, 'Category', ic_gd)
    color_list = alg.CategValsUnique()['color']
    s=ttk.Style(master=None)
    combo = ttk.Combobox(master=iColor_frame, values=list(color_list), state='readonly')
    combo.bind('<<ComboboxSelected>>', lambda x: UpdateColor(combo.get()))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=ic_gd['row'], column=ic_gd['column'])
    combo.current(0)
    UpdateColor(choice=combo.get())

    #1,0
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    ic_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', ic_ld, 'OUTPUT', ic_gd)
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    ic_gd['cspan'] = 1

    #2,0
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', ic_bd, 'Back', ic_gd)
    back_b.widg.config(command=lambda: iDriveWheels(frame=iColor_frame))

    #2,1
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', ic_bd, 'Next', ic_gd)
    go_b.widg.config(command=lambda: iNumericalInput(frame=iColor_frame))

    iColor_frame.pack()
    return

def UpdateNumericInput(turbo, wheel_side, leather):
    global c_wheelSide
    global c_turbo
    global c_leather
    if turbo.lower() == 'yes':
        c_turbo = 1
    else:
        c_turbo = 0

    if leather.lower() == 'yes':
        c_leather = 1
    else:
        c_leather = 0

    c_wheelSide = wheel_side.lower()
    print('UPDATE')
#ALL FRAMES for taking CATEGORICAL input (Chronological)
def iNumericalInput(frame):
    '''
    FRAME for taking all numerical inputs
    '''
    hideFrame(frame=frame)

    in_bd = button_dict
    in_ld = label_dict
    in_ed = entry_dict
    in_bd['master'] = iNumericInp_frame
    in_ld['master'] = iNumericInp_frame
    in_ed['master'] = iNumericInp_frame
    in_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0],
                  [0,0],
                  [0,0],
                  [0,0]]

    # 0,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    manufacPrompt_l = gf.GenFunc('label', in_ld, 'Manufacture Year: ', in_gd)

    # 0,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    in_ed['width'] = 10
    s=ttk.Style(master=None)
    s.theme_use('xpnative')
    def CheckYear(var, i, mode):
        val = string.get()
        msg_l.widg.config(text='')
        if val.isnumeric() and '.' not in val:
            if int(val) in range(1950,2021):
                global c_year
                c_year = int(val)
                msg_l.widg.config(text='Valid Year')
                return
            else:
                msg_l.widg.config(text='Out of range')
                return
        elif val == '':
            msg_l.widg.config(text='Year must be 1950 - 2020')
        return
    string = StringVar()
    string.trace_add('write', CheckYear)
    manufac_e = gf.GenFunc('entry', in_ed, '', in_gd)
    manufac_e.widg.config(textvariable=string)
    
    # 1,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    in_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', in_ld, 'Year must be 1950 - 2020', in_gd)
    in_gd['cspan'] = 1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)

    # 2,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    turboPrompt_l = gf.GenFunc('label', in_ld, 'Turbo: ', in_gd)

    # 2,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    s=ttk.Style(master=None)
    combo_turbo = ttk.Combobox(master=iNumericInp_frame, values=['Yes','No'], state='readonly', width=in_ed['width']-3)
    combo_turbo.bind('<<ComboboxSelected>>', lambda x: UpdateNumericInput(combo_turbo.get(), combo_wheel.get(), combo_leather.get()))
    s.configure('small.TButton', font=(None, 11))
    combo_turbo.grid(row=in_gd['row'], column=in_gd['column'])
    combo_turbo.current(0)

    # 3,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    leatherPrompt_l = gf.GenFunc('label', in_ld, 'Leather Interior: ', in_gd)

    # 3,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    s=ttk.Style(master=None)
    combo_leather = ttk.Combobox(master=iNumericInp_frame, values=['Yes','No'], state='readonly', width=in_ed['width']-3)
    combo_leather.bind('<<ComboboxSelected>>', lambda x: UpdateNumericInput(combo_turbo.get(), combo_wheel.get(), combo_leather.get()))
    s.configure('small.TButton', font=(None, 11))
    combo_leather.grid(row=in_gd['row'], column=in_gd['column'])
    combo_leather.current(0)

    # 4,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    wheelPrompt_l = gf.GenFunc('label', in_ld, 'Wheel Side: ', in_gd)

    # 4,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    #s=ttk.Style(master=None)
    combo_wheel = ttk.Combobox(master=iNumericInp_frame, values=['Left','Right'], state='readonly', width=in_ed['width']-3)
    #s.configure('small.TButton', font=(None, 11))
    combo_wheel.bind('<<ComboboxSelected>>', lambda x: UpdateNumericInput(combo_turbo.get(), combo_wheel.get(), combo_leather.get()))
    combo_wheel.grid(row=in_gd['row'], column=in_gd['column'], padx=10)
    combo_wheel.current(0)
    
    # 5,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', in_bd, 'Back', in_gd)
    back_b.widg.config(command= lambda: iColor(frame=iNumericInp_frame))

    # 5,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', in_bd, 'Next', in_gd)

    UpdateNumericInput(combo_turbo.get(), combo_wheel.get(), combo_leather.get())
    iNumericInp_frame.pack()
    return
iNumericalInput(frame=None)
root.mainloop()
