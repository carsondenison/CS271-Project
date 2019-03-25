import json
import numpy as np 

def main():
	#Write some shit
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

main()