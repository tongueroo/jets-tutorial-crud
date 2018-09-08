from pprint import pprint
import json
import platform

def lambda_handler(event, context):
    message = 'PostsController#index hi from python %s' % platform.python_version()
    return response({'message': message}, 200)

def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json'
            },
        }