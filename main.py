import random 
import time

# Adding floating text message with smooth animation.
def floating_message():
    text = [
        "Welcome to the Number Guessing Game!",
        "Get ready to test your luck and skill.",
        "Can you guess the correct number? Let's find out! \n"
    ]
    
    for more_text in text:
        print("\n\t\t\t\t\t", end='')  # Aligning the text
        for char in more_text:
            print(char, end='', flush=True)  # Print each character with flush
            time.sleep(0.04)  # Adjust the speed of typing here
        time.sleep(0.4)  # Pause before the next message

# Function for choosing difficulty level
def choice_difficulty():
    print("\nHello sir..!! choose the difficulty level:")
    print("\t 1. Easy: Range 1-50, unlimited attempts.")
    print("\t 2. Medium: Range 1-100, 10 attempts.")
    print("\t 3. Hard: Range 1-200, 7 attempts \n")

    difficulty_level = int(input("Choose your difficulty level (1-3): "))

    # Select the range of attempt.
    if difficulty_level == 1:
        return random.randint(1, 50), None      # Easy with unlimited attempts
    elif difficulty_level == 2:
        return random.randint(1, 100), 10       # Medium with 10 attempts
    elif difficulty_level == 3:
        return random.randint(1, 200), 7        # Hard with 7 attempts
    else:
        print("Invalid choice. Defaulting to Easy mode.")
        return random.randint(1, 50), None      # Default to Easy


# Function for randomly generate motivational feedback message
def motivated_feedback():
    message = [
        "You are almost closer bro...!!!😉",
        "Keep going, you can do it...!!!😎",
        "Don't give up now...!!!🥴",
        "Almost there, try again...!!!🤪",
        "Great effort, you are on the right track...!!!🏃‍♀️‍➡️🏃‍♀️‍➡️"
    ]
    return random.choice(message)


# Main game function
def guessing_game():
    floating_message()
    # Infinite loop, this loop will break if the user doesn't want to play again.
    while True:  
        auto_generate, max_attempt = choice_difficulty()
        guess_count = 0
        score = 100         # Initially the user starts with a score of 100
        hint_counter = 0    # Used to provide hints after a few wrong attempts
        user_input = -1

        while user_input != auto_generate:
            guess_count += 1

            # Check if the user has exceeded the allowed attempts
            if max_attempt and guess_count > max_attempt:
                print(f"\nYou've used all {max_attempt} attempts! The correct number was {auto_generate}.")
                print("Better luck next time!")
                break

            # Validate user input using try-except
            try:
                user_input = int(input(f"Guess the number (Attempt {guess_count}) >>> "))
            except ValueError or TypeError:
                print("Invalid input! Please enter a valid number.")
                continue                # Skip this loop iteration and prompt again

            # Reduce score with each incorrect guess
            score -= 10

            if (user_input > auto_generate):
                print("Lower number please...!!!")
            elif (user_input < auto_generate):
                print("Higher number please...!!!")   


            # Provide a motivational message every 2 attempts
            if guess_count % 2 == 0:
                print(motivated_feedback())
            
            
            # Provide a hint after 3 wrong attempts
            if guess_count >= 3 and hint_counter < 1:
                hint_counter += 1
                if auto_generate % 2 == 0:
                    print("\t\t\t\tHint: The number is even.😁")
                else:
                    print("\t\t\t\tHint: The number is odd.😁")
        
        
        # When the correct guess is made
        if user_input == auto_generate:
            print(f"\nCongrats! The correct number is {auto_generate}")
            print(f"You guessed the number correctly in {guess_count} attempts.")
        
        # Ensure the score does not go below 0
        if score < 0:
            score = 0
        print(f"Your score: {score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            another_text = [ "Thanks for playing...!!!❤️❤️❤️❤️❤️"]
            for word in another_text:
                print("\t\t\t\t\t\t\t", end=" ")
                for another_char in word:
                    print(another_char, end="", flush=True)
                    time.sleep(0.05)
            break  # Exit the loop and end the game

# Run the game
guessing_game()
