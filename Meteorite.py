class Meteorite(object):

	def __init__(self, time, location):

		self.created = time
		self.location = location
		self.destroyed = -1

	def getCreated(self):
		return self.created

	def getLocation(self):
		return self.location

	def getDestroyed(self):
		return self.destroyed

	def setDestroyed(self, time):
		self.destroyed = time