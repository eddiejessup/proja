#!/usr/bin/env python

import os
import wx
import wx.gizmos as gizmos
import csv


class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.CreateStatusBar()  # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
        menuSave = filemenu.Append(
            wx.ID_SAVE, "&Save", " Save the current file")
        menuAbout = filemenu.Append(
            wx.ID_ABOUT, "&About", " Information about this program")
        menuExit = filemenu.Append(
            wx.ID_EXIT, "E&xit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        # Adding the "filemenu" to the MenuBar
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        # self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnOpen(self, e):
            self.dirname = ''
            dlg = wx.FileDialog(
                self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
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
                # # self.cl = wx.CheckListBox(self, pos=(5, 20), choices=names)
                # for i in range(len(stockeds)):
                #     if stockeds[i]:
                #         self.cl.Check(i)

            self.tree = gizmos.TreeListCtrl(self, -1, style=
                                            wx.TR_DEFAULT_STYLE
                                            #| wx.TR_HAS_BUTTONS
                                            #| wx.TR_TWIST_BUTTONS
                                            #| wx.TR_ROW_LINES
                                            #| wx.TR_COLUMN_LINES
                                            #| wx.TR_NO_LINES
                                            | wx.TR_FULL_ROW_HIGHLIGHT
                                            )

            # create some columns
            self.tree.AddColumn("Main column")
            self.tree.AddColumn("Column 1")
            self.tree.AddColumn("Column 2")
            self.tree.SetMainColumn(0)  # the one with the tree in it...
            self.tree.SetColumnWidth(0, 175)

            self.root = self.tree.AddRoot("The Root Item")
            self.tree.SetItemText(self.root, "col 1 root", 1)
            self.tree.SetItemText(self.root, "col 2 root", 2)

            for x in range(15):
                txt = "Item %d" % x
                child = self.tree.AppendItem(self.root, txt)
                self.tree.SetItemText(child, txt + "(c1)", 1)
                self.tree.SetItemText(child, txt + "(c2)", 2)

                for y in range(5):
                    txt = "item %d-%s" % (x, chr(ord("a") + y))
                    last = self.tree.AppendItem(child, txt)
                    self.tree.SetItemText(last, txt + "(c1)", 1)
                    self.tree.SetItemText(last, txt + "(c2)", 2)

                    for z in range(5):
                        txt = "item %d-%s-%d" % (x, chr(ord("a") + y), z)
                        item = self.tree.AppendItem(last,  txt)
                        self.tree.SetItemText(item, txt + "(c1)", 1)
                        self.tree.SetItemText(item, txt + "(c2)", 2)

            self.tree.Expand(self.root)

            # self.tree.GetMainWindow().Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
            # self.tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate)

            dlg.Destroy()

    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in
        # wxWidgets.
        dlg = wx.MessageDialog(
            self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
