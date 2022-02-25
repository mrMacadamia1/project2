import csv
import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')
html_data = BeautifulSoup(response.text)
quotes = html_data.find_all(class_='quote')

with open('quotes.csv', 'w') as file:
	# headers_list = ['Author', 'Text', 'Keywords']
	csv_writer = csv.writer(file)
	csv_writer.writerow(['Text','Author','Keywords'])
	for quote in quotes:
		text = quote.find(class_='text').get_text()
		author = quote.find(class_='author').get_text()
		keywords = quote.find(class_='keywords')['content']
		csv_writer.writerow([text, author, keywords])