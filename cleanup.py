import os
from gen_init import *

# Put the list of visualizations to keep in here, copied from view_vega.html:
save_list = ['scatter_50', 'scatter_200']

if not save_list:
	print("If you want to remove all your files, use the command line instead")
else:
	print("Removing files:")
	for vega_file in os.listdir(vega_directory):
		if vega_file.split('.')[0] not in save_list:
			os.remove(vega_directory + vega_file)
			print("removed: " + vega_directory + vega_file)
	print()
	print("Remaining files:")
	for vega_file in os.listdir(vega_directory):
		print(vega_directory + vega_file)