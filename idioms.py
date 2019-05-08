from filters import *
from gen_init import *

# Iterates through color and stroke width for rectilinear plots from heer study. 
# Ordinal x, quant y
# Looks through template file and splits at SPLIT_LOCATION. Inserts different combinations
#	of variables into the splits.
def rect(template, prefix, data_file):
	data = ''
	with open(file=data_directory + data_file,mode='r') as data_json:
		data = data_json.read()
		with open(file = template_directory + template,mode='r') as template_file:
			template = template_file.read().split('SPLIT_LOCATION')
			for padding in paddings:
				for color in colors:
					for stroke_width in stroke_widths:
						with open(file = vega_directory+prefix+color+'_'+str(stroke_width)+'_'+str(padding)+'.vl',mode='w+') as out:
							vega = template[0] + data + template[1] + str(padding) + template[2] + color + template[3] + str(stroke_width) + template[4]
							out.write(vega)

# Similar to rect, but does it for a simple vega-lite scatter plot
def scatter(template, prefix, data_file):
	data = ''
	with open(file=data_directory + data_file,mode='r') as data_json:
		data = data_json.read()
		with open(template_directory + template,mode='r') as template_file:
			template = template_file.read().split('SPLIT_LOCATION')
			for size in sizes:
				for flt in flts_s:
					if strToFilter[flt](data, size): 
						with open(file = vega_directory+prefix+str(size)+'.vl',mode='w+') as out:
							vega = template[0] + data + template[1] + str(size) + template[2]
							out.write(vega)

# Lookup table from idiom to functions
strToFunc = {
	"scatter": scatter, 
	"grouped_bar": rect, 
	"stacked_bar": rect
	}