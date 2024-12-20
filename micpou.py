import time
import random
import csv

SAVE_FILE = "pet_data.csv"

default_pet = {
    "name": "",
    "hunger": 50,
    "happiness": 50,
    "energy": 50,
    "health": 100,
    "age": 0
}

meals = {
    "Tapsilog": {"hunger": -15, "energy": 10},
    "fruits": {"hunger": -10, "happiness": 5},
    "vegetables": {"hunger": -12, "energy": 8},
    "desserts": {"hunger": -8, "happiness": 10}
}

pet = {}

def main():
    print("Welcome to the Micpou!")
    load_or_create_pet()
    game_loop()

def load_or_create_pet():
    global pet
    saved_pets = read_pets_from_csv()

    if saved_pets:
        print("\nAvailable pets:")
        pet_names = [p["name"] for p in saved_pets]
        for i, pet_name in enumerate(pet_names, 1):
            print(f"{i}. {pet_name}")
        print(f"{len(saved_pets) + 1}. Create a new pet")

        choice = input("\nSelect a pet by number: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(pet_names):
                pet = saved_pets[choice - 1]
                print(f"Welcome back! {pet['name']} missed you.")
            elif choice == len(saved_pets) + 1:
                create_new_pet()
            else:
                print("Invalid choice. Starting fresh!")
                create_new_pet()
        else:
            print("Invalid input. Starting fresh!")
            create_new_pet()
    else:
        print("No saved pets found. Creating a new one.")
        create_new_pet()

def create_new_pet():
    global pet
    pet_name = input("What would you like to name your new pet? ")
    pet = default_pet.copy()
    pet["name"] = pet_name
    print(f"Say hello to {pet_name}!")

def save_pet():
    global pet
    if pet and "name" in pet and pet["name"]:
        saved_pets = read_pets_from_csv()
        updated = False

        for saved_pet in saved_pets:
            if saved_pet["name"] == pet["name"]:
                saved_pet.update(pet)
                updated = True
                break

        if not updated:
            saved_pets.append(pet)

        write_pets_to_csv(saved_pets)
        print("Progress saved successfully!")

def read_pets_from_csv():
    try:
        with open(SAVE_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            return [
                {key: int(value) if key != "name" else value for key, value in row.items()}
                for row in reader
            ]
    except FileNotFoundError:
        return []

def write_pets_to_csv(pets):
    with open(SAVE_FILE, "w", newline="") as file:
        fieldnames = ["name", "hunger", "happiness", "energy", "health", "age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for pet in pets:
            writer.writerow(pet)

def logout_pet():
    global pet
    save_pet()
    pet = {}
    print("You have logged out. Thank you for playing!")

def feed_pet():
    print("\nWhat would you like to feed your pet?")
    for idx, meal in enumerate(meals, 1):
        print(f"{idx}. {meal.capitalize()}")

    choice = input("Enter your choice (1-4): ")

    if choice in ["1", "2", "3", "4"]:
        meal_choice = list(meals.keys())[int(choice) - 1]
        pet["hunger"] += meals[meal_choice]["hunger"]
        pet["happiness"] += meals.get(meal_choice, {}).get("happiness", 0)
        pet["energy"] += meals.get(meal_choice, {}).get("energy", 0)
        print(f"{pet['name']} is eating {meal_choice}! Stats updated.")
    else:
        print("Invalid choice. Please choose a valid meal option.")
    update_stats()

def rest_pet():
    if pet["energy"] < 100:
        pet["energy"] += 20
        print(f"{pet['name']} is resting. Energy restored.")
    else:
        print(f"{pet['name']} is already full of energy!")
    update_stats()

def train_pet():
    if pet["energy"] >= 20:
        print(f"{pet['name']} is training hard!")
        pet["health"] += 15
        pet["energy"] -= 20
        pet["happiness"] += 5
    else:
        print(f"{pet['name']} is too tired to train. Let them rest first!")
    update_stats()

def play_with_pet():
    print("\nLet's play some games!")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the Number")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        rock_paper_scissors()
    elif choice == "2":
        guess_the_number()
    else:
        print("Invalid choice. Please try again.")

def rock_paper_scissors():
    print("\nLet's play Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    pet_choice = random.choice(choices)
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    while player_choice not in choices:
        player_choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()

    print(f"{pet['name']} chose {pet_choice}.")
    if player_choice == pet_choice:
        print("It's a tie! Happiness increased slightly.")
        pet["happiness"] += 5
    elif (player_choice == "rock" and pet_choice == "scissors") or \
         (player_choice == "paper" and pet_choice == "rock") or \
         (player_choice == "scissors" and pet_choice == "paper"):
        print("You win! Happiness increased.")
        pet["happiness"] += 15
        pet["energy"] -= 10
    else:
        print("You lose! Happiness decreased slightly.")
        pet["happiness"] -= 10
        pet["energy"] -= 5
    update_stats()

def guess_the_number():
    print("\nLet's play 'Guess the Number'!")
    number_to_guess = random.randint(1, 10)
    attempts = 3
    guessed_correctly = False

    print(f"{pet['name']} is thinking of a number between 1 and 10. Can you guess it?")
    while attempts > 0 and not guessed_correctly:
        try:
            player_guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            if player_guess == number_to_guess:
                print("Correct! You guessed the number!")
                pet["happiness"] += 20
                guessed_correctly = True
            elif player_guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            attempts -= 1
        except ValueError:
            print("Invalid input! Please enter a number.")

    if not guessed_correctly:
        print(f"Out of attempts! The number was {number_to_guess}.")
        pet["happiness"] -= 10

    pet["energy"] -= 5
    update_stats()

def random_event():
    events = [
        ("Your pet found a treat! Happiness increased.", "happiness", 10),
        ("Oh no! Your pet got sick. Health decreased.", "health", -15),
        ("Your pet is bored. Happiness decreased.", "happiness", -10),
        ("Your pet had a nap. Energy increased.", "energy", 10)
    ]
    if random.random() < 0.3:
        event = random.choice(events)
        print(f"\n[Random Event] {event[0]}")
        stat = event[1]
        pet[stat] += event[2]
        update_stats()

def update_stats():
    pet["hunger"] = min(max(pet["hunger"], 0), 100)
    pet["happiness"] = min(max(pet["happiness"], 0), 100)
    pet["energy"] = min(max(pet["energy"], 0), 100)
    pet["health"] = min(max(pet["health"], 0), 100)

    print("\nCurrent Stats:")
    print(f"  Hunger: {pet['hunger']}")
    print(f"  Happiness: {pet['happiness']}")
    print(f"  Energy: {pet['energy']}")
    print(f"  Health: {pet['health']}")
    print(f"  Age: {pet['age']} days\n")

    if pet["health"] <= 0:
        print(f"Game Over! {pet['name']} passed away.")
        exit()

def game_loop():
    print("\nStarting the game loop!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet rest")
        print("3. Train your pet")
        print("4. Play with your pet")
        print("5. Save and logout")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            feed_pet()
        elif choice == "2":
            rest_pet()
        elif choice == "3":
            train_pet()
        elif choice == "4":
            play_with_pet()
        elif choice == "5":
            logout_pet()
            break
        else:
            print("Invalid choice. Please try again.")

        random_event()
        time.sleep(1)
    
if __name__ == "__main__":
    main()
