# WizardlyWorld-Harry-Potter
The provided Python program is a text-based wizarding world interactive quiz application implemented using the curses library. It simulates the experience of registering, logging in, and participating in three different quizzes to determine a user's Hogwarts house, wand details, and Patronus.

The provided program is a text-based interactive Python application that simulates a wizarding world experience, where users can register, log in, and participate in three different quizzes: Sorting Hat Quiz, Wand Quiz, and Patronus Quiz. The program utilizes the curses library to create a simple text-based user interface within the terminal.

Here's a brief description of the main components and functionalities:

1. ser Registration and Login:
   - Users can register by providing a username, email, and password. The registration information is stored in a CSV file named 'users.csv.'
   - After registration, users can log in by entering their username.

2. Sorting Hat Quiz:
   - Users who successfully log in are prompted to take the Sorting Hat Quiz.
   - The quiz consists of eight questions, each associated with one of the four Hogwarts houses: Gryffindor, Slytherin, Hufflepuff, and Ravenclaw.
   - Users answer the questions by selecting options corresponding to the different houses.
   - Based on their answers, the program assigns the user to one of the Hogwarts houses.

3. Wand Quiz:
   - After the Sorting Hat Quiz, users proceed to the Wand Quiz.
   - The Wand Quiz asks three questions related to the user's wand preferences, such as the type of wood, magical core, and preferred length.
   - Users provide answers, and the program assembles the details of their magical wand.

4. Patronus Quiz:
   - Following the Wand Quiz, users take the Patronus Quiz.
   - The Patronus Quiz includes questions related to the user's favorite animal, personality, connection to elements, and happiest memory.
   - Users provide answers, and the program reveals their assigned Patronus.

5. **User Data Storage:**
   - User information, including quiz results and house assignments, is stored in the 'users.csv' file.
   - The program reads and writes user data to maintain user profiles and track their progress.

6. Curses Library Usage:
   - The curses library is employed to create a text-based graphical user interface with a simple menu and interactive quiz screens.
   - The layout and formatting of questions and options are handled using curses functions.
   - The program takes advantage of curses' ability to capture user input and update the display dynamically.

7. Error Handling:
   - The program includes error handling to manage scenarios such as file not found (e.g., during the initial run) and user not found (during login).

8. Main Loop:
   - The main loop of the program continually displays the home screen, allowing users to navigate through registration, login, and quizzes.

Overall, the program provides a fun and interactive experience, allowing users to immerse themselves in the magical world of Hogwarts through a text-based interface.

