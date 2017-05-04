from pygameWrapper import PYGAMEWRAPPER
from timer import TIMER

window = PYGAMEWRAPPER(width=1000,height=1000)

# ---------------------------------------------- 

timer = TIMER(5)

while 1:

    window.Wipe()

    window.Draw_Text( "Time remaining: " + str( timer.Time_Remaining() ) + "s" , x = 300, y = 300 )

    if ( timer.Time_Elapsed() ):

    	timer.Reset()

    window.Refresh()
