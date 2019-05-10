import os
import sys
from gen_init import *


if len(sys.argv) < 2:
	print("If you want to remove all your files, use the command line instead")
else:
	save_list = sys.argv[1]
	print("Removing files:")
	for vega_file in os.listdir(vega_directory):
		if vega_file.split('.')[0] not in save_list:
			os.remove(vega_directory + vega_file)
			print("removed: " + vega_directory + vega_file)
	print()
	print("Remaining files:")
	for vega_file in os.listdir(vega_directory):
		print(vega_directory + vega_file)