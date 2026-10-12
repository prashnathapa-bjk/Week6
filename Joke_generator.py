
import pyjokes
print("Welcome to the Joke Generator!")
#Display three jokes
for i in range(3):
    joke = pyjokes.get_joke()
    print(f"Joke {i+1}: {joke}")

#Ask the user if they want to hear more jokes
while True:
    answer = input("Do you want to hear another joke? (yes/no): ").strip().lower()
    if answer.lower() == "yes":
        joke = pyjokes.get_joke()
        print(pyjokes.get_joke())

    elif answer.lower() == "no":
        print("Thanks for using the Joke Generator! Goodbye!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
        