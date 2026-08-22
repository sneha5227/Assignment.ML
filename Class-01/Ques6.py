def extract_hashtags(post):
    hashtags = []

    words = post.split()

    for word in words:
        if word.startswith("#"):
            hashtag = word[1:].lower() #The # at index 0 is removed.
            hashtags.append(hashtag)

    return hashtags


post = "Loving the SUNSET! #Nature  #Sunset_Vibes #beautiful"
print(extract_hashtags(post)) 