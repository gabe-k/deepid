# CERTAINTY_BASE = 0
# CERTAINTY_PARTIAL = 1
# CERTAINTY_MAX = 2

class DeepIdentifier:
	NAME = "ISO Identifier Template"

	# filename is optional
	def __init__(self, file, filename=""):
		self.file = file
		self.filename = filename
		self.attributes = []

		self.file.seek(0)

	# returns int from 0 to 100 of how certain it is of its identification
	def identify(self):
		return 0
