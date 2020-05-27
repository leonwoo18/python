import csv
from cs50 import get_string

file = open("phonebook.csv", "a")
name = get_string("Name: ")
number = get_string("Number: ")

writer = csv.writer(file) #.writer()来自csv这个包
writer.writerow((name, number)) #.writerow()也来自csv

file.close()
