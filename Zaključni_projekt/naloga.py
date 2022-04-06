import time

#   Kviz

score = 0

name = str(input("Enter your name: "))
print(f"Welcome to the quiz! {name}")
print("For every correct answer you get 1 point and for the wrong answer you loose 1 point.")


start = time.time()

def q1():
    global score
    print("-> What is the capital city of South Korea?")
    print("a) Busan ")
    print("b) Incheon")
    print("c) Seoul")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "c":
        print("Congratulations! That's correct!")
        score += 1

    else:
        print("Sorry, that was the wrong answer!")
        score -= 1

    q2()


def q2():
    global score
    print("-> What is the population of South Korea?")
    print("a) 45 million")
    print("b) 51 million")
    print("c) 57 million")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "b":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q3()


def q3():
    global score
    print("-> What is the typical dress in South Korea called?")
    print("a) Yukata")
    print("b) Kimono")
    print("c) Hanbok")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "c":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q4()


def q4():
    global score
    print("-> What is South Korea’s formal name?")
    print("a) Republic of Korea")
    print("b) Republic of South Korea")
    print("c) Democratic People's Republic of Korea")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "a":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q5()


def q5():
    global score
    print("-> What is the most popular sport in Korea?")
    print("a) Basketball")
    print("b) Karate")
    print("c) T'aekwondo")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "c":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q6()


def q6():
    global score
    print("-> What is kimchi? ")
    print("a) Pieces of chicken with herbs")
    print("b) A spicy vegetable dish traditionally made from cabbage")
    print("c) Spicy soup with seafood")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "b":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q7()


def q7():
    global score
    print("-> When do Koreans celebrate their birthdays?")
    print("a) Lunar New Year's Day")
    print("b) Ch'usok - Harvest Moon Festival")
    print("c) Hangeul Day")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "a":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q8()


def q8():
    global score
    print("-> What is the major religion of Korea?")
    print("a) Christianity")
    print("b) Buddhism")
    print("c) No preference")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "c":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1
    q9()


def q9():
    global score
    print("-> How many percent of Koreans share the same surname?")
    print("a) 20%")
    print("b) 35%")
    print("c) 50%")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "a":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1

    q10()


def q10():
    global score
    print("-> South Korea is particularly good at one thing. In which category has the country always been in the top five in recent years?")
    print("a) GDP per capita")
    print("b) Highest IQ")
    print("c) Green Growth Index")

    answer = str(input("Your answer [a, b, c]: "))

    if answer == "b":
        print("Congratulations! That's correct!")
        score += 1
    else:
        print("Sorry, that was the wrong answer!")
        score -= 1


q1()

end = time.time()
dd = round(end - start)

if (score >= 7):
    print(f"Wow!!! Excellent job {name}! You needed {dd} seconds to complete the quiz.")
    print(f"Your score is: {score}")

elif (3 < score < 7):
    print(f"Good job {name}! You needed {dd} seconds to complete the quiz.")
    print(f"Your score is: {score}")

else:
    print(f"Better luck next time {name}...You needed {dd} seconds to complete the quiz.")
    print(f"Your score is: {score}")