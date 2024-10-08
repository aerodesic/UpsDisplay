# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Fri Aug 16 15:31:18 2024
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ShowMessage(wx.Dialog):
    def __init__(self, message="", heading=None, parent=None, buttons={"OK": wx.ID_OK}, *args, **kwds):
        kwds['parent'] = parent

        # begin wxGlade: ShowMessage.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((300, 200))
        self.SetTitle(_("Error"))

        mainSizer = wx.FlexGridSizer(2, 1, 0, 0)

        self.message_body = wx.TextCtrl(self, wx.ID_ANY, _("Message goes here"), style=wx.TE_CENTRE | wx.TE_MULTILINE | wx.TE_READONLY)
        self.message_body.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Ubuntu"))
        self.message_body.SetValue(message)
        if heading is not None:
            self.SetTitle(heading)
        mainSizer.Add(self.message_body, 0, wx.ALL | wx.EXPAND, 0)

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(buttonSizer, 1, wx.ALIGN_CENTER | wx.ALL, 0)

        mainSizer.AddGrowableRow(0)
        mainSizer.AddGrowableCol(0)
        self.SetSizer(mainSizer)

        self.Layout()
        for button_text in buttons:
            button = wx.Button(self, buttons[button_text], button_text)
            buttonSizer.Add(button, 0, 0, 0)
        # end wxGlade

# end of class ShowMessage
