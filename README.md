# AirBnB_clone
<img src="https://raw.githubusercontent.com/nickssilver/AirBnB_clone/main/img/hbnb_screenshot.png" alt="cover" />

AirBnB clone - The console
This is the first step towards building the AirBnB clone. It collectively covers the fundamental concepts of higher level programming.
The project involves creating a clone of the Airbnb website, which is an online platform that enables people to book unique accommodations around the world.
The website allows users to search for various types of accommodations, such as apartments, villas, hotels, and hostels, and book them online.
The project is suitable for developers who want to improve their web development skills, especially in front-end development, back-end development, and database management.


The Console
command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
This is the command interpreter for the Airbnb clone website, implementing a back-end system that can interpret user commands and manipulate data without a visual interface.
It is a custom shell or command-line interface (CLI) that allows developers to interact with the website's database directly.
The console should provide a set of commands that developers can use to manipulate data in the database, such as creating new listings, updating existing ones, deleting listings, and querying for information about specific listings
It is built using the Python3 programming language


Installation:
•	Clone this repository: git clone "https://github.com/git@github.com:Sommyj1/AirBnB_clone.git
•	Access AirBnb directory: cd AirBnB_clone
•	Run hbnb(interactively): ./console and enter command
•	Run hbnb(non-interactively): echo "<command>" | ./console.py


Environment:

•	This project is interpreted/tested on 20.04 LTS using python3 (version 3.8.5)


Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.
Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id) | ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all or (hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

Examples:
•	In interactive mode:
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
•	In Non-interactive mode
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$


Models
The folder models contains all the classes used in this project.
File | Description | Attributes
---- | ----------- | ---------- |
base_model.py | ```BaseModel class for all the other classes | ```id, created_at, updated_at```
