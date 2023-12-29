import csv
import curses

# File paths
USER_FILE = 'users.csv'

def create_user_file():
    with open(USER_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'username', 'email', 'password', 'house', 'wand', 'patronus'])

def read_users():
    try:
        with open(USER_FILE, newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        create_user_file()
        return []

def write_user(user):
    with open(USER_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user.values())

def find_user_by_username(username):
    users = read_users()
    for user in users:
        if user['username'] == username:
            return user
    return None

def display_home(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the Wizarding World")
    stdscr.addstr(2, 0, "Explore the magic!")
    stdscr.addstr(4, 0, "1. Register")
    stdscr.addstr(5, 0, "2. Login")

    key = stdscr.getch()

    if key == ord('1'):
        display_registration(stdscr)
    elif key == ord('2'):
        user = display_login(stdscr)
        if user:
            display_sorting_hat_quiz(stdscr)
            display_wand_quiz(stdscr)
            display_patronus_quiz(stdscr)

def display_registration(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Register")
    stdscr.addstr(2, 0, "Enter your information:")

    stdscr.addstr(4, 0, "Username:")
    username = stdscr.getstr(5, 0).decode('utf-8')

    stdscr.addstr(6, 0, "Email:")
    email = stdscr.getstr(7, 0).decode('utf-8')

    stdscr.addstr(8, 0, "Password:")
    password = stdscr.getstr(9, 0).decode('utf-8')

    user_data = {'username': username, 'email': email, 'password': password, 'house': '', 'wand': '', 'patronus': ''}
    write_user(user_data)

    stdscr.addstr(11, 0, "Registration successful. Press any key to return to the home screen.")
    stdscr.getch()

def display_login(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Login")
    stdscr.addstr(2, 0, "Enter your login information:")

    stdscr.addstr(4, 0, "Username:")
    username = stdscr.getstr(5, 0).decode('utf-8')

    user = find_user_by_username(username)

    if user:
        stdscr.addstr(7, 0, "Login successful. Press any key to return to the home screen.")
        return user
    else:
        stdscr.addstr(7, 0, "User not found. Press any key to return to the home screen.")
        stdscr.getch()
        return None

# ... (previous code)

# ... (previous code)

def display_sorting_hat_quiz(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Sorting Hat Quiz")
    stdscr.addstr(2, 0, "Answer the following questions:")

    sorting_questions = [
        "What is your preferred element?",
        "What animal do you relate to the most?",
        "What quality do you value the most?",
        "How do you approach challenges?",
        "Which Hogwarts subject is your favorite?",
        "What type of magical creature would you befriend?",
        "What is your ideal way to spend a weekend at Hogwarts?",
        "Which wizarding world profession interests you the most?"
    ]

    sorting_answers = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    
    user_sorting_answers = []

    for i, question in enumerate(sorting_questions):
        stdscr.addstr(4 + i * 3, 0, question)
        
        if i == 1 or i == 5:  # Display options only for the second and sixth questions
            stdscr.addstr(5 + i * 3, 2, "Options:")
            options = sorting_answers
            for j, option in enumerate(options):
                stdscr.addstr(6 + i * 3 + j, 4, f"{j + 1}. {option}")

        stdscr.refresh()
        answer = stdscr.getch() - ord('1')

        if 0 <= answer < len(sorting_answers):
            user_sorting_answers.append(sorting_answers[answer])

    house_assignment = assign_house(user_sorting_answers)

    stdscr.addstr(20, 0, f"You have been assigned to {house_assignment}. Press any key to return to the home screen.")
    update_user_house(house_assignment)
    stdscr.getch()

def assign_house(answers):
    gryffindor_score = answers.count('courage')
    slytherin_score = answers.count('ambition')
    hufflepuff_score = answers.count('loyalty')
    ravenclaw_score = answers.count('knowledge')

    scores = {
        "Gryffindor": gryffindor_score,
        "Slytherin": slytherin_score,
        "Hufflepuff": hufflepuff_score,
        "Ravenclaw": ravenclaw_score
    }

    assigned_house = max(scores, key=scores.get)
    return assigned_house

def update_user_house(house):
    users = read_users()
    user = users[-1]  # Assuming the last user is the one who just registered
    user['house'] = house

    with open(USER_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'username', 'email', 'password', 'house', 'wand', 'patronus'])
        for user in users:
            writer.writerow(user.values())

def display_wand_quiz(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Wand Quiz")
    stdscr.addstr(2, 0, "Answer the following questions:")

    wand_questions = [
        "1. What is your favorite type of wood?",
        "2. Choose a magical core for your wand:",
        "3. What length do you prefer for your wand?"
    ]

    wand_woods = ["Oak", "Holly", "Willow", "Mahogany"]
    wand_cores = ["Phoenix feather", "Dragon heartstring", "Unicorn hair"]
    wand_lengths = ["Short", "Average", "Long"]

    user_wand_answers = []

    for i, question in enumerate(wand_questions):
        stdscr.addstr(4 + i * 2, 0, question)
        
        if i == 0 or i == 1:  # Display options only for the first and second questions
            stdscr.addstr(5 + i * 2, 0, "Options:")
            if i == 0:
                options = wand_woods
            elif i == 1:
                options = wand_cores
            for j, option in enumerate(options):
                stdscr.addstr(6 + i * 2 + j, 2, f"{j + 1}. {option}")

        stdscr.refresh()
        answer = stdscr.getch() - ord('1')

        if 0 <= answer < len(options):
            user_wand_answers.append(options[answer])

    wand_details = assemble_wand(user_wand_answers)

    stdscr.addstr(18, 0, f"Your wand has been crafted! Details: {wand_details}. Press any key to return to the home screen.")
    update_user_wand(wand_details)
    stdscr.getch()

# ... (previous code)

def assemble_wand(answers):
    if not answers:
        return "Not enough information to assemble wand."

    wood, core, length = answers
    return f"Wood: {wood}, Core: {core}, Length: {length}"

# ... (remaining code)

def update_user_wand(wand_details):
    users = read_users()
    user = users[-1]  # Assuming the last user is the one who just registered
    user['wand'] = wand_details

    with open(USER_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'username', 'email', 'password', 'house', 'wand', 'patronus'])
        for user in users:
            writer.writerow(user.values())

def display_patronus_quiz(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Patronus Quiz")
    stdscr.addstr(2, 0, "Answer the following questions:")

    patronus_questions = [
        "1. What is your favorite animal?",
        "2. How would you describe your personality?",
        "3. What element do you feel most connected to?",
        "4. What is your happiest memory?"
    ]

    patronus_animals = ["Stag", "Dolphin", "Phoenix", "Wolf", "Owl", "Hare"]
    
    user_patronus_answers = []

    for i, question in enumerate(patronus_questions):
        stdscr.addstr(4 + i * 2, 0, question)
        
        if i == 0 or i == 2:  # Display options only for the first and third questions
            stdscr.addstr(5 + i * 2, 0, "Options:")
            if i == 0:
                options = patronus_animals
            elif i == 2:
                options = ["Earth", "Air", "Fire", "Water"]
            for j, option in enumerate(options):
                stdscr.addstr(6 + i * 2 + j, 2, f"{j + 1}. {option}")

        stdscr.refresh()
        answer = stdscr.getch() - ord('1')

        if 0 <= answer < len(options):
            user_patronus_answers.append(options[answer])

    patronus_assignment = determine_patronus(user_patronus_answers)

    stdscr.addstr(18, 0, f"Your Patronus is revealed! It's a {patronus_assignment}. Press any key to return to the home screen.")
    update_user_patronus(patronus_assignment)
    stdscr.getch()

def determine_patronus(answers):
    return answers[0]

def update_user_patronus(patronus):
    users = read_users()
    user = users[-1]  # Assuming the last user is the one who just registered
    user['patronus'] = patronus

    with open(USER_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'username', 'email', 'password', 'house', 'wand', 'patronus'])
        for user in users:
            writer.writerow(user.values())

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    while True:
        display_home(stdscr)

if __name__ == '__main__':
    create_user_file()
    curses.wrapper(main)
