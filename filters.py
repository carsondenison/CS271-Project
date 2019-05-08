from gen_init import x, y
import json
import numpy as np 

# Takes nasty vega data format and converts it to a nice list of 2d numpy
# points. Put names of x and y coords in as optional params.
def format_data(data):
	stripped = data.strip(" ")
	# If list, turn it into a dictionary
	if stripped[0] == '[':
		stripped = stripped[1:-1]
	data_dict = json.loads(stripped)
	points = []
	vals = data_dict["values"]
	for entry in vals:
		points.append(np.array([entry[x], entry[y]]))
	return points

# Takes json of data. Returns True if not overlapping,
# False if overlapping
def no_overlap(data, r):
	points = format_data(data)
	for i in range(len(points) - 1):
		for j in range(i + 1, len(points)):
			if np.linalg.norm(points[i] - points[j]) > 2 * r:
				return False
	return True

# Lookup table from filters to filtering functions
strToFilter = {
	"scatter_overlap": no_overlap
	}