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

'''

PLEASE INSTALL FIREFOX-GECKODRIVER IN THE SERVER FIRST BY RUNNING sudo apt install firefox-geckodriver

'''
import numpy as np
from instapy import InstaPy
from instapy import smart_run
from utilities import *
from datetime import datetime,timedelta



user_name = 'kx_imaginary'
print(datetime.now())

if datetime.now().hour > 18 and datetime.now().hour <20:
    remove_cookie(user_name)

# get a session!
session = InstaPy(username=user_name, password=readgateway(4), headless_browser=True)

# let's go! :>
with smart_run(session):
    hashtags = ["modelingphotography","portaitsquad","bevisuallyinspried","Senseports","portraitgasm",
                "写真好きな人と繋がりたい","portraitpage","portrait","actorlife","setlife","portraitphotography"
                ,"igtones"
                ,"gramkilla"
                ,"portraitclub"
                ,"portraits_vision"
                ,"doports"
                ,"portraitstorm"
                ,"portraitkillers"
                ,"exploremore"
                ,"doports"
                ,"moodyports"
                ,"portraitstream"
                ,"bravoportraits"
                ,"portrait_society"
                ,"vscoportrait"
                ,"artofsystem"
                ,"portraithood"
                ,"worldofportraits"
                ,"portraitcentral"
                ,"portraitenvy"
                ,"portraitsnyc"
                ,"collectivetrend"
                ,"theportraitcentral"
                ,"creative_portraits"
                ,"ourportraitsdays"
                ,"portraitinspo"
                ,"portraitinspiration"
                ,"creativeportraits"
                ,"portraitideas"]
    
    hashtags2 = ['travelcouples', 'travelcommunity', 'passionpassport',
                    'travelingcouple',
                    'backpackerlife', 'travelguide', 'travelbloggers',
                    'travelblog', 'letsgoeverywhere',
                    'travelislife', 'stayandwander', 'beautifuldestinations',
                    'moodygrams',
                    'ourplanetdaily', 'travelyoga', 'travelgram',
                    'lonelyplanet',
                    'igtravel', 'instapassport', 'travelling', 'instatraveling',
                    'travelingram',
                    'mytravelgram', 'skyporn', 'traveler', 'sunrise',
                    'sunsetlovers', 'travelblog',
                    'sunset_pics', 'visiting', 'ilovetravel',
                    'photographyoftheday', 'sunsetphotography',
                    'explorenature', 'landscapeporn', 'exploring_shotz',
                    'landscapehunter',
                    'earthfocus', 'ig_shotz', 'ig_nature', 'discoverearth',
                    'thegreatoutdoors',"life","写真好きな人と繋がりたい"]

#     random.shuffle(hashtags)
#     my_hashtags = hashtags[:10]
    my_hashtags = np.random.choice(hashtags2,6)


    # general settings
    session.set_dont_like(['depression'])
    session.set_do_follow(enabled=True, percentage=20, times=1)
    session.set_do_comment(enabled=True, percentage=15)
    session.set_comments([
                             u'Awesome photo! 😎'
                             u'What an amazing shot! :heart_eyes: ',
                             u'Wonderful!! :heart_eyes:',
                             "I like that! Would love to hear your comments on my work",
                             u'Nice shot! 😊',
                             u'This is awesome!! :heart_eyes:',
                             u'Nice shot! '
                             u'bet you like my photos, too :wink:',
                             u'Great capture!! :smiley: Any feedback for my '
                             u'recent shot? 🤩',
                             u'Great capture!! :smiley: :thumbsup:',
                             "🔥🔥🔥🔥🔥🔥🔥🔥🔥",
                              "Love it! 😎",
                             "😎😎😎😎 Nice shot!",
                             "Good work! Keep going.",
                             "Not bad. 😊",
                             "Nice work. 😎",
                             "I like your photo.",
                             "Stunning shot!🔥🔥",
                             "I think it can be more contract. What do you think?",
                             "Color looks good. Keep the good work."
                            
                             ],
                         media='Photo')
    # session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=50, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=10, min_comments=0)
    # session.set_dont_unfollow_active_users(enabled=True, posts=5)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=10000,
                                    max_following=3000,
                                    min_followers=20,
                                    min_following=0)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows","unfollows"],
                                 sleepyhead=True, stochastic_flow=False,
                                 notify_me=True,
                                 peak_likes_hourly=50,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=50,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=50,
                                 peak_follows_daily=200,
                                 peak_unfollows_hourly=50,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4000)

#     session.set_quota_supervisor(enabled=True,
#                                  sleep_after=["likes", "follows", "server_calls", "unfollows"],
#                                  sleepyhead=True, stochastic_flow=True,
#                                  notify_me=True,
#                                  peak_likes=(80, 300),
#                                  peak_comments=(21, 250),
#                                  peak_follows=(40, 300),
#                                  peak_unfollows=(40, 300),
#                                  peak_server_calls=(500, None))


    # session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    
                          
    
    session.like_by_tags(my_hashtags, amount=10, media="Photo")

#     session.unfollow_users(amount=30, instapy_followed_enabled=True, instapy_followed_param="all",
#                            style="FIFO", unfollow_after=24 * 60 * 60,
#                            sleep_delay=601)
    session.unfollow_users(amount=20, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO", unfollow_after=24 * 60 * 60, sleep_delay=655)
    session.unfollow_users(amount=15, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='travel', engagement_mode='no_comments')