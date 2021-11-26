import instaloader

L = instaloader.Instaloader()

# Login or load session
username = input("Enter your username: ")
password = input("Enter your password: ")

L.login(username, password)


profile = instaloader.Profile.from_username(L.context, username)

print("Fetching followers of profile {}.".format(profile.username))
followers = set(profile.get_followers())

print("Fetching followings of profile {}.".format(profile.username))
followings = set(profile.get_followees())

print("Storing non loyal people you follow")
with open("People that don't follow back", 'w') as f:
    for fings in followings:
        theyLoyal = 0
        for fers in followers:
            if (fings.username == fers.username):
                theyLoyal = 1
        if (theyLoyal == 0):
            print("damn", fings.username, "ain't loyal")
            print(fings.username, file=f)
