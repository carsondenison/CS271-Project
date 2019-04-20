import json

vega_directory = './vega_files/'
template_directory = './templates/'
colors  = ['black', 'red', 'blue', 'green', 'orange', 'yellow', 'purple', 'white']
paddings = [0.1 * i for i in range(5)]

'''
#test matt jiang
def try1():
	schema = "https://vega.github.io/schema/vega-lite/v3.json"
	data = "data/cars.json"
	marks = ["area", "bar", "circle", "line", "point", "rect", "rule", 
			 "square", "text", "tick", "geoshape"]
	for i in range(len(marks)):
		filenum = str(i).zfill(1 + int(np.log10(len(marks))))
		mark = marks[i]
		with open('./out/viz' + filenum + '.json', 'w') as outfile:
			json.dump({
				"$schema": schema,
				"data": {"url": data},
				"mark": mark,
				"encoding": {
					"x": {"field": "Horsepower", "type": "quantitative"},
					"y": {"field": "Miles_per_Gallon", "type": "quantitative"}
				}}, outfile)
'''

# Iterates through color and stroke width for rectilinear plots from heer study. 
# Ordinal x, quant y
def rect(template, prefix, data_location):
	data = ''
	with open(file=data_location,mode='r') as data_file:
		data = data_file.read()
		with open(file = template_directory + template,mode='r') as template_file:
			template = template_file.read().split('SPLIT_LOCATION')
			for padding in paddings:
				for color in colors:
					for stroke_width in range(1, 5):
						with open(file = vega_directory+prefix+color+'_'+str(stroke_width)+'_'+str(padding)+'.vl',mode='w+') as out:
							vega = template[0] + data + template[1] + str(padding) + template[2] + color + template[3] + str(stroke_width) + template[4]
							out.write(vega)

def scatter(template, prefix, data_location):
	data = ''
	with open(file=data_location,mode='r') as data_file:
		data = data_file.read()
		with open(file = template_directory + template,mode='r') as template_file:
			template = template_file.read().split('SPLIT_LOCATION')
			print(template[0] + data + template[1] + str(200) + template[2])

#scatter('scatter_template.vl', 'scatter_', 'data_s.txt')

rect('t1_template.vl', 't1_', './data.txt')
#rect('t2_template.vl', 't2_', './data2.txt')
#rect('t1_template.vl', 't3_', './data3.txt')

