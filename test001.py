# 2023.06.08
# Source: https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio

import time
# Import library
import adi


# Create radio object
sdr = adi.Pluto ()
# Configure properties
sdr.rx_rf_bandwidth = 4000000
# Get data
data = sdr.rx ()
while True :
    print ( data )
    time.sleep ( 3 )