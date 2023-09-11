#Scraping a sample website
from bs4 import BeautifulSoup

with open('sample.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    #tags = soup.find('h5') #searches the first tag presence
    # course_html_tags = soup.find_all('h5')
    # print("List: ",course_html_tags)
    # for course in course_html_tags:
    #     print(course.text)

    #Target : Find all the course prices corresponding to the course
    course_cards = soup.find_all('div',class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
