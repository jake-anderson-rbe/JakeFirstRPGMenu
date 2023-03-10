# Jake Anderson, CS30
# RPG Menu Practice
import sys

# prints intro and correct or valid actions for player
print("you are at the entrance of campbell")
correct_actions = ["actions", "directions"]
places = ["gym", "bathroom", "class", "library"]
actions = ["go somewhere", "punch", "block", "eat", "quit"]
# prints a list of valid actions
# valid actions
while True:
    print("what will you do?")
    for action in actions:
      print(f"* {action}")
    # prints out chosen action
    action_input = input("you: ")
    # checks if action is in the "actions" list
    if action_input.lower() in actions:
     if action_input.lower() == "go somewhere":
        for place in places:
          print(f"* {place}")
        place_input = input("where do you go? ")
        # checks if input is in "places" list
        if place_input.lower() in places:
          print(f"you go to the {place_input}")
        elif place_input.lower() not in places:
          print("you can't go there!")
    elif action_input.lower() == "quit":
        print("see you later!")
        sys.exit()
    # checking if input is in "actions" list
    elif action_input.lower() in actions:
        print(f"you {action_input.title()}!")

    elif action_input.lower() not in actions:
      print("you can't do that!")