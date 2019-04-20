import boto3
import os
import random
from init import *

# Remember to modify the URL below when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'


# Opening connection to the Mturk server
keys = open(file=key_location, mode='r').read().splitlines()
mturk = boto3.client('mturk',
   aws_access_key_id = keys[0],
   aws_secret_access_key = keys[1],
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# Taking the basic xml template and inserting the vega (or vega lite) code
specs = []
with open(file=xml_location, mode='r') as xml_wrapper:
	split_xml_wrapper = xml_wrapper.read().split('LOCATION_FOR_VEGA_CODE')
	for vega_file in os.listdir(vega_directory):
		with open (file=vega_directory + vega_file, mode='r') as vega:
			contents = vega.read()
			specs.append(split_xml_wrapper[0] + contents + split_xml_wrapper[1])

# Loop through the different HIT's and launch each one
with open(file='hit_ids.txt', mode='w+') as hit_id_file:
	for i in range(len(specs)):
		new_hit = mturk.create_hit(
	    	Title = 'AYYY WE TESTING!!! (' + str(random.randint(1, 100000000)) + str(i) + ')',
	    	Description = 'Answer our questions about visualization!',
	    	Keywords = 'text, quick, labeling',
	    	Reward = '0.15',
	    	MaxAssignments = 100,
	    	LifetimeInSeconds = 172800,
	    	AssignmentDurationInSeconds = 600,
	    	AutoApprovalDelayInSeconds = 14400,
	    	Question = specs[i],
		)	

		# These prints are not necessary, but are nice for testing in sandbox
		print("A new HIT has been created. You can preview it here (" + str(i) + "):")
		print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
		print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")	

		# Write the HIT id to a file so we can get the data back
		hit_id_file.write(new_hit['HIT']['HITId'] + "\n")
		