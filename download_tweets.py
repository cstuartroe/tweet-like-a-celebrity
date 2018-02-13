import twitter

api = twitter.Twitter(auth = twitter.OAuth(consumer_key='gafkoAHgzhezUbu03gQ1LWG5N',
                  consumer_secret='WeSTTsNKYAoqyt5HqNCMgqy4cdkUlaA0lIhaWggdORpEgXsON6',
                token='2319318205-dMtFoL3Ge8oVOn7dLYp7PbSqdLkuXx4cYBvfllW',
                  token_secret='p8oCn4YLsgwwaUDmsPWzBHVeGKean6j7svuYEcTtxboSZ'))

users = ['realDonaldTrump','rihanna','elonmusk','KingJames','neiltyson']

def get_timeline(username):
    statuses = api.statuses.user_timeline(screen_name = username, tweet_mode = 'extended', count = 200)
    return [status['full_text'].replace('\n','') for status in statuses]

for user in users:
    tweets = get_timeline(user)

    with open(user + '_tweets.txt','w',encoding='utf-8') as f:
        f.write('\n'.join(tweets))
