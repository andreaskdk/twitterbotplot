import twitter

max_api_calls=10000

def getData(screenName):
    with open('secrets/consumerkey', 'r') as file:
        consumerkey = file.read().strip()
    with open('secrets/consumersecret', 'r') as file:
        consumersecret = file.read().strip()
    with open('secrets/accesstoken', 'r') as file:
        accesstoken = file.read().strip()
    with open('secrets/accesstokensecret', 'r') as file:
        accesstokensecret = file.read().strip()

    api = twitter.Api(consumer_key=consumerkey,
                  consumer_secret=consumersecret,
                  access_token_key=accesstoken,
                  access_token_secret=accesstokensecret,
                  sleep_on_rate_limit=True)

    with open(screenName, "w") as data_file:
        cursor =- 1
        api_calls = 0
        while cursor != 0 and api_calls < max_api_calls:
            api_calls += 1
            cursor, previous_cursor, data=api.GetFollowersPaged(screen_name=screenName, cursor=cursor)
            print(cursor)
            print(previous_cursor)
            print(data)
            for u in data:
                data_file.write(u.created_at+'\n')


if __name__ == "__main__":
    getData("SamsungDK")
    #getData("larsloekke")


