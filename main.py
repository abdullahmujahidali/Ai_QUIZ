from random import randint

print("Welcome to my quiz!")


def MlAdv():
    with open("MlAdv.txt", "r") as topic2:
        score = 0
        difficultyLevel = input("Choose the difficulty: Easy, Medium or Hard!")
        questionsForMlAdv = topic2.readlines()
        if difficultyLevel == "Easy":
            for y in range(0, 3):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2 or 3):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect\n")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 2nd question
            for y in range(5, 8):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2 or 3):")
            if userAnswer2 == "2":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 3rd question
            for y in range(10, 13):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2 or 3):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 4th question
            for y in range(15, 18):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2 or 3):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 5th question
            for y in range(20, 23):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2 or 3):")
            if userAnswer2 == "2":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
        elif difficultyLevel == "Medium":
            for y in range(0, 4):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3 or 4):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 2nd question
            for y in range(5, 9):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3 or 4):")
            if userAnswer2 == "2":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 3rd question
            for y in range(10, 14):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3 or 4):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 4th question
            for y in range(15, 19):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3 or 4):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 5th question
            for y in range(20, 24):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3 or 4):")
            if userAnswer2 == "2":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
        elif difficultyLevel == "Hard":
            for y in range(0, 5):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3, 4 or 5):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 2th question
            for y in range(5, 10):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3, 4 or 5):")
            if userAnswer2 == "2":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 3rd question
            for y in range(10, 15):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3, 4 or 5):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 4th question
            for y in range(15, 20):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3, 4 or 5):")
            if userAnswer2 == "3":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
            # 5th question
            for y in range(20, 25):
                print(questionsForMlAdv[y].rstrip())
            userAnswer2 = input("Choose from the following(1, 2, 3, 4 or 5):")
            if userAnswer2 == "2":
                print("Correct!\n")
                with open("Score.txt", "a") as results:
                    results.write("Correct" + "\n")
            else:
                print("incorrect")
                with open("Score.txt", "a") as results:
                    results.write("Incorrect" + "\n")
    calcScore()


def calcScore():
    score = 0
    with open("Score.txt", "r") as results:
        scoreCalc = results.readlines()
        for y in range(0, 5):
            if scoreCalc[y].rstrip() == "Correct":
                score = score + 1

    percentage = (score / 5) * 100
    print("The percentage of questions correct is", percentage)
    if percentage < 40.0:
        print("You have failed the quiz")
        with open("reports.txt", "a") as reports:
            reports.write("\n" + fullUsername + " " + "achieved a grade of fail" + " " + "in the quiz")
    elif percentage >= 40.0 and percentage <= 60.0:
        print("You have passed the quiz")
        with open("reports.txt", "a") as reports:
            reports.write("\n" + fullUsername + " " + "achieved a grade of pass" + " " + "in the quiz")
    elif percentage >= 60.0 and percentage <= 80.0:
        print("You have achieved merit for the quiz")
        with open("reports.txt", "a") as reports:
            reports.write("\n" + fullUsername + " " + "achieved a grade of merit" + " " + "in the quiz")
    elif percentage > 80.0:
        print("You have achieved distinction for quiz")
        with open("reports.txt", "a") as reports:
            reports.write("\n" + fullUsername + " " + "achieved a grade of distinction" + " " + "in the quiz")
    with open("reports.txt", "a") as reports:
        reports.write(
            "\n" + fullUsername + " " + "did the quiz and" + " " + "achieved a score of" + " " + str(score))
        reports.write(
            "\n" + fullUsername + " " + "did the quiz and" + " " + "achieved a percentage of" + " " + str(
                percentage))
    f = open("Score.txt", "w")
    f.close()


with open("useraccount.txt", "w") as userFile:
    usernamePart1 = input("Enter your name:")
    while not usernamePart1.isalpha():
        print("Invalid name, try again")
        usernamePart1 = input("Enter your name:")
    usernamePart2 = input("Enter your age:")
    while not usernamePart2.isdigit():
        print("try again")
        usernamePart2 = input("Enter your age:")
    fullUsername = usernamePart1[:3] + usernamePart2
    userFile.write("Username:" + fullUsername)
    with open("reports.txt", "a") as reports:
        reports.write("\n" + "Username:" + fullUsername)
    print(fullUsername)

MlAdv()