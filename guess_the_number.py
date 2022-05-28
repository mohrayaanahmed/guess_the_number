user = int(input("Guess the number between 1 and 10 in a maximum of two tries"))
import random as rd
x = rd.randint(1, 10)
print("\nYou guessed", user)

if user == x:
    print("\nThe number was indeed", x)
    print("\nGuessed on the first try! Congratulations")
else:
    if x > user:
        user2 = int(input("\nWhoops, wrong! HINT: The number is higher than the one you've guessed. Guess again."))
    elif x < user:
        user2 = int(input("\nWhoops, wrong! HINT: The number is lower than the one you've guessed. Guess again."))

if user2 == x:
    print("\nThe number was indeed", x)
    print("\nGuessed on the second try! Congratulations")
else:
    print("\nStill wrong, sorry. The number was", x)