import json
import os

import cv2
import slack
from EmoPy.src.fermodel import FERModel
from ibm_watson import AssistantV2


@slack.RTMClient.run_on(event='message')
def react(**payload):
    data = payload['data']
    if 'client_msg_id' in data:
        global emotion
        if not emotion:
            _, frame = cv2.VideoCapture(0).read()
            cv2.imwrite('capture.png', frame)
            model.predict('capture.png')
            emotion = model.dominant_emotion

        intent = service.message(
            assistant_id=os.environ["ASSISTANT_ID"],
            session_id=session_id,
            input={'message_type': 'text',
                   'text': data['text']}
        ).get_result()['output']['intents'][0]['intent']

        web_client = payload['web_client']
        channel_id = data['channel']
        web_client.chat_postMessage(
            channel=channel_id,
            text=text[emotion][intent]
        )

        if intent == "感謝":
            rtm_client = payload['rtm_client']
            rtm_client.stop()


target_emotions = ['anger', 'happiness', 'calm']
model = FERModel(target_emotions, verbose=True)
model.model._make_predict_function()
emotion = ''

service = AssistantV2(
    iam_apikey=os.environ["WATSON_API_KEY"],
    version='2019-02-28',
    url='https://gateway.watsonplatform.net/assistant/api'
)
session_id = service.create_session(
    assistant_id=os.environ["ASSISTANT_ID"]
).get_result()['session_id']

text = json.load(open('text.json'))

slack_token = os.environ["SLACK_BOT_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
