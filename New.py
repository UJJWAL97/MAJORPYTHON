import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import tkintergui
from featureextractor import featureextractor
from scipy.special import expit
import numpy as np
import tkFont

from tkinter import messagebox as tkMessageBox


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = PHISHING_DETECTION_SYSTEM(root)
    tkintergui.init(root, top)
    root.mainloop()


w = None


def create_PHISHING_DETECTION_SYSTEM(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = PHISHING_DETECTION_SYSTEM(w)
    tkintergui.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_PHISHING_DETECTION_SYSTEM():
    global w
    w.destroy()
    w = None


def predict(str):
    temp = featureextractor(str)
    feature = []
    feature.append(1)
    for i in range(0, len(temp)):
        feature.append(temp[i])

    feature = np.array(feature)

    theta = ([
        -0.905877,
        1.474401,
        0.508719,
        - 0.633691,
        0.470666,
        - 0.312943,
        2.966641,
        2.875487,
        8.158240,
        - 2.047143,
        0.304662,
        0.488862,
        - 0.325627,
        2.664044,
        6.269800,
        2.363358,
        2.253615,
        0.461469,
        - 0.370708,
        - 0.356877,
        0.325309,
        - 0.095074,
        1.224013,
        1.076416,
        3.245338,
        0.724740])
    theta = np.array(theta)

    temp = np.dot(feature, theta)
    temp = expit(temp)
    if temp >= 0.5:
        return 1;
    else:
        return 0


class PHISHING_DETECTION_SYSTEM:

    def checkurl(self):
        url = self.urlInput.get()
        tkMessageBox.showinfo("Checking URL", url)
        if predict(url):
            self.Message2.configure(text='''Phishing''')
        else:
            self.Message2.configure(text='''Url is safe''')

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X1age1 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("1032x682+581+127")
        top.title("PHISHING DETECTION SYSTEM")
        top.configure(borderwidth="3")
        top.configure(background="#204424")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.inputFrame = Frame(top)
        self.inputFrame.place(relx=0.01, rely=0.04, relheight=0.29
                              , relwidth=0.97)
        self.inputFrame.configure(relief=GROOVE)
        self.inputFrame.configure(borderwidth="2")
        self.inputFrame.configure(relief=GROOVE)
        self.inputFrame.configure(background="#d9d9d9")
        self.inputFrame.configure(highlightbackground="#d9d9d9")
        self.inputFrame.configure(highlightcolor="black")
        self.inputFrame.configure(width=1005)

        self.urlInput = Entry(self.inputFrame)
        self.urlInput.place(relx=0.02, rely=0.46, height=46, relwidth=0.96)
        self.urlInput.configure(background="white")
        self.urlInput.configure(disabledforeground="#a3a3a3")
        self.urlInput.configure(font="TkFixedFont")
        self.urlInput.configure(foreground="#000000")
        self.urlInput.configure(highlightbackground="#d9d9d9")
        self.urlInput.configure(highlightcolor="black")
        self.urlInput.configure(insertbackground="black")
        self.urlInput.configure(selectbackground="#c4c4c4")
        self.urlInput.configure(selectforeground="black")

        self.inputMessage = Message(self.inputFrame)
        self.inputMessage.place(relx=0.02, rely=0.1, relheight=0.32
                                , relwidth=0.13)
        self.inputMessage.configure(background="#d9d9d9")
        self.inputMessage.configure(foreground="#000000")
        self.inputMessage.configure(highlightbackground="#d9d9d9")
        self.inputMessage.configure(highlightcolor="black")
        self.inputMessage.configure(relief=RIDGE)
        self.inputMessage.configure(text='''INPUT URL :''')
        self.inputMessage.configure(width=127)

        self.checkButton = Button(top)
        self.checkButton.place(relx=0.22, rely=0.35, height=92, width=558)
        self.checkButton.configure(activebackground="#d9d9d9")
        self.checkButton.configure(activeforeground="#000000")
        self.checkButton.configure(background="#888888")
        self.checkButton.configure(disabledforeground="#a3a3a3")
        self.checkButton.configure(foreground="#000000")
        self.checkButton.configure(highlightbackground="#d9d9d9")
        self.checkButton.configure(highlightcolor="black")
        self.checkButton.configure(pady="0")
        self.checkButton.configure(text='''CHECK URL''')
        self.checkButton.configure(command=self.checkurl)

        self.messageFrame = Frame(top)
        self.messageFrame.place(relx=0.02, rely=0.51, relheight=0.45
                                , relwidth=0.96)
        self.messageFrame.configure(relief=GROOVE)
        self.messageFrame.configure(borderwidth="2")
        self.messageFrame.configure(relief=GROOVE)
        self.messageFrame.configure(background="#d9d9d9")
        self.messageFrame.configure(highlightbackground="#d9d9d9")
        self.messageFrame.configure(highlightcolor="black")
        self.messageFrame.configure(width=995)

        self.Message2 = Message(self.messageFrame)
        self.Message2.place(relx=0.04, rely=0.13, relheight=0.09, relwidth=0.49)
        self.Message2.configure(background="#84d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''please Enter Url''')
        self.Message2.configure(width=891)


if __name__ == '__main__':
    vp_start_gui()
