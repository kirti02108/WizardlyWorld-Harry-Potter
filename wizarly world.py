import curses
import csv
import os

USER_FILE = 'users.csv'

def get_visible_input(stdscr, y, x, prompt):
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()
    curses.echo()
    curses.curs_set(1)
    input_bytes = stdscr.getstr(y + 1, x, 50)
    curses.noecho()
    curses.curs_set(0)
    return input_bytes.decode('utf-8').strip()

def create_user_file():
    if not os.path.exists(USER_FILE):
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

def get_next_id():
    users = read_users()
    return str(len(users) + 1)

def write_user(user):
    with open(USER_FILE, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'username', 'email', 'password', 'house', 'wand', 'patronus'])
        writer.writerow(user)

def find_user_by_username(username):
    users = read_users()
    for user in users:
        if user['username'] == username:
            return user
    return None

def update_user_field(user, field, value):
    users = read_users()
    for u in users:
        if u['username'] == user['username']:
            u[field] = value
            break
    with open(USER_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'username', 'email', 'password', 'house', 'wand', 'patronus'])
        writer.writeheader()
        writer.writerows(users)

def display_home(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome to the Wizarding World")
        stdscr.addstr(2, 0, "1. Register")
        stdscr.addstr(3, 0, "2. Login")
        stdscr.addstr(4, 0, "3. Exit")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            display_registration(stdscr)
        elif key == ord('2'):
            user = display_login(stdscr)
            if user:
                display_sorting_hat_quiz(stdscr, user)
                display_wand_quiz(stdscr, user)
                display_patronus_quiz(stdscr, user)
        elif key == ord('3'):
            break

def display_registration(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Register New Wizard")
    username = get_visible_input(stdscr, 2, 0, "Username:")
    email = get_visible_input(stdscr, 4, 0, "Email:")
    password = get_visible_input(stdscr, 6, 0, "Password:")

    user_data = {
        'id': get_next_id(),
        'username': username,
        'email': email,
        'password': password,
        'house': '',
        'wand': '',
        'patronus': ''
    }

    write_user(user_data)
    stdscr.addstr(8, 0, "Registration successful! Press any key to return.")
    stdscr.getch()

def display_login(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Login")
    username = get_visible_input(stdscr, 2, 0, "Username:")
    password = get_visible_input(stdscr, 4, 0, "Password:")

    user = find_user_by_username(username)
    if user and user['password'] == password:
        stdscr.addstr(6, 0, "Login successful. Press any key to continue.")
        stdscr.getch()
        return user
    else:
        stdscr.addstr(6, 0, "Invalid username or password. Press any key to retry.")
        stdscr.getch()
        return None

def display_sorting_hat_quiz(stdscr, user):
    stdscr.clear()
    stdscr.addstr(0, 0, "Sorting Hat Quiz")

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

    user_answers = []
    for i, q in enumerate(sorting_questions):
        answer = get_visible_input(stdscr, 2 + i * 2, 0, f"{q}")
        user_answers.append(answer)

    house = assign_house(user_answers)
    update_user_field(user, 'house', house)
    stdscr.addstr(20, 0, f"You have been sorted into {house}! Press any key to continue.")
    stdscr.getch()

def assign_house(answers):
    traits = {
        'gryffindor': ['bravery', 'courage', 'daring', 'fire'],
        'slytherin': ['ambition', 'cunning', 'resourceful', 'water'],
        'hufflepuff': ['loyalty', 'kindness', 'earth', 'friendship'],
        'ravenclaw': ['intelligence', 'wisdom', 'air', 'creativity']
    }

    scores = {'Gryffindor': 0, 'Slytherin': 0, 'Hufflepuff': 0, 'Ravenclaw': 0}

    for ans in answers:
        a = ans.lower()
        for house, keywords in traits.items():
            if any(k in a for k in keywords):
                scores[house.capitalize()] += 1

    return max(scores, key=scores.get)

def display_wand_quiz(stdscr, user):
    stdscr.clear()
    stdscr.addstr(0, 0, "Wand Quiz")

    wand_questions = [
        "What is your favorite type of wood?",
        "Choose a magical core for your wand:",
        "What length do you prefer for your wand?"
    ]

    answers = []
    for i, q in enumerate(wand_questions):
        answer = get_visible_input(stdscr, 2 + i * 2, 0, f"{q}")
        answers.append(answer)

    wand = f"{answers[0]} wood with a {answers[1]} core, {answers[2]} length"
    update_user_field(user, 'wand', wand)
    stdscr.addstr(10, 0, f"Your wand: {wand}. Press any key to continue.")
    stdscr.getch()

def display_patronus_quiz(stdscr, user):
    stdscr.clear()
    stdscr.addstr(0, 0, "Patronus Quiz")

    questions = [
        "What is your favorite animal?",
        "How would you describe your personality?",
        "What element do you feel most connected to?",
        "What is your happiest memory?"
    ]

    answers = []
    for i, q in enumerate(questions):
        answer = get_visible_input(stdscr, 2 + i * 2, 0, f"{q}")
        answers.append(answer)

    patronus = determine_patronus(answers)
    update_user_field(user, 'patronus', patronus)
    stdscr.addstr(12, 0, f"Your Patronus is: {patronus}. Press any key to finish.")
    stdscr.getch()

def determine_patronus(answers):
    # Very basic logic: use first answer as the Patronus
    return answers[0].title()

def main(stdscr):
    curses.curs_set(1)
    create_user_file()
    display_home(stdscr)

if __name__ == '__main__':
    curses.wrapper(main)
