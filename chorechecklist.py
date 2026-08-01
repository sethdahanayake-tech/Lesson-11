#A Chore Checklist Countdown that asks about each chore one at a time, uses a while loop to keep checking until the entire list is empty, and prints a final summary of every chore completed today.
# My Chore Checklist Countdown

# PART 1: Set today's total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today.")

# PART 2: Keep a counter for completed chores and current chore number
completed_chores = 0
current_chore = 1

# PART 3: Repeat while there are still chores left to check off
while current_chore <= total_chores:

    #PART 4: Work out the current chore name from its number
    if current_chore == 1: next_chore = "Make your bed"
    elif current_chore == 2: next_chore = "Feed the pet"
    elif current_chore == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    # PART 5: Only move on to the next chore once it is marked done
    if answer == "yes":
        completed_count += 1
        print ("Great job! Chore completed .")
    else:
        print("Okay, finish it and check again!")

    # PART 6: Print how many chores remain after each check
    print("Chores remaining:" , total_chores - completed_count)
    print()

# PART 7 : This only prints once every chore is marked done
print("===== ALL CHORES COMPLETED =====")
print("Great work finishing your entire checklist today)!\n")

#PART 8: A safe look at what an infinite loop would look like
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose) - a real infinite loop would never stop on own!")

        break 

    #PART 9: Print the final chore checklist summary
    print("\n===== CHORE CHECKLIST SUMMARY =====")
    print("Chores Assigned Today:", original_count)
    print("Chores Completed:", completed_count)
    print("Chores Remaining:", total_chores - completed_count)
    print("====================================")

