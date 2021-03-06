import pygame

class PYGAMEWRAPPER:

        def __init__(self,width=800,height=240):

		pygame.init()

		size = width,height

		self.screen = pygame.display.set_mode(size)

		self.myfont = pygame.font.Font("Anonymous_Pro.ttf",26)

	def Draw_Text(self, textString , x = 10 , y = 10 ):

		label = self.myfont.render(textString, 1, (0,0,0))

        	textrect = label.get_rect()

                textrect.left = self.screen.get_rect().left + x

		textrect.top = self.screen.get_rect().top + y

        	self.screen.blit(label, textrect)

	def Refresh(self):

		pygame.display.flip()

	def Wipe(self):

		backgroundColor = 255, 255, 255

		self.screen.fill(backgroundColor)
	
