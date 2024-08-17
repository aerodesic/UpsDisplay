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
    # choose can be 'zero-or-more', 'one-or-more' or 'any-one-of'
    def __init__(self, parent=None, choose="zero-or-more",choices=['a','b','c'], selected=[], title=None, *args, **kwds):
        kwds['parent'] = parent
        self.choose = choose
        self.choices = choices
        self.selected = selected
        print("TextCheckboxSelect: choose_one %s" % choose)
        print("                    choices %s" % str(choices))
        print("                    selected %s" % str(selected))
        # begin wxGlade: TextCheckboxSelect.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(_("Select zero or more items"))

        mainSizer = wx.FlexGridSizer(2, 1, 0, 0)

        self.choiceList = wx.CheckListBox(self, wx.ID_ANY, choices=[_("a"), _("b"), _("c")], style=wx.LB_SINGLE)
        self.choiceList.Clear()
        self.choiceList.InsertItems(self.choices, 0)
        self.choiceList.SetCheckedStrings(self.selected)
        mainSizer.Add(self.choiceList, 1, wx.ALL | wx.EXPAND, 1)

        buttonSizer = wx.FlexGridSizer(1, 2, 0, 0)
        mainSizer.Add(buttonSizer, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.buttonOK = wx.Button(self, wx.ID_OK, "")
        self.buttonOK.SetDefault()
        buttonSizer.Add(self.buttonOK, 0, 0, 0)

        self.buttonCANCEL = wx.Button(self, wx.ID_CANCEL, "")
        buttonSizer.Add(self.buttonCANCEL, 0, 0, 0)

        mainSizer.AddGrowableRow(0)
        mainSizer.AddGrowableCol(0)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)

        self.SetAffirmativeId(self.buttonOK.GetId())
        self.SetEscapeId(self.buttonCANCEL.GetId())

        self.Layout()
        if title is not None:
            self.SetTitle(title)
        self.Layout()
        mainSizer.Fit(self)
        self.Maximize()

        self.Bind(wx.EVT_CHECKLISTBOX, self.OnCheckboxItemSelected, self.choiceList)
        # end wxGlade

    # Return the current selected items in the checkbox list
    def GetSelectedItems(self):
        print("TextCheckboxSelect: GetSelectedItems returning %s" % str(list(self.choiceList.GetCheckedStrings())))
        return list(self.choiceList.GetCheckedStrings())

    def OnCheckboxItemSelected(self, event):  # wxGlade: TextCheckboxSelect.<event_handler>
        if "any-one-of" in self.choose:
            # Deselect all other items in the checkbox
            pass
        event.Skip()
# end of class TextCheckboxSelect
