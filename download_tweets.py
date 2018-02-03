import twitter
api = twitter.Api(consumer_key='gafkoAHgzhezUbu03gQ1LWG5N',
                  consumer_secret='WeSTTsNKYAoqyt5HqNCMgqy4cdkUlaA0lIhaWggdORpEgXsON6',
                  access_token_key='2319318205-dMtFoL3Ge8oVOn7dLYp7PbSqdLkuXx4cYBvfllW',
                  access_token_secret='p8oCn4YLsgwwaUDmsPWzBHVeGKean6j7svuYEcTtxboSZ')

user_ids = {'neiltyson':'19725644','realDonaldTrump':'25073877','rihanna':'79293791',
            'elonmusk':'44196397','KingJames':'23083404'}

statuses = api.GetUserTimeline('19725644')

##all_comments = []
##for submission in rscotland.top(limit=25):
##    comment_forest = submission.comments
##    comment_forest.replace_more()
##    for comment in list(comment_forest):
##        all_comments += expand(comment)
##
##comment_bodies = [comment.body.replace('\u200b','') for comment in all_comments]
###if we want to ignore newlines in our language model:
##comment_bodies = [comment_body.replace('\n',' ') for comment_body in comment_bodies]
##with open('rscotland_corpus.txt','w',encoding='utf-8') as f:
##    f.write('\n'.join(comment_bodies))
