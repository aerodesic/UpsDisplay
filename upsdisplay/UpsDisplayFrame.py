# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri Mar 19 10:57:37 2021
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


import traceback
try:
    from queue import Queue
except:
    from Queue import Queue


from PlotGraph import *
import time
import math
import numpy as np
import json
from vartab import *
import math
from ConfigDialog import *

CONFIGFILE = ".upsdisplay"

class UpsDisplayFrame(wx.Frame):
    __DEFAULT_CONFIG = {
        'global': {
        },
        # numbered in display order
        'systems': {
            '0': {
                'name': u"Nimbus",
                'dns': "nimbus.aerodesic.net",
            },
            '1': {
                'name': u"Cumulus",
                'dns': "cumulus.aerodesic.net",
            },
            '2': {
                'name': u"Nas2",
                'dns': "nas2.aerodesic.net",
            },
            '3': {
                'name': u"Nas3",
                'dns': "nas3.aerodesic.net",
            },
        },
    }

    def __init__(self, *args, **kwds):
        # begin wxGlade: UpsDisplayFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("UPS and PDU control"))

        self.mainPanel = wx.Panel(self, wx.ID_ANY)

        self.mainSizer = wx.FlexGridSizer(3, 1, 3, 3)

        topSizer = wx.FlexGridSizer(1, 0, 0, 0)
        self.mainSizer.Add(topSizer, 1, wx.EXPAND, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.mainPanel, wx.ID_ANY, "", style=wx.TE_READONLY)
        topSizer.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)

        self.statusSizer = wx.FlexGridSizer(0, 2, 0, 0)
        self.mainSizer.Add(self.statusSizer, 1, wx.EXPAND, 0)

        buttonSizer = wx.FlexGridSizer(1, 4, 5, 10)
        self.mainSizer.Add(buttonSizer, 1, wx.ALIGN_CENTER, 0)

        self.startButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Start"))
        buttonSizer.Add(self.startButton, 0, 0, 0)

        self.stopButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Stop"))
        buttonSizer.Add(self.stopButton, 0, 0, 0)

        self.shutdownButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Shutdown"))
        buttonSizer.Add(self.shutdownButton, 0, 0, 0)

        self.Config = wx.Button(self.mainPanel, wx.ID_ANY, _("Config"))
        buttonSizer.Add(self.Config, 0, 0, 0)

        buttonSizer.AddGrowableCol(0)
        buttonSizer.AddGrowableCol(1)
        buttonSizer.AddGrowableCol(2)
        buttonSizer.AddGrowableCol(3)

        self.statusSizer.AddGrowableCol(1)

        topSizer.AddGrowableCol(0)

        self.mainSizer.AddGrowableRow(1)
        self.mainSizer.AddGrowableCol(0)
        self.mainPanel.SetSizer(self.mainSizer)

        self.mainSizer.Fit(self)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnStartButton, self.startButton)
        self.Bind(wx.EVT_BUTTON, self.OnStopButton, self.stopButton)
        self.Bind(wx.EVT_BUTTON, self.OnShutdownButton, self.shutdownButton)
        self.Bind(wx.EVT_BUTTON, self.OnConfigButton, self.Config)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        # end wxGlade

        self.__config = VarTab()
        self.__system_objects = {}

        # Try to load from config file and not not successful, preset the configuration
        try:
            with open(os.path.join(os.getenv("HOME"), CONFIGFILE)) as f:
                self.__config.Load(json.reads(f.read()))

        except:
            # Failed to load - reset config and load initial values
            self.__config.Load(self.__DEFAULT_CONFIG)

            try:
                with open(os.path.join(os.getenv("HOME"), CONFIGFILE), "w") as f:
                   f.write(json.dumps(self.__config.GetValue(), indent=4, sort_keys=True))

            except Exception as e:
                traceback.print_exc()

        self.ReloadObjects()


    def ReloadObjects(self):
        # Remove all children
        for index in sorted(list(self.__system_objects)):
            element = self.__system_objects[index]
            print("Removing item %s" % index)
            self.statusSizer.Detach(element['status'])
            self.statusSizer.Detach(element['button'])
            del self.__system_objects[index]

        self.statusSizer.SetRows(0)

        try:
            # Fetch list of graphs to be displayed, in order of appearance
            systems = self.__config.GetValue("systems")

            indices = sorted(list(systems))
            print("indices: %s" % indices)

            print("systems: %s" % systems)

            row = 0

            # For each graph, get configuration and allocate the graph
            for index in indices:
                system_object = self.__config.GetValue("%s" % index, base=systems)

                print("Add at %s item for %s (%s)" % (index, system_object["name"], system_object["dns"]))

                # Add the system name and status button (which doubles as control button)
                systemNameText = wx.StaticText(self.mainPanel, wx.ID_ANY, u"%s:" % system_object["name"])
                self.statusSizer.Add(systemNameText, proportion=1, border=0, flag=wx.ALIGN_CENTER)
                systemControlButton = wx.Button(self.mainPanel, wx.ID_ANY, u"---")
                self.statusSizer.Add(systemControlButton, proportion=1, border=0, flag=wx.EXPAND)

                self.__system_objects[index] = { 'status': systemNameText, 'button': systemControlButton }

        except Exception as e:
            traceback.print_exc()

        self.statusSizer.Layout()
        self.mainSizer.Layout()
        self.Fit()

    def OnClose(self, event):  # wxGlade: UpsDisplayFrae.<event_handler>
        self.CloseUps()
        event.Skip()

    def CloseUps(self):
        pass

    def OnClose(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        print("Event handler 'OnClose' not implemented!")
        event.Skip()
    def OnStartButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        print("Event handler 'OnStartButton' not implemented!")
        event.Skip()
    def OnStopButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        print("Event handler 'OnStopButton' not implemented!")
        event.Skip()
    def OnShutdownButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        self.ReloadObjects()
        event.Skip()
    def OnConfigButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        print("Event handler 'OnConfigButton' not implemented!")
        event.Skip()
# end of class UpsDisplayFrame

