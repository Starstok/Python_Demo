class desktop_light():
	def __init__ (self,level,color):
		self.level = level
		self.color = color

	# def on(func):
	# 	print('kk')

	@classmethod
	def power(self):
		return 'on'

open = desktop_light('100%','red')

print(open.power(),open.level,open.color)
