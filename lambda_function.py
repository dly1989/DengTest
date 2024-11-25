import json

def lambda_handler(event, context):

    # 我想测试下提交更新aws， 今天天气下雨了
    # 再测试下423424243
    print('context', context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }