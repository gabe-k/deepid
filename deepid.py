import deep_identifier
import xbox360_identifier
import p3do_identifier
import ps2_identifier
import gameboy_identifier
import gamecube_identifier

import sys

identifiers = [deep_identifier.DeepIdentifier, \
				p3do_identifier.P3DOIdentifier, \
				ps2_identifier.PS2Identifier, \
				gameboy_identifier.GameBoyIdentifier, \
				gamecube_identifier.GameCubeIdentifier ]

def main():
	file = open(sys.argv[1], 'r')

	for identifier in identifiers:
		i = identifier(file)

		print i.NAME + " | Match: " + str(i.identify())

	file.close()

main()
