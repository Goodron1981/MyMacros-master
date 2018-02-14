import urllib3
from bs4 import BeautifulSoup
import lxml
import html5lib
import re
#[А-Я][а-яё]+\S*\s{,1}\S*\s{,1}\S*\s{,1}[.!?]
#https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
pattern = re.compile('[А-ЯЁ].+[а-яё]+[.!?]')
#pattern = re.compile('^[А-Яа-яЁё\s]+$')
urllib3.disable_warnings()
#from urllib3 import urlopen
proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
http = urllib3.PoolManager()
#page = proxy.request('GET','https://f.ua/articles/kak-vybrat-skovorodu.html',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
page = http.request('GET','https://dobre.stb.ua/ua/2016/04/18/kak-vy-brat-ideal-nuyu-skovorodku/',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
#print(page.data)
trace = BeautifulSoup(page.data, "html5lib")
#"lxml"
foop = trace.body
#foop2 = foop.replace('\u2192', '/n')
troof = foop.text
result = pattern.findall(troof)
print(result)
f = open('test.txt', 'w')
for wen in result:
    #if wen !='\u2192' and wen !='\xd7':
        f.write(wen)
    #else:f.write('\n')
f.close()
