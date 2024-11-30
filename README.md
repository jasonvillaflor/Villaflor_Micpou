# Villaflor_Micpou
Micpou: Virtual Pet Game
Welcome to Micpou, a fun and interactive virtual pet game where you can take care of your own pet, feed it, play with it, train it, and ensure it stays happy and healthy!

Features
Create a new pet: You can name and start a new pet.
Feed your pet: Choose from various meals that affect your pet's hunger, energy, and happiness.
Play games: Enjoy two games: Rock, Paper, Scissors or Guess the Number with your pet.
Train your pet: Improve your pet’s health and energy.
Rest your pet: Let your pet rest to regain energy.
Random events: Occasional events like finding a treat or getting sick that impact the pet’s stats.
Save your progress: Save and load your pet’s data in between sessions.
Game over conditions: Your pet can pass away due to poor health, hunger, or sadness.

How to Play
Starting the Game
When you run the game, you can either load an existing pet or create a new one. If no saved pet is found, you'll be prompted to create a new pet.
Pet Actions
You can interact with your pet through a series of options:
Feed your pet: Choose a meal to reduce hunger and restore energy or happiness.
Play with your pet: Play either Rock, Paper, Scissors or Guess the Number to increase happiness and sometimes affect energy.
Train your pet: Train your pet to improve its health at the cost of energy and happiness.
Let your pet rest: Your pet can rest to regain energy.

Random Events
Occasionally, a random event will occur, like your pet finding a treat or getting sick. These events can either increase or decrease your pet's stats.

Saving and Logging Out

Save: Your pet’s progress is automatically saved to a file called pet_data.json.

Logout: You can logout at any time to save your progress.

End Game Conditions
The game will end if any of the following occur:

Your pet's health drops to 0.
Your pet's hunger reaches 100.
Your pet’s happiness reaches 0.
When the game ends, your pet will pass away, and you will be given the option to save your progress.

Code Structure

Main Functions
main(): Initializes the game and calls the main game loop.
load_or_create_pet(): Loads an existing pet or creates a new one.
create_new_pet(): Creates a new pet with a user-defined name.
save_pet(): Saves the current pet's progress to a file.
logout_pet(): Logs out the user and saves the current pet's data.
feed_pet(): Allows the user to feed the pet and update its stats.
rest_pet(): Restores the pet's energy.
train_pet(): Improves the pet's health by using energy and happiness.
play_with_pet(): Starts a mini-game (Rock, Paper, Scissors or Guess the Number).
random_event(): Triggers random events that affect the pet’s stats.
update_stats(): Updates and displays the pet’s current stats.
time_decay(): Simulates the passage of time, impacting the pet’s hunger, happiness, energy, and age.
