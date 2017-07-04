from deep_identifier import *

# Constants
Z_STRING = '\x01ZZZZZ\x01'
CD_ROM_STRING = 'CD-ROM'
DUCK_STRING = 'iamaduck'

class P3DOIdentifier(DeepIdentifier):
	NAME = "Panasonic 3DO ISO Identifier"
	TYPE = "3do_iso"

	def identify(self):
		match = 0

		# Always seek back to the start just to be safe
		self.file.seek(0)
		
		# check for the string of Zs with the 01 bytes around it
		z_str = self.file.read(len(Z_STRING))
		if z_str == Z_STRING:
			match += 25
		else:
			return match

		# check for the 'CD-ROM' string
		self.file.seek(0x28)
		cdrom_str = self.file.read(len(CD_ROM_STRING))
		if cdrom_str == CD_ROM_STRING:
			match += 25
		else:
			return match

		#look for the iamaduck string from 0x88 to 0x800
		self.file.seek(0x88)
		while self.file.tell() < 0x800:
			duck_str = self.file.read(len(DUCK_STRING))
			if duck_str == DUCK_STRING:
				match += 50
				break

		return match
