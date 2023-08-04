"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

connection = psycopg2.connect(host="localhost", database="north", user="postgres", password="24586744")


def reads_csv_and_adds_to_bd(path, query):
    """Функция для считывания и записи данных в файл"""
    with open(path) as file:
        csv_list = csv.reader(file)
        next(csv_list)
        with connection.cursor() as curs:
            curs.executemany(query, csv_list)
    connection.commit()


query_customers = "INSERT INTO customers VALUES (%s, %s, %s)"
query_employees = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)"
query_orders = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)"

reads_csv_and_adds_to_bd('north_data/customers_data.csv', query_customers)
reads_csv_and_adds_to_bd('north_data/employees_data.csv', query_employees)
reads_csv_and_adds_to_bd('north_data/orders_data.csv', query_orders)
