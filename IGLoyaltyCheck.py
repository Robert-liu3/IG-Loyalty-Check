import instaloader

L = instaloader.Instaloader()

USER = "your_account"
PROFILE = USER

profile = instaloader.Profile.from_username(L.context, PROFILE)

print("Fetching followers of profile {}.".format(profile.username))
followers = set(profile.get_followers())
