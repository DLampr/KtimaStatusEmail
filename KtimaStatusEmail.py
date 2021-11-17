import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.ktimatologio.gr/el/anazitisi-periohon/ota/12058" #You should find the url for the specific district you are interested in. This is for ΕΡΕΤΡΙΑ ΕΥΒΟΙΑΣ
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("p") #We get the cadastre status for the body of the email
divs = soup.find_all("div", class_="field__item") #We get the district name status for the subject of the email

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()

conn.login('sender@gmail.com', 'password') #Your email and password

#We send the email from sender@gmail.com to received@hotmail.com
conn.sendmail('sender@gmail.com', 'received@hotmail.com', f'Subject:Κτηματογράφηση {divs[1].text} {divs[0].text}\n\n{results.text.strip()}'.encode('utf-8').strip())

conn.quit()