import sys
import os

HEADER_SIZE = 0x18
READ_SIZE = 0x800
FOOTER_SIZE = 0x118

if len(sys.argv) == 2:
	filename = sys.argv[1]
	out_filename = filename[:-4] + '.iso' # replace .bin with .iso
	
	in_file = open(filename, 'rb')
	in_file.seek(0, os.SEEK_END) # seek to end
	size = in_file.tell() # get the size of the file
	in_file.seek(0, os.SEEK_SET) # seek back to start

	block_count = size / 0x930

	out_file = open(out_filename, 'wb')

	for i in xrange(block_count):
		in_file.seek(HEADER_SIZE, os.SEEK_CUR) # skip forward 0x18 bytes
		out_file.write(in_file.read(READ_SIZE))
		in_file.seek(FOOTER_SIZE, os.SEEK_CUR)

	in_file.close()
	out_file.close()