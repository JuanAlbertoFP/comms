from datetime import datetime
from pyModbusTCP.client import ModbusClient
import sys
import time

numofpolls = 20

c = ModbusClient(
        host="0.0.0.0",
        port=502,
        debug=False,
        unit_id=10,
        auto_open=True,
        auto_close=False,  # Don't close the TCP connection after each request
        timeout=5,
    )


filename = datetime.now()
 

with open("output/mdbs_output_"+filename.strftime("%Y%m%d_%H%M%S")+".csv", "w") as file:
    s = "Timestamp;Register #;Value;Connected"
    file.write(s)

    while numofpolls >0:

        numofpolls = numofpolls -1

        reg001 = c.read_holding_registers(1109, 1)
        reg002 = c.read_holding_registers(1152, 1)

        file.write("\n")
        
        if reg001:
            current_time = datetime.now()
            current_time=current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            s = str(current_time)+";41110;"+str(reg001[0])+";1"
            print(s+" - Connected")
            file.write(s)
            
        else:
            
            current_time = datetime.now()           
            current_time=current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            s = str(current_time)+";41110;;0"  
            print(s+" -  Not Connected")
            file.write(s)
        
        file.write("\n")
        
        if reg002:
            current_time = datetime.now()
            current_time=current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            s = str(current_time)+";41152;"+str(reg002[0])+";1"
            print(s+" - Connected")
            file.write(s)
            
        else:
            current_time = datetime.now()           
            current_time=current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            s = str(current_time)+";41152;;0"  
            print(s+" - Not Connected")
            file.write(s)
        
        # sleep 2s before next polling
        time.sleep(2)
    
    file.close()