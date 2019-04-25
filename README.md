FOR THE GENERATOR:-------------------------------------------------------------

THE BASICS: 
The file "gen_init.py" contains all the things a user must change before running the generator. 
To run the generator itself and create your vega files (and images), run "python generator.py". 
To add more idioms to the generator, add more functions to "idioms.py"
To add more filters, edit "filters.py"



THE SPECIFICS:

The dependency tree looks as follows:

generator.py is dependent on idioms.py, filters.py, and gen_init.py
idioms.py    is dependent on filters.py, and gen_init.py
filters.py   is dependent on gen_init.py
gen_init.py  has no dependencies.

The generator requires python's json library (installed with python) and the library "numpy".


THE SPECIFICS (gen_init.py):
At the top of the file there are relative paths to the important directories. These are:
vega_directory     --- the directory in which to output vega files
template_directory --- the directory containing template files
data_directory     --- the directory containing data files
image_directory    --- the directory in which to output images

For each idiom, there are certain variables which can be iterated over. The user selects the range over which to iterate, and the code will generate all combinations of those. At the moment there are only bar and scatter plots.

The section COMMANDS TO RUN is a list of the commands to run. Chooses the specific idiom (at the moment the options are scatter, grouped_bar, and stacked bar), the prefix for the files which will be output, and the data file. You can have as many commands as you want and they will run sequentially.

The dictionary strToTemplate is a lookup table from idiom <--> template file. This does not need to be changed unless new idioms are added.

The section INTELLIGENCE has the intelligent filtering capabilities. You list the names for your dependent and independent variables, so that the code knows on what to operate. Each idiom has a list of filters to apply. At the moment the only implemented filter is "scatter_overlap" which filters out plots which have overlapping scatter plot points.


THE SPECIFICS (filters.py)

This file contains the code for filtering out bad visualizations. It contains two functions. One takes a data file and returns a list of length two numpy arrays (points). The other filters out overlapping scatterplots. This file is where you put more filters for intelligent generation.

THE SPECIFICS (idioms.py)

This file contains two functions. One iterates through padding, line color, and stroke witdh for a rectilinear plot, the other iterates through different sizes for a scatter plot. They both work by taking in a template, which is a vega spec with the data and variables of interest replaced with the string "SPLIT_LOCATION". They then iterate through the combinations of vars and replace SPLIT_LOCATION with the appropriate values. They also take a prefix which is prepended to the file name of the output file. The output file will have the name 
"prefix_firstVar_secondVar_..._nthVar.vl"

The specifics (generator.py):

This file just runs all the commands from gen_init.py and uses the functions in idioms to do so.