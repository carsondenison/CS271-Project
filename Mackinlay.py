# Initializer values and locations for dependencies
vega_directory = './vega_files/'
template_directory = './templates/'
data_directory = './data/'
image_directory = './images/'
view_vega_template = './view_vega_template.html'
view_vega_html = './view_vega.html'


# Here we have created a basic init template that researchers can use to generate the optimal
# control group graphs based on the users inputted data. Researchers can then use these graphs 
# as a baseline to compare the effectiveness of their own visualizations. We rank the "optimal" 
# visual variables on Jock D. Mackinlay's ranking of perceptual tasks 

# User indicates the type of data that they are inputting: either quantitative or nominal.
# Quantitative = 1, Nominal = 2
# Currently set to quantitative

dtype = 1

# FOR BAR CHARTS: 
#------------------------------------------------------------------------------

# Colors for borders, fills are set by data. See vega docs for full set
if dtype = 1: 
    colors = ['black']
else:
    colors = ['black', 'blue', 'green', 'purple', 'white']

# Padding between groups of columns
paddings = [0.2]

# Width of bar borders
if dtype = 2: 
    stroke_widths = [2]
else:
    stroke_widths = [1, 2, 3, 4]

# FOR SCATTER PLOTS:
#------------------------------------------------------------------------------

# Size of scatter plot points
sizes = [10, 50, 100, 200]

# COMMANDS TO RUN:
#------------------------------------------------------------------------------

# Each entry should look like: (idiom, file prefix, data file)
cmds = [
	('scatter', 'scatter_', 'data_s.txt'),
	('grouped_bar', 't1_', './data.txt')#,
#	('grouped_bar', 't2_', './data2.txt'),
#	('stacked_bar', 't3_', './data3.txt'),
#	('stacked_bar', 't4_', './data4.txt'),
#	('stacked_bar', 't5_', './data5.txt')
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

# BELOW HERE IS JUST CONSTANTS FOR VISUAL CHECK
#------------------------------------------------------------------------------

container = '''
    <div id="DIV_NAME"></div>
    <input type="checkbox" value="DIV_NAME" class="check">
    <script type="text/javascript">
      var SPEC_NAME = VEGA_LOCATION
    vegaEmbed(DIV_NAME, SPEC_NAME)   
    </script>
    '''

spec_stub = 'spec'