import os
import time

# Display the welcome message
print("Welcome to CineChronicle!")
print("Let us help you keep a log of movies you have watched!")
print("You can add movies to your log, give them a rating, and look up movies you have watched before.")

# Create the log file if it doesn't exist
if not os.path.exists("movie_log.txt"):
    with open("movie_log.txt", "w"):
        pass

# Loop until the user quits
while True:
    # Prompt the user for an action
    action = input("\nEnter 'a' to add a movie, 's' to search for a movie, 'u' to undo your last entry, "
                   "'r' to see your Year In Review, or 'q' to quit: ")

    # Add a movie to the log
    if action.lower() == "a":
        # Prompt the user for the movie details
        title = input("\nEnter the movie title: ")
        rating = int(input("Enter your rating for the movie (1-5 stars): "))
        date = input("What is the date you watched this film? (mm/dd/yyy): ")
        times_watched = 1

        # Confirm the user's input before adding the movie to the log
        print(f"\nYou entered: {title}, {rating} stars, watched on {date}")
        confirm = input("Is this correct? (y/n) ")
        if confirm.lower() == "y":
            # Add the movie to the log file
            with open("movie_log.txt", "a") as log_file:
                log_file.write(f"{title},{rating},{date}\n")
            print(f"{title} added to the movie log.")
        else:
            confirm = input("Entry not added to the movie log. Would you like to try inputting a different way? (y/n): ")
            if confirm.lower() == "y":
                input("Great! Let me help you with that. Try typing the movie you'd like to add here: ")

    # Search for a movie in the log
    elif action.lower() == "s":
        # Prompt the user for the movie title to search for
        title = input("\nEnter the movie title to search for: ")

        # Search for the movie in the log file
        found_movie = False
        with open("movie_log.txt", "r") as log_file:
            for line in log_file:
                fields = line.strip().split(",")
                if fields[0] == title:
                    found_movie = True
                    rating = int(fields[1])
                    date = fields[2]
                    print(f"{title}: {rating} stars, watched on: {date}")
                    break
        # Print an error message if the movie is not found
        if not found_movie:
            print(f"{title} not found in the movie log, please try another movie.")

    # Undo the last entry
    elif action.lower() == "u":
        # Confirm that the user wants to undo the last entry
        confirm = input("\nAre you sure you want to undo the last entry? (y/n) ")
        if confirm.lower() == "y":
            # Remove the last entry from the log file
            with open("movie_log.txt", "r") as log_file:
                lines = log_file.readlines()
            with open("movie_log.txt", "w") as log_file:
                log_file.writelines(lines[:-1])
            print("Last entry removed from the movie log.")
        else:
            print("Last entry not removed from the movie log.")

    # Microservice
    elif action.lower() == "r":
        year = input("Enter the year to search: ")
        # Write year to the command file to trigger the first program
        with open("start_file.txt", "w") as f:
            f.write(year)

        # Wait for the result to be written to the command file
        while True:
            with open("start_file.txt", "r") as f:
                result = f.read().strip()
                if result != year:
                    break
            time.sleep(1)  # Wait for 1 second before checking again

            # Display the result
        print(f"You watched {result} movies in {year}.")

    # Quit the program
    elif action.lower() == "q":
        print("Thanks for using CineChronicle!")
        break

    # Handle invalid input
    else:
        print("Invalid input. Please choose an action from the menu.")
