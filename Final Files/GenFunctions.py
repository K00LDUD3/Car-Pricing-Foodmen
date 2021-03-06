from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk

theme = 'xpnative'
class GenFunc:
    FONT = None
    widg = None
    text = ''
    wd = {} #Widget Dictionary
    gd = {}
    #frame = None
    def __init__(self, type, widg_dict, text, grid_dict) -> None:
        #Assigning param variables to class variables
        self.FONT = 11
        self.text = text
        self.wd = widg_dict
        self.gd = grid_dict
        '''
        gd = {
            'column':None,
            'row':None,
            'cspan':None,
            'rspan':None,
            'padx':None,
            'pady':None,
            'ipadx':None,
            'ipady':None
        }
        '''

        #checking type of widg (button, label, textbox), then call a function to create that specific widg
        if type.upper() == 'BUTTON':
            self.createB()
        elif type.upper() == 'LABEL':
            self.createL()
        elif type.upper() == 'ENTRY':
            self.createE()
        else:
            print('err: widget unidentified')
        return

    #Generating a BUTTON using parameters stored in a dictionary
    def createB(self):
        s=ttk.Style(master=None)
        s.theme_use(theme)
        s.configure(style=theme, font="Helvetica 10 bold")
        self.widg = Button(
            master= self.wd['master'],
            text=self.text,
            width=self.wd['w'],
            height=self.wd['height'],
            highlightbackground=self.wd['highl_color'],
            background=self.wd['bg'],
            foreground=self.wd['fg'],
            justify=self.wd['justify'],
            padx=self.wd['padx'],
            pady=self.wd['pady'],
            wraplength=self.wd['wraplength'],
            relief=self.wd['relief'],
            underline=self.wd['underline'],
            style='small.TButton'
        )

        s.configure('small.TButton', font=(None, self.FONT))
        self.widg.grid(
            column= self.gd['column'],
            row= self.gd['row'],
            columnspan= self.gd['cspan'],
            rowspan= self.gd['rspan'],
            padx= self.gd['padx'],
            pady= self.gd['pady'],
            ipadx= self.gd['ipadx'],
            ipady= self.gd['ipady']
        )
        '''
        button_widg_dict = {
            'master':Nones,
            'act_bg':None,
            'act_fg':None,
            'bg':None,
            'fg':None,
            'border':None,
            'font':None,
            'height':None,
            'highl_color':None,
            'image':None,
            'justify':None,
            'padx':None,
            'pady':None,
            'relief':None,
            'underline':None,
            'w':None,
            'wraplength':None
        }
        '''
        return

    #Generating a LABEL using parameters stored in a dictionary
    def createL(self):
        s=ttk.Style(master=None)
        s.theme_use(theme)
        self.widg = tk.Label(
            master= self.wd['master'],
            text=  self.text,
            anchor=  self.wd['anchor'],
            background=  self.wd['bg'],
            foreground=  self.wd['fg'],
            bitmap=  self.wd['bitmap'],
            bd=  self.wd['bd'],
            height=  self.wd['height'],
            image=  self.wd['image'],
            justify=  self.wd['justify'],
            padx=  self.wd['padx'],
            pady=  self.wd['pady'],
            relief=  self.wd['relief'],
            underline=  self.wd['underline'],
            width=  self.wd['w'],
            wraplength=  self.wd['wraplength'],
            #style='small.TButton'
            font=(None, 11)
        )
        s.configure('xpnative', font=(None, self.FONT))
        self.widg.grid(
            column= self.gd['column'],
            row= self.gd['row'],
            columnspan= self.gd['cspan'],
            rowspan= self.gd['rspan'],
            padx= self.gd['padx'],
            pady= self.gd['pady'],
            ipadx= self.gd['ipadx'],
            ipady= self.gd['ipady']
        )
        '''
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
        '''
        return

    #Generating a ENTRY (aka textbox) using parameters stored in a dictionary
    def createE(self):
        s=ttk.Style(master=None)
        s.theme_use(theme)
        self.widg = Entry(
            master= self.wd['master'],
            textvariable= self.text,
            width= self.wd['width'],
            bd= self.wd['bd'],
            background= self.wd['bg'],
            foreground= self.wd['fg'],
            font= self.wd['font'],
            insertofftime= self.wd['insertofftime'],
            insertontime= self.wd['insertontime'],
            relief= self.wd['relief'],
            highlightthickness= self.wd['highthick'],
            xscrollcommand= self.wd['xscrollcommand'],
        )
        self.widg.grid(
            column= self.gd['column'],
            row= self.gd['row'],
            columnspan= self.gd['cspan'],
            rowspan= self.gd['rspan'],
            padx= self.gd['padx'],
            pady= self.gd['pady'],
            ipadx= self.gd['ipadx'],
            ipady= self.gd['ipady']
        )
        '''
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
        '''
        return