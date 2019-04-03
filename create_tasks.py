import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
keys = open(file='keys.txt',mode='r').read().splitlines()

mturk = boto3.client('mturk',
   aws_access_key_id = keys[0],
   aws_secret_access_key = keys[1],
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

print("I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my Sandbox account")

# List of urls of images to use for testing
urls = open(file='urls.txt', mode='r').read().splitlines()
for i in range(len(urls)):
	#print(url)
	question = open(file='questions.xml',mode='r').read().split("IMAGE_URL")
	question_xml = question[0] + urls[i] + question[1]

	new_hit = mturk.create_hit(
    	Title = 'What percentage is region 1 of region 2? (125' + str(i) + ')',
    	Description = 'Look at the graph and type a percent (0 to 100) which is the relative size of the two values',
    	Keywords = 'text, quick, labeling',
    	Reward = '0.15',
    	MaxAssignments = 100,
    	LifetimeInSeconds = 172800,
    	AssignmentDurationInSeconds = 600,
    	AutoApprovalDelayInSeconds = 14400,
    	Question = question_xml,
	)

	print("A new HIT has been created. You can preview it here:")
	print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
	print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")

# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=