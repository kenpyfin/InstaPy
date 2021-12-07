"""
This template is written by @the-unknown
What does this quickstart script aim to do?
- This is my template which includes the new QS system.
  It includes a randomizer for my hashtags... with every run, it selects 10
  random hashtags from the list.
NOTES:
- I am using the bot headless on my vServer and proxy into a Raspberry PI I
have at home, to always use my home IP to connect to Instagram.
  In my comments, I always ask for feedback, use more than 4 words and
  always have emojis.
  My comments work very well, as I get a lot of feedback to my posts and
  profile visits since I use this tactic.
  As I target mainly active accounts, I use two unfollow methods. 
  The first will unfollow everyone who did not follow back within 12h.
  The second one will unfollow the followers within 24h.
"""

import random
from instapy import InstaPy
from instapy import smart_run
from utilities import *

# get a session!
session = InstaPy(username='ken_c_c_photography', password=readgateway(2), headless_browser=True)

# let's go! :>
with smart_run(session):
    hashtags = ['travelcouples', 'travelcommunity', 'passionpassport',
                'travelingcouple',
                'backpackerlife', 'travelguide', 'travelbloggers',
                'travelblog', 'letsgoeverywhere',
                'travelislife', 'stayandwander', 'beautifuldestinations',
                'moodygrams',
                'ourplanetdaily', 'travelyoga', 'travelgram', 'sunsetporn',
                'lonelyplanet',
                'igtravel', 'instapassport', 'travelling', 'instatraveling',
                'travelingram',
                'mytravelgram', 'skyporn', 'traveler', 'sunrise',
                'sunsetlovers', 'travelblog',
                'sunset_pics', 'visiting', 'ilovetravel',
                'photographyoftheday', 'sunsetphotography',
                'explorenature', 'landscapeporn', 'exploring_shotz',
                'landscapehunter', 'colors_of_day',
                'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                'thegreatoutdoors',"life","#写真好きな人と繋がりたい"]

    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=50, times=1)
    session.set_do_comment(enabled=True, percentage=60)
    session.set_comments([
                             u'Amazing!!',
                             u'Awesome photo! 😎'
                             u'What an amazing shot! :heart_eyes: What do '
                             u'you think of my recent shot?',
                             u'Wonderful!! :heart_eyes: Would be awesome if '
                             u'you would checkout my photos as well!',
                             u'Wonderful!! :heart_eyes: I would be honored '
                             u'if you would checkout my images and tell me '
                             u'what you think. :wink:',
                             u'Nice shot! Feel free to take a look at my recent shots. 😊',
                             u'This is awesome!! :heart_eyes: Any feedback '
                             u'for my photos? :wink:',
                             u'This is awesome!! :heart_eyes:  maybe you '
                             u'like my photos, too? :wink:',
                             u'I really like the way you captured this. I '
                             u'bet you like my photos, too :wink:',
                             u'Great capture!! :smiley: Any feedback for my '
                             u'recent shot? :wink:',
                             u'Great capture!! :smiley: :thumbsup:',
                             u"What camera did you use?"],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows","unfollows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=10,
                                 peak_follows_daily=20,
                                 peak_unfollows_hourly=150,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=5000)

#     session.set_quota_supervisor(enabled=True,
#                                  sleep_after=["likes", "follows", "server_calls", "unfollows"],
#                                  sleepyhead=True, stochastic_flow=True,
#                                  notify_me=True,
#                                  peak_likes=(80, 300),
#                                  peak_comments=(21, 250),
#                                  peak_follows=(40, 300),
#                                  peak_unfollows=(40, 300),
#                                  peak_server_calls=(500, None))


    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_tags(my_hashtags, amount=30, media="Photo")
    session.unfollow_users(amount=20, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=24 * 60 * 60, sleep_delay=655)
#     session.unfollow_users(amount=20, instapy_followed_enabled=True, instapy_followed_param="all",
#                            style="FIFO", unfollow_after=24 * 60 * 60,
#                            sleep_delay=601)
#     session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='travel', engagement_mode='no_comments')