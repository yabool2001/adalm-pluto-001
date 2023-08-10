# 2023.08.10
# Source: https://pysdr.org/content/pluto.html

import numpy as np
import adi
import matplotlib.pyplot as plt

sample_rate = 1e6 # Hz
center_freq = 915e6 # Hz
num_samps = 100000 # number of samples per call to rx()

sdr = adi.Pluto ( "ip:192.168.2.1" )
sdr.sample_rate = int ( sample_rate )

# Config Tx
sdr.tx_rf_bandwidth = int ( sample_rate ) # filter cutoff, just set it to the same as sample rate
sdr.tx_lo = int ( center_freq )
# sdr.tx_hardwaregain_chan0 = -90 # Increase to increase tx power, valid range is -90 to 0 dB
 

# Config Rx
sdr.rx_lo = int ( center_freq )
sdr.rx_rf_bandwidth = int ( sample_rate )
sdr.rx_buffer_size = num_samps
sdr.gain_control_mode_chan0 = 'slow_attack'
sdr.rx_hardwaregain_chan0 = 0.0 # dB, increase to increase the receive gain, but be careful not to saturate the ADC

