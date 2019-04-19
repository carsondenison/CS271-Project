import json

vega_directory = './vega_files/'
template_directory = './templates/'
colors  = ['black', 'red', 'blue', 'green', 'orange', 'yellow', 'purple', 'white']

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

# Iterates through color and stroke width for t1 from heer study
def t1():
	with open(file = template_directory + 't1_template.vl',mode='r') as template_file:
		template = template_file.read().split('SPLIT_LOCATION')
		for color in colors:
			for stroke_width in range(1, 5):
				with open(file = vega_directory+'t1_'+color+'_'+str(stroke_width),mode='w+') as out:
					out.write(template[0] + color + template[1] + str(stroke_width) + template[2])

def t2():


t1()
