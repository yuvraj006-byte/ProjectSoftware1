1. Database Setup

	> Locate the database file
	> Find the folder containing the game database. Download the .sql file.

	> Open MariaDB (or MySQL).

	> Create the database
	> Run the following command in MariaDB:

	------ CREATE DATABASE project;

	> Import the database
	> Select the new database:

	----- USE project;

	> Then import the .sql file:

	----- SOURCE [DRAG AND DROP THE DATABASE FILE HERE];

	Press Enter. ✅ Your database is now ready.

2. Project Setup

	> Download GameProject
	> Download the folder as a .zip and extract it.

	> Open in a code editor
	> Use PyCharm, VS Code, or any editor of your choice.

3. Install Python Libraries

	> Open a terminal in the project folder and run:

	> pip install bcrypt datetime mysql-connector-python pwinput tabulate

	> Note: Modules like random, sys, time, and json are built into Python and do not need installation.

4. Configure Database Connection

	> Navigate to the folder: getQuery.

	> Open the file getQuery.py.

	> Update your database credentials:

	----	username = "your_username"
	----	password = "your_password"
	----	database = "project"

	> Save the file.

5. Run the Game

	> Open main.py in your editor.

	> Run the file.

	> Enjoy the game! 🎮

6. Tips & Notes

	> Ensure MariaDB is running before starting the game.

	> Double-check credentials in getQuery.py if you encounter connection errors.

	> Recommended: Python 3.10+ for best compatibility.

	> If you encounter missing library errors, re-run the pip install command above.