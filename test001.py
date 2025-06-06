# 2023.06.08
# Source: https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio
# check address of the Pluto device "iio_info -s"

import time
# Import library
import adi

print ( f"Hello! test001.py running." )

# Create radio object
# sdr = adi.Pluto () # Wersja na komputer Win10 MSI
# sdr = adi.Pluto ( uri = "usb:4.7.5" ) # Wersja z Libiio release >= v0.25 na MW50-SV0
sdr = adi.Pluto ( uri = "usb:" ) # Wersja z Libiio release >= v0.25 na RPi400
# sdr = adi.Pluto ('ip:192.168.2.1') # Wersja na komputer Win11 GO3 
print ( sdr )
# Configure properties
sdr.rx_rf_bandwidth = 2_400_000_000
# Get data
print ( sdr.rx_hardwaregain_chan0 )
data = sdr.rx ()
print ( data )
while True :
    print ( sdr.rx_hardwaregain_chan0 )
    time.sleep ( 3 )
    print ( data )