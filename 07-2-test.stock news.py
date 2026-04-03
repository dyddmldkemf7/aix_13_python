from urllib import request
from bs4 import BeautifulSoup

url="https://news.naver.com/section/105"
target=request.urlopen(url) #접속정보 등록
soup = BeautifulSoup(target,"html.parser")


tag = "li.rl_item .rl_txt" 
#포함한 모든 글들을 추출
temp=soup.select(tag)
for t in temp:
    title = t.get_text()
    print('기사제목',title)
