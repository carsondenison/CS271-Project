# Initializer values and locations for dependencies
vega_directory = './vega_files/'
template_directory = './templates/'
data_directory = './data/'
image_directory = './images/'


# Change here to filter visualizations

# FOR BAR CHARTS: 
#------------------------------------------------------------------------------

# Colors for borders, fills are set by data. See vega docs for full set
colors = ['black', 'blue', 'green', 'purple', 'white']

# Padding between groups of columns
paddings = [0.2]

# Width of bar borders
stroke_widths = [1, 2, 3, 4]



# FOR SCATTER PLOTS:
#------------------------------------------------------------------------------

# Size of scatter plot points
sizes = [10, 50, 100, 200, 300]



# COMMANDS TO RUN:
#------------------------------------------------------------------------------

# Each entry should look like: (idiom, file prefix, data file)
cmds = [
	('scatter', 'scatter_', 'data_s.txt'),
	('grouped_bar', 't1_', './data.txt'),
	('grouped_bar', 't2_', './data2.txt'),
	('stacked_bar', 't3_', './data3.txt'),
	('stacked_bar', 't4_', './data4.txt'),
	('stacked_bar', 't5_', './data5.txt')
	]

# Lookup table from idiom to appropriate template
strToTemplate = {
	"scatter": "scatter_template.vl", 
	"grouped_bar": "t1_template.vl", 
	"stacked_bar": "t2_template.vl"
	}


# INTELLIGENCE:
#------------------------------------------------------------------------------

# What do you call your dependent and independent variables? The filter needs
# to know so that it can extract the data and act on it
x = "x"
y = "y"

# List of intelligent filters to remove bad images from scatter plots
flts_s = ["scatter_overlap"]

# List of intelligent filters to remove bad images from rectilinear plots
flts_r = []


