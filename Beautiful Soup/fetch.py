#Scrapping a Real Website
from bs4 import BeautifulSoup 
import requests
import time

print("Enter the skill you are unfamiliar with: ")
unfamiliar_skill = input('>')
print(" ")
print("Recent Jobs Available are:")
def find_jobs():
    url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&txtLocation=&cboWorkExp1=-1'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li')
    for index,job in enumerate(jobs):
        published_date = getattr(job.find('span',class_="posting-time"),'text',None)
        if(published_date!=None): published_date=published_date[:-1]
        if (published_date!=None and int(published_date)<=10):
            job_name = job.find('h4').text.replace(' ','')
            skills = job.find('div',class_="srp-keyskills").text.replace(' ','')   #replace for removing unwanted spaces
            more_info = job.h3.a['href']
            if unfamiliar_skill not in skills:
                with open(f'data/{index}.txt','w') as f:
                        f.write(f"Company Name: {job_name.strip()}\n")
                        f.write(f"Required Skills: {skills.strip()}\n")
                        f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes....")
        time.sleep(time_wait*60)