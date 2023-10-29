import random


characters = ["Alex", "Bob", "Kevin", "Dan", "Sydney"]
settings = ["a magical forest", "an ancient castle", "a futuristic city", "a quiet village", "a mysterious island"]
problems = ["lost their way", "discovered a hidden treasure", "met a talking animal", "solved a riddle", "uncovered a secret"]
solutions = ["with the help of a wise old wizard", "through their own bravery", "by using their problem-solving skills", "by making new friends", "through a stroke of luck"]


def generatestory():
    character = random.choice(characters)
    setting = random.choice(settings)
    problem = random.choice(problems)
    solution = random.choice(solutions)

    story = f"{character} found themselves in {setting}. They {problem} and had to find a solution. Fortunately, {character} managed to resolve the issue {solution}."

    return story



print("Welcome to the Story Generator!")

while True:
        user_input = input("Do you want to generate a story? (yes/no): ").lower()

        if user_input != "yes":
            print("Goodbye!")
            break

        story = generatestory()
        print("\nHere's your story:")
        print(story)
