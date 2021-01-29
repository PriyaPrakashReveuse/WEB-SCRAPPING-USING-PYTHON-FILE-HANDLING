import sqlite3
import codecs
import urllib.request
from bs4 import BeautifulSoup

file1=open("D:\\rejectlist.txt","r")
ignore=file1.read().split()
ignoreset=set(ignore)
file1.close()
str1=None
chances=input("Enter the no. of website you want to scrap: ")
website=input("Enter the website : ")
req=urllib.request.Request(website)
D={}
f=codecs.open("code.txt", "a+", "utf-8")
page=urllib.request.urlopen(req)
soup=BeautifulSoup(page,"html.parser")
print(soup.title)
print(soup.title.string)
for script in soup(["script","style"]):
    script.extract()
text=soup.get_text()
lines=(line.strip() for line in text.splitlines())
for line in lines:
    print(line)
    line=line.replace(","," ")
    f.write(line)
f.close()
D={}
f=open("code.txt","rb")
words=f.read().split()
wc=len(words)
print(wc)


for word in words:
    if word not in ignoreset:
        if word not in D:
            D[word]=1
        else:
            D[word]+=1
f.close()
for word in sorted(D.keys()):
    print(word,D[word],(D[word]/wc)*100)
conn=sqlite3.connect('proj.sqlite3')
conn.execute("DROP TABLE IF EXISTS WORDS")
conn.execute("CREATE TABLE WORDS(url text,word text,count int)")
for word in sorted(D.keys()):
    #word=word.replace(","," ")
    str1="INSERT INTO WORDS VALUES('www.python.org','"+word+"','"+str(D[word])+"')"
print(str1)

conn.execute("INSERT INTO WORDS VALUES('www.python.org','"+word+"','"+str(D[word])+"')")

cursor = conn.execute("SELECT * FROM WORDS ORDER BY COUNT DESC")

count=1

for row in cursor:
    print("word= ",row[0])
    print("count= ",row[1])
    count+=1
    if (count==1):
        break

