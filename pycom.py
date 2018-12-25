#!/usr/bin/env python

import serial
from datetime import datetime

log = open('pycom.log', 'a')

with serial.Serial('/dev/ttyUSB1', 115200, timeout=1) as ser:
    while True:
        try:
            line = ser.readline().decode('ascii')
            if line:
                line = "[%s] %s" % (datetime.now().isoformat(), line)
                print(line, end='')
                log.write(line)
                log.flush()
        except KeyboardInterrupt:
            break
        except Exception as ex:
            print(ex)
