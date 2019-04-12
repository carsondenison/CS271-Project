import boto3

# Initializer values and locations for dependencies
xml_location = 'vega_test_3.xml'
vega_location = './vega_files/vega_test_chart_001.vl'
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
keys = open(file='keys.txt',mode='r').read().splitlines()

# Opening connection to the Mturk server
mturk = boto3.client('mturk',
   aws_access_key_id = keys[0],
   aws_secret_access_key = keys[1],
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# Taking the basic xml template and inserting the vega (or vega lite) code
xml = ''
with open(file=xml_location, mode='r') as xml_wrapper:
	with open (file=vega_location, mode='r') as vega:
		split_xml_wrapper = xml_wrapper.read().split('LOCATION_FOR_VEGA_CODE')
		xml = split_xml_wrapper[0] + vega.read() + split_xml_wrapper[1]

# Loop through the different HIT's and launch each one
for i in range(1):
	new_hit = mturk.create_hit(
    	Title = 'What percentage is region 1 of region 2? (123o5622gdd07' + str(i) + ')',
    	Description = 'Look at the graph and type a percent (0 to 100) which is the relative size of the two values',
    	Keywords = 'text, quick, labeling',
    	Reward = '0.15',
    	MaxAssignments = 100,
    	LifetimeInSeconds = 172800,
    	AssignmentDurationInSeconds = 600,
    	AutoApprovalDelayInSeconds = 14400,
    	Question = xml,
	)

	print("A new HIT has been created. You can preview it here:")
	print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
	print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")

	# Write the HIT id to a file so we can get the data back
	# !!! NOTE THIS WILL OVERWRITE IF WE DO MORE THAN ONE HIT
	with open(file='hit_id.txt', mode='w') as hit_id_file:
		hit_id_file.write(new_hit['HIT']['HITId'])

# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=