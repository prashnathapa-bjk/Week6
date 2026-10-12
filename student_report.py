from colorama import Fore, init
init(autoreset=True)

name=input("Enter student's name: ")
marks=float(input("Enter student's marks: "))

print(Fore.GREEN + "\nStudent Name: {name}")
print("Marks:", marks)
if 40<=marks<=100:
        print(Fore.GREEN + "Result: Pass")
elif 0<=marks<40:
            print(Fore.RED + "Result: Fail")    
else:
    print(Fore.YELLOW + "Invalid marks entered. Please enter marks between 0 and 100.")
