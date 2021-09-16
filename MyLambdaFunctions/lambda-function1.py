import json
def lambda_handler(event, context):
    return{
        'status code': 200,
        'body':json.dumps('Hello from Lambda')
    }

