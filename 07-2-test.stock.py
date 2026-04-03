from urllib import request
from bs4 import BeautifulSoup

def get_stock():
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90+%EC%A3%BC%EA%B0%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%84%9C%EC%9A%B8&tqi=jN8EolqXKZwsskOxczl-235822&ackey=ra305oyu"
    target=request.urlopen(url) #접속정보 등록
    soup = BeautifulSoup(target,"html.parser")


    tag = "a._target" #온도
#포함한 모든 글들을 추출
    temp=soup.select_one(tag).get_text()
    print('주가:',temp)
    print("end")
get_stock()