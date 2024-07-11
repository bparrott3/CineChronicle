import os

# Display the welcome message
def display_welcome_message():
    print("╔══════════════════════════════════╗")
    print("║     Welcome to CineChronicle     ║")
    print("╚══════════════════════════════════╝")
    print("Let us help you keep a log of movies you have watched!")
    print("You can add movies to your log, give them a rating, and look up movies you have watched before.")
    print()

# Display the main menu
def display_main_menu():
    print("\n════════════════════════════════════")
    print(" Main Menu")
    print("════════════════════════════════════")
    print("Enter 'a' to add a movie")
    print("Enter 's' to search for a movie")
    print("Enter 'u' to undo your last entry")
    print("Enter 'd' to delete a movie in the log")
    print("Enter 'r' for a Year In Review")
    print("Enter 'l' to view your Movie Log")
    print("Enter 'h' for a help menu about what each menu entry does")
    print("Enter 'q' to quit")
    print()

# Display the movie log
def display_movie_log():
    print("╔══════════════════════════════════════╗")
    print("║            Movie Log                 ║")
    print("╚══════════════════════════════════════╝")
    with open("movie_log.txt", "r") as log_file:
        for line in log_file:
            fields = line.strip().split(",")
            movie_title = fields[0]
            movie_rating = int(fields[1])
            movie_date = fields[2]
            print(f"{movie_title} ({movie_rating}/5 stars) - Watched on {movie_date}")
    print()

# Display the welcome message
display_welcome_message()

# Create the log file if it doesn't exist
if not os.path.exists("movie_log.txt"):
    with open("movie_log.txt", "w"):
        pass

# Loop until the user quits
while True:
    # Display the main menu
    display_main_menu()

    # Prompt the user for an action
    action = input("Please enter your selection: ")

    # Add a movie to the log
    if action.lower() == "a":
        # Prompt the user for the movie details
        title = input("\nEnter the movie title: ")
        rating = int(input("Enter your rating for the movie (1-5 stars): "))
        date = input("What is the date you watched this film? (mm/dd/yyyy): ")
        times_watched = 1

        # Confirm the user's input before adding the movie to the log
        print(f"\nYou entered: {title}, {rating} out of 5 stars, watched on {date}")
        confirm = input("Is this correct? (y/n) ")
        if confirm.lower() == "y":
            # Add the movie to the log file
            with open("movie_log.txt", "a") as log_file:
                log_file.write(f"{title},{rating},{date}\n")
                log_file.flush()
            print(f"{title} added to the movie log.")
        else:
            confirm = input("Entry not added to the movie log. Would you like to return to the main menu? (y/n): ")
            if confirm.lower() == "y":
                print("Ok! Remember, you can select 'h' from the Main Menu if you need more help!")
            else:
                break

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
        confirm = input("\nAre you sure you want to erase/undo the last entry? (y/n): ")
        if confirm.lower() == "y":
            # Remove the last entry from the log file
            with open("movie_log.txt", "r") as log_file:
                lines = log_file.readlines()
            with open("movie_log.txt", "w") as log_file:
                log_file.writelines(lines[:-1])
                log_file.flush()
            print("Last entry removed from the movie log.")
        if confirm.lower() == "n":
            confirm2 = input("Would you like to remove a movie other than the most recent entry? (y/n): ")
            if confirm2.lower() == "y":
                print("Select 'd' from the Main Menu to remove a specific movie from the log or choose 'h' for more help.")
            else:
                print("Last entry not removed from the log. Taking you back to the Main Menu.")

    # Delete a movie from the log
    elif action.lower() == "d":
        # Prompt the user for the movie title to delete
        title = input("Enter the movie title to delete: ")

        # Search for the movie in the log file
        found_movie = False
        log_lines = []
        with open("movie_log.txt", "r") as log_file:
            for line in log_file:
                fields = line.strip().split(",")
                if fields[0] == title:
                    found_movie = True
                    print(f"{title} deleted from the movie log.")
                else:
                    log_lines.append(line)

        # Update the log file without the deleted movie
        with open("movie_log.txt", "w") as log_file:
            log_file.writelines(log_lines)
            log_file.flush()  # Flush the buffer to immediately write to the file

        # Print an error message if the movie is not found
        if not found_movie:
            print(f"{title} not found in the movie log, please try another movie.")

    # Retrieve the list of movies watched in a specific year or display the count (Microservice)
    elif action.lower() == "r":
        year = input("Enter the year to search: ")

        # Prompt the user for the display option
        display_option = input("Enter 'list' to view the list of movies or 'count' to view the count: ")

        if display_option.lower() == "list":
            # Read the movie log file and filter movies by the specified year
            movies = []
            with open("movie_log.txt", "r") as log_file:
                for line in log_file:
                    fields = line.strip().split(",")
                    movie_year = fields[2].split("/")[-1]  # Extract the year from the date
                    if movie_year == year:
                        movie_title = fields[0]
                        movie_rating = int(fields[1])
                        movies.append((movie_title, movie_rating))

            # Sort movies by rating (in descending order)
            movies.sort(key=lambda x: x[1], reverse=True)

            if movies:
                print(f"You watched {len(movies)} movies in {year}.")
                print("Top 5 movies:")
                for i, movie in enumerate(movies[:5]):
                    print(f"{i + 1}. {movie[0]} ({movie[1]}/5 stars)")
            else:
                print(f"No movies found in {year}.")
        elif display_option.lower() == "count":
            # Read the movie log file and count movies watched in the specified year
            count = 0
            with open("movie_log.txt", "r") as log_file:
                for line in log_file:
                    fields = line.strip().split(",")
                    movie_year = fields[2].split("/")[-1]  # Extract the year from the date
                    if movie_year == year:
                        count += 1

            print(f"You watched {count} movies in {year}.")
        else:
            print("Invalid display option. Please try again.")

    # Display the movie log
    elif action.lower() == "l":
        display_movie_log()

    # Help menu
    elif action.lower() == "h":
        print("\n════════════════════════════════════")
        print(" Help Menu")
        print("════════════════════════════════════")
        print("Enter 'a' to add a movie: Adds a movie to the log by entering a movie title, rating on a scale of 1-5, and the date you watched the movie")
        print("Enter 's' to search for a movie: Searches to see if a movie is in the log")
        print("Enter 'u' to undo your last entry: Removes the last entry from the log")
        print("Enter 'd' to delete a movie int the log: Deletes/Removes a specific movie from your log by entering the movie title")
        print("Enter 'r' for a Year In Review: Shows a list of movies you watched in a specific year")
        print("Enter 'l' to view your Movie Log: Shows a list of all of the movies currently in your log")
        print("Enter 'q' to quit: Quits and exits the program")
        print()

    # Quit the program
    elif action.lower() == "q":
        print("Thanks for using CineChronicle!")
        break

    # Handle invalid input
    else:
        print("Invalid input. Please choose an action from the menu.")
