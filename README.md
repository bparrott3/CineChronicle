# CS361-Portfolio-Project

# Communication Contract

1. Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.
      - To request data from the microservice, a command is entered by the user to see if they have me their calorie goal for the day. The user     enters their calories eaten, calories burned, and their calorie goal these numbers are written to a txt file. Once this is completed, the main program will write "start" to a separate txt file, which is read by the microservice to then begin calculation.
      - Example call would be on a CLI with an option given to the user. "Would you like to see if you ahve met your goal for today (y/n)?" The user then enters "y", which will then have the main program ask them for their numbers. Once the user enters those numbers, the process is begun with the main program then writing "start" to a txt file.
      
2. Clear instructions for how to RECEIVE data from the microservice you implemented
      - Once the request is sent and calorie numbers are written in a txt file and the "start" command written in a separate txt file, the    microservice will then read the start txt file and see a start command written there. Once this is detected using a while loop, it then reads the other txt file with calorie numbers, and performs a calculation to see if the user has met thteir calorie goal for the day. It then writes a "yes" or "no" in the start txt file, overwriting the "start" command that was there before. The main program waits for a response and reads the start txt file for a yes or no, and returns that answer to the user with a message.
      
3. UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand

<img width="995" alt="Screenshot 2023-05-08 at 9 00 59 PM" src="https://user-images.githubusercontent.com/107897092/236967882-a3d6dea5-c51f-4e24-aea5-2122515ccab9.png">
