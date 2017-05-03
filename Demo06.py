from pygameWrapper import PYGAMEWRAPPER
import time
window = PYGAMEWRAPPER(width=1000,height=1000)
import numpy as np

start_time = time.time()

while 1:

    window.Wipe()

    time_passed =  np.floor(time.time() - start_time)

    window.Draw_Text( "Time passed: "+ str(time_passed)+ " s." , x= 300, y=300)

    window.Refresh()
