# -*- coding: utf-8 -*-
import requests
import json
import re
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr

LINE_BOT_ENDPOINT  = 'https://api.line.me/v2/bot/message/reply'
LINE_PUSH_ENDPOINT = 'https://api.line.me/v2/bot/message/push'
LINE_POST_HEADERS = {
        'Content-type': 'application/json; charset=UTF-8',
        'Authorization':'Bearer '+os.environ['ACCESS_TOKEN'],
}
LINE_GET_HEADERS = {
        'Authorization':'Bearer '+os.environ['ACCESS_TOKEN'],
}

def lambda_handler(event, context):
        print (event.keys())
        print (event.values())
        print (event.items())
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('linebot')
        
        to =''
        # user id の抽出
        user_id = os.environ['USERID']

        payload={
                "to":user_id,
                "messages":[{
                        "type":"text",
                        "text":"push!!!"
            }]
            }
        try:
                post_response = requests.post(LINE_PUSH_ENDPOINT, headers=LINE_POST_HEADERS, data=json.dumps(payload))
        except ValueError:
                  print ("failed access")



