countries = {
            "Japan": "Tokyo",
            "Korea": "Seoul",
            "China": "Bejing",
            "India": "New Delhi",
            "Indonesia": "Jakarta",
            "Cyprus": "Nicosia",
            "Malaysia": "Kuala Lampur",
            "North Korea": "Pyongyang"
            }

correct = 0
incorrect = 0

print("Let's play a captial guessing game. Guess the capitals of the 8 following countries.")

for country in countries:
    capital = countries[country]
    print("What is the capital of:", country)
    answer = input("Please type your answer: ")
    if answer == capital:
        print("Correct, you guessed it!")
        correct = +1
    else:
        print("Incorrect, the correct answer is: ", capital)
        incorrect += 1
print("You got", correct, "correct and", incorrect, "incorrect answers.")



