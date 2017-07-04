from deep_identifier import *

# Constants
CD001_STRING = '\x01CD001\x01'
PLAYSTATION_STRING_1 = 'PLAYSTATION                                                     '
PLAYSTATION_STRING_2 = 'PLAYSTATION                                                                                                                     '

class PS2Identifier(DeepIdentifier):
	NAME = "PS2 ISO Identifier"

	def identify(self):
		match = 0

		# check the CD001 string
		self.file.seek(0x8000)
		cd_str = self.file.read(len(CD001_STRING))
		if cd_str == CD001_STRING:
			match += 25

		# check the first playstation string
		self.file.seek(0x8008)
		ps_string_1 = self.file.read(len(PLAYSTATION_STRING_1))
		if ps_string_1 == PLAYSTATION_STRING_1:
			match += 25

		# check the second playstation string
		self.file.seek(0x823E)
		ps_string_2 = self.file.read(len(PLAYSTATION_STRING_2))
		if ps_string_2 == PLAYSTATION_STRING_2:
			match += 50

		return match

	def get_primary_type(self):
		return "ps2_iso"