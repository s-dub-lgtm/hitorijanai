# hitorijanai

Hitorijanai supports your single life. This work originates in [CODE FOR SOMEONE](https://talent.supporterz.jp/events/2cdd4c2d-7efd-40d1-9887-59500928e3f2).

## How to Run

Install the dependencies using pip.

```
$ pip install -r requirements.txt
```

Edit lines 106-108 in EmoPy/src/fermodel.py. Set `dominant_emotion` as instance variable of `FERModel`.

```python
        self.dominant_emotion = emotion                                                                                                                                                              
        break
print('Dominant emotion: %s' % self.dominant_emotion)
```

Set three environment variables cosidering security.

```
$ export WATSON_API_KEY="XXXX"
$ export ASSISTANT_ID="XXXX"
$ export SLACK_BOT_TOKEN="XXXX"
```

Run the [Real Time Messaging (RTM) API](https://api.slack.com/rtm).

```
$ python main.py
```