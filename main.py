# import the function solve riddle and end game from game_utils
from game_utils import solve_riddle, end_game

# Function to greet the user and explain the game.
def greeting():
    print("Welcome to 'The Lost Treasure Hunt!'")
    print("In this game, you will navigate through different rooms to solve the riddles.")
    print("Your goal is to find the lost treasure. \nYou can navigate by typing commands like 'top' (north), 'down' (south), 'right' (east), 'left' (west).")
    print("Good luck!")

    

def enter_room (current_room):
    print(f"\nYou are now in: {current_room['name']}")
    print(current_room['description'])

    if current_room['riddle']:
        while not solve_riddle(current_room['riddle']):
            pass

# Define the room structure and riddles
rooms = {
    'start_room': {
        'name': 'Starting Room',
        'description': 'You are in a dark room with only one door ahead of you.' ,
        'riddle': {
            'question': 'What has many keys but cant open a single door?',
            'answer': 'Piano'
        },
        'connections': {'top': 'hallway'}
    },
    'hallway': {
        'name': 'Hallway',
        'description': 'A long hallway with doors to the east and west. The treasure room is to the north.',
        'riddle': {
            'question': 'The more of this you take, the larger it becomes. What is it?',
            'answer': 'Footstep'
        },
        'connections': {'top': 'treasure_room', 'left': 'library', 'right': 'garden', 'down': 'start_room'}
    },
    'library': {
        'name': 'Library',
        'description': 'You are in a library filled with ancient books. There is a door to the west.',
        'riddle': {
            'question': 'What can travel around the world while staying in the same corner?',
            'answer': 'Stamp'
        },
        'connections': {'right': 'hallway'}
    },
    'garden': {
        'name': 'Garden',
        'description': 'A beautiful garden with flowers. There is a door to the east.',
        'riddle': {
            'question': 'I speak without a mouth and hear without ears. What am I?',
            'answer': 'Echo'
        },
        'connections': {'left': 'hallway'}
    },
    'treasure_room': {
        'name': 'Treasure Room',
        'description': 'You have found the treasure room. The treasure lies before you.',
        'riddle': None,  # No riddle, the game ends here
        'connections': {}
    }
}

def main():
    greeting()

    current_room_key = 'start_room'
    while True:
        current_room = rooms[current_room_key]
        enter_room(current_room)

        if current_room_key == 'treasure_room':
            print("\nCongratulations! You have found the hidden Treasure!")
            end_game()
        
        direction = input("Which direction would you like to go (top, down, right, left): ").lower()
        if direction in current_room['connections']:
            current_room_key = current_room['connections'][direction]
        else:
            print("You cannot go in that direction. Try another way.")

# Start the game
if __name__ == "__main__":
    main()