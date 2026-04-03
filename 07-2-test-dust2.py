from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_dust(city="서울"):
    city = quote_plus(city)
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"+city
    target=request.urlopen(url) #접속정보 등록
    soup = BeautifulSoup(target,"html.parser")
    tag = "div.detail_info.lv3 > dl" #미세먼지 오전
    dust=soup.select_one(tag).get_text()
    dust=' '.join(dust.split())
    dust=dust.split()
    result={dust[0]:dust[1]} #'오전':'나쁨

    tag = "div.detail_info.lv2>dl"
    dust=soup.select_one(tag).get_text()
    dust=' '.join(dust.split())
    dust=dust.split()
    result[dust[0]]=dust[1] #'오후':'나쁨'
    # print('result',result)
    return result

get_dust()


# dust=soup.select("dd.lvl") #여러개
# print(list(dust))