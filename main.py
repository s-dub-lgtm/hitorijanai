import os
import slack


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'client_msg_id' in data:
        channel_id = data['channel']
        web_client.chat_postMessage(
            channel=channel_id,
            text="ringo",
        )


slack_token = os.environ["SLACK_API_TOKEN"]
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
