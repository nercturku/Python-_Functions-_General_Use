import os
import mysql.connector as database


connection = database.connect(
    user = 'root',
    password = 'Aurinko88',
    host = '127.0.0.1',
    database = "forforecasting")

cursor = connection.cursor()

def get_data(tableName, columnName, start, stop):
    try:
      statement = "SELECT `datetime`, {} FROM `{}` WHERE `datetime` BETWEEN '{}' AND '{}'".format(columnName,tableName, start, stop)
      cursor.execute(statement)
      data = cursor.fetchall()
      dateTime, kWh = zip(*data)
      dateTime = [date_obj.strftime("%Y-%m-%d, %H:%M:%S") for date_obj in dateTime]
      load = list(kWh)
      print(load)
      print(dateTime)
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")


get_data('load', 'kWh', '2021-01-01 00:00:00', '2021-01-01 23:59:59')

connection.close()