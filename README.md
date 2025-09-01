**Getting Started**
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

**Prerequisites**
Python (import mysql.connector, csv,  date)

**Installing**
Download the project
Go to "https://github.com/BoasLee/Event-Ticket-System" -> code -> Download Zip

Open project
Navigate to where you downloaded the zip folder (step 1) -> Right click -> extract all
Navigate to unzipped folder -> Event-Ticket-System-main -> Event Ticket System -> main.py then open the python file.

**Running the tests**
Scroll down to "main" function and look for "PLEASE UPDATE PARAMETER VALUES" section (right below the main definition).
Fill out the parameter values (user, password, host, port, database, table_name, file_path ('third_party_sales.csv' is included in the folder), curr_date (for my same output, I used the date date(2020, 9, 1))
Run the Python program (there should be something like "Here are the most popular tickets in the past month:..." displayed in the console).

**Verify output**
Once the program is run, the output on the console should match the "Output.txt" (included in the folder) file.
