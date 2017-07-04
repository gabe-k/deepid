from deep_identifier import *

# Constants
MAGIC = '\xC2\x33\x9F\x3D'
TITLE_ID_LEN = 6

class GameCubeIdentifier(DeepIdentifier):
	NAME = "Nintendo GameCube ISO Identifier"
	TYPE = "gamecube_iso"

	def identify(self):
		match = 0

		# Check for the magic first
		self.file.seek(0x1C)
		magic_str = self.file.read(len(MAGIC))
		if magic_str == MAGIC:
			match += 50
		else:
			return match
			

		# Seek to the start of the disk
		self.file.seek(0)

		# Read the title id
		self.title_id = self.file.read(TITLE_ID_LEN)
		if len(self.title_id) == TITLE_ID_LEN and self.title_id.isalnum():
			match += 50

		return match
