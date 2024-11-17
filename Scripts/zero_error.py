import pyvisa
import time
#const
OAM_50 = 50
OAM1M = 1
V_DIV = [5,10,20,50,100,200,500,1000,2000,5000,10000]

def check_connection(instrument_address):

    try:
        rm = pyvisa.ResourceManager()
        instrument = rm.open_resource(instrument_address)
        return instrument

    except pyvisa.VisaIOError:
        print('The instrument address is not found')

def measure(device):
    for
# data structure
instruments_setup =[
    'dut'
]
# measurement dictionary
measurements = {
    'channel1': [[OAM_50,OAM1M], V_DIV],
    'channel2': [[OAM_50,OAM1M], V_DIV],
    'channel3': [[OAM_50,OAM1M], V_DIV],
    'channel4': [[OAM_50,OAM1M], V_DIV]
}
# prolink {50 oams, 5mv/div - 10 v/div}
for i in sessions:
    writeval

if __name__ == '__main__':
    address = input('please insert the address of the instrument')
    dut = check_connection(address)
    if