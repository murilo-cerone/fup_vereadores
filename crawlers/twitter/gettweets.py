import sys
import tweepy
from tweepy import OAuthHandler

consumer_key = 'Rs1Awf2CODUamrBBsoDYrLJZv'
consumer_secret = 'wnMk1IJYOVAKDj1I0mw7J2AS525oHDC0Hh6H6GQuJN3rVNs0cU'
access_token = '244041130-XWV1YKiXpuDJdVrlbziO1RjxSkoqCpHuF2jBPNGy'
access_secret = 'Kzn2TTblPcsHHkO043RwcQc3E28jG5iyWGyFaHq8Rxm6B'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user = api.get_user('adoteumver_sp')
twts=api.user_timeline(user.id,count=200)


def status_detail(stat):
    #print(dir(stat))
    print("#########################################################################################")
    print("author:",stat.author)
    print("contributors: ",stat.contributors)
    print("coordinates: ",stat.coordinates)
    print("created at: ",stat.created_at)
    print("Destroy: ",stat.destroy)
    print("Entities: ",stat.entities)
    print("Favorite: ",stat.favorite)
    print("Favorite Count: ",stat.favorite_count)
    print("Favorited: ",stat.favorited)
    print("Geo: ",stat.geo)
    print("status ID: ",stat.id)
    print("In reply to (user): ",stat.in_reply_to_screen_name)
    print("In reply to(status): ",stat.in_reply_to_status_id)
    print("is quote: ",stat.is_quote_status)
    print("lang: ",stat.lang)
    print("Parse: ",stat.parse)
    print("Parse List: ",stat.parse_list)
    print("Place: ",stat.place)
    #print("Possibly Sensitive: ",stat.possibly_sensitive)
    print("Retweet: ",stat.retweet)
    print("Retweet Count: ",stat.retweet_count)
    print("Retweeted: ",stat.retweeted)
    print("Retweets: ",stat.retweets)
    print("Source: ",stat.source)
    print("Source(url): ",stat.source_url)
    print("Text: ",stat.text)
    print("User:",stat.user)
    print("Truncated: ",stat.truncated)
    print("#########################################################################################")


for t in twts:
    print(user.name," tweetou:")
    print (t.text,"[",t.created_at,"]")
    #status_detail(t)
	