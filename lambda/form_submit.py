import boto3
import json

ses = boto3.client("sesv2")

def handler(event, context):
    body = event["body"]
    body = json.loads("{}".format(body))
    replyto = body["email"]
    subject = body["subject"]
    message = "Name: " + body["name"] + "\n" + "Message: " + body["message"]
    email = ses.send_email(
        FromEmailAddress = "web@jestonlewiscreative.com",
        Destination = {"ToAddresses": ["info@jestonlewiscreative.com"]},
        ReplyToAddresses = [replyto],
        Content = {
            "Simple": {
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": message}}
            }
        }
    )
    
    responseBody = {}
    responseBody["date"] = email["ResponseMetadata"]["HTTPHeaders"]["date"]
    responseBody["id"] = email["MessageId"]
    responseBody["message"] = "Thank you for your email!"
    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = "applications/json"
    responseObject["body"] = json.dumps(responseBody)
    return responseObject
    