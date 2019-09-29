import os
import slack
from ibm_watson import AssistantV2


@slack.RTMClient.run_on(event='message')
def react(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'client_msg_id' in data:
        response = service.message(
            assistant_id=os.environ["ASSISTANT_ID"],
            session_id=session_id,
            input={'message_type': 'text',
                   'text': data['text']}
        ).get_result()
        print(response)

        channel_id = data['channel']
        web_client.chat_postMessage(
            channel=channel_id,
            text=response['output']['generic'][0]['text'],
        )


service = AssistantV2(
    iam_apikey=os.environ["WATSON_API_KEY"],
    version='2019-02-28',
    url='https://gateway.watsonplatform.net/assistant/api'
)
session_id = service.create_session(
    assistant_id=os.environ["ASSISTANT_ID"]
).get_result()['session_id']

slack_token = os.environ["SLACK_BOT_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
