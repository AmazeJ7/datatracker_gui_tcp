#############################
## Johnny's Branch Ya Bish ##
#############################

import sys
import socket
import datetime
import threading
from tkinter import *
from time import sleep

test_string_health = b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00{\xdc3\x1d\x10\x1dB\x1d\x9e\x00\x00\x0c\xea\x0c\xe2\x0c\xea\x0c\xd7\t\xc1\t\xca\t\xd6\t\xbf\x07\x07\x07\x07\x07\x0c\x06\xfa\x03\xe1\x03\xe7\x03\xf1\x03\xda\x03\xb5\x03\xb6\x03\xbb\x03\xb2\t\xc4\t\xa7\n`\x00\x00\x02q\x02q\x02q\x02q\x07\xef\x08r\t\xc4\x07S\x04\xe2\x04\x86\x04\xe2\x04E\x06\xb6\x05\xcd\x06\xb6\x04\xe2\x08\x8b\x08\x8b\x08\x8b\x08\x8b}\xfajR\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x1b\x00\x00\x00%\xcc\xcc\xdc'

test_string_tile = b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00J\xdc\x88\x00\x00\xd7\xe8\x02\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x03\x00\x00\x00\x00\x00\x00\x07\xeb\x07\xeb\x07\xeb\x00\x03\xcc\xcc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdc\x00\x00\x00\x00\x00\x00\xc0'

test_string_power = b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdb\xdc\x00\x00e\xb7\x00\x00\n\xe2\x00\xc5\x00\xc5\x00\x00\x00\x00\x00\x00\x00\x03\x00\xac\x00\x00\x00\x00\x03\xa7\x02o\x02\x18\x02\x14\x01\xc9\x01\xbf\x02p\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00>\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc4\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0e\x01\x08\x01\x0c\x01\x08\x01\x0c\x01\x08\x02\x13\x02\x19\x02\x12\x02\x17\x02\x12\x02\x19\x81\xff\x82\x00\x81\xf8\x82\x00\x81\xff\x81\xf4S\xb6\xdb\xdc\xdb\xdc\xdb\xdc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0'

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
Coeff['LARGE_V'] = [0, 0.01368, 'V']
Coeff['STD_I'] = [0, 1.611328125, 'mA']
Coeff['STD_V'] = [0, 0.005317, 'V']
Coeff['AD590_TEMP'] = [-273, 0.5462080078, 'C']
Coeff['SA_TEMP'] = [-273, 0.7661, 'C']
Coeff['33EPS_I'] = [0, 0.035413769, 'mA']
Coeff['HIST_SA_P'] = [0, 0.00142185467128, 'W']
Coeff['BUS_TEMP'] = [-238.85, 0.5776, 'C']
Coeff['BUS_I'] = [10, 10, 'mA']
Coeff['EPS_WDT'] = [0, 0.0115833333333333, 'Hours']
Coeff['None'] = [0, 1, '']

power_offset = 10
main_offset = 18
data_offset = 32

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

        Label(self, height=3, bg='black', fg='white', text="Time: ").grid(row=1, column=1, sticky=W)
        Label(self, height=3, bg='black', fg='white', text="Last Recieved: ").grid(row=1, column=3, sticky=W)

        Label(self, bg='black', fg='white', text="TILE DATA: ").grid(row=4, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="S6 Count: ").grid(row=5, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="ACT_TILES: ").grid(row=5, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED TILES: ").grid(row=5, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED COUNT1: ").grid(row=5, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED COUNT2: ").grid(row=5, column=9, sticky=W)

        Label(self, bg='black', fg='white', text="FAULTED COUNT3: ").grid(row=6, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED COUNT4: ").grid(row=6, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED COUNT5: ").grid(row=6, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED COUNT6: ").grid(row=6, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTED COUNT7: ").grid(row=6, column=9, sticky=W)

        Label(self, bg='black', fg='white', text="FAULTED COUNT8: ").grid(row=7, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="FAULTS INJECTED: ").grid(row=7, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="TOTAL FAULTS  : ").grid(row=7, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="MOVE_TILE_COUNT: ").grid(row=7, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="NEXT_SPARE    : ").grid(row=7, column=9, sticky=W)

        Label(self, bg='black', fg='white', text="Readback Faults: ").grid(row=8, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="Watchdog: ").grid(row=8, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="ACT PROC1: ").grid(row=8, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="ACT PROC2: ").grid(row=8, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="ACT PROC3: ").grid(row=8, column=9, sticky=W)

        Label(self, bg='black', fg='white', text="ACTPROCCNT1: ").grid(row=9, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="ACTPROCCNT2: ").grid(row=9, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="ACTPROCCNT3: ").grid(row=9, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="VOTER_COUNTS: ").grid(row=9, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="CRC : ").grid(row=9, column=9, sticky=W)
        Label(self, bg='black', fg='white', text="SYNC: ").grid(row=9, column=11, sticky=W)

        Frame(height=2, bg='black').grid(row=10, column=1, stick="nwes")

        Label(self, bg='black', fg='white', text="Health data: ").grid(row=11, column=1, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=test_string_health.hex()).grid(row=11, column=2, sticky=W)
        Label(self, bg='black', fg='white', text=" ").grid(row=12, column=2, sticky=W)

        Label(self, bg='black', fg='white', text="POWER DATA: ").grid(row=15 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="Bytes Sent: ").grid(row=16 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="Bytes Recv: ").grid(row=16 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="PKTS Sent: ").grid(row=17 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="PKTS Recv: ").grid(row=17 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="Invld Pack: ").grid(row=18 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="CRC  Fails: ").grid(row=18 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="status  : ").grid(row=19 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="Reset flag: ").grid(row=19 + power_offset, column=3, sticky=W)

        Label(self, bg='black', fg='white', text="SA1_BOOST_V: ").grid(row=20 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="SA1_V: ").grid(row=20 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="SA2_BOOST_V: ").grid(row=21 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="SA2_V: ").grid(row=21 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="SA3_V: ").grid(row=22 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="SA3_BOOST_V: ").grid(row=22 + power_offset, column=3, sticky=W)

        Label(self, bg='black', fg='white', text="BATT2_TEMP: ").grid(row=23 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="BATT1_TEMP: ").grid(row=23 + power_offset, column=3, sticky=W)

        Label(self, bg='black', fg='white', text="5V0BUS_V: ").grid(row=23 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="3V3BUS_V: ").grid(row=23 + power_offset, column=7, sticky=W)

        Label(self, bg='black', fg='white', text="VBATT2_V: ").grid(row=24 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="VBATT_V : ").grid(row=24 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="VBATT1_V: ").grid(row=24 + power_offset, column=5, sticky=W)

        Label(self, bg='black', fg='white', text="3V3BUS_TEMP: ").grid(row=25 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="5V0BUS_TEMP: ").grid(row=25 + power_offset, column=3, sticky=W)

        Label(self, bg='black', fg='white', text="3V3EPS_V   : ").grid(row=25 + power_offset, column=5, sticky=W)

        Label(self, bg='black', fg='white', text="SA1_I: ").grid(row=26 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="SA2_I: ").grid(row=26 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="SA3_I: ").grid(row=26 + power_offset, column=5, sticky=W)

        Label(self, bg='black', fg='white', text="DISCHARGE_I: ").grid(row=27 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="CHARGE_I   : ").grid(row=27 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="3V3BUS_I   : ").grid(row=27 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="VBATT1_I   : ").grid(row=27 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="VBATT2_I   : ").grid(row=27 + power_offset, column=9, sticky=W)

        Label(self, bg='black', fg='white', text="SA_Ym_TEMP: ").grid(row=28 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="SA_Zp_TEMP: ").grid(row=28 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="SA_Zm_TEMP: ").grid(row=28 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="SA_Xp_TEMP: ").grid(row=28 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="SA_Yp_TEMP: ").grid(row=28 + power_offset, column=9, sticky=W)

        Label(self, bg='black', fg='white', text="3V3EPS_I: ").grid(row=29 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="5V0BUS_I: ").grid(row=29 + power_offset, column=3, sticky=W)

        Label(self, bg='black', fg='white', text="HIST_SA_1_P_1: ").grid(row=30 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_1_P_2: ").grid(row=30 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_1_P_3: ").grid(row=30 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_1_P_4: ").grid(row=30 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_1_P_5: ").grid(row=30 + power_offset, column=9, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_1_P_6: ").grid(row=30 + power_offset, column=11, sticky=W)

        Label(self, bg='black', fg='white', text="HIST_SA_2_P_1: ").grid(row=31 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_2_P_2: ").grid(row=31 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_2_P_3: ").grid(row=31 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_2_P_4: ").grid(row=31 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_2_P_5: ").grid(row=31 + power_offset, column=9, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_2_P_6: ").grid(row=31 + power_offset, column=11, sticky=W)

        Label(self, bg='black', fg='white', text="HIST_SA_3_P_1: ").grid(row=32 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_3_P_2: ").grid(row=32 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_3_P_3: ").grid(row=32 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_3_P_4: ").grid(row=32 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_3_P_5: ").grid(row=32 + power_offset, column=9, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_SA_3_P_6: ").grid(row=32 + power_offset, column=11, sticky=W)

        Label(self, bg='black', fg='white', text="HIST_BATT_V_1: ").grid(row=33 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_V_2: ").grid(row=33 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_V_3: ").grid(row=33 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_V_4: ").grid(row=33 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_V_5: ").grid(row=33 + power_offset, column=9, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_V_6: ").grid(row=33 + power_offset, column=11, sticky=W)

        Label(self, bg='black', fg='white', text="HIST_BATT_I_1: ").grid(row=34 + power_offset, column=1, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_I_2: ").grid(row=34 + power_offset, column=3, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_I_3: ").grid(row=34 + power_offset, column=5, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_I_4: ").grid(row=34 + power_offset, column=7, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_I_5: ").grid(row=34 + power_offset, column=9, sticky=W)
        Label(self, bg='black', fg='white', text="HIST_BATT_I_6: ").grid(row=34 + power_offset, column=11, sticky=W)

        Label(self, bg='black', fg='white', text="Misc data/Powerchunk: ").grid(row=100, column=1, sticky=W)

    def update_tile(self, data):
        global main_offset
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[0 + main_offset:3 + main_offset].hex()).grid(row=5, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[3 + main_offset:5 + main_offset].hex()).grid(row=5, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[5 + main_offset:7 + main_offset].hex()).grid(row=5, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[7 + main_offset:9 + main_offset].hex()).grid(row=5, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[9 + main_offset:11 + main_offset].hex()).grid(row=5, column=10, sticky=W)

        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[11 + main_offset:13 + main_offset].hex()).grid(row=6, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[13 + main_offset:15 + main_offset].hex()).grid(row=6, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[15 + main_offset:17 + main_offset].hex()).grid(row=6, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[17 + main_offset:19 + main_offset].hex()).grid(row=6, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[19 + main_offset:21 + main_offset].hex()).grid(row=6, column=10, sticky=W)

        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[23 + main_offset:25 + main_offset].hex()).grid(row=7, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[25 + main_offset:27 + main_offset].hex()).grid(row=7, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[27 + main_offset:29 + main_offset].hex()).grid(row=7, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[29 + main_offset:31 + main_offset].hex()).grid(row=7, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[31 + main_offset:32 + main_offset].hex()).grid(row=7, column=10, sticky=W)

        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[33 + main_offset:34 + main_offset].hex()).grid(row=8, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[34 + main_offset:35 + main_offset].hex()).grid(row=8, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[35 + main_offset:36 + main_offset].hex()).grid(row=8, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[36 + main_offset:37 + main_offset].hex()).grid(row=8, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[37 + main_offset:38 + main_offset].hex()).grid(row=8, column=10, sticky=W)

        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[38 + main_offset:40 + main_offset].hex()).grid(row=9, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[40 + main_offset:42 + main_offset].hex()).grid(row=9, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[42 + main_offset:44 + main_offset].hex()).grid(row=9, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[44 + main_offset:46 + main_offset].hex()).grid(row=9, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[46 + main_offset:48 + main_offset].hex()).grid(row=9, column=10, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data[48 + main_offset:49 + main_offset].hex()).grid(row=9, column=12, sticky=W)

    def update_health(self, data):
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data.hex()).grid(row=11, column=2, sticky=W)

    def update_power(self, data):
        global data_offset
        # Initial set of data from EPS
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[0 + data_offset:4 + data_offset].hex(), 16))).grid(row=16 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[4 + data_offset:8 + data_offset].hex(), 16))).grid(row=16 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[8 + data_offset:10 + data_offset].hex(), 16))).grid(row=17 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[10 + data_offset:12 + data_offset].hex(), 16))).grid(row=17 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[12 + data_offset:14 + data_offset].hex(), 16))).grid(row=18 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[14 + data_offset:16 + data_offset].hex(), 16))).grid(row=18 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[16 + data_offset:18 + data_offset].hex(), 16))).grid(row=19 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[18 + data_offset:20 + data_offset].hex(), 16))).grid(row=19 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[20 + data_offset:22 + data_offset].hex(), 16))).grid(row=20 + power_offset, column=2, sticky=W)

        # SA1 SA2 SA3
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[22 + data_offset:24 + data_offset].hex(), 16))).grid(row=20 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[24 + data_offset:26 + data_offset].hex(), 16))).grid(row=20 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[26 + data_offset:28 + data_offset].hex(), 16))).grid(row=21 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[28 + data_offset:30 + data_offset].hex(), 16))).grid(row=21 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[30 + data_offset:32 + data_offset].hex(), 16))).grid(row=22 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[32 + data_offset:34 + data_offset].hex(), 16))).grid(row=22 + power_offset, column=4, sticky=W)

        # BATT TEMPS
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[34 + data_offset:36 + data_offset].hex(), 16))).grid(row=23 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[36 + data_offset:38 + data_offset].hex(), 16))).grid(row=23 + power_offset, column=4, sticky=W)

        # BUS VOLTAGE
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[38 + data_offset:40 + data_offset].hex(), 16))).grid(row=23 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[40 + data_offset:42 + data_offset].hex(), 16))).grid(row=23 + power_offset, column=8, sticky=W)

        # BATTERY VOLTAGE
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[42 + data_offset:44 + data_offset].hex(), 16))).grid(row=24 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[44 + data_offset:46 + data_offset].hex(), 16))).grid(row=24 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[46 + data_offset:48 + data_offset].hex(), 16))).grid(row=24 + power_offset, column=6, sticky=W)

        # BUS TEMPS
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[48 + data_offset:50 + data_offset].hex(), 16))).grid(row=25 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[50 + data_offset:52 + data_offset].hex(), 16))).grid(row=25 + power_offset, column=4, sticky=W)

        # 3V3EPS
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[52 + data_offset:54 + data_offset].hex(), 16))).grid(row=25 + power_offset, column=6, sticky=W)

        # SAx_I
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[54 + data_offset:56 + data_offset].hex(), 16))).grid(row=26 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[56 + data_offset:58 + data_offset].hex(), 16))).grid(row=26 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[58 + data_offset:60 + data_offset].hex(), 16))).grid(row=26 + power_offset, column=6, sticky=W)

        # CURRENT STATS
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[60 + data_offset:62 + data_offset].hex(), 16))).grid(row=27 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[62 + data_offset:64 + data_offset].hex(), 16))).grid(row=27 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[64 + data_offset:66 + data_offset].hex(), 16))).grid(row=27 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[66 + data_offset:68 + data_offset].hex(), 16))).grid(row=27 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[68 + data_offset:70 + data_offset].hex(), 16))).grid(row=27 + power_offset, column=10, sticky=W)

        # SA TEMPS
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[70 + data_offset:72 + data_offset].hex(), 16))).grid(row=28 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[72 + data_offset:74 + data_offset].hex(), 16))).grid(row=28 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[74 + data_offset:76 + data_offset].hex(), 16))).grid(row=28 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[76 + data_offset:78 + data_offset].hex(), 16))).grid(row=28 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[78 + data_offset:80 + data_offset].hex(), 16))).grid(row=28 + power_offset, column=10, sticky=W)

        # 3V3EPS_I
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[80 + data_offset:82 + data_offset].hex(), 16))).grid(row=29 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[82 + data_offset:84 + data_offset].hex(), 16))).grid(row=29 + power_offset, column=4, sticky=W)

        # HIST_SA_1
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[84 + data_offset:86 + data_offset].hex(), 16))).grid(row=30 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[86 + data_offset:88 + data_offset].hex(), 16))).grid(row=30 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[88 + data_offset:90 + data_offset].hex(), 16))).grid(row=30 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[90 + data_offset:92 + data_offset].hex(), 16))).grid(row=30 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[92 + data_offset:94 + data_offset].hex(), 16))).grid(row=30 + power_offset, column=10, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[94 + data_offset:96 + data_offset].hex(), 16))).grid(row=30 + power_offset, column=12, sticky=W)

        # HIST_SA_2
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[96 + data_offset:98 + data_offset].hex(), 16))).grid(row=31 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[98 + data_offset:100 + data_offset].hex(), 16))).grid(row=31 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[100 + data_offset:102 + data_offset].hex(), 16))).grid(row=31 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[102 + data_offset:104 + data_offset].hex(), 16))).grid(row=31 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[104 + data_offset:106 + data_offset].hex(), 16))).grid(row=31 + power_offset, column=10, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[106 + data_offset:108 + data_offset].hex(), 16))).grid(row=31 + power_offset, column=12, sticky=W)

        # HIST_SA_3
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[108 + data_offset:110 + data_offset].hex(), 16))).grid(row=32 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[110 + data_offset:112 + data_offset].hex(), 16))).grid(row=32 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[112 + data_offset:114 + data_offset].hex(), 16))).grid(row=32 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[114 + data_offset:116 + data_offset].hex(), 16))).grid(row=32 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[116 + data_offset:118 + data_offset].hex(), 16))).grid(row=32 + power_offset, column=10, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[118 + data_offset:120 + data_offset].hex(), 16))).grid(row=32 + power_offset, column=12, sticky=W)

        # HIST_BATT_V
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[120 + data_offset:122 + data_offset].hex(), 16))).grid(row=33 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[122 + data_offset:124 + data_offset].hex(), 16))).grid(row=33 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[124 + data_offset:126 + data_offset].hex(), 16))).grid(row=33 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[126 + data_offset:128 + data_offset].hex(), 16))).grid(row=33 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[128 + data_offset:130 + data_offset].hex(), 16))).grid(row=33 + power_offset, column=10, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[130 + data_offset:132 + data_offset].hex(), 16))).grid(row=33 + power_offset, column=12, sticky=W)

        # HIST_BATT_I
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[132 + data_offset:134 + data_offset].hex(), 16))).grid(row=34 + power_offset, column=2, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[134 + data_offset:136 + data_offset].hex(), 16))).grid(row=34 + power_offset, column=4, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[136 + data_offset:138 + data_offset].hex(), 16))).grid(row=34 + power_offset, column=6, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[138 + data_offset:140 + data_offset].hex(), 16))).grid(row=34 + power_offset, column=8, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[140 + data_offset:142 + data_offset].hex(), 16))).grid(row=34 + power_offset, column=10, sticky=W)
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=str(int(data[142 + data_offset:144 + data_offset].hex(), 16))).grid(row=34 + power_offset, column=12, sticky=W)

    def update_misc(self, data):
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=400, text=data.hex()).grid(row=100, column=2, sticky=W)

    def clock(self):
        Label(self, height=3, bg='black', fg='white', text=datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")).grid(row=1, column=2)
        self.after(100, self.clock)

    def frame_count(self):
        # will change this to represent the number of times that we have read data from the tcp port later
        DataGui.framcount += 1

    def threaded_clock(self):
        update_clock = threading.Thread(target=self.clock)
        update_clock.isDaemon()
        update_clock.run()

    def last_packet_recieved(self, data):
        Label(self, bg='black', fg='white', justify=LEFT, wraplength=800, text=data).grid(row=1, column=4, sticky=W)


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
                gui.last_packet_recieved(now)
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
