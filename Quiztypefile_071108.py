import random

def load_credentials():
    credentials = {}
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                # Ensure the line matches the expected format
                if "Name: " in line and ", Password: " in line:
                    try:
                        name, password = line.strip().split(", Password: ")
                        name = name.replace("Name: ", "").strip()
                        password = password.strip()
                        credentials[name] = password
                    except ValueError:
                        print(f"Skipping improperly formatted line: {line.strip()}")
    except FileNotFoundError:
        print("The file 'user_data.txt' does not exist. Starting with an empty credential list.")
    return credentials



def save_credentials(name, password):
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Password: {password}\n")


credentials = load_credentials()


print("Welcome to the quiz")


user_type = input("Are you a new user? (yes/no): ").strip().lower()

if user_type == "no":
    name = input("Enter your name: ")
    if name in credentials:
        password = input("Enter your password: ")
        if credentials[name] == password:
            print("Login successful!")
        else:
            print("Incorrect password. Exiting the program.")
            exit()
    else:
        print("No such user found. Please register as a new user.")
        exit()
else:
    name = input("Enter your name: ")
    password = input("Set a password you want: ")
    save_credentials(name, password)
    print("Registration successful!")

class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, 5)
        self.answers = {}

    def take_quiz(self):
        for i, (question, options, correct_answer) in enumerate(self.questions, 1):
            print(f"Question {i}: {question}")
            for j, option in enumerate(options, 1):
                print(f"  {j}. {option}")
            answer = input("Select an option (1-4) or type 'mark' to attempt later: ")
            if answer.lower() == 'mark':
                self.answers[i] = None
            else:
                self.answers[i] = int(answer)

        for i, (question, options, correct_answer) in enumerate(self.questions, 1):
            if self.answers[i] is None:
                print(f"\nMarked for Review - Question {i}: {question}")
                for j, option in enumerate(options, 1):
                    print(f"  {j}. {option}")
                answer = input("Select an option (1-4): ")
                self.answers[i] = int(answer)

    def calculate_score(self):
        score = 0
        for i, (_, _, correct_answer) in enumerate(self.questions, 1):
            if self.answers[i] == correct_answer:
                score += 1
        return score                                              

questions_python = [
    ("What is the output of print(2 ** 3)?", ["6", "8", "9", "5"], 2),
    ("Which data type is used for text?", ["int", "float", "str", "bool"], 3),
    ("What keyword is used to define a function?", ["def", "func", "define", "lambda"], 1),
    ("What is the default data type for numbers in Python?", ["int", "float", "double", "str"], 1),
    ("Which module is used for math operations?", ["sys", "math", "random", "os"], 2),
    ("What will be the output of print(10 // 3)?", ["3.33", "3", "3.0", "None"], 2),
    ("Which function is used to get the length of a list in Python?", ["size()", "length()", "len()", "count()"], 3),
    ("What is the output of print('Hello'[1])?", ["e", "H", "l", "o"], 1),
    ("Which of the following data types is immutable in Python?", ["list", "dict", "set", "tuple"], 4),
    ("Which keyword is used to start a function definition in Python?", ["func", "def", "function", "define"], 2),
    ("What is the output of print(5 % 2)?", ["0", "2", "1", "5"], 3),
    ("Which of the following methods is used to add an item to a list?", ["add()", "append()", "insert()", "extend()"],2),
    ("How do you start a comment in Python?", ["//", "/*", "#", "<!-- -->"], 3),
    ("What is the result of bool('') in Python?", ["True", "False", "1", "0"], 2),
    ("Which of the following is used to create a new set in Python?", ["[]", "{}", "()", "set()"], 4),
    ("Which method is used to convert a string to lowercase in Python?",["toLower()", "lowercase()", "lower()", "casefold()"], 3),
    ("What does range(5) produce in Python?",["[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4, 5]", "[1, 2, 3, 4]"], 1),
    ("Which of the following is a built-in Python data type?", ["stack", "queue", "dict", "graph"], 3),
    ("What is the correct syntax to check if a is equal to b in Python?", ["a = b", "a == b", "a eq b", "a != b"], 2),
    ("What is the output of print(type(5.0))?",["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'decimal'>"], 2)
]

questions_sql = [
    ("What does SQL stand for?", ["Structured Query Language", "Standard Query Language", "Simple Query Language", "Statement Query Language"], 1),
    ("Which SQL keyword is used to retrieve data from a database?", ["GET", "SELECT", "FETCH", "RETRIEVE"], 2),
    ("Which clause is used to filter rows in SQL?", ["WHERE", "FILTER", "HAVING", "ROW"], 1),
    ("Which function is used to calculate the total of a column in SQL?", ["SUM()", "TOTAL()", "COUNT()", "ADD()"], 1),
    ("What does the `JOIN` keyword do in SQL?", ["Combines data from multiple tables", "Deletes a table", "Filters data", "Creates a new table"], 1),
    ("What is the purpose of the `PRIMARY KEY` constraint?", ["Ensures uniqueness", "Links tables", "Allows null values", "Sorts data"], 1),
    ("Which command is used to insert data into a table?", ["INSERT INTO", "ADD ROW", "CREATE RECORD", "APPEND DATA"], 1),
    ("Which SQL statement is used to delete a table?", ["DELETE TABLE", "REMOVE TABLE", "DROP TABLE", "TRUNCATE"], 3),
    ("What does the `LIKE` operator do?", ["Matches patterns", "Sorts data", "Filters duplicates", "Joins tables"], 1),
    ("Which SQL function is used to count rows?", ["COUNT()", "SUM()", "LENGTH()", "ROWS()"], 1),
    ("What does `DISTINCT` do in a SELECT statement?", ["Sorts the data", "Filters duplicates", "Joins tables", "Calculates totals"], 2),
    ("What is the purpose of the `ORDER BY` clause?", ["Filters rows", "Groups data", "Sorts rows", "Joins tables"], 3),
    ("Which SQL command creates a new table?", ["CREATE TABLE", "NEW TABLE", "MAKE TABLE", "TABLE CREATE"], 1),
    ("What does the `GROUP BY` clause do?", ["Filters data", "Aggregates data", "Sorts data", "Joins data"], 2),
    ("Which SQL keyword is used to update data?", ["SET", "UPDATE", "MODIFY", "CHANGE"], 2),
    ("What does the `FOREIGN KEY` constraint do?", ["Ensures a unique identifier", "Links tables", "Allows null values", "Sorts data"], 2),
    ("Which SQL function is used to find the maximum value?", ["MAX()", "HIGHEST()", "TOP()", "GREATEST()"], 1),
    ("What is the purpose of the `HAVING` clause?", ["Filters groups", "Filters rows", "Sorts data", "Joins tables"], 1),
    ("Which of the following is a valid SQL data type?", ["varchar", "string", "text", "array"], 1),
    ("Which SQL keyword is used to remove duplicates from a result set?", ["REMOVE", "DELETE", "DISTINCT", "FILTER"], 3)
]


questions_html = [
    ("What does HTML stand for?", ["Hyper Text Markdown Language", "Hyper Text Markup Language", "High Text Markup Language", "Hyper Text Making Language"], 2),
    ("Which HTML tag is used to define a hyperlink?", ["<a>", "<link>", "<href>", "<hyperlink>"], 1),
    ("Which attribute is used to provide a unique identifier for an HTML element?", ["id", "class", "name", "style"], 1),
    ("What is the correct HTML tag for inserting a line break?", ["<br>", "<lb>", "<break>", "<hr>"], 1),
    ("Which HTML tag is used to define an unordered list?", ["<ul>", "<ol>", "<list>", "<unordered>"], 1),
    ("Which attribute is used to specify an alternate text for an image?", ["alt", "src", "title", "text"], 1),
    ("Which tag is used to define a table row?", ["<row>", "<td>", "<tr>", "<table>"], 3),
    ("What is the default alignment of text inside a `<p>` tag?", ["center", "left", "right", "justify"], 2),
    ("Which tag is used to embed a video in HTML?", ["<video>", "<embed>", "<source>", "<media>"], 1),
    ("What is the purpose of the `<meta>` tag in HTML?", ["Styling", "Scripting", "Metadata", "Navigation"], 3),
    ("Which of the following tags is used to create a checkbox?", ["<input type='checkbox'>", "<checkbox>", "<box>", "<check>"], 1),
    ("Which tag is used to add a title to an HTML document?", ["<title>", "<head>", "<meta>", "<h1>"], 1),
    ("What is the correct HTML element to define emphasized text?", ["<i>", "<b>", "<em>", "<mark>"], 3),
    ("Which tag is used to display an image in HTML?", ["<img>", "<src>", "<picture>", "<image>"], 1),
    ("What is the correct way to write a comment in HTML?", ["//", "/* */", "<!-- -->", "#"], 3),
    ("Which HTML attribute is used to specify the URL of a linked resource?", ["src", "href", "link", "target"], 2),
    ("Which HTML tag is used to define a division or a section?", ["<section>", "<div>", "<span>", "<body>"], 2),
    ("What does the `<strong>` tag indicate in HTML?", ["Bold text", "Important text", "Header text", "Italic text"], 2),
    ("What is the purpose of the `<form>` element in HTML?", ["To create a table", "To create a form for user input", "To create a link", "To create a navigation bar"], 2),
    ("Which attribute specifies the destination of a link in the `<a>` tag?", ["src", "href", "link", "target"], 2)
]

questions_dsa = [
    ("Which data structure follows LIFO?", ["Queue", "Stack", "Tree", "Graph"], 2),
    ("What is the time complexity of binary search?", ["O(n)", "O(log n)", "O(n^2)", "O(n log n)"], 2),
    ("Which is a linear data structure?", ["Graph", "Tree", "Stack", "Heap"], 3),
    ("Which sorting algorithm has the best average case performance?", ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort"], 2),
    ("What is the height of a balanced binary tree?", ["O(log n)", "O(n)", "O(n^2)", "O(1)"], 1),
    ("What is the size of an int data type in Java?", ["16-bit", "32-bit", "64-bit", "8-bit"], 2),
    ("Which of the following is not a Java keyword?", ["static", "public", "void", "integer"], 4),
    ("What is the purpose of the 'this' keyword in Java?",["Refers to current object", "Refers to parent class", "Refers to super class", "Refers to any class"], 1),
    ("Which method is called when an object is created in Java?", ["constructor", "method", "getter", "setter"], 1),
    ("What is the extension of a compiled Java class?", [".java", ".class", ".jav", ".byte"], 2),
    ("Which keyword is used for inheritance in Java?", ["inherits", "extends", "implements", "instanceof"], 2),
    ("What does JVM stand for?",["Java Variable Machine", "Java Virtual Machine", "Java Vector Machine", "Java Verification Machine"], 2),
    ("Which method can be used to find the length of a string in Java?", ["getSize()", "size()", "length()", "strlen()"],3),
    ("Which of these is not a feature of Java?",["Platform-Independent", "Object-Oriented", "Pointers", "Multithreading"], 3),
    ("Which keyword is used to create an interface in Java?", ["class", "extends", "interface", "implements"], 3),
    ("What is the default value of a boolean variable in Java?", ["true", "false", "1", "null"], 2),
    ("Which keyword in Java is used to handle exceptions?", ["try", "catch", "throw", "All of the above"], 4),
    ("Which of the following loops is entry-controlled?", ["do-while", "while", "for", "Both while and for"], 4),
    ("Which operator is used for bitwise AND in Java?", ["&", "|", "^", "%"], 1),
    ("How can you stop a loop in Java?", ["break", "return", "exit", "continue"], 1)
]


topics = {
    "1": ("Python", questions_python),
    "2": ("Sql", questions_sql),
    "3": ("html", questions_html),
    "4": ("DSA", questions_dsa)
}


while True:
    print("\nSelect a topic for the quiz:")
    print("1. Python")
    print("2. Sql")
    print("3. html")
    print("4. DSA")
    topic_choice = input("Enter the topic number of your choice: ")

    if topic_choice in topics:
        topic_name, questions = topics[topic_choice]
        print(f"\nStarting quiz on {topic_name}...\n")
        quiz = Quiz(questions)
        quiz.take_quiz()
        score = quiz.calculate_score()
        print(f"\nYour score: {score}/{len(quiz.questions)}")


        with open("user_data.txt", "a") as file:
            file.write(f"Name: {name}, Topic: {topic_name}, Score: {score}/{len(quiz.questions)}\n")

    else:
        print("Invalid choice. Please select a valid topic.")