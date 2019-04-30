from idioms import *
from gen_init import *
import os

for cmd in cmds:
	strToFunc[cmd[0]](strToTemplate[cmd[0]], cmd[1], cmd[2])

container = ['''
    <!-- Container for the visualization -->
    <div id="visINT_REPLACE"></div>
    <script>
      // Assign the specification to a local variable vlSpec.
      var vlSpec = 
      '''
      , 
      ''';

      // Embed the visualization in the container with id `vis`
      vegaEmbed('#visINT_REPLACE', vlSpec);
    </script>
    ''']

i = 0
html = ''
with open(file=view_vega_template, mode='r') as html_wrapper:
	split_html_wrapper = html_wrapper.read().split('VEGA_LOCATION')
	for vega_file in os.listdir(vega_directory):
		i = i + 1
		with open (file=vega_directory + vega_file, mode='r') as vega:
			contents = vega.read()
			html = (html + 
					container[0].replace('INT_REPLACE', str(i)) + 
					contents + 
					container[1].replace('INT_REPLACE', str(i))
					)
	html = split_html_wrapper[0] + html + split_html_wrapper[1]

with open(file=view_vega_html, mode='w') as html_outfile:
	html_outfile.write(html)
			