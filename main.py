from bs4 import BeautifulSoup
import requests
import csv


response = requests.get("https://www.audible.in/")
soup = BeautifulSoup(response.text, 'html.parser')
book_names = soup.findAll(class_="bc-heading bc-color-base bc-text-bold")
book_names_list = [book.getText() for book in book_names]

book_list_array = []
book_array = []


for book in book_names_list:
    book_array.append(book)
    book_list_array.append(book_array)
    book_array = []


fields = ['Name Of Audio Book']
filename = "Audible_Most_Popular_Audio_Books.csv"

with open(filename, 'w', encoding='UTF8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(book_list_array)