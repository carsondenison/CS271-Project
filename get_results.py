import boto3
# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict

keys = open(file='keys.txt',mode='r').read().splitlines()
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'


mturk = boto3.client('mturk',
	aws_access_key_id = keys[0],
	aws_secret_access_key = keys[1],
	region_name='us-east-1',
	endpoint_url = MTURK_SANDBOX
)

# Get a list of the HIT ID's so we can loop through and get all results
hit_id_file = 'hit_ids.txt'
hit_ids = ''
with open(file=hit_id_file, mode='r') as file_contents:
	hit_ids = file_contents.read().splitlines()

# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed
for i in range(len(hit_ids)):
	hit_id = hit_ids[i]
	worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])
	print()
	print("For HIT number " + str(i) + ":")
	if worker_results['NumResults'] > 0:
		for assignment in worker_results['Assignments']:
			xml_doc = xmltodict.parse(assignment['Answer'])
			print("Worker's answer was:")
			if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
				# Multiple fields in HIT layout
				for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
					print("For input field: " + answer_field['QuestionIdentifier'])
					print("Submitted answer: " + answer_field['FreeText'])
			else:
				# One field found in HIT layout
				print("For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier'])
				print("Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText'])
	else:
		print("No results ready yet for HIT")