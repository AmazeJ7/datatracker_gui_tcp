#####################
## Johnny's Branch ##
#####################

import socket
import datetime
import threading
from tkinter import *

key_order = ['BYTES_SENT',
             'BYTES_RECIEVED',
             '',
             'PKTS_SENT',
             'PKTS_RECIEVED',
             '',
             'INVALID_PKTS_RECIEVED',
             'CRC_FAILS',
             '',
             'STATUS',
             'EPS_PIC_RESET_FLAGS',
             'EPS_WDT',
             '',
             'SA1_BOOST_V',
             'SA1_V',
             'SA1_I',
             '',
             'SA2_BOOST_V',
             'SA2_V',
             'SA2_I',
             '',
             'SA3_BOOST_V',
             'SA3_V',
             'SA3_I',
             '',
             'SA_Ym_TEMP',
             'SA_Zp_TEMP',
             'SA_Zm_TEMP',
             'SA_Xp_TEMP',
             'SA_Yp_TEMP',
             '',
             'VBATT_V',
             'CHARGE_I',
             'DISCHARGE_I',
             'BATT1_TEMP',
             'BATT2_TEMP',
             '',
             '5VBUS_V',
             '5VBUS_I',
             '5VBUS_TEMP',
             '',
             '33VBUS_V',
             '33VBUS_I',
             '33VBUS_TEMP',
             '',
             '33VEPS_V',
             '33VEPS_I',
             '',
             'VBATT1_V',
             'VBATT1_I',
             '',
             'VBATT2_V',
             'VBATT2_I']

Coeff = {}
Coeff['LARGE_V'] =      [0,         0.01368,            'V']
Coeff['STD_I'] =        [0,         1.611328125,        'mA']
Coeff['STD_V'] =        [0,         0.005317,           'V']
Coeff['AD590_TEMP'] =   [-273,      0.5462080078,       'C']
Coeff['SA_TEMP'] =      [-273,      0.7661,             'C']
Coeff['33EPS_I'] =      [0,         0.035413769,        'mA']
Coeff['HIST_SA_P'] =    [0,         0.00142185467128,   'W']
Coeff['BUS_TEMP'] =     [-238.85,   0.5776,             'C']
Coeff['BUS_I'] =        [10,        10,                 'mA']
Coeff['EPS_WDT'] =      [0,         0.0115833333333333, 'Hours']
Coeff['None'] =         [0,         1,                  '']

tile_offset = 18
power_offset = 14
health_offset = 15

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect(('153.90.121.248', 3000))


class DataGui(Frame):
    def __init__(self, parent, *args, **kwargs):
        global power_offset
        Frame.__init__(self, parent, *args, **kwargs, bg='black')

        self.root = parent
        self.root.title("Data Gui")
        self.grid(column=0, row=0, sticky='nsew')

        self.clock()
        self.time_label = Label(self, height=3, bg='black', fg='white', text=datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")).grid(row=1, column=2)

        self.TIME_LABEL = Label(self,height=3, bg='black', fg='white', text="Time: ").grid(row=1, column=1,sticky=W)
        self.LAST_RECIEVED = Label(self,height=3, bg='black', fg='white', text="Last Recieved: ").grid(row=1, column=3,sticky=W)

        self.TILE_DATA = Label(self, bg='black', fg='white', text="TILE DATA: ")
        self.TILE_DATA.grid(row=4, column=1,sticky=W)
        self.S6_COUNT = Label(self, bg='black', fg='white', text="S6 Count: ")
        self.S6_COUNT.grid(row=5, column=1,sticky=W)
        self.ACT_TILES = Label(self, bg='black', fg='white', text="ACT_TILES: ")
        self.ACT_TILES.grid(row=5, column=3,sticky=W)
        self.FAULTED_TILES = Label(self, bg='black', fg='white', text="FAULTED TILES: ")
        self.FAULTED_TILES.grid(row=5, column=5,sticky=W)
        self.FAULTED_COUNT1 = Label(self, bg='black', fg='white', text="FAULTED COUNT1: ")
        self.FAULTED_COUNT1.grid(row=5, column=7,sticky=W)
        self.FAULTED_COUNT2 = Label(self, bg='black', fg='white', text="FAULTED COUNT2: ")
        self.FAULTED_COUNT2.grid(row=5, column=9,sticky=W)
        self.FAULTED_COUNT3 = Label(self, bg='black', fg='white', text="FAULTED COUNT3: ")
        self.FAULTED_COUNT3.grid(row=6, column=1,sticky=W)
        self.FAULTED_COUNT4 = Label(self, bg='black', fg='white', text="FAULTED COUNT4: ")
        self.FAULTED_COUNT4.grid(row=6, column=3,sticky=W)
        self.FAULTED_COUNT5 = Label(self, bg='black', fg='white', text="FAULTED COUNT5: ")
        self.FAULTED_COUNT5.grid(row=6, column=5,sticky=W)
        self.FAULTED_COUNT6 = Label(self, bg='black', fg='white', text="FAULTED COUNT6: ")
        self.FAULTED_COUNT6.grid(row=6, column=7,sticky=W)
        self.FAULTED_COUNT7 = Label(self, bg='black', fg='white', text="FAULTED COUNT7: ")
        self.FAULTED_COUNT7.grid(row=6, column=9,sticky=W)

        self.FAULTED_COUNT8 = Label(self, bg='black', fg='white', text="FAULTED COUNT8: ")
        self.FAULTED_COUNT8.grid(row=7, column=1,sticky=W)
        self.FAULTS_INJECTED = Label(self, bg='black', fg='white', text="FAULTS INJECTED: ")
        self.FAULTS_INJECTED.grid(row=7, column=3,sticky=W)
        self.TOTAL_FAULTS = Label(self, bg='black', fg='white', text="TOTAL FAULTS  : ")
        self.TOTAL_FAULTS.grid(row=7, column=5,sticky=W)
        self.MOVE_TILE_COUNT = Label(self, bg='black', fg='white', text="MOVE_TILE_COUNT: ")
        self.MOVE_TILE_COUNT.grid(row=7, column=7,sticky=W)
        self.NEXT_SPARE = Label(self, bg='black', fg='white', text="NEXT_SPARE    : ")
        self.NEXT_SPARE.grid(row=7, column=9,sticky=W)

        self.READBACK_FAULTS = Label(self, bg='black', fg='white', text="Readback Faults: ")
        self.READBACK_FAULTS.grid(row=8, column=1,sticky=W)
        self.WATCHDOG = Label(self, bg='black', fg='white', text="Watchdog: ")
        self.WATCHDOG.grid(row=8, column=3,sticky=W)
        self.ACT_PROC1 = Label(self, bg='black', fg='white', text="ACT PROC1: ")
        self.ACT_PROC1.grid(row=8, column=5,sticky=W)
        self.ACT_PROC2 = Label(self, bg='black', fg='white', text="ACT PROC2: ")
        self.ACT_PROC2.grid(row=8, column=7,sticky=W)
        self.ACT_PROC3 = Label(self, bg='black', fg='white', text="ACT PROC3: ")
        self.ACT_PROC3.grid(row=8, column=9,sticky=W)

        self.ACTPROCCNT1 = Label(self, bg='black', fg='white', text="ACTPROCCNT1: ")
        self.ACTPROCCNT1.grid(row=9, column=1,sticky=W)
        self.ACTPROCCNT2 = Label(self, bg='black', fg='white', text="ACTPROCCNT2: ")
        self.ACTPROCCNT2.grid(row=9, column=3,sticky=W)
        self.ACTPROCCNT3 = Label(self, bg='black', fg='white', text="ACTPROCCNT3: ")
        self.ACTPROCCNT3.grid(row=9, column=5,sticky=W)
        self.VOTER_COUNTS = Label(self, bg='black', fg='white', text="VOTER_COUNTS: ")
        self.VOTER_COUNTS.grid(row=9, column=7,sticky=W)
        self.CRC_TILE = Label(self, bg='black', fg='white', text="CRC : ")
        self.CRC_TILE.grid(row=9, column=9,sticky=W)
        self.SYNC = Label(self, bg='black', fg='white', text="SYNC: ")
        self.SYNC.grid(row=9, column=11,sticky=W)

        Frame(height=2, bg="black").grid(row=10,column=1,stick="nwes")

        self.HEALTH_DATA = Label(self, bg='black', fg='white', text="HEALTH DATA: ").grid(row=11, column=1, sticky=W)

        # VOLTAGE
        self.VOLTAGE_INS_IN = Label(self, bg='black', fg='white', text="VOLTAGE_INS_IN: ")
        self.VOLTAGE_INS_IN.grid(row=13, column=1, sticky=W)
        self.VOLTAGE_AVE_IN = Label(self, bg='black', fg='white', text="VOLTAGE_AVE_IN: ")
        self.VOLTAGE_AVE_IN.grid(row=14, column=1, sticky=W)
        self.VOLTAGE_MAX_IN = Label(self, bg='black', fg='white', text="VOLTAGE_MAX_IN: ")
        self.VOLTAGE_MAX_IN.grid(row=15, column=1, sticky=W)
        self.VOLTAGE_MIN_IN = Label(self, bg='black', fg='white', text="VOLTAGE_MIN_IN: ")
        self.VOLTAGE_MIN_IN.grid(row=16, column=1, sticky=W)
        self.VOLTAGE_INS_3V3D = Label(self, bg='black', fg='white', text="VOLTAGE_INS_3V3D: ")
        self.VOLTAGE_INS_3V3D.grid(row=17, column=1, sticky=W)
        self.VOLTAGE_AVE_3V3D = Label(self, bg='black', fg='white', text="VOLTAGE_AVE_3V3D: ")
        self.VOLTAGE_AVE_3V3D.grid(row=18, column=1, sticky=W)
        self.VOLTAGE_MAX_3V3D = Label(self, bg='black', fg='white', text="VOLTAGE_MAX_3V3D: ")
        self.VOLTAGE_MAX_3V3D.grid(row=19, column=1, sticky=W)
        self.VOLTAGE_MIN_3V3D = Label(self, bg='black', fg='white', text="VOLTAGE_MIN_3V3D: ")
        self.VOLTAGE_MIN_3V3D.grid(row=20, column=1, sticky=W)
        self.VOLTAGE_INS_2V5D = Label(self, bg='black', fg='white', text="VOLTAGE_INS_2V5D: ")
        self.VOLTAGE_INS_2V5D.grid(row=13, column=3, sticky=W)
        self.VOLTAGE_AVE_2V5D = Label(self, bg='black', fg='white', text="VOLTAGE_AVE_2V5D: ")
        self.VOLTAGE_AVE_2V5D.grid(row=14, column=3, sticky=W)
        self.VOLTAGE_MAX_2V5D = Label(self, bg='black', fg='white', text="VOLTAGE_MAX_2V5D: ")
        self.VOLTAGE_MAX_2V5D.grid(row=15, column=3, sticky=W)
        self.VOLTAGE_MIN_2V5D = Label(self, bg='black', fg='white', text="VOLTAGE_MIN_2V5D: ")
        self.VOLTAGE_MIN_2V5D.grid(row=16, column=3, sticky=W)
        self.VOLTAGE_INS_1V8D = Label(self, bg='black', fg='white', text="VOLTAGE_INS_1V8D: ")
        self.VOLTAGE_INS_1V8D.grid(row=17, column=3, sticky=W)
        self.VOLTAGE_AVE_1V8D = Label(self, bg='black', fg='white', text="VOLTAGE_AVE_1V8D: ")
        self.VOLTAGE_AVE_1V8D.grid(row=18, column=3, sticky=W)
        self.VOLTAGE_MAX_1V8D = Label(self, bg='black', fg='white', text="VOLTAGE_MAX_1V8D: ")
        self.VOLTAGE_MAX_1V8D.grid(row=19, column=3, sticky=W)
        self.VOLTAGE_MIN_1V8D = Label(self, bg='black', fg='white', text="VOLTAGE_MIN_1V8D: ")
        self.VOLTAGE_MIN_1V8D.grid(row=20, column=3, sticky=W)
        self.VOLTAGE_INS_1V0SD = Label(self, bg='black', fg='white', text="VOLTAGE_INS_1V0SD: ")
        self.VOLTAGE_INS_1V0SD.grid(row=13, column=5, sticky=W)
        self.VOLTAGE_AVE_1V0SD = Label(self, bg='black', fg='white', text="VOLTAGE_AVE_1V0SD: ")
        self.VOLTAGE_AVE_1V0SD.grid(row=14, column=5, sticky=W)
        self.VOLTAGE_MAX_1V0SD = Label(self, bg='black', fg='white', text="VOLTAGE_MAX_1V0SD: ")
        self.VOLTAGE_MAX_1V0SD.grid(row=15, column=5, sticky=W)
        self.VOLTAGE_MIN_1V0SD = Label(self, bg='black', fg='white', text="VOLTAGE_MIN_1V0SD: ")
        self.VOLTAGE_MIN_1V0SD.grid(row=16, column=5, sticky=W)
        self.VOLTAGE_INS_0V95AD = Label(self, bg='black', fg='white', text="VOLTAGE_INS_0V95AD: ")
        self.VOLTAGE_INS_0V95AD.grid(row=17, column=5, sticky=W)
        self.VOLTAGE_AVE_0V95AD = Label(self, bg='black', fg='white', text="VOLTAGE_AVE_0V95AD: ")
        self.VOLTAGE_AVE_0V95AD.grid(row=18, column=5, sticky=W)
        self.VOLTAGE_MAX_0V95AD = Label(self, bg='black', fg='white', text="VOLTAGE_MAX_0V95AD: ")
        self.VOLTAGE_MAX_0V95AD.grid(row=19, column=5, sticky=W)
        self.VOLTAGE_MIN_0V95AD = Label(self, bg='black', fg='white', text="VOLTAGE_MIN_0V95AD: ")
        self.VOLTAGE_MIN_0V95AD.grid(row=20, column=5, sticky=W)

        # CURRENTS
        self.CURRENT_INS_IN = Label(self, bg='black', fg='white', text="CURRENT_INS_IN: ")
        self.CURRENT_INS_IN.grid(row=13, column=   7, sticky=W)
        self.CURRENT_AVE_IN = Label(self, bg='black', fg='white', text="CURRENT_AVE_IN: ")
        self.CURRENT_AVE_IN.grid(row=14, column=   7, sticky=W)
        self.CURRENT_MAX_IN = Label(self, bg='black', fg='white', text="CURRENT_MAX_IN: ")
        self.CURRENT_MAX_IN.grid(row=15, column=   7, sticky=W)
        self.CURRENT_MIN_IN = Label(self, bg='black', fg='white', text="CURRENT_MIN_IN: ")
        self.CURRENT_MIN_IN.grid(row=16, column=   7, sticky=W)
        self.CURRENT_INS_3V3D = Label(self, bg='black', fg='white', text="CURRENT_INS_3V3D: ")
        self.CURRENT_INS_3V3D.grid(row=17, column= 7, sticky=W)
        self.CURRENT_AVE_3V3D = Label(self, bg='black', fg='white', text="CURRENT_AVE_3V3D: ")
        self.CURRENT_AVE_3V3D.grid(row=18, column= 7, sticky=W)
        self.CURRENT_MAX_3V3D = Label(self, bg='black', fg='white', text="CURRENT_MAX_3V3D: ")
        self.CURRENT_MAX_3V3D.grid(row=19, column= 7, sticky=W)
        self.CURRENT_MIN_3V3D = Label(self, bg='black', fg='white', text="CURRENT_MIN_3V3D: ")
        self.CURRENT_MIN_3V3D.grid(row=20, column= 7, sticky=W)
        self.CURRENT_INS_2V5D = Label(self, bg='black', fg='white', text="CURRENT_INS_2V5D: ")
        self.CURRENT_INS_2V5D.grid(row=13, column= 9, sticky=W)
        self.CURRENT_AVE_2V5D = Label(self, bg='black', fg='white', text="CURRENT_AVE_2V5D: ")
        self.CURRENT_AVE_2V5D.grid(row=14, column= 9, sticky=W)
        self.CURRENT_MAX_2V5D = Label(self, bg='black', fg='white', text="CURRENT_MAX_2V5D: ")
        self.CURRENT_MAX_2V5D.grid(row=15, column= 9, sticky=W)
        self.CURRENT_MIN_2V5D = Label(self, bg='black', fg='white', text="CURRENT_MIN_2V5D: ")
        self.CURRENT_MIN_2V5D.grid(row=16, column= 9, sticky=W)
        self.CURRENT_INS_1V8D = Label(self, bg='black', fg='white', text="CURRENT_INS_1V8D: ")
        self.CURRENT_INS_1V8D.grid(row=17, column= 9, sticky=W)
        self.CURRENT_AVE_1V8D = Label(self, bg='black', fg='white', text="CURRENT_AVE_1V8D: ")
        self.CURRENT_AVE_1V8D.grid(row=18, column= 9, sticky=W)
        self.CURRENT_MAX_1V8D = Label(self, bg='black', fg='white', text="CURRENT_MAX_1V8D: ")
        self.CURRENT_MAX_1V8D.grid(row=19, column= 9, sticky=W)
        self.CURRENT_MIN_1V8D = Label(self, bg='black', fg='white', text="CURRENT_MIN_1V8D: ")
        self.CURRENT_MIN_1V8D.grid(row=20, column= 9, sticky=W)
        self.CURRENT_INS_1V0SD = Label(self, bg='black', fg='white', text="CURRENT_INS_1V0SD: ")
        self.CURRENT_INS_1V0SD.grid(row=13, column= 11, sticky=W)
        self.CURRENT_AVE_1V0SD = Label(self, bg='black', fg='white', text="CURRENT_AVE_1V0SD: ")
        self.CURRENT_AVE_1V0SD.grid(row=14, column= 11, sticky=W)
        self.CURRENT_MAX_1V0SD = Label(self, bg='black', fg='white', text="CURRENT_MAX_1V0SD: ")
        self.CURRENT_MAX_1V0SD.grid(row=15, column= 11, sticky=W)
        self.CURRENT_MIN_1V0SD = Label(self, bg='black', fg='white', text="CURRENT_MIN_1V0SD: ")
        self.CURRENT_MIN_1V0SD.grid(row=16, column= 11, sticky=W)
        self.CURRENT_INS_0V95AD = Label(self, bg='black', fg='white', text="CURRENT_INS_0V95AD: ")
        self.CURRENT_INS_0V95AD.grid(row=17, column=11, sticky=W)
        self.CURRENT_AVE_0V95AD = Label(self, bg='black', fg='white', text="CURRENT_AVE_0V95AD: ")
        self.CURRENT_AVE_0V95AD.grid(row=18, column=11, sticky=W)
        self.CURRENT_MAX_0V95AD = Label(self, bg='black', fg='white', text="CURRENT_MAX_0V95AD: ")
        self.CURRENT_MAX_0V95AD.grid(row=19, column=11, sticky=W)
        self.CURRENT_MIN_0V95AD = Label(self, bg='black', fg='white', text="CURRENT_MIN_0V95AD: ")
        self.CURRENT_MIN_0V95AD.grid(row=20, column=11, sticky=W)

        self.A7_TEMPERATURE = Label(self, bg='black', fg='white', text="A7_TEMPERATURE: ")
        self.A7_TEMPERATURE.grid(row=13, column=13, stick=W)
        self.PC1_TEMPERATURE = Label(self, bg='black', fg='white', text="PC1_TEMPERATURE: ")
        self.PC1_TEMPERATURE.grid(row=14, column=13, stick=W)
        self.PC2_TEMPERATURE = Label(self, bg='black', fg='white', text="PC2_TEMPERATURE: ")
        self.PC2_TEMPERATURE.grid(row=15, column=13, stick=W)

        self.DAYS = Label(self, bg='black', fg='white', text="DAYS: ")
        self.DAYS.grid(row=16, column=   13, sticky=W)
        self.HOURS = Label(self, bg='black', fg='white', text="HOURS: ")
        self.HOURS.grid(row=17, column=  13, sticky=W)
        self.MINUTES = Label(self, bg='black', fg='white', text="MINUTES: ")
        self.MINUTES.grid(row=18, column=13, sticky=W)
        self.SECONDS = Label(self, bg='black', fg='white', text="SECONDS: ")
        self.SECONDS.grid(row=19, column=13, sticky=W)
        self.CRC_HEALTH = Label(self, bg='black', fg='white', text="CRC: ")
        self.CRC_HEALTH.grid(row=20, column=13, sticky=W)

        self.POWER_DATA = Label(self, bg='black', fg='white', text="POWER DATA: ")
        self.POWER_DATA.grid(row=15+power_offset, column=1, sticky=W)
        self.BYTES_SENT = Label(self, bg='black', fg='white', text="Bytes Sent: ")
        self.BYTES_SENT.grid(row=16+power_offset, column=1, sticky=W)
        self.BYTES_RECV = Label(self, bg='black', fg='white', text="Bytes Recv: ")
        self.BYTES_RECV.grid(row=16+power_offset, column=3, sticky=W)
        self.PKTS_SENT = Label(self, bg='black', fg='white', text="PKTS Sent: ")
        self.PKTS_SENT.grid(row=17+power_offset, column=1, sticky=W)
        self.PKTS_RECV = Label(self, bg='black', fg='white', text="PKTS Recv: ")
        self.PKTS_RECV.grid(row=17+power_offset, column=3, sticky=W)
        self.INVLD_PACK = Label(self, bg='black', fg='white', text="Invld Pack: ")
        self.INVLD_PACK.grid(row=18+power_offset, column=1, sticky=W)
        self.CRC_FAILS = Label(self, bg='black', fg='white', text="CRC  Fails: ")
        self.CRC_FAILS.grid(row=18+power_offset, column=3, sticky=W)
        self.STATUS = Label(self, bg='black', fg='white', text="status  : ")
        self.STATUS.grid(row=19+power_offset, column=1, sticky=W)
        self.RESET_FLAG = Label(self, bg='black', fg='white', text="Reset flag: ")
        self.RESET_FLAG.grid(row=19+power_offset, column=3, sticky=W)
        self.SA1_BOOST_V = Label(self, bg='black', fg='white', text="SA1_BOOST_V: ")
        self.SA1_BOOST_V.grid( row=20+power_offset, column=1, sticky=W)
        self.SA1_V = Label(self, bg='black', fg='white', text="SA1_V: ")
        self.SA1_V.grid(row=20+power_offset, column=3, sticky=W)
        self.SA2_BOOST_V = Label(self, bg='black', fg='white', text="SA2_BOOST_V: ")
        self.SA2_BOOST_V.grid( row=21+power_offset, column=1, sticky=W)
        self.SA2_V = Label(self, bg='black', fg='white', text="SA2_V: ")
        self.SA2_V.grid(row=21+power_offset, column=3, sticky=W)
        self.SA3_V = Label(self, bg='black', fg='white', text="SA3_V: ")
        self.SA3_V.grid(row=22+power_offset, column=1, sticky=W)
        self.SA3_BOOST_V = Label(self, bg='black', fg='white', text="SA3_BOOST_V: ")
        self.SA3_BOOST_V.grid( row=22+power_offset, column=3, sticky=W)

        self.BATT2_TEMP = Label(self, bg='black', fg='white', text="BATT2_TEMP: ")
        self.BATT2_TEMP.grid(row=23+power_offset, column=1, sticky=W)
        self.BATT1_TEMP = Label(self, bg='black', fg='white', text="BATT1_TEMP: ")
        self.BATT1_TEMP.grid(row=23+power_offset, column=3, sticky=W)

        self.FIVEV0BUS_V = Label(self, bg='black', fg='white', text="5V0BUS_V: ")
        self.FIVEV0BUS_V.grid(row=23+power_offset, column=5, sticky=W)
        self.THREEV3BUS_V = Label(self, bg='black', fg='white', text="3V3BUS_V: ")
        self.THREEV3BUS_V.grid(row=23+power_offset, column=7, sticky=W)

        self.VBATT2_V = Label(self, bg='black', fg='white', text="VBATT2_V: ")
        self.VBATT2_V.grid(row=24+power_offset, column=1, sticky=W)
        self.VBATT_V = Label(self, bg='black', fg='white', text="VBATT_V : ")
        self.VBATT_V.grid(row=24+power_offset, column=3, sticky=W)
        self.VBATT1_V = Label(self, bg='black', fg='white', text="VBATT1_V: ")
        self.VBATT1_V.grid(row=24+power_offset, column=5, sticky=W)

        self.THREEV3BUS_TEMP = Label(self, bg='black', fg='white', text="3V3BUS_TEMP: ")
        self.THREEV3BUS_TEMP.grid(row=25+power_offset, column=1, sticky=W)
        self.FIVEV0BUS_TEMP = Label(self, bg='black', fg='white', text="5V0BUS_TEMP: ")
        self.FIVEV0BUS_TEMP.grid(row=25+power_offset, column=3, sticky=W)

        self.THREEV3EPS_V = Label(self, bg='black', fg='white', text="3V3EPS_V   : ")
        self.THREEV3EPS_V.grid(row=25+power_offset, column=5, sticky=W)

        self.SA1_I = Label(self, bg='black', fg='white', text="SA1_I: ")
        self.SA1_I.grid(row=26+power_offset, column=1, sticky=W)
        self.SA2_I = Label(self, bg='black', fg='white', text="SA2_I: ")
        self.SA2_I.grid(row=26+power_offset, column=3, sticky=W)
        self.SA3_I = Label(self, bg='black', fg='white', text="SA3_I: ")
        self.SA3_I.grid(row=26+power_offset, column=5, sticky=W)

        self.DISCHARGE_I = Label(self, bg='black', fg='white', text="DISCHARGE_I: ")
        self.DISCHARGE_I.grid(row=27+power_offset, column=1, sticky=W)
        self.CHARGE_I = Label(self, bg='black', fg='white', text="CHARGE_I   : ")
        self.CHARGE_I.grid(row=27+power_offset, column=3, sticky=W)
        self.THREEV3BUS_I = Label(self, bg='black', fg='white', text="3V3BUS_I   : ")
        self.THREEV3BUS_I.grid(row=27+power_offset, column=5, sticky=W)
        self.VBATT1_I = Label(self, bg='black', fg='white', text="VBATT1_I   : ")
        self.VBATT1_I.grid(row=27+power_offset, column=7, sticky=W)
        self.VBATT2_I = Label(self, bg='black', fg='white', text="VBATT2_I   : ")
        self.VBATT2_I.grid(row=27+power_offset, column=9, sticky=W)

        self.SA_YM_TEMP = Label(self, bg='black', fg='white', text="SA_Ym_TEMP: ")
        self.SA_YM_TEMP.grid(row=28+power_offset, column=1, sticky=W)
        self.SA_ZP_TEMP = Label(self, bg='black', fg='white', text="SA_Zp_TEMP: ")
        self.SA_ZP_TEMP.grid(row=28+power_offset, column=3, sticky=W)
        self.SA_ZM_TEMP = Label(self, bg='black', fg='white', text="SA_Zm_TEMP: ")
        self.SA_ZM_TEMP.grid(row=28+power_offset, column=5, sticky=W)
        self.SA_XP_TEMP = Label(self, bg='black', fg='white', text="SA_Xp_TEMP: ")
        self.SA_XP_TEMP.grid(row=28+power_offset, column=7, sticky=W)
        self.SA_YP_TEMP = Label(self, bg='black', fg='white', text="SA_Yp_TEMP: ")
        self.SA_YP_TEMP.grid(row=28+power_offset, column=9, sticky=W)

        self.THREEV3EPS_I = Label(self, bg='black', fg='white', text="3V3EPS_I: ")
        self.THREEV3EPS_I.grid(row=29+power_offset, column=1, sticky=W)
        self.FIVEV0EPS_I = Label(self, bg='black', fg='white', text="5V0BUS_I: ")
        self.FIVEV0EPS_I.grid(row=29+power_offset, column=3, sticky=W)

        self.HIST_SA_1_P_1 = Label(self, bg='black', fg='white', text="HIST_SA_1_P_1: ")
        self.HIST_SA_1_P_1.grid(row=30+power_offset, column=1, sticky=W)
        self.HIST_SA_1_P_2 = Label(self, bg='black', fg='white', text="HIST_SA_1_P_2: ")
        self.HIST_SA_1_P_2.grid(row=30+power_offset, column=3, sticky=W)
        self.HIST_SA_1_P_3 = Label(self, bg='black', fg='white', text="HIST_SA_1_P_3: ")
        self.HIST_SA_1_P_3.grid(row=30+power_offset, column=5, sticky=W)
        self.HIST_SA_1_P_4 = Label(self, bg='black', fg='white', text="HIST_SA_1_P_4: ")
        self.HIST_SA_1_P_4.grid(row=30+power_offset, column=7, sticky=W)
        self.HIST_SA_1_P_5 = Label(self, bg='black', fg='white', text="HIST_SA_1_P_5: ")
        self.HIST_SA_1_P_5.grid(row=30+power_offset, column=9, sticky=W)
        self.HIST_SA_1_P_6 = Label(self, bg='black', fg='white', text="HIST_SA_1_P_6: ")
        self.HIST_SA_1_P_6.grid(row=30+power_offset, column=11, sticky=W)

        self.HIST_SA_2_P_1 = Label(self, bg='black', fg='white', text="HIST_SA_2_P_1: ")
        self.HIST_SA_2_P_1.grid(row=31+power_offset, column=1, sticky=W)
        self.HIST_SA_2_P_2 = Label(self, bg='black', fg='white', text="HIST_SA_2_P_2: ")
        self.HIST_SA_2_P_2.grid(row=31+power_offset, column=3, sticky=W)
        self.HIST_SA_2_P_3 = Label(self, bg='black', fg='white', text="HIST_SA_2_P_3: ")
        self.HIST_SA_2_P_3.grid(row=31+power_offset, column=5, sticky=W)
        self.HIST_SA_2_P_4 = Label(self, bg='black', fg='white', text="HIST_SA_2_P_4: ")
        self.HIST_SA_2_P_4.grid(row=31+power_offset, column=7, sticky=W)
        self.HIST_SA_2_P_5 = Label(self, bg='black', fg='white', text="HIST_SA_2_P_5: ")
        self.HIST_SA_2_P_5.grid(row=31+power_offset, column=9, sticky=W)
        self.HIST_SA_2_P_6 = Label(self, bg='black', fg='white', text="HIST_SA_2_P_6: ")
        self.HIST_SA_2_P_6.grid(row=31+power_offset, column=11, sticky=W)

        self.HIST_SA_3_P_1 = Label(self, bg='black', fg='white', text="HIST_SA_3_P_1: ")
        self.HIST_SA_3_P_1.grid(row=32+power_offset, column=1, sticky=W)
        self.HIST_SA_3_P_2 = Label(self, bg='black', fg='white', text="HIST_SA_3_P_2: ")
        self.HIST_SA_3_P_2.grid(row=32+power_offset, column=3, sticky=W)
        self.HIST_SA_3_P_3 = Label(self, bg='black', fg='white', text="HIST_SA_3_P_3: ")
        self.HIST_SA_3_P_3.grid(row=32+power_offset, column=5, sticky=W)
        self.HIST_SA_3_P_4 = Label(self, bg='black', fg='white', text="HIST_SA_3_P_4: ")
        self.HIST_SA_3_P_4.grid(row=32+power_offset, column=7, sticky=W)
        self.HIST_SA_3_P_5 = Label(self, bg='black', fg='white', text="HIST_SA_3_P_5: ")
        self.HIST_SA_3_P_5.grid(row=32+power_offset, column=9, sticky=W)
        self.HIST_SA_3_P_6 = Label(self, bg='black', fg='white', text="HIST_SA_3_P_6: ")
        self.HIST_SA_3_P_6.grid(row=32+power_offset, column=11, sticky=W)

        self.HIST_BATT_V_1 = Label(self, bg='black', fg='white', text="HIST_BATT_V_1: ")
        self.HIST_BATT_V_1.grid(row=33+power_offset, column=1, sticky=W)
        self.HIST_BATT_V_2 = Label(self, bg='black', fg='white', text="HIST_BATT_V_2: ")
        self.HIST_BATT_V_2.grid(row=33+power_offset, column=3, sticky=W)
        self.HIST_BATT_V_3 = Label(self, bg='black', fg='white', text="HIST_BATT_V_3: ")
        self.HIST_BATT_V_3.grid(row=33+power_offset, column=5, sticky=W)
        self.HIST_BATT_V_4 = Label(self, bg='black', fg='white', text="HIST_BATT_V_4: ")
        self.HIST_BATT_V_4.grid(row=33+power_offset, column=7, sticky=W)
        self.HIST_BATT_V_5 = Label(self, bg='black', fg='white', text="HIST_BATT_V_5: ")
        self.HIST_BATT_V_5.grid(row=33+power_offset, column=9, sticky=W)
        self.HIST_BATT_V_6 = Label(self, bg='black', fg='white', text="HIST_BATT_V_6: ")
        self.HIST_BATT_V_6.grid(row=33+power_offset, column=11, sticky=W)

        self.HIST_BATT_I_1 = Label(self, bg='black', fg='white', text="HIST_BATT_I_1: ")
        self.HIST_BATT_I_1.grid(row=34+power_offset, column=1, sticky=W)
        self.HIST_BATT_I_2 = Label(self, bg='black', fg='white', text="HIST_BATT_I_2: ")
        self.HIST_BATT_I_2.grid(row=34+power_offset, column=3, sticky=W)
        self.HIST_BATT_I_3 = Label(self, bg='black', fg='white', text="HIST_BATT_I_3: ")
        self.HIST_BATT_I_3.grid(row=34+power_offset, column=5, sticky=W)
        self.HIST_BATT_I_4 = Label(self, bg='black', fg='white', text="HIST_BATT_I_4: ")
        self.HIST_BATT_I_4.grid(row=34+power_offset, column=7, sticky=W)
        self.HIST_BATT_I_5 = Label(self, bg='black', fg='white', text="HIST_BATT_I_5: ")
        self.HIST_BATT_I_5.grid(row=34+power_offset, column=9, sticky=W)
        self.HIST_BATT_I_6 = Label(self, bg='black', fg='white', text="HIST_BATT_I_6: ")
        self.HIST_BATT_I_6.grid(row=34+power_offset, column=11, sticky=W)

        self.Misc_data_Powerchunk = Label(self, bg='black', fg='white', text="Misc data/Powerchunk: ")
        self.Misc_data_Powerchunk.grid(row=100, column=1, sticky=W)
        self.last_packet = Label(self, bg="black", fg="white", justify=LEFT, wraplength=800, text="")
        self.last_packet.grid(row=1, column=4, sticky=W)
        self.time_label = Label(self, height=3, bg="black", fg="white", text=datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"))
        self.time_label.grid(row=1, column=2)

    def update_tile(self, data):
        self.S6_COUNT["text"] = "S6 Count: " + data[0 + tile_offset:3 + tile_offset].hex()
        self.ACT_TILES["text"] = "ACT TILES: " + data[3 + tile_offset:5 + tile_offset].hex()
        self.FAULTED_TILES["text"] = "FAULTED TILES: " + data[5 + tile_offset:7 + tile_offset].hex()
        self.FAULTED_COUNT1["text"] = "FAULTED COUNT 1: " + data[7 + tile_offset:9 + tile_offset].hex()
        self.FAULTED_COUNT2["text"] = "FAULTED COUNT 2: " + data[9 + tile_offset:11 + tile_offset].hex()

        self.FAULTED_COUNT3["text"] = "FAULTED COUNT 3: " + data[11 + tile_offset:13 + tile_offset].hex()
        self.FAULTED_COUNT4["text"] = "FAULTED COUNT 4: " + data[13 + tile_offset:15 + tile_offset].hex()
        self.FAULTED_COUNT5["text"] = "FAULTED COUNT 5: " + data[15 + tile_offset:17 + tile_offset].hex()
        self.FAULTED_COUNT6["text"] = "FAULTED COUNT 6: " + data[17 + tile_offset:19 + tile_offset].hex()
        self.FAULTED_COUNT7["text"] = "FAULTED COUNT 7: " + data[19 + tile_offset:21 + tile_offset].hex()
        self.FAULTED_COUNT8["text"] = "FAULTED COUNT 8: " + data[23 + tile_offset:25 + tile_offset].hex()
        self.FAULTS_INJECTED["text"] = "FAULTS INJECTED: " + data[25 + tile_offset:27 + tile_offset].hex()
        self.TOTAL_FAULTS["text"] = "TOTAL FAULTS: " + data[27 + tile_offset:29 + tile_offset].hex()
        self.MOVE_TILE_COUNT["text"] = "MOVE TILE COUNT: " + data[29 + tile_offset:31 + tile_offset].hex()
        self.NEXT_SPARE["text"] = "NEXT SPARE: " + data[31 + tile_offset:32 + tile_offset].hex()
        self.READBACK_FAULTS["text"] = "Readback Faults: " + data[33 + tile_offset:34 + tile_offset].hex()
        self.WATCHDOG["text"] = "Watchdog: " + data[34 + tile_offset:35 + tile_offset].hex()
        self.ACT_PROC1["text"] = "ACT PROC1: " + data[35 + tile_offset:36 + tile_offset].hex()
        self.ACT_PROC2["text"] = "ACT PROC2: " + data[36 + tile_offset:37 + tile_offset].hex()
        self.ACT_PROC3["text"] = "ACT PROC3: " + data[37 + tile_offset:38 + tile_offset].hex()
        self.ACTPROCCNT1["text"] = "ACTPROCCNT1" + data[38 + tile_offset:40 + tile_offset].hex()
        self.ACTPROCCNT2["text"] = "ACTPROCCNT2" + data[40 + tile_offset:42 + tile_offset].hex()
        self.ACTPROCCNT3["text"] = "ACTPROCCNT3" + data[42 + tile_offset:44 + tile_offset].hex()
        self.VOTER_COUNTS["text"] = "VOTER COUNTS: " + data[44 + tile_offset:46 + tile_offset].hex()
        self.CRC_TILE["text"] = "CRC: " + data[46 + tile_offset:48 + tile_offset].hex()
        self.SYNC["text"] = "SYNC: " + data[48 + tile_offset:49 + tile_offset].hex()

    def update_health(self, data):
        # VOLTAGES
        self.VOLTAGE_INS_IN["text"] = "VOLTAGE_INS_IN: " + str(int(data[2 + health_offset:4 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_AVE_IN["text"] = "VOLTAGE_INS_IN: " + str(int(data[4 + health_offset:6 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MAX_IN["text"] = "VOLTAGE_INS_IN: " + str(int(data[6 + health_offset:8 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MIN_IN["text"] = "VOLTAGE_INS_IN: " + str(int(data[8 + health_offset:10 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_INS_3V3D["text"] = "VOLTAGE_INS_3V3D: " + str(int(data[10 + health_offset:12 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_AVE_3V3D["text"] = "VOLTAGE_INS_3V3D: " + str(int(data[12 + health_offset:14 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MAX_3V3D["text"] = "VOLTAGE_INS_3V3D: " + str(int(data[14 + health_offset:16 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MIN_3V3D["text"] = "VOLTAGE_INS_3V3D: " + str(int(data[16 + health_offset:18 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_INS_2V5D["text"] = "VOLTAGE_INS_2V5D: " + str(int(data[18 + health_offset:20 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_AVE_2V5D["text"] = "VOLTAGE_INS_2V5D: " + str(int(data[20 + health_offset:22 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MAX_2V5D["text"] = "VOLTAGE_INS_2V5D: " + str(int(data[22 + health_offset:24 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MIN_2V5D["text"] = "VOLTAGE_INS_2V5D: " + str(int(data[24 + health_offset:26 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_INS_1V8D["text"] = "VOLTAGE_INS_1V8D: " + str(int(data[26 + health_offset:28 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_AVE_1V8D["text"] = "VOLTAGE_INS_1V8D: " + str(int(data[28 + health_offset:30 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MAX_1V8D["text"] = "VOLTAGE_INS_1V8D: " + str(int(data[30 + health_offset:32 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MIN_1V8D["text"] = "VOLTAGE_INS_1V8D: " + str(int(data[32 + health_offset:34 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_INS_1V0SD["text"] = "VOLTAGE_INS_1V0SD: " + str(int(data[34 + health_offset:36 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_AVE_1V0SD["text"] = "VOLTAGE_INS_1V0SD: " + str(int(data[36 + health_offset:38 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MAX_1V0SD["text"] = "VOLTAGE_INS_1V0SD: " + str(int(data[38 + health_offset:40 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MIN_1V0SD["text"] = "VOLTAGE_INS_1V0SD: " + str(int(data[40 + health_offset:42 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_INS_0V95AD["text"] = "VOLTAGE_INS_0V95AD: " + str(int(data[42 + health_offset:44 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_AVE_0V95AD["text"] = "VOLTAGE_INS_0V95AD: " + str(int(data[44 + health_offset:46 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MAX_0V95AD["text"] = "VOLTAGE_INS_0V95AD: " + str(int(data[46 + health_offset:48 + health_offset].hex(), 16) / 1000) + " V"
        self.VOLTAGE_MIN_0V95AD["text"] = "VOLTAGE_INS_0V95AD: " + str(int(data[48 + health_offset:50 + health_offset].hex(), 16) / 1000) + " V"

        # CURRENTS
        self.CURRENT_INS_IN["text"] = "CURRENT INS IN: " + str(int(data[48 + 2 + health_offset: 48 + 4 + health_offset].hex(), 16))
        self.CURRENT_AVE_IN["text"] = "CURRENT AVE IN: " + str(int(data[48 + 4 + health_offset: 48 + 6 + health_offset].hex(), 16))
        self.CURRENT_MAX_IN["text"] = "CURRENT MAX IN: " + str(int(data[48 + 6 + health_offset: 48 + 8 + health_offset].hex(), 16))
        self.CURRENT_MIN_IN["text"] = "CURRENT MIN IN: " + str(int(data[48 + 8 + health_offset: 48 + 10 + health_offset].hex(), 16))
        self.CURRENT_INS_3V3D["text"] = "CURRENT INS 3V3D: " + str(int(data[48 + 10 + health_offset:48 + 12 + health_offset].hex(), 16))
        self.CURRENT_AVE_3V3D["text"] = "CURRENT AVE 3V3D: " + str(int(data[48 + 12 + health_offset:48 + 14 + health_offset].hex(), 16))
        self.CURRENT_MAX_3V3D["text"] = "CURRENT MAX 3V3D: " + str(int(data[48 + 14 + health_offset:48 + 16 + health_offset].hex(), 16))
        self.CURRENT_MIN_3V3D["text"] = "CURRENT MIN 3V3D: " + str(int(data[48 + 16 + health_offset:48 + 18 + health_offset].hex(), 16))
        self.CURRENT_INS_2V5D["text"] = "CURRENT INS 2V5D: " + str(int(data[48 + 18 + health_offset:48 + 20 + health_offset].hex(), 16))
        self.CURRENT_AVE_2V5D["text"] = "CURRENT AVE 2V5D: " + str(int(data[48 + 20 + health_offset:48 + 22 + health_offset].hex(), 16))
        self.CURRENT_MAX_2V5D["text"] = "CURRENT MAX 2V5D: " + str(int(data[48 + 22 + health_offset:48 + 24 + health_offset].hex(), 16))
        self.CURRENT_MIN_2V5D["text"] = "CURRENT MIN 2V5D: " + str(int(data[48 + 24 + health_offset:48 + 26 + health_offset].hex(), 16))
        self.CURRENT_INS_1V8D["text"] = "CURRENT INS 1V8D: " + str(int(data[48 + 26 + health_offset:48 + 28 + health_offset].hex(), 16))
        self.CURRENT_AVE_1V8D["text"] = "CURRENT AVE 1V8D: " + str(int(data[48 + 28 + health_offset:48 + 30 + health_offset].hex(), 16))
        self.CURRENT_MAX_1V8D["text"] = "CURRENT MAX 1V8D: " + str(int(data[48 + 30 + health_offset:48 + 32 + health_offset].hex(), 16))
        self.CURRENT_MIN_1V8D["text"] = "CURRENT MIN 1V8D: " + str(int(data[48 + 32 + health_offset:48 + 34 + health_offset].hex(), 16))
        self.CURRENT_INS_1V0SD["text"] = "CURRENT INS 1V0SD: " + str(int(data[48 + 34 + health_offset:48 + 36 + health_offset].hex(), 16))
        self.CURRENT_AVE_1V0SD["text"] = "CURRENT AVE 1V0SD: " + str(int(data[48 + 36 + health_offset:48 + 38 + health_offset].hex(), 16))
        self.CURRENT_MAX_1V0SD["text"] = "CURRENT MAX 1V0SD: " + str(int(data[48 + 38 + health_offset:48 + 40 + health_offset].hex(), 16))
        self.CURRENT_MIN_1V0SD["text"] = "CURRENT MIN 1V0SD: " + str(int(data[48 + 40 + health_offset:48 + 42 + health_offset].hex(), 16))
        self.CURRENT_INS_0V95AD["text"] = "CURRENT INS 0V95AD: " + str(int(data[48 + 42 + health_offset:48 + 44 + health_offset].hex(), 16))
        self.CURRENT_AVE_0V95AD["text"] = "CURRENT AVE 0V95AD: " + str(int(data[48 + 44 + health_offset:48 + 46 + health_offset].hex(), 16))
        self.CURRENT_MAX_0V95AD["text"] = "CURRENT MAX 0V95AD: " + str(int(data[48 + 46 + health_offset:48 + 48 + health_offset].hex(), 16))
        self.CURRENT_MIN_0V95AD["text"] = "CURRENT MIN 0V95AD: " + str(int(data[48 + 48 + health_offset:48 + 50 + health_offset].hex(), 16))

        self.A7_TEMPERATURE["text"] = "A7 TEMPERATURE: " + str(int(data[98 + health_offset:100 + health_offset].hex(), 16))
        self.PC1_TEMPERATURE["text"] = "PC1 TEMPERATURE: " + str(int(data[100 + health_offset:102 + health_offset].hex(), 16))
        self.PC2_TEMPERATURE["text"] = "PC2 TEMPERATURE: " + str(int(data[102 + health_offset:104 + health_offset].hex(), 16))

        # RUNTIME
        self.DAYS["text"] = "DAYS: " + str(int(data[104 + health_offset:108 + health_offset].hex(), 16))
        self.HOURS["text"] = "HOURS: " + str(int(data[108 + health_offset:112 + health_offset].hex(), 16))
        self.MINUTES["text"] = "MINUTES: " + str(int(data[112 + health_offset:116 + health_offset].hex(), 16))
        self.SECONDS["text"] = "SECONDS: " + str(int(data[116 + health_offset:120 + health_offset].hex(), 16))

        self.CRC_HEALTH["text"] = "CRC: " + str(int(data[120 + health_offset:122 + health_offset].hex(), 16))

    def update_power(self, data):
        # Initial set of data from EPS
        self.POWER_DATA["text"] = "POWER DATA: " + str(int(data[0 + power_offset:4 + power_offset].hex(), 16))
        self.BYTES_SENT["text"] = "Bytes Sent: " + str(int(data[4 + power_offset:8 + power_offset].hex(), 16))
        self.BYTES_RECV["text"] = "Bytes Recv: " + str(int(data[8 + power_offset:10 + power_offset].hex(), 16))
        self.PKTS_SENT["text"] = "PKTS Sent: " + str(int(data[10 + power_offset:12 + power_offset].hex(), 16))
        self.PKTS_RECV["text"] = "PKTS Recv: " + str(int(data[12 + power_offset:14 + power_offset].hex(), 16))
        self.INVLD_PACK["text"] = "Invld Pack: " + str(int(data[14 + power_offset:16 + power_offset].hex(), 16))
        self.CRC_FAILS["text"] = "CRC Fails: " + str(int(data[16 + power_offset:18 + power_offset].hex(), 16))
        self.STATUS["text"] = "STATUS: " + str(int(data[18 + power_offset:20 + power_offset].hex(), 16))
        self.RESET_FLAG["text"] = "Reset Flag: " + str(int(data[20 + power_offset:22 + power_offset].hex(), 16))

        # SA1 SA2 SA3
        self.SA1_BOOST_V["text"] = "SA1 BOOST V: " + str(int(data[22 + power_offset:24 + power_offset].hex(), 16))
        self.SA1_V["text"] = "SA1 V: " + str(int(data[24 + power_offset:26 + power_offset].hex(), 16))
        self.SA2_BOOST_V["text"] = "SA2 BOOST V: " + str(int(data[26 + power_offset:28 + power_offset].hex(), 16))
        self.SA2_V["text"] = "SA2 V: " + str(int(data[28 + power_offset:30 + power_offset].hex(), 16))
        self.SA3_BOOST_V["text"] = "SA3 BOOST V: " + str(int(data[30 + power_offset:32 + power_offset].hex(), 16))
        self.SA3_V["text"] = "SA3_V: " + str(int(data[32 + power_offset:34 + power_offset].hex(), 16))

        # BATT TEMPS
        self.BATT2_TEMP["text"] = "BATT2 TEMP: " + str(int(data[34 + power_offset:36 + power_offset].hex(), 16))
        self.BATT1_TEMP["text"] = "BATT1 TEMP: " + str(int(data[36 + power_offset:38 + power_offset].hex(), 16))

        # BUS VOLTAGE
        self.FIVEV0BUS_V["text"] = "5V0BUS V: " + str(int(data[38 + power_offset:40 + power_offset].hex(), 16))
        self.THREEV3BUS_V["text"] = "3V3BUS_V" + str(int(data[40 + power_offset:42 + power_offset].hex(), 16))

        # BATTERY VOLTAGE
        self.VBATT2_V["text"] = "VBATT2 V: " + str(int(data[42 + power_offset:44 + power_offset].hex(), 16))
        self.VBATT_V["text"] = "VBATT V: " + str(int(data[44 + power_offset:46 + power_offset].hex(), 16))
        self.VBATT1_V["text"] = "VBATT1 V: " + str(int(data[46 + power_offset:48 + power_offset].hex(), 16))

        # BUS TEMPS
        self.THREEV3BUS_TEMP["text"] = "3V3BUS TEMP: " + str(int(data[48 + power_offset:50 + power_offset].hex(), 16))
        self.FIVEV0BUS_TEMP["text"] = "5V0BUS_TEMP: " + str(int(data[50 + power_offset:52 + power_offset].hex(), 16))

        # 3V3EPS
        self.THREEV3EPS_V["text"] = "3V3EPS V: " + str(int(data[52 + power_offset:54 + power_offset].hex(), 16))

        # SAx_I
        self.SA1_I["text"] = "SA1_I: " + str(int(data[54 + power_offset:56 + power_offset].hex(), 16))
        self.SA2_I["text"] = "SA2_I: " + str(int(data[56 + power_offset:58 + power_offset].hex(), 16))
        self.SA3_I["text"] = "SA3_I: " + str(int(data[58 + power_offset:60 + power_offset].hex(), 16))

        # CURRENT STATS
        self.DISCHARGE_I["text"] = "DISCHARGE_I: " + str(int(data[60 + power_offset:62 + power_offset].hex(), 16))
        self.CHARGE_I["text"] = "CHARGE_I: " + str(int(data[62 + power_offset:64 + power_offset].hex(), 16))
        self.THREEV3BUS_I["text"] = "3V3BUS_I: " + str(int(data[64 + power_offset:66 + power_offset].hex(), 16))
        self.VBATT1_I["text"] = "VBATT1_I: " + str(int(data[66 + power_offset:68 + power_offset].hex(), 16))
        self.VBATT2_I["text"] = "VBATT2_I: " + str(int(data[68 + power_offset:70 + power_offset].hex(), 16))

        # SA TEMPS
        self.SA_YM_TEMP["text"] = "SA_YM_TEMP: " + str(int(data[70 + power_offset:72 + power_offset].hex(), 16))
        self.SA_ZP_TEMP["text"] = "SA_ZP_TEMP: " + str(int(data[72 + power_offset:74 + power_offset].hex(), 16))
        self.SA_ZM_TEMP["text"] = "SA_ZM_TEMP: " + str(int(data[74 + power_offset:76 + power_offset].hex(), 16))
        self.SA_XP_TEMP["text"] = "SA_XP_TEMP: " + str(int(data[76 + power_offset:78 + power_offset].hex(), 16))
        self.SA_YP_TEMP["text"] = "SA_YP_TEMP: " + str(int(data[78 + power_offset:80 + power_offset].hex(), 16))

        # 3V3EPS_I
        self.THREEV3EPS_I["text"] = "3V3EPS_I: " + str(int(data[80 + power_offset:82 + power_offset].hex(), 16))
        self.FIVEV0EPS_I["text"] = "5V0EPS_I: " + str(int(data[82 + power_offset:84 + power_offset].hex(), 16))

        # HIST_SA_1
        self.HIST_SA_1_P_1["text"] = "HIST SA 1 P 1: " + str(int(data[84 + power_offset:86 + power_offset].hex(), 16))
        self.HIST_SA_1_P_2["text"] = "HIST SA 1 P 2: " + str(int(data[86 + power_offset:88 + power_offset].hex(), 16))
        self.HIST_SA_1_P_3["text"] = "HIST SA 1 P 3: " + str(int(data[88 + power_offset:90 + power_offset].hex(), 16))
        self.HIST_SA_1_P_4["text"] = "HIST SA 1 P 4: " + str(int(data[90 + power_offset:92 + power_offset].hex(), 16))
        self.HIST_SA_1_P_5["text"] = "HIST SA 1 P 5: " + str(int(data[92 + power_offset:94 + power_offset].hex(), 16))
        self.HIST_SA_1_P_6["text"] = "HIST SA 1 P 6: " + str(int(data[94 + power_offset:96 + power_offset].hex(), 16))

        # HIST_SA_2
        self.HIST_SA_2_P_1["text"] = "HIST SA 2 P 1: " + str(int(data[96 + power_offset:98 + power_offset].hex(), 16))
        self.HIST_SA_2_P_2["text"] = "HIST SA 2 P 2: " + str(int(data[98 + power_offset:100 + power_offset].hex(), 16))
        self.HIST_SA_2_P_3["text"] = "HIST SA 2 P 3: " + str(int(data[100 + power_offset:102 + power_offset].hex(), 16))
        self.HIST_SA_2_P_4["text"] = "HIST SA 2 P 4: " + str(int(data[102 + power_offset:104 + power_offset].hex(), 16))
        self.HIST_SA_2_P_5["text"] = "HIST SA 2 P 5: " + str(int(data[104 + power_offset:106 + power_offset].hex(), 16))
        self.HIST_SA_2_P_6["text"] = "HIST SA 2 P 6: " + str(int(data[106 + power_offset:108 + power_offset].hex(), 16))

        # HIST_SA_3
        self.HIST_SA_3_P_1["text"] = "HIST SA 3 P 1" + str(int(data[108 + power_offset:110 + power_offset].hex(), 16))
        self.HIST_SA_3_P_2["text"] = "HIST SA 3 P 2" + str(int(data[110 + power_offset:112 + power_offset].hex(), 16))
        self.HIST_SA_3_P_3["text"] = "HIST SA 3 P 3" + str(int(data[112 + power_offset:114 + power_offset].hex(), 16))
        self.HIST_SA_3_P_4["text"] = "HIST SA 3 P 4" + str(int(data[114 + power_offset:116 + power_offset].hex(), 16))
        self.HIST_SA_3_P_5["text"] = "HIST SA 3 P 5" + str(int(data[116 + power_offset:118 + power_offset].hex(), 16))
        self.HIST_SA_3_P_6["text"] = "HIST SA 3 P 6" + str(int(data[118 + power_offset:120 + power_offset].hex(), 16))

        # HIST_BATT_V
        self.HIST_BATT_V_1["text"] = "HIST_BATT_V_1: " + str(int(data[120 + power_offset:122 + power_offset].hex(), 16))
        self.HIST_BATT_V_2["text"] = "HIST_BATT_V_2: " + str(int(data[122 + power_offset:124 + power_offset].hex(), 16))
        self.HIST_BATT_V_3["text"] = "HIST_BATT_V_3: " + str(int(data[124 + power_offset:126 + power_offset].hex(), 16))
        self.HIST_BATT_V_4["text"] = "HIST_BATT_V_4: " + str(int(data[126 + power_offset:128 + power_offset].hex(), 16))
        self.HIST_BATT_V_5["text"] = "HIST_BATT_V_5: " + str(int(data[128 + power_offset:130 + power_offset].hex(), 16))
        self.HIST_BATT_V_6["text"] = "HIST_BATT_V_6: " + str(int(data[130 + power_offset:132 + power_offset].hex(), 16))

        # HIST_BATT_I
        self.HIST_BATT_I_1["text"] = "HIST_BATT_I_1: " + str(int(data[132 + power_offset:134 + power_offset].hex(), 16))
        self.HIST_BATT_I_2["text"] = "HIST_BATT_I_2: " + str(int(data[134 + power_offset:136 + power_offset].hex(), 16))
        self.HIST_BATT_I_3["text"] = "HIST_BATT_I_3: " + str(int(data[136 + power_offset:138 + power_offset].hex(), 16))
        self.HIST_BATT_I_4["text"] = "HIST_BATT_I_4: " + str(int(data[138 + power_offset:140 + power_offset].hex(), 16))
        self.HIST_BATT_I_5["text"] = "HIST_BATT_I_5: " + str(int(data[140 + power_offset:142 + power_offset].hex(), 16))
        self.HIST_BATT_I_6["text"] = "HIST_BATT_I_6: " + str(int(data[142 + power_offset:144 + power_offset].hex(), 16))

    def update_misc(self, data):
        pass

    def clock(self):
        try:
            self.time_label["text"] = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
            self.after(500, self.clock)
        except AttributeError:
            self.after(500, self.clock)

    def last_packet_received(self, data):
        self.last_packet["text"] = data


class TrackTCP(threading.Thread):
    def run(self):
        while True:
            try:
                now = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('153.90.121.248', 3000))
                data = s.recv(1024)
                s.close()
                print("\n\n--------------------------------------")
                print("       " + now + "       ")
                print("--------------------------------------")
                if 75 < len(data) < 100:
                    print("Tile data: " + str(len(data)))
                    gui.update_tile(data)
                elif len(data) < 213:
                    print("Health data: " + str(len(data)))
                    gui.update_health(data)
                elif len(data) > 213:
                    print("Power data: " + str(len(data)))
                    gui.update_power(data)
                    gui.update_misc(data)
                else:
                    print("Miscellaneous data: " + str(len(data)))
                    gui.update_misc(data)
                gui.last_packet_received(now)
                print("{}".format(data))

            except KeyboardInterrupt:
                print("should be exiting")
                s.close()
                break


if __name__ == "__main__":
    time = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
    root = Tk()
    gui = DataGui(root)
    test = TrackTCP()
    test.start()
    gui.mainloop()
