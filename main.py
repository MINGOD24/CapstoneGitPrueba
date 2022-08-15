import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings("ignore")

def main():
    # raw_tweets = pd.read_json(r'farmers-protest-tweets-2021-03-5.json', lines=True)
    # raw_tweets = raw_tweets[raw_tweets['lang']=='en']
    # print("Shape: ", raw_tweets.shape)
    # raw_tweets.head(5)
    # users = json_normalize(raw_tweets['user'])
    # users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
    # users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)
    # users.head(5)
    # users = pd.DataFrame(users)
    # users.drop_duplicates(subset=['userId'], inplace=True)
    # print("Shape: ", users.shape)
    # users.head(5)
    # user_id = []
    # for user in raw_tweets['user']:
    #     uid = user['id']
    #     user_id.append(uid)
    # raw_tweets['userId'] = user_id

    # # Remove less important columns
    # cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'source', 'media', 'retweetedTweet', 'quotedTweet', 'mentionedUsers']
    # tweets = raw_tweets[cols]
    # tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)
    # tweets.head(5)
    # tweets = pd.DataFrame(tweets)
    # tweets.drop_duplicates(subset=['tweetId'], inplace=True)
    # print("Shape: ", tweets.shape)
    # tweets.head(5)
    print("Select the function that you want to use:")
    print("[1]: Los top 10 tweets más retweeted")
    print("[2]: Los top 10 usuarios en función de la cantidad de tweets que emitieron.")
    print("[3]: Los top 10 días donde hay más tweets.")
    print("[4]:Los top 10 hashtags más usados.")
    optionSelected = input("Write here your option: ")
    if optionSelected == "1":
        MostRetweeted()
    elif optionSelected == "2":
        MostActiveUsers()
    elif optionSelected == "3":
        MostActiveDays()
    elif optionSelected == "4":
        MostPopularHashtags()
    else:
        print("Invalid option try again")
        main()

def MostRetweeted():
    print("The tweets with most retweeted are: ...")

def MostActiveUsers():
    print("The users with more tweets are: ...")

def MostActiveDays():
    print("The days with more tweets are: ...")

def MostPopularHashtags():
    print("The hashtagas more popular are: ...")


if __name__ == "__main__":
    main()