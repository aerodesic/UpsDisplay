# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Thu Aug 15 17:13:58 2024
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class EditNode(wx.Dialog):
    def __init__(self, data=None, schema=None, *args, **kwds):
        # begin wxGlade: EditNode.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)

        mainSizer = wx.FlexGridSizer(1, 2, 0, 0)

        mainSizer.Add((0, 0), 0, 0, 0)

        buttonSizer = wx.FlexGridSizer(1, 2, 0, 0)
        mainSizer.Add(buttonSizer, 0, wx.ALL | wx.EXPAND, 4)

        self.buttonOk = wx.Button(self, wx.ID_ANY, _("OK"))
        self.buttonOk.SetDefault()
        buttonSizer.Add(self.buttonOk, 0, 0, 0)

        self.buttonCancel = wx.Button(self, wx.ID_ANY, _("Cancel"))
        buttonSizer.Add(self.buttonCancel, 0, 0, 0)

        self.SetSizer(mainSizer)
        mainSizer.Fit(self)

        self.SetAffirmativeId(self.buttonOk.GetId())
        self.SetEscapeId(self.buttonCancel.GetId())

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnOkButton, self.buttonOk)
        # end wxGlade

    def OnOkButton(self, event):  # wxGlade: EditNode.<event_handler>
        print("Event handler 'OnOkButton' not implemented!")
        event.Skip()
# end of class EditNode
