import boto3

MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

mturk = boto3.client('mturk',
   aws_access_key_id = "AKIAI5D5VTE72BHZFIQQ ",
   aws_secret_access_key = "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",
   region_name='us-east-1',
   endpoint_url = MTURK_SANDBOX
)

print "I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my Sandbox account"