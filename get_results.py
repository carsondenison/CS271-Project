import boto3

mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAI5D5VTE72BHZFIQQ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

# You will need the following library
# to help parse the XML answers supplied from MTurk
# Install it in your local environment with
# pip install xmltodict
import xmltodict

# Use the hit_id previously created
hit_id = 'PASTE_IN_YOUR_HIT_ID'

# We are only publishing this task to one Worker
# So we will get back an array with one item if it has been completed

worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])