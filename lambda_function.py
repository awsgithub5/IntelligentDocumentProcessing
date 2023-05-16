import json
import boto3
import textract_utils
import ast
import dynamodb_utils

textract_client=boto3.client('textract',region_name='us-east-1')
s3_client = boto3.client("s3")


def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
    file_reader = json_object['Body'].read().decode("utf-8")
    json_file = ast.literal_eval(file_reader)
    
    
    print("Before event --------")
    #print(event)
    #print(json_file)
    #textract_result = textract_utils.main(event)
    textract_result = textract_utils.main(json_file)

    dynamodb_utils.put_data(textract_result)
    
    return textract_result
