# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Thu Aug 15 10:46:33 2024
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
from wx.lib.mixins import listctrl
class TableListCtrl(wx.ListCtrl, listctrl.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listctrl.ListCtrlAutoWidthMixin.__init__(self)
        self.setResizeColumn(0)
# end wxGlade


#
# data is the base of the config tree of data to be selected as a table
# fields is the fields within each data element that will be displayed in the list
# headers is the display-form of the field name (e.g. field='name' header='Node'
# editEntry is an optional dialog used to edit a table entry
#
class EditTable(wx.Dialog):
    def __init__(self, parent=None, data={}, fields=[], headers=[], editEntry=None, *args, **kwds):
        self.parent = parent
        self.data = data
        self.fields = fields
        self.headers = headers
        self.editEntry = editEntry

        kwds['parent'] = parent

        # begin wxGlade: EditTable.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle(_("dialog"))

        mainSizer = wx.FlexGridSizer(2, 1, 0, 0)

        self.itemList = TableListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        # Popluate the header
        for header in self.headers:
            self.itemList.AppendColumn(header)
        # Populate the rows
        for row in data:
            self.itemList.Append([row[field] for field in self.fields])
        mainSizer.Add(self.itemList, 1, wx.EXPAND, 0)

        buttonSizer = wx.StdDialogButtonSizer()
        mainSizer.Add(buttonSizer, 0, wx.ALIGN_CENTER | wx.ALL, 4)

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
        self.Maximize()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.itemList)
        # end wxGlade

    # On selected item, open editEntry dialog
    def OnItemSelected(self, event):  # wxGlade: EditTable.<event_handler>
        print("OnItemSelected: %s" % event.GetEventObject())
        if self.editEntry is not None:
            item = event.GetEventObject()
            dlg = self.editEntry(self, entry)
            if dlg.ShowModal() is wx.ID_OK:
                # Change the parent data element with the results
                pass
                
        event.Skip()

# end of class EditTable
