from pygameWrapper import PYGAMEWRAPPER

window = PYGAMEWRAPPER(width=1000,height=1000)

while 1:

	window.Wipe()

	window.Draw_Text( 'hello world!' )

	window.Refresh()
