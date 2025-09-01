import mysql.connector
import csv
from datetime import date


def get_db_connection(user, password, host, port, database ):
    try:
        connection = mysql.connector.connect(user=user,
        password=password,
        host=host,
        port=port,
        database=database)
    except Exception as error:
        print("Error while connecting")
        return None
    if connection.is_connected():
        return connection


def create_table(table_name, dbconnection):
    sql = f""" CREATE TABLE IF NOT EXISTS {table_name}(
    ticket_id INT PRIMARY KEY,
    trans_date INT,
    event_id INT,
    event_name VARCHAR(50),
    event_date DATE,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    customer_id INT,
    price DECIMAL(10, 2),
    num_tickets INT);"""
    cursor = dbconnection.cursor()
    cursor.execute(sql)
    dbconnection.commit()
    cursor.close()


def convert_csv_to_list_of_tuples_values(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        data = []

        for row in reader:
            ticket_id = int(row[0])
            trans_date = int(row[1].replace("-", ""))
            event_id = int(row[2])
            event_name = row[3]
            event_date = date.fromisoformat(row[4])  # string "YYYY-MM-DD"
            event_type = row[5]
            event_city = row[6]
            customer_id = int(row[7])
            price = float(row[8])
            num_tickets = int(row[9])
            data.append((ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets))
    return data


def load_third_party(connection, table_name, file_path_csv):
    cursor = connection.cursor()
    insert_sql = f""" INSERT IGNORE  INTO {table_name} 
    (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    data = convert_csv_to_list_of_tuples_values(file_path_csv)

    cursor.executemany(insert_sql, data)
    connection.commit()
    cursor.close()

def query_popular_tickets(connection, table_name, curr_date):
    sql_statement = f"""SELECT * FROM {table_name} 
    WHERE event_date >= DATE_SUB('{curr_date}', 
    INTERVAL 1 MONTH)
    ORDER BY num_tickets DESC;"""

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records


def print_most_popular_tickets(data):
    print("Here are the most popular tickets in the past month:")
    for row in data:
        print("- ", row[3])

def main():
    """ PLEASE UPDATE PARAMETER VALUES
    user, password, host, port, database = '', '', '', '', ''
    table_name = ''
    file_path = ""
    curr_date = date(, , )
    """

    connection = get_db_connection(user, password, host, port, database)
    create_table(table_name, connection)
    load_third_party(connection, table_name, file_path)
    popular_tickets = query_popular_tickets(connection, table_name, curr_date)
    print_most_popular_tickets(popular_tickets)


if __name__ == "__main__":
    main()
