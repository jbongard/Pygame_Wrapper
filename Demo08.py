from pygameWrapper import PYGAMEWRAPPER
import time
window = PYGAMEWRAPPER(width=1000,height=1000)
import numpy as np

targetTime = 0 

def Reset_Timer():

	currentTime = time.time()

	global targetTime

	targetTime = currentTime + 5

def Time_Remaining():

	currentTime = time.time()

	timeRemaining = targetTime - currentTime

	secondsRemaining = int( np.floor( timeRemaining ) )

	return secondsRemaining

def Time_Elapsed():

	currentTime = time.time()

	return currentTime >= targetTime

# ---------------------------------------------- 

Reset_Timer()

while 1:

    window.Wipe()

    window.Draw_Text( "Time remaining: " + str( Time_Remaining() ) + "s" , x = 300, y = 300 )

    if ( Time_Elapsed() ):

	Reset_Timer()

    window.Refresh()
