from datetime import datetime
from pyModbusTCP.client import ModbusClient
import sys


# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and
file1 = open ("output\hh_tesla_modbus_output.txt", "w")
#L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
#file1.writelines(L)
 
# Closing file
file1.close()

c = ModbusClient(
        host="0.0.0.0",
        port=502,
        debug=False,
        unit_id=1,
        auto_open=True,
        auto_close=False,  # Don't close the TCP connection after each request
        timeout=5,
    )
 
# read 1 register at address 101, store result in regs list
regs = c.read_holding_registers(310, 2)

if regs:
    #print(regs)
    print('reg #310 "Battery Meter Frequency": %s' % regs)
else:
    print("read error")
    
    