from idioms import *
from gen_init import *
import os

# Generate vega files
for cmd in cmds:
	strToFunc[cmd[0]](strToTemplate[cmd[0]], cmd[1], cmd[2])

# Generate webpage so we can visually select the ones we want
i = 0
html_body = ''
with open(view_vega_template, mode='r') as template_wrapper:
	html_wrapper = template_wrapper.read()
	for vega_file in os.listdir(vega_directory):
		i = i + 1
		with open (vega_directory + vega_file, mode='r') as vega:
			vega_str = vega.read()
			div_name = vega_file.split(".")[0]
			spec_name = spec_stub + str(i)
			next_embedding = container.replace('DIV_NAME', div_name).replace('SPEC_NAME', spec_name).replace('VEGA_LOCATION', vega_str)
			html_body = html_body + next_embedding

with open(view_vega_html, mode='w') as html_outfile:
	html = html_wrapper.replace('CONTAINER', html_body)
	html_outfile.write(html)
			