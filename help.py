import adi
# help ( adi.Pluto.gain_control_mode_chan0 )
# help ( adi.Pluto.tx_lo )
# help ( adi.Pluto.tx  )

sdr = adi.Pluto ( "ip:192.168.2.1" )

# Source: https://analogdevicesinc.github.io/pyadi-iio/fpga/index.html
# Generate a single complex tone
dds_freq_hz = 10000
dds_scale = 0.9
# Enable all DDSs
sdr.dds_single_tone ( dds_freq_hz , dds_scale )