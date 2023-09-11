import requests 
from bs4 import BeautifulSoup

#url = "https://news.google.com/search?q=covid&hl=en-IN&gl=IN&ceid=IN%3Aen" #this will restrict the code to only one url query ie covid here

#to make it functional for multiple queries we will split and join the start end and the query as follows
start = "https://news.google.com/search?q="
query = "covid".split()
query_separator = "%20".join(query)
end = "&hl=en-IN&gl=IN&ceid=IN%3Aen"

url = start+query_separator+end
html_text = requests.get(url)
soup = BeautifulSoup(html_text.content,'html.parser') #will try lxml also
headlines = soup.find_all('a')
for i in headlines:
    print(i.text)