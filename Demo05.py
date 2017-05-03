from pygameWrapper import PYGAMEWRAPPER
import time
window = PYGAMEWRAPPER(width=1000,height=1000)

x_start = 300
x_stop = 50
x_loc = x_start

while 1:

    window.Wipe()

    if x_loc != x_stop:

        window.Draw_Text( 'Ling Ling' , x=x_loc, y=200)

        x_loc = x_loc - 1

    window.Refresh()
