# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri Mar 19 10:57:37 2021
#

import wx
# begin wxGlade: dependencies
# end wxGlade

import json
# begin wxGlade: extracode
from EditTable import *
from EditNode import *
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

from config import DEFAULT_CONFIG

class UpsDisplayFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        # begin wxGlade: UpsDisplayFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("UPS and PDU control"))

        self.mainPanel = wx.Panel(self, wx.ID_ANY)

        self.mainSizer = wx.FlexGridSizer(3, 1, 0, 3)

        topSizer = wx.FlexGridSizer(1, 0, 0, 0)
        self.mainSizer.Add(topSizer, 1, wx.ALL | wx.EXPAND, 5)

        self.statusSizer = wx.FlexGridSizer(0, 2, 10, 0)
        self.mainSizer.Add(self.statusSizer, 1, wx.ALL | wx.EXPAND, 5)

        buttonSizer = wx.FlexGridSizer(1, 3, 5, 10)
        self.mainSizer.Add(buttonSizer, 1, wx.ALIGN_CENTER, 0)

        self.nodeConfigButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Nodes"))
        self.nodeConfigButton.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        buttonSizer.Add(self.nodeConfigButton, 0, 0, 0)

        self.deviceConfigButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Devices"))
        self.deviceConfigButton.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        buttonSizer.Add(self.deviceConfigButton, 0, 0, 0)

        buttonSizer.AddGrowableCol(0)

        self.statusSizer.AddGrowableCol(1)

        topSizer.AddGrowableCol(0)

        self.mainSizer.AddGrowableRow(1)
        self.mainSizer.AddGrowableCol(0)
        self.mainPanel.SetSizer(self.mainSizer)

        self.mainSizer.Fit(self)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnNodeConfigButton, self.nodeConfigButton)
        self.Bind(wx.EVT_BUTTON, self.OnDevicesConfigButton, self.deviceConfigButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        # end wxGlade

        # self.ReloadObjects()

        self.statusSizer.Layout()
        self.mainSizer.Layout()
        self.Fit()

    def CloseUps(self):
        pass

    def OnClose(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        print('OnClose called')
        self.CloseUps()
        event.Skip()

    def OnNodeConfigButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        config = self.GetConfig()

        dlg=EditTable(self, title="Edit Nodes", config=config["nodes"], table_fields=config['nodes']['table_fields'], edit_fields=config['nodes']['edit_fields'], editEntry=EditNode)
        if dlg.ShowModal() == wx.ID_OK:
            print("IsDataChanged: %s" % str(dlg.IsDataChanged()))
            if dlg.IsDataChanged():
                config['nodes']['data'] = dlg.GetResults()
                self.PutConfig(config)
        event.Skip()

    def OnDevicesConfigButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        print("Event handler 'OnDevicesConfigButton' not implemented!")
        event.Skip()

    def GetConfig(self):
        try:
            with open(CONFIGFILE, "r") as f:
                config = json.load(f)
        except:
            config = DEFAULT_CONFIG
        return config

    def PutConfig(self, config):
        try:
            with open(CONFIGFILE, "w") as f:
                f.write(json.dumps(config, indent=4, sort_keys=True))
        except Exception as e:
            print("PutConfig: %s" % str(e))
        
# end of class UpsDisplayFrame

