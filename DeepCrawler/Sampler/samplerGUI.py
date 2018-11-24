from tkinter import Label,Button,Frame
import tkinter as tk

class SAMPLERGUI():
    def __init__(self, master):
        self.master = master
        master.title("Sampler (DeepCrawler)")
        master.geometry("1000x700")
        master.resizable(0,0)

        # Initialize Frame
        buttonFrame = Frame(self.master,side='top').pack()
        SetupFrame = Frame(self.master,side='bottom').pack()
        SampleFrame = Frame(self.master,side='bottom').pack()

        # Button Frame
        self.setup_button = Button(buttonFrame, width=50,height=2,text="Setup", command=master.quit)
        self.setup_button.pack(side = 'left')
        self.sample_button = Button(buttonFrame, width=50,height=2,text="Sample", command=master.quit)
        self.sample_button.pack(side = 'right')

        # Setup Frame
        # TODO Make Setup Frame and make crawler calling method
        

        # Sample Frame
        # TODO Make Sample Frame and make sampling and saving method