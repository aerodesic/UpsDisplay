# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Fri Mar 19 10:57:37 2021
#

import wx
# begin wxGlade: dependencies
# end wxGlade

import random
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

CONFIGFILE = ".upsdisplay"

from config import DEFAULT_CONFIG

class NodeItem(wx.Button):
    UNKNOWN = "Unknown"
    STOPPED = "Stopped"
    STARTING = "Starting"
    RUNNING = "Running"
    STOPPING = "Stopping"
    ERROR = "Error"

    def __init__(self, parent, id=wx.ID_ANY, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, validator=wx.DefaultValidator, name=wx.ButtonNameStr, nodeinfo=[]):
        # print("NodeItem: %s" % (str(nodeinfo)))

        self.status = None
        self.nodeinfo = nodeinfo

        super(NodeItem, self).__init__(parent, id, label, pos, size, style, validator, name)
        # self.SetLabel("%s\n%s" % (nodeinfo['name'], "<Status>"))

        font=wx.Font(10, wx.FONTFAMILY_DEFAULT,  wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, underline=False, faceName="Ubuntu", encoding=wx.FONTENCODING_DEFAULT)
        self.SetFont(font)

        self.SetStatus(self.UNKNOWN)

    def SetInfo(self, info):
        self.info.SetLabel(info)

    def SetStatus(self, status=UNKNOWN, msg=None):
        if status != self.status:
            if status == self.STOPPED:
                self.SetBackgroundColour(wx.Colour("white"))
                self.SetForegroundColour(wx.Colour("black"))

            elif status == self.STARTING:
                self.SetBackgroundColour(wx.Colour("yellow"))
                self.SetForegroundColour(wx.Colour("black"))

            elif status == self.RUNNING:
                self.SetBackgroundColour(wx.Colour("green"))
                self.SetForegroundColour(wx.Colour("white"))

            elif status == self.STOPPING:
                self.SetBackgroundColour(wx.Colour("orange"))
                self.SetForegroundColour(wx.Colour("black"))

            elif status == self.UNKNOWN:
                self.SetBackgroundColour(wx.Colour("black"))
                self.SetForegroundColour(wx.Colour("red"))

            elif status == self.ERROR:
                self.SetBackgroundColour(wx.Colour("red"))
                self.SetForegroundColour(wx.Colour("white"))

        self.SetLabel("%s\n%s" % (self.nodeinfo['name'], msg if msg else status))

class UpsDisplayFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        # begin wxGlade: UpsDisplayFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetTitle(_("UPS and PDU control"))

        self.mainPanel = wx.Panel(self, wx.ID_ANY)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mainSizer.Add(self.controlSizer, 0, wx.ALIGN_RIGHT | wx.ALL, 0)

        self.displayAllNodes = wx.CheckBox(self.mainPanel, wx.ID_ANY, _("Show All"))
        self.displayAllNodes.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.controlSizer.Add(self.displayAllNodes, 1, wx.ALIGN_CENTER_VERTICAL, 3)

        self.nodeConfigButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Nodes"))
        self.nodeConfigButton.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.controlSizer.Add(self.nodeConfigButton, 1, wx.ALL, 0)

        self.deviceConfigButton = wx.Button(self.mainPanel, wx.ID_ANY, _("Devices"))
        self.deviceConfigButton.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.controlSizer.Add(self.deviceConfigButton, 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.mainPanel, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.mainSizer.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)

        self.infoSizer = wx.WrapSizer(wx.HORIZONTAL)
        self.mainSizer.Add(self.infoSizer, 0, wx.ALL, 5)

        self.mainPanel.SetSizer(self.mainSizer)

        self.mainSizer.Fit(self)
        self.Layout()

        self.Bind(wx.EVT_CHECKBOX, self.OnShowAllClicked, self.displayAllNodes)
        self.Bind(wx.EVT_BUTTON, self.OnNodeConfigButton, self.nodeConfigButton)
        self.Bind(wx.EVT_BUTTON, self.OnDevicesConfigButton, self.deviceConfigButton)
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        # end wxGlade

        wx.CallLater(500, self.LoadObjects)

    def CloseUps(self):
        pass

    def OnClose(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        # print('OnClose called')
        self.CloseUps()
        event.Skip()

    def OnNodeConfigButton(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        config = self.GetConfig()

        dlg=EditTable(self, title="Edit Nodes", config=config["nodes"], editEntry=EditNode)
        if dlg.ShowModal() == wx.ID_OK:
            # print("IsDataChanged: %s" % str(dlg.IsDataChanged()))
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

    # 
    # Load the objects from the config information and propagate the Node display
    #
    def LoadObjects(self, config=None):
        if config is None:
            config = self.GetConfig()
        
        # Remove all info panels
        self.infoSizer.Clear(True)
        for node in config['nodes']['data']:
            if self.displayAllNodes.IsChecked() or node['showmain']:
                # Build Node object and add to display
                nodebutton = NodeItem(self.mainPanel, size=wx.Size(100, 100), nodeinfo=node)
                self.infoSizer.Add(nodebutton, 0, wx.ALL, 5)
                self.Bind(wx.EVT_BUTTON, self.OnNodeItemSelected, nodebutton)

        self.mainPanel.Layout()
        self.Fit()
    

    def PutConfig(self, config):
        try:
            with open(CONFIGFILE, "w") as f:
                f.write(json.dumps(config, indent=4, sort_keys=True))

        except Exception as e:
            print("PutConfig: %s" % str(e))

        self.LoadObjects(config)
        
    def OnNodeItemSelected(self, event):
        item = event.GetEventObject()
        # print("OnNodeItemSelected: %s '%s'" % (item.GetName(), item.nodeinfo))
        random_status = int(random.random() * 6)

        if random_status == 0:
            status = NodeItem.UNKNOWN
        elif random_status == 1:
            status = NodeItem.STARTING
        elif random_status == 2:
            status = NodeItem.RUNNING
        elif random_status == 3:
            status = NodeItem.STOPPING
        elif random_status == 4:
            status = NodeItem.STOPPED
        else:
            status = NodeItem.ERROR

        item.SetStatus(status)
        event.Skip()

    def OnShowAllClicked(self, event):  # wxGlade: UpsDisplayFrame.<event_handler>
        self.LoadObjects()
        event.Skip()
# end of class UpsDisplayFrame


