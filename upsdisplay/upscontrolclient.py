# -*- coding: utf-8 -*-
#######################################################################################################
# Copyright 2019, CPAC Equipment, Inc.
# All rights reserved.
#######################################################################################################

#
# Simple wrapper class for DBUS activity (services and emitters)
#

from threading import *
import dbus
import dbus.service
import dbus.glib
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject as gobject
import syslog
import logging
import json

UPSCONTROL_BUSNAME_CONTROL = "com.robosity.upscontrol.control"
UPSCONTROL_SERVICENAME_CONTROL = "/com/robosity/upscontrol/control"


def callback(self, reason, data):
    print("__default_callback: reason '%s' data %s" % (reason, json.loads(data)))

class UpscontrolClient(Thread):

    def __init__(self, busname = UPSCONTROL_BUSNAME_CONTROL, servicename = UPSCONTROL_SERVICENAME_CONTROL, bus = None, callback = None, loop = None):
        super(UpscontrolClient, self).__init__()
        self.__busname_control = busname
        self.__servicename_control = servicename
        self.__bus = bus if bus else dbus.SystemBus()
        self.__loop = None
        self.__callback = callback
        self.__start_mutex = Lock()
        self.__start_mutex.acquire()
        self.__loop = loop
        self.__stoppable = self.__loop == None
        self.__indicate_data_receiver = None

    def __startup(self):
        if self.__callback:
            self.__callback("running", True)
        else:
            syslog.syslog("UpscontrolClient started")

    def __shutdown(self):
        if self.__callback:
            self.__callback("running", False)
        else:
            syslog.syslog("UpscontrolClient stopped")

    def __exception(self, e):
        if self.__callback:
            self.__callback("exception", e)
        else:
            syslog.syslog("UpscontrolClient exception '%s'" % e)

    # Run in thread generated by call to start()
    def run(self):
        # self.__gobject = DBusGMainLoop(set_as_default=True)
        self.__gobject = DBusGMainLoop()

        self.__upscontrol_obj = self.__bus.get_object(self.__busname_control, self.__servicename_control)
        self.__upscontrol = dbus.Interface(self.__upscontrol_obj, self.__busname_control)

        # Capture data reports
        self.__indicate_data_receiver = self.__bus.add_signal_receiver(self.__indicate_data_function, dbus_interface=self.__busname_control, signal_name="IndicateData")

        # Indicate started
        self.__startup()

        self.__start_mutex.release()

        # Launch loop if needed
        if self.__loop == None:
            try:
                if self.__loop == None:
                    self.__loop = gobject.MainLoop()
                    self.__loop.run()

            except Exception as e:
                self.__exception(e)

            self.__shutdown()

    def run_as_thread(self):
        self.__run_thread = Thread(target=self.run)
        self.__run_thread.start()
        return self.__run_thread

    def wait_running(self):
        self.__start_mutex.acquire()

    def stop(self):
        # Wait for stuff to quit and join
        if self.__loop and self.__stoppable:
            self.__loop.quit()
            self.join()

    def __indicate_data_function(self, reason, data):
        if self.__callback:
            self.__callback(reason, json.loads(data))

    def SetValue(self, name, value):
        self.__upscontrol.SetValue(name, json.dumps(value))

    def GetValue(self, name):
        return json.loads(self.__upscontrol.GetValue(name))

