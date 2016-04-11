import tweepy

consumer_key = "WH8IzKBOXqlUWrBGU1AYvd0zT";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "pFCv9hLen5bruUIVHwCZEAza6rVxOMIZwl1xOVaMFr7MjRl9zc";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "157636123-C8gEfPuBl6h4izea5FajZhKixtpsUwnYkPyv63me";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "4IimbrhNKNXgZTwK3ro2uqHCf1zANO5Xrk7tJaACOB3SG";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



