from ctypes.wintypes import HGDIOBJ
from re import I
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.font as font
import numpy as np
import GenFunctions as gf
import AlgoData as alg
import mysql.connector

mydb = mysql.connector.connect(host="sql6.freesqldatabase.com", user="sql6524697", password="RHmy8YbEy4", database="sql6524697")

#Creating window
root = Tk()
root.title('Used Car Pricing')

#MISC
pass_dot = '\u2022'

#FRAMES
signChoose_frame = LabelFrame(root)
signIn_frame = LabelFrame(root)
signUp_frame = LabelFrame(root)

home_frame = LabelFrame(root)

hist_frame = LabelFrame(root)

#CATEGORICAL input frames
iManufacturer_frame = LabelFrame(root)
iModel_frame = LabelFrame(root)
iCategory_frame = LabelFrame(root)
iFuelType_frame = LabelFrame(root)
iGearBox_frame = LabelFrame(root)
iDriveWheels_frame = LabelFrame(root)
iColor_frame = LabelFrame(root)

#NUMERICAL input frames
iNumericInpS1_frame = LabelFrame(root)
iNumericInpS2_frame = LabelFrame(root)

#OUTPUT frame
op_frame = LabelFrame(root)

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

c_enginevol = 0
c_levy = 0
c_cylinders = 0
c_airbags = 0
c_mileage = 0

categorical_cols = alg.CategValsUnique() #CATEGORICAL options

current_user = None

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
        for i in frame.winfo_children():
            i.grid_forget()
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

def SignChoose(frame):
    '''
    Sign In/Up FRAME
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)
    
    s_gd = gd
    s_bd = button_dict
    s_gd['ipady'] = 5
    s_bd['master'] = signChoose_frame
    s_bd['w'] = 25

    placements = [[0], [0], [0]]

    # 0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    signIn_b = gf.GenFunc('button', s_bd, 'Sign In', s_gd)
    signIn_b.widg.config(command= lambda: SignIn(frame=signChoose_frame))

    # 1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    signUp_b = gf.GenFunc('button', s_bd, 'Sign Up', s_gd)
    signUp_b.widg.config(command= lambda: SignUp(frame=signChoose_frame))

    # 2
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    guest_b = gf.GenFunc('button', s_bd, 'Continue As Guest', s_gd)
    guest_b.widg.config(command= lambda: home(frame=signChoose_frame))

    # 3
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    exit_b = gf.GenFunc('button', s_bd, 'Exit', s_gd)
    exit_b.widg.config(command= lambda: root.destroy())

    signChoose_frame.pack()
    
    current_user = None
    return

def SignIn(frame):
    '''
    Sign In FRAME
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)

    s_gd = gd
    s_bd = button_dict
    s_ld = label_dict
    s_ed = entry_dict
    s_gd['ipady'] = 5
    s_bd['master'] = signIn_frame
    s_ld['master'] = signIn_frame
    s_ed['master'] = signIn_frame
    # s_bd['w'] = 20

    placements = [[0,0],[0,0],[0,0],[0,0]]

    # 0,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    userPrompt_l = gf.GenFunc('label', s_ld, 'Username: ', s_gd)

    # 0,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    user_e = gf.GenFunc('entry', s_ed, StringVar(), s_gd)

    # 1,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    passPrompt_l = gf.GenFunc('label', s_ld, 'Password: ', s_gd)
    
    # 1,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    pass_e = gf.GenFunc('entry', s_ed, StringVar(), s_gd)
    pass_e.widg.config(show=pass_dot)
    
    # 2,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    s_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', s_ld, 'Enter Credentials', s_gd)
    s_gd['cspan'] = 1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)

    # 3,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', s_bd, 'back', s_gd)
    back_b.widg.config(command= lambda: SignChoose(frame=signIn_frame))

    # 3,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', s_bd, 'Sign In', s_gd)
    go_b.widg.config(command=lambda: CredVer(user_e.widg.get(), pass_e.widg.get(), msg_l))
    signIn_frame.pack()
    return

def SignUp(frame):
    '''
    Sign Up FRAME
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)

    s_gd = gd
    s_bd = button_dict
    s_ld = label_dict
    s_ed = entry_dict
    s_gd['ipady'] = 5
    s_bd['master'] = signUp_frame
    s_ld['master'] = signUp_frame
    s_ed['master'] = signUp_frame
    # s_bd['w'] = 20

    placements = [[0,0],[0,0],[0,0],[0,0],[0,0]]

    # 0,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    userPrompt_l = gf.GenFunc('label', s_ld, 'Username: ', s_gd)

    # 0,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    user_e = gf.GenFunc('entry', s_ed, StringVar(), s_gd)

    # 1,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    passPrompt_l = gf.GenFunc('label', s_ld, 'Password: ', s_gd)
    
    # 1,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    pass_e = gf.GenFunc('entry', s_ed, StringVar(), s_gd)
    pass_e.widg.config(show=pass_dot)

    # 2,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    confpassprompt_l = gf.GenFunc('label', s_ld, 'Confirm Password: ', s_gd)
    
    # 2,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    confpass_e = gf.GenFunc('entry', s_ed, StringVar(), s_gd)
    confpass_e.widg.config(show=pass_dot)

    # 3,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    s_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', s_ld, 'Enter Credentials', s_gd)
    s_gd['cspan'] = 1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)

    # 4,0
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', s_bd, 'Back', s_gd)
    back_b.widg.config(command= lambda: SignChoose(frame=signUp_frame))
    
    # 4,1
    s_gd['row'], s_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', s_bd, 'Sign In', s_gd)
    go_b.widg.config(command=lambda: SignUpConf(user_e.widg.get(), pass_e.widg.get(), confpass_e.widg.get(), msg_l))
    signUp_frame.pack()
    return

def home(frame):
    '''
    Homescreen to display available options(sign out, start pricing)
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)
    h_gd = gd
    h_bd = button_dict
    h_gd['ipady'] = 5
    h_bd['master'] = home_frame
    h_bd['w'] = 20
    
    placements = [[0],
                  [0],
                  [0]]

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    start_b = gf.GenFunc('button', h_bd, 'Start', h_gd)
    start_b.widg.config(command= lambda: iManufacturer(frame=home_frame))

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    disp = 'Sign Out'
    if current_user == None:
        disp = 'Back'
    back_b = gf.GenFunc('button', h_bd, disp, h_gd)
    back_b.widg.config(command= lambda: SignChoose(frame=home_frame))

    h_gd['row'], h_gd['column'], placements = GetFreeCoor(placements)
    history_b = gf.GenFunc('button', h_bd, 'History', h_gd)
    if current_user == None:
        history_b.widg.config(state = 'disabled')
    else:
        history_b.widg.config(state = 'active')
    history_b.widg.config(command=lambda: History(frame=home_frame))
    home_frame.pack()
    return

#History retrieving for user to see
def History(frame):
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)
    h_gd = gd
    h_bd = button_dict
    h_ld = label_dict
    h_ld['master'] = hist_frame
    h_gd['ipady'] = 0
    h_bd['master'] = hist_frame
    h_bd['w'] = 8
    
    global current_user

    def GetHistory():
        
        mycursor = mydb.cursor( )
        query = f"Select * from records where Username='{current_user}'"
        mycursor.execute(query)
        myres = mycursor.fetchall( )

        l = len(myres)
        n = 3
        li = [("Username",
        "Levy",
        "Product Year",
        "Leather Interior",
        "Engine Volume",
        "Mileage",
        "Cylinders",
        "Airbags",
        "Turbo",
        "Wheel Side",
        "Manufacturer",
        "Model",
        "Category",
        "Fuel Type",
        "Gear Box Type",
        "Drive Wheels",
        "Color")]
        try:
            for i in range(l-1,(l-n)-1,-1):
                temp1 = myres[i]
                temp = list(temp1)
                val = 'right'
                if temp[9] == 1:
                    val = 'left'
                del temp[10]
                temp[9] = val
                if temp[3] == 1:
                    temp[3] = "Yes"
                else:
                    temp[3] = "No"
                if temp[8] == 1:
                    temp[8] = "Yes"
                else:
                    temp[8] = "No"
                li.append(temp)     
                
            mydb.commit( )    
        except:
            pass

        
        return li
    h = GetHistory()

    print(h)
    print(len(h), len(h[0]))
    for i in range(len(h)):
        for j in range(len(h[0])-1):
            h_gd['row'], h_gd['column'] = i,j+1
            temp = gf.GenFunc('label', h_ld, h[i][j+1], h_gd)
    h_gd['row'], h_gd['column'] = len(h) + 1, 16
    back_b = gf.GenFunc('button', h_bd, 'Back', h_gd)
    back_b.widg.config(command= lambda: home(frame=hist_frame))
    
    hist_frame.pack()

    return

#
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
    #Hiding previous frame to avoid colisions
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
    cancel_b =  gf.GenFunc('button', im_bd, 'Cancel', im_gd)
    cancel_b.widg.config(command= lambda: home(frame=iManufacturer_frame))
    
    #1,1
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
    #Hiding previous frame to avoid colisions
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
    back_b =  gf.GenFunc('button', im_bd, 'Back', im_gd)
    back_b.widg.config(command=lambda: iManufacturer(frame=iModel_frame))
    
    #1,1
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
    #Hiding previous frame to avoid colisions
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
    back_b = gf.GenFunc('button', ic_bd, 'Back', ic_gd)
    back_b.widg.config(command=lambda: iModel(frame=iCategory_frame))

    #1,1
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
    #Hiding previous frame to avoid colisions
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
    back_b =  gf.GenFunc('button', if_bd, 'Back', if_gd)
    back_b.widg.config(command= lambda: iModel(frame=iFuelType_frame))

    #1,1
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
    #Hiding previous frame to avoid colisions
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
    back_b = gf.GenFunc('button', igb_bd, 'Back', igb_gd)
    back_b.widg.config(command= lambda: iFuelType(frame=iGearBox_frame))
    
    #1,1
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
    #Hiding previous frame to avoid colisions
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
    back_b = gf.GenFunc('button', id_bd, 'Back', id_gd)
    back_b.widg.config(command= lambda: iGearBox(frame=iDriveWheels_frame))

    #1,1
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
    #Hiding previous frame to avoid colisions
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
    back_b = gf.GenFunc('button', ic_bd, 'Back', ic_gd)
    back_b.widg.config(command=lambda: iDriveWheels(frame=iColor_frame))

    #1,1
    ic_gd['row'], ic_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', ic_bd, 'Next', ic_gd)
    go_b.widg.config(command=lambda: iNumericalInput_set1(frame=iColor_frame))

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
    return
#ALL FRAMES for taking CATEGORICAL input (Chronological)
def iNumericalInput_set1(frame):
    '''
    FRAME for taking first set of numerical inputs
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)

    in_bd = button_dict
    in_ld = label_dict
    in_ed = entry_dict
    in_bd['master'] = iNumericInpS1_frame
    in_ld['master'] = iNumericInpS1_frame
    in_ed['master'] = iNumericInpS1_frame
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
        go_b.widg.config(state='disabled')
        val = string.get()
        msg_l.widg.config(text='     ')
        if val.isnumeric() and '.' not in val:
            if int(val) in range(1950,2021):
                global c_year
                c_year = int(val)
                msg_l.widg.config(text='Valid Year')
                go_b.widg.config(state='enabled')
                return
            else:
                msg_l.widg.config(text='Out of range')
                return
        elif val == '':
            msg_l.widg.config(text='Year must be 1950 - 2020')
        else:
            msg_l.widg.config(text='Enter a number!')
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
    combo_turbo = ttk.Combobox(master=iNumericInpS1_frame, values=['Yes','No'], state='readonly', width=in_ed['width']-3)
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
    combo_leather = ttk.Combobox(master=iNumericInpS1_frame, values=['Yes','No'], state='readonly', width=in_ed['width']-3)
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
    combo_wheel = ttk.Combobox(master=iNumericInpS1_frame, values=['Left','Right'], state='readonly', width=in_ed['width']-3)
    #s.configure('small.TButton', font=(None, 11))
    combo_wheel.bind('<<ComboboxSelected>>', lambda x: UpdateNumericInput(combo_turbo.get(), combo_wheel.get(), combo_leather.get()))
    combo_wheel.grid(row=in_gd['row'], column=in_gd['column'], padx=10)
    combo_wheel.current(0)
    
    # 5,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', in_bd, 'Back', in_gd)
    back_b.widg.config(command= lambda: iColor(frame=iNumericInpS1_frame))

    # 5,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', in_bd, 'Next', in_gd)
    go_b.widg.config(command= lambda: iNumericalInput_set2(frame=iNumericInpS1_frame))

    UpdateNumericInput(combo_turbo.get(), combo_wheel.get(), combo_leather.get())
    iNumericInpS1_frame.pack()
    CheckYear(None, None, None)

    return

def iNumericalInput_set2(frame):
    '''
    FRAME for taking first set of numerical inputs
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)
    
    in_bd = button_dict
    in_ld = label_dict
    in_ed = entry_dict
    in_bd['master'] = iNumericInpS2_frame
    in_ld['master'] = iNumericInpS2_frame
    in_ed['master'] = iNumericInpS2_frame
    in_ed['width'] = 10
    in_gd = gd

    placements = [[0,0],
                  [0,0],
                  [0,0],
                  [0,0],
                  [0,0],
                  [0,0],
                  [0,0]]
    #Internal function for checking and assigning parameters in realtime
    def CheckAssignParams(var, i, mode):
        #Disabling button 
        go_b.widg.config(state='disabled')

        #Removing negative symbols
        s_engVol.set(s_engVol.get().strip('-').replace(',', ''))
        s_levy.set(s_levy.get().strip('-').replace(',',''))
        s_airbags.set(s_airbags.get().strip('-').replace(',',''))
        s_mileage.set(s_mileage.get().strip('-').replace(',',''))

        #Fetching values
        eng_vol = s_engVol.get()
        levy = s_levy.get()
        airbags = s_airbags.get()
        mileage = s_mileage.get()
        global c_enginevol, c_levy, c_cylinders, c_airbags, c_mileage
        c_cylinders = int(combo.get())

        # Nested func to check whether int, float or invalid
        def CheckNumeric(val, choice = 'int'):
            try:
                float(val)
            except ValueError:
                return False
            if choice == 'number':
                return True
            elif '.' not in val and choice == 'int':
                return True
            else:
                return False

        if CheckNumeric(eng_vol, 'number'):
            if float(eng_vol) > 0:
                c_enginevol = float(eng_vol)
        else:
            msg_l.widg.config(text='Enter a valid number (Engine Volume)!')
            return
        if CheckNumeric(levy, 'number'):
            if float(levy) >= 0:
                c_levy = float(levy) * 0.013 #Converting to dollars
        else:
            msg_l.widg.config(text='Enter a valid number (Levy)!')
            return
        if CheckNumeric(airbags, 'int'):
            if int(airbags) >= 0:
                c_airbags = int(airbags)
        else:
            msg_l.widg.config(text='Enter an integer (airbags)!')
            return
        if CheckNumeric(mileage, 'number'):
            if float(mileage) > 0:
                c_mileage = float(mileage) * 0.621371 #Kms to miles
        else:
            msg_l.widg.config(text='Enter a valid number (mileage)!')
            return
        msg_l.widg.config(text='Valid ')
        go_b.widg.config(state='enabled')
        return 


    # 0,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    engVolPrompt_l = gf.GenFunc('label', in_ld, 'Engine Volume (cc): ', in_gd)
    # 0,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    s_engVol = StringVar()
    s_engVol.trace_add('write', CheckAssignParams)
    engVol_e = gf.GenFunc('entry', in_ed, '', in_gd)
    engVol_e.widg.config(textvariable=s_engVol)

    # 1,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    levyPrompt_l = gf.GenFunc('label', in_ld, 'Levy (₹): ', in_gd)
    # 1,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    s_levy = StringVar()
    s_levy.trace_add('write', CheckAssignParams)
    levy_e = gf.GenFunc('entry', in_ed, s_levy, in_gd)

    # 2,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    cylindersPrompt_l = gf.GenFunc('label', in_ld, 'Cylinders: ', in_gd)
    # 2,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    cylinders = [i for i in range(1,17)]
    s=ttk.Style(master=None)
    combo = ttk.Combobox(master=iNumericInpS2_frame, values=cylinders, state='readonly', width=in_ed['width']-3)
    combo.bind('<<ComboboxSelected>>', lambda x: CheckAssignParams(None, None, None))
    s.configure('small.TButton', font=(None, 11))
    combo.grid(row=in_gd['row'], column=in_gd['column'])
    combo.current(0)


    # 3,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    airbagsPrompt_l = gf.GenFunc('label', in_ld, 'Airbags: ', in_gd)
    # 3,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    s_airbags = StringVar()
    s_airbags.trace_add('write', CheckAssignParams)
    airbags_e = gf.GenFunc('entry', in_ed, s_airbags, in_gd)

    # 4,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    mileagePrompt_l = gf.GenFunc('label', in_ld, 'Mileage (Km): ', in_gd)
    # 4,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    s_mileage = StringVar()
    s_mileage.trace_add('write', CheckAssignParams)
    mileage_e = gf.GenFunc('entry', in_ed, s_mileage, in_gd)

    # 5,0
    # 5,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    in_gd['cspan'] = 2
    msg_l = gf.GenFunc('label', in_ld, 'OUTPUT', in_gd)
    in_gd['cspan'] = 1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)

    # 6,0
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    back_b = gf.GenFunc('button', in_bd, 'Back', in_gd)
    back_b.widg.config(command= lambda: iNumericalInput_set1(frame=iNumericInpS2_frame))
    
    # 6,1
    in_gd['row'], in_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', in_bd, 'Predict', in_gd)
    go_b.widg.config(command= lambda: Predict(frame=iNumericInpS2_frame))

    CheckAssignParams(None, None, None)
    iNumericInpS2_frame.pack()
    return

def Predict(frame):
    '''
    FRAME for calculating and displaying OUTPUT, storing HISTORY too
    '''
    #Hiding previous frame to avoid colisions
    hideFrame(frame=frame)
    
    ip_bd = button_dict
    ip_ld = label_dict
    ip_bd['master'] = op_frame
    ip_ld['master'] = op_frame
    ip_gd = gd

    placements = [[0],
                  [0],
                  [0]]

    #0
    ip_gd['row'], ip_gd['column'], placements = GetFreeCoor(placements)
    prompt_l = gf.GenFunc('label', ip_ld, 'Price (₹)', ip_gd)

    #1
    ip_gd['row'], ip_gd['column'], placements = GetFreeCoor(placements)
    op_l = gf.GenFunc('label', ip_ld, 'Please Wait...', ip_gd)

    #2
    ip_gd['row'], ip_gd['column'], placements = GetFreeCoor(placements)
    go_b = gf.GenFunc('button', ip_bd, 'OK', ip_gd)
    go_b.widg.config(command= lambda: home(frame=op_frame), state='disabled')

    op_frame.pack()

    param_dict = {
        'levy': c_levy,
        'prod_year': c_year,
        'leather':c_leather,
        'engine_vol':c_enginevol,
        'mileage':c_mileage,
        'cylinders':c_cylinders,
        'airbags':c_airbags,
        'turbo':c_turbo,
        'left':0,
        'right':0,

        'manufacturer':c_manufacturer,
        'model':c_model,
        'category':c_category,
        'fuel_type':c_fueltype,
        'gear_box_type':c_gearbox,
        'drive_wheels':c_drivewheels,
        'color':c_color
    }
    if c_wheelSide == 'right':
        param_dict['right'] = 1
    else:
        param_dict['left'] = 1
    data = alg.ArrangeInput(params=param_dict).head()
    result = f'{alg.Predict(data):.2f}'
    op_l.widg.config(text= result)

    if current_user != None:
        RecordEntry(param_dict)

    go_b.widg.config(state='enabled')


    return

#Record Entry (history)

def RecordEntry(p):
    mycursor = mydb.cursor( )
    global current_user
    query = "INSERT INTO records values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # records = [(p['levy'], p['prod_year'], p['leather'], p['engine_vol'], p[])]
    records = [current_user]
    records.extend(p[i] for i in p.keys())
    records = [tuple(records)]
    mycursor.executemany(query,records)
    mydb.commit( )    
    

#User Verify for Signing up
def SignUpConf(user, password, conf_password, lab_obj):
    query = "INSERT INTO accounts values(%s,%s)"
    mycursor = mydb.cursor( )
    if(password == conf_password):
        acc = [(user,password)]
        try:
            mycursor.executemany(query,acc)
            mydb.commit( )
        except:
            lab_obj.widg.config(text='Username Already Exists!')
            return
        lab_obj.widg.config(text='Account Created')
        return
    lab_obj.widg.config(text='Passwords dont match')
    return

#Credentials verification for sign in
def CredVer(user, password, lab_obj):

    mycursorU = mydb.cursor( )
    mycursorP = mydb.cursor( )
    mycursorU.execute(f"select Username from accounts where Username='{user}'")
    log = False
    users = mycursorU.fetchall( ) #list 
    #print(users)
    if(users==[]):
        # account doesnt exist
        log = False
    else:
        mycursorP.execute(f"select Password from accounts where Username='{user}'")
        passwor = (mycursorP.fetchall( ))[0][0]
        #print(passwor)
        if(passwor==password):
            log = True
    
    if(log==True):
        users = users[0][0]
        #successful
        global current_user
        current_user = user
        print(f'{current_user=}')
        home(frame=signIn_frame)
        return
    # acc doesnt exist 
    lab_obj.widg.config(text='Invalid Credentials!')
    return
SignChoose(frame=None)
root.mainloop()
