from deep_identifier import *

# Constants
CONST_DATA = '\xCE\xED\x66\x66\xCC\x0D\x00\x0B\x03\x73\x00\x83\x00\x0C\x00\x0D\x00\x08\x11\x1F\x88\x89\x00\x0E\xDC\xCC\x6E\xE6\xDD\xDD\xD9\x99\xBB\xBB\x67\x63\x6E\x0E\xEC\xCC\xDD\xDC\x99\x9F\xBB\xB9\x33\x3E'

class GameBoyIdentifier(DeepIdentifier):
	NAME = "Nintendo Game Boy ROM Identifier"
	TYPE = "gameboy_rom"

	def identify(self):
		# check the constant 0x30 bytes
		self.file.seek(0x104)
		const_buf = self.file.read(len(CONST_DATA))
		if const_buf == CONST_DATA:
			return 100

		return 0

