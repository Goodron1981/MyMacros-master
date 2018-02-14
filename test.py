import urllib3
from bs4 import BeautifulSoup
import lxml
import html5lib
import re
pattern = re.compile('\S[а-я]+.+\.\n')
urllib3.disable_warnings()
#from urllib3 import urlopen
proxy = urllib3.ProxyManager('http://10.18.7.6:3128', maxsize=10)
page = proxy.request('GET','https://f.ua/articles/kak-vybrat-skovorodu.html',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
#page = http.request('GET','https://f.ua/articles/kak-vybrat-skovorodu.html',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
#print(page.data)
trace = BeautifulSoup(page.data, "html5lib")
#"lxml"
foop = trace.body
#foop2 = foop.replace('\u2192', '/n')
troof = foop.text
result = pattern.findall(troof)
print(result)
f = open('Testfile.txt', 'w')
for wen in result:
    #if wen !='\u2192' and wen !='\xd7':
        f.write(wen)
    #else:f.write('\n')
f.close()
