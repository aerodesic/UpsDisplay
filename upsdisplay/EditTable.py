# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Thu Aug 15 10:46:33 2024
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
from wx.lib.mixins import listctrl
import wx.lib.agw.ultimatelistctrl as ULC
import sys
from copy import deepcopy
class MyListCtrl(ULC.UltimateListCtrl):
    def __init__(self, parent, ID, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        agwStyle=wx.LC_REPORT|ULC.ULC_USER_ROW_HEIGHT|ULC.ULC_SINGLE_SEL|ULC.ULC_BORDER_SELECT|ULC.ULC_AUTO_TOGGLE_CHILD|ULC.ULC_HRULES|ULC.ULC_VRULES
        super(MyListCtrl, self).__init__(id=ID, parent=parent, size=size, style=style, agwStyle=agwStyle)

    def AppendColumn(self, header):
        self.InsertColumn(self.GetColumnCount(), header, format=ULC.ULC_FORMAT_LEFT)

    def AppendRow(self, datalist):
        print("Append: %s" % datalist)
        row = self.InsertStringItem(sys.maxsize, datalist[0])
        for column in range(1, len(datalist)):
            field = datalist[column]
            self.SetColumnData(row, column, datalist[column])

    def SetColumnData(self, row, column, value):
        if type(value) is list:
            value = ", ".join(value)
        else:
            value = "%s" % value

        self.SetStringItem(row, column, value)

    def UpdateColumnWidths(self):
        for column in range(self.GetColumnCount()):
            # Set column width to largest of header width and data width
            self.SetColumnWidth(column, width=wx.LIST_AUTOSIZE)
            datawidth = self.GetColumnWidth(column)
            self.SetColumnWidth(column, width=wx.LIST_AUTOSIZE_USEHEADER)
            hdrwidth = self.GetColumnWidth(column)
            if hdrwidth < datawidth:
                self.SetColumnWidth(column, datawidth)
# end wxGlade


#
# data is the base of the config tree of data to be selected as a table
# fields is the fields within each data element that will be displayed in the list
# headers is the display-form of the field name (e.g. field='name' header='Node'
# editEntry is an optional dialog used to edit a table entry
#
class EditTable(wx.Dialog):
    def __init__(self, parent=None, title="Edit Table", config=None, fields=[], headers=[], editEntry=None, *args, **kwds):
        self.parent = parent
        self.config = config
        self.data = deepcopy(config["data"])
        self.schema = config["schema"]
        self.fields = fields
        self.headers = [config["headers"][node] for node in fields]
        self.editEntry = editEntry
        self.data_changed = False

        kwds['parent'] = parent

        # begin wxGlade: EditTable.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)

        mainSizer = wx.FlexGridSizer(2, 1, 0, 0)

        self.itemList = MyListCtrl(self, wx.ID_ANY, style=wx.LC_LIST)
        # Popluate the header
        for header in self.headers:
            self.itemList.AppendColumn(header)

        # Populate the rows
        for row in self.data:
            self.itemList.AppendRow([row[field] for field in self.fields])

        # Force autosize columns
        self.itemList.UpdateColumnWidths()
        #for col in range(0, len(self.headers) - 1):
        #    self.itemList.SetColumnWidth(col, width=wx.LIST_AUTOSIZE)
        #    datawidth = self.itemList.GetColumnWidth(col)
        #    self.itemList.SetColumnWidth(col, width=wx.LIST_AUTOSIZE_USEHEADER)
        #    hdrwidth = self.itemList.GetColumnWidth(col)
        #    if hdrwidth < datawidth:
        #        self.itemList.SetColumnWidth(col, datawidth)

        self.itemList.SetColumnWidth(len(self.headers) - 1, width=-3) #AUTOSIZE_FILL last column
        mainSizer.Add(self.itemList, 1, wx.ALL | wx.EXPAND, 0)

        buttonSizer = wx.FlexGridSizer(1, 4, 0, 0)
        mainSizer.Add(buttonSizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.buttonOk = wx.Button(self, wx.ID_OK, "")
        buttonSizer.Add(self.buttonOk, 0, 0, 0)

        self.buttonCancel = wx.Button(self, wx.ID_CANCEL, "")
        buttonSizer.Add(self.buttonCancel, 0, 0, 0)

        self.buttonNew = wx.Button(self, wx.ID_ADD, "")
        buttonSizer.Add(self.buttonNew, 0, 0, 0)

        self.buttonDelete = wx.Button(self, wx.ID_DELETE, "")
        buttonSizer.Add(self.buttonDelete, 0, 0, 0)

        mainSizer.AddGrowableRow(0)
        mainSizer.AddGrowableCol(0)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)

        self.SetAffirmativeId(self.buttonOk.GetId())
        self.SetEscapeId(self.buttonCancel.GetId())

        self.Layout()
        self.Maximize()
        self.Fit()
        self.Layout()
        self.SetTitle(title)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.itemList)
        self.Bind(wx.EVT_BUTTON, self.OnAddButton, self.buttonNew)
        self.Bind(wx.EVT_BUTTON, self.OnDeleteButton, self.buttonDelete)
        # end wxGlade

    # On selected item, open editEntry dialog
    def OnItemSelected(self, event):  # wxGlade: EditTable.<event_handler>
        item = event.GetEventObject()
        row = event.GetIndex()
        itemdata = deepcopy(self.data[row])
        name = item.GetItem(row).GetText()
        # print("OnItemSelected: item is %s index is %d" % (str(item), row))
        # print("Item data is %s name is %s" % (str(item.GetItem(row)), item.GetItem(row).GetText()))
        # print("Item data is %s" % itemdata)
        # print("Item data schema is %s" % self.schema)

        if self.editEntry is not None:
            # Must pass original headers 'dict' to get mappings
            dlg = self.editEntry(self, config=self.config, schema=self.schema, headers=self.config["headers"], data=itemdata)
            if dlg.ShowModal() == wx.ID_OK:
                # Change the parent data element with the results
                print("Results: changed %s row %s data %s" % (dlg.IsDataChanged(), row, dlg.GetResults()))
                if dlg.IsDataChanged():
                    results = dlg.GetResults()
                    # Refill this row's data
                    # self.itemList.SetColumnData(row, 
                    for column in range(len(self.fields)):
                        self.itemList.SetColumnData(row, column, results[self.fields[column]])
                    self.itemList.UpdateColumnWidths()
                    self.data[row] = results
                    self.data_changed = True
            else:
                print("editEntry failed")
                
        event.Skip()

    def OnAddButton(self, event):  # wxGlade: EditTable.<event_handler>
        print("Event handler 'OnAddButton' not implemented!")
        event.Skip()

    def OnDeleteButton(self, event):  # wxGlade: EditTable.<event_handler>
        print("Event handler 'OnDeleteButton' not implemented!")
        event.Skip()

    def IsDataChanged(self):
        return self.data_changed

    def GetResults(self):
        return self.data

# end of class EditTable
