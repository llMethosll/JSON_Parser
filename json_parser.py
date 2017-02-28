#!/usr/bin/python
import sqlite3
import json

conn = sqlite3.connect('json_table.sqlite')
cursor = conn.cursor()

def add_into_db(country_name, years, population):
    """The function of entering the data into the database """
    cursor.execute("INSERT INTO country (country_name, year, population) VALUES "
                   "('%s', %s, %s)"%(country_name, years, population))
    conn.commit()


def read_json(filename):
    """ json file reading function"""
    with open(filename) as f:
        json_data = json.load(f)
        return json_data

def parse_json(data):
    """ The function works with data from json file"""
    for row in data:
        country_name = row['Country Name']
        population = int(float(row['Value']))
        year = int(float(row['Year']))
        add_into_db(country_name, year, population)

def main():
    """Main function """
    filename = 'population_data.json'
    json_data = read_json(filename)
    parse_json(json_data)


if __name__ == '__main__':
    main()
    cursor.close()
    conn.close