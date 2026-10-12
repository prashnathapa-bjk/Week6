import emoji

name = input("Enter your name: ")

print(emoji.emojize("Hello " + name + "! :smile:"))

activity = input("What is your favorite activity? ")

print("Your favorite activity is", activity + "!")

print(emoji.emojize("Keep learning Python! :thumbs_up:"))
