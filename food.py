#!/usr/bin/env python

import os
import wx
import csv
import numpy as np

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", " Save the current file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnOpen(self, e):
            self.dirname = ''
            dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()

                with open(os.path.join(self.dirname, self.filename), 'r') as f:
                    r = csv.reader(f)
                    names, stockeds = [], []
                    for i, row in enumerate(r):
                        names.append(row[0])
                        stockeds.append(bool(int(row[1])))

                        # cb = wx.CheckBox(self, pos=(5, 20*i))
                        # nb = wx.StaticText(self, pos=(50, 20*i), label=name)
                        # cb.SetValue(stocked)
                        # self.controls.append(cb)
                self.cl = wx.CheckListBox(self, pos=(5, 20), choices=names)
                for i in range(len(stockeds)):
                    if stockeds[i]:
                        self.cl.Check(i)

            dlg.Destroy()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
import wx
