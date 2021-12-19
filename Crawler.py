from bs4 import BeautifulSoup
import random
import time
import requests
import csv

MAX_PAGES = 100

# Creating list.csv file for links and number outlinks
with open('list.csv', 'w', encoding='UTF8', newline='') as list:
    writer = csv.writer(list)
    list.close()

def crawler():
    seed = "https://www.apple.com/" 
    page_num = 1
    all_links = [seed] 
    counter = 0

    header_row = ['Link', 'Count', 'Outlink']
    with open('list.csv', 'a', encoding='UTF8', newline='') as list:
        writer = csv.writer(list)
        writer.writerow(header_row)


    while page_num <= MAX_PAGES:
        outlink_count = 0 
        outlinks = []  

        # send request to a page and parsed its url to get html content
        html_page = requests.get(all_links[counter]).text
        soup = BeautifulSoup(html_page, "html.parser")
        body = soup.find('body')

        # Loop to find all links with href on the page that also match to the domain
        for link in body.find_all('a', href=True):
            if link['href'].startswith("https://") and ("apple.com" in link['href']):
                all_links.append(link['href'])
                outlinks.append(link['href'])
                outlink_count += 1

        # Writes links, number of outlinks, and list of outlinks to list.csv
        report_row = [all_links[counter], outlink_count, outlinks]
        with open('list.csv', 'a', encoding='UTF8', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(report_row)


        page_num += 1 
        counter += 1 

    list.close()

# Call Crawler
crawler()
