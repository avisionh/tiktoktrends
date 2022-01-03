from TikTokApi import TikTokApi


# starts TikTok API
api = TikTokApi.get_instance()

# number of trending TikToks to display
N_RESULTS = 1000

# get list of dictionaries of trending objects
trending = api.by_trending(count=N_RESULTS)

for tiktok in trending:
    print(tiktok['id'])

print(len(trending))

# look at first trending
trending[3]

## extract as json
## get most trending videos at end of each UK day
