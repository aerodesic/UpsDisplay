# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Wed Aug 14 10:20:55 2024
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class TextCheckboxSelect(wx.Dialog):
    def __init__(self, parent=None, choose_one=False, choices=['a','b','c'], selected=[], title=None, *args, **kwds):
        kwds['parent'] = parent
        self.choices = choices
        self.selected = selected
        print("TextCheckboxSelect: choose_one %s" % choose_one)
        # begin wxGlade: TextCheckboxSelect.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(_("Select zero or more items"))

        mainSizer = wx.FlexGridSizer(2, 1, 0, 0)

        self.choiceList = wx.CheckListBox(self, wx.ID_ANY, choices=[_("a"), _("b"), _("c")], style=wx.LB_SINGLE)
        self.choiceList.Clear()
        self.choiceList.InsertItems(self.choices, 0)
        self.choiceList.SetCheckedStrings(self.selected)
        # oldstyle = self.choiceList.GetWindowStyle()
        # self.choiceList.SetWindowStyle(oldstyle | wx.LB_SINGLE if choose_one else wx.LB_MULTIPLE)
        mainSizer.Add(self.choiceList, 1, wx.ALL | wx.EXPAND, 1)

        buttonSizer = wx.StdDialogButtonSizer()
        mainSizer.Add(buttonSizer, 1, wx.ALIGN_CENTER, 0)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        buttonSizer.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        buttonSizer.AddButton(self.button_CANCEL)

        buttonSizer.Realize()

        mainSizer.AddGrowableRow(0)
        mainSizer.AddGrowableCol(0)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()
        if title is not None:
            self.SetTitle(title)
        self.Layout()
        mainSizer.Fit(self)
        self.Maximize()
        # end wxGlade

    # Return the current selected items in the checkbox list
    def GetSelectedItems(self):
        return list(self.choiceList.GetCheckedStrings())

# end of class TextCheckboxSelect
