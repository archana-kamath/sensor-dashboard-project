import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


sns = boto3.client('sns')
client = boto3.resource('dynamodb', region_name='us-east-1')


def lambda_handler(event, context):
  
 
    table = client.Table('sensorData-dev')
    response = table.scan(
            FilterExpression=(Attr('moisture').lt(305) & Attr('temperature').gt(25) | Attr('humidity').gt(66))
            )

    
    sns_message = str("Hello, \n\n Mail from IoT Sensor Dashboard \n\n Attention Please!! Your plant may need to be watered for healthy growth...")
    try:
        print(response['Items'])
        if response['Items']:
          print(str(sns_message))
		
        subject= "It's time to water your plant"
        print(subject)
		
        sns_response = sns.publish(
        
  		TargetArn='arn:aws:sns:us-east-1:902331659163:MoistureSensorAlerts',
          
  		Message= str(sns_message),
          Subject= str(subject)
          )
          
    except Exception as e:
        print(e)
        raise e
        
    return {
      'statusCode': 200,
      'body': json.dumps('Notification sent successfully!!')
    }
