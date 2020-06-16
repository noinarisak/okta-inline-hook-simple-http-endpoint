import json
import datetime


def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def add_claim(event, context):
    body = {
        "commands": [
            {
            "type": "com.okta.identity.patch",
            "value": [
                {
                    "op": "add",
                    "path": "/claims/extPatientId",
                    "value": "42"
                }
            ]
            }
        ],
        "debugContext": {
            "debugData": {
                "requestUri": "/uri/info/here"
            }
        },
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response