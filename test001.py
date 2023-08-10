# 2023.06.08
# Source: https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio

import time
# Import library
import adi

print ( f"Hello! test001.py running." )

# Create radio object
# sdr = adi.Pluto () # Wersja na komputer Win10 MSI
# sdr = adi.Pluto ( uri = "usb:1.24.5" )
sdr = adi.Pluto ('ip:192.168.2.1') # Wersja na komputer Win11 GO3 
print ( sdr )
# Configure properties
sdr.rx_rf_bandwidth = 4000000
# Get data
data = sdr.rx ()
print ( data )
while True :
    time.sleep ( 3 )
    print ( data )