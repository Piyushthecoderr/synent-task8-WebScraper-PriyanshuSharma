import csv
import json

def save_CSV(data):
    with open("data/books.csv","w",newline="",encoding="utf-8") as csvFile:
        fieldnames=["Title","Cost","Rating","Availability"]
        writer=csv.DictWriter(csvFile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("Successful creation of CSV file")

def save_JSON(data):
    with open("data/books.json","w",encoding="utf-8") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    print("Successful creation of JSON file")