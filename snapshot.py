#!/usr/bin/env python
# encoding=utf8
import psutil
from psutil._common import bytes2human
from datetime import datetime
import time
import configparser
import os
import json


class UserIO:

    def HelpPrint(self):
        ''' Print utility help to console for user '''
        print('\n        ----------------------------\n\
        snapshot utility (C)Com 2019\n\
        ----------------------------\n\
        Retrieve information of the system state each <timeinterval>\n\
        and write snapshots outputs in the file on text or JSON formats.\n\
        Each snapshot includes:\n\
        Snapshot #; TimeStamp;\n\
            ● Overall CPU load;\n\
            ● Overall memory usage;\n\
            ● Overall virtual memory usage;\n\
            ● IO information;\n\
            ● Network information.\n\
        Information outputs in file on text or JSON formats.\n\
        All paramerers are configurable thrue\
        snapshop.ini file in current directory\n\
        ----------------------------')

    def ConfigRead(self, path):

        ''' Read snapshop.ini configuration file and stores config variables\
        TimeInterval (default=1min) and OutputType (default=1 - json) '''
        global TimeInterval
        global OutputType
        if not os.path.exists(path):
            UserIO.HelpPrint(self)
            print('Error: snapshot.ini file not found')
            exit(1)
        config = configparser.ConfigParser()
        config.read(path)
        OutputType = config.get("common", "output")
        TimeInterval = int(config.get("common", "interval"))

    def write_ntuple(self, nt, filedescr):
        '''convert tuple's nt elements to human readable format'''
        for name in nt._fields:
            value = getattr(nt, name)
            if name != 'percent':
                value = bytes2human(value)
            filedescr.write(name.capitalize() + ': ' + str(value) + ';\n')

    def human_ntuple(self, nt):
        OutNT = {}
        for name in nt._fields:
            value = getattr(nt, name)
            if name != 'percent':
                value = bytes2human(value)
            OutNT[name.capitalize()] = value
        return OutNT


class CompInteract:

    def ReadCPU(self):
        psutil.cpu_percent(interval=None, percpu=False)
        return psutil.cpu_percent(interval=0.1, percpu=False)

    def ReadMem(self):
        return psutil.swap_memory()

    def ReadVirtMem(self):
        return psutil.virtual_memory()

    def ReadIO(self):
        return psutil.disk_io_counters(perdisk=False, nowrap=True)

    def ReadNet(self):
        return psutil.net_io_counters(pernic=False, nowrap=True)


def main():
    UI = UserIO()
    CI = CompInteract()
    Pathini = "snapshot.ini"
    PathOut = "output"
    global TimeInterval
    global OutputType
    TimeInterval = 0
    OutputType = ""
    if UI.ConfigRead(Pathini):
        exit(1)
    PathOut += "." + OutputType
    ouf = open(PathOut, 'w')
    ouf.close()
    i = 1
    # try:
    while 1:
        ouf = open(PathOut, 'a')
        if OutputType == 'json':
            data = {}
            data['Sn'] = []
            data['TimeStamp'] = []
            data['CPU'] = []
            data['Memory'] = []
            data['Virtual Memory'] = []
            data['I/O operations'] = []
            data['Network'] = []
            data['Sn'].append({'Snapshot #': i})
            data['TimeStamp'].append({'TimeStamp123:': str(datetime.now())})
            data['CPU'].append({'CPU utilization': CI.ReadCPU()})
            data['Memory'].append(UI.human_ntuple(CI.ReadMem()))
            data['Virtual Memory'].append(UI.human_ntuple(CI.ReadVirtMem()))
            data['I/O operations'].append(UI.human_ntuple(CI.ReadIO()))
            data['Network'].append(UI.human_ntuple(CI.ReadNet()))
            json.dump(data, ouf)
        elif OutputType == 'txt':
            ouf.write('Snapshot # ' + str(i)
                      + ' TimeStamp: ' + str(datetime.now()))
            ouf.write('\n------\nCPU\n')
            ouf.write(str(CI.ReadCPU()))
            ouf.write('\n------\nMemory\n')
            UI.write_ntuple(CI.ReadMem(), ouf)
            ouf.write('\n------\nVirtual Memory\n')
            UI.write_ntuple(CI.ReadVirtMem(), ouf)
            ouf.write('\n------\nI/O operations\n')
            UI.write_ntuple(CI.ReadIO(), ouf)
            ouf.write('\n------\nNetwork\n')
            UI.write_ntuple(CI.ReadNet(), ouf)
            ouf.write('\n------\n')
        else:
            UI.HelpPrint()
            exit(1)
        ouf.close()
        time.sleep(TimeInterval)
        i += 1


if __name__ == '__main__':
    main()
