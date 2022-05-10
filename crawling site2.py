proxies = {'https':'85.25.95.117:9999',
           'https':'190.145.200.126:9999' ,
           'https':'20.47.108.204:9999' ,
           'https':'54.36.176.76:9999' ,
           'https':'167.114.174.168:9999' ,
           'https':'24.14.225.100:9999' ,
           'https':'212.129.15.88:9999' ,
           'https':'5.189.184.6:9999' ,
          }


import csv 
import random
import time
import requests
import uuid
from bs4 import BeautifulSoup
index = 0
row = []
i = random.choice(list(proxies.values()))
for num in range (0, 10):
    print("page:" + str(num))
    url = 'https://lyricstranslate.com/en/translations/328/32/none/none/none/0/0/0/0?page='+str(num)
    num = int(num)
    result = requests.get(url, i)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    content = bs_obj.find("div", {"class":"ltsearch-results-line"})
    announcement1s = content.findAll("td", {"class" : "ltsearch-songtitle"})
    announcement2s = content.findAll("td", {"class" : "ltsearch-translatelanguages"})
    
 
    for item, lang in zip(announcement1s,announcement2s ):
        #print(item)
        atag = item.find("a")['href']
        time.sleep(1)
        english_only = lang.find("td", {"class" : "ltsearch-translatelanguages"})
        #print(atag)
        #print(lang.text)

    
        link = "https://lyricstranslate.com/" + atag
        #print("https://lyricstranslate.com/" + atag)
        linkResult = requests.get(link)
        subpage = BeautifulSoup(linkResult.content, "html.parser")
        
        if lang.text == "English → Korean":
            #print("correct")
            index += 1
            print(index)
            original = subpage.find("div", {"class" : "song-node-text"})
            translate = subpage.find("div", {"class" : "translate-node-text"})
            #print(original)
            #print(translate)
            artist = subpage.find("li", {"class" : "song-node-info-artist"})
            artist_site = artist.find("a")['href']
            song_name = subpage.find("li", {"class" : "song-node-info-album"})
            song_url_name = song_name.find("a")['href']
            #print(song_url_name)
            #print(artist_site)
            artist_site = artist_site.replace("-lyrics.html","")
            #print(artist_site)
            
            origin_linkResult = requests.get("https://lyricstranslate.com/" + song_url_name)
            origin_song_page = BeautifulSoup(origin_linkResult.content, "html.parser")
        
            for i in range(0,50):
                origin = []
                trans = []
                for j in range(1,50):
                    origin_song = origin_song_page.find("div", {"class" : f"ll-{i}-{j}"})
                    trans_song = translate.find("div", {"class" : f"ll-{i}-{j}"})
                    
                    if origin_song == None and trans_song == None:
                        break    
                    elif origin_song == None:
                        #print("번역 " + trans_song.text.replace('\n',""))
                        trans.append(trans_song.text.replace('\n',""))
                    elif trans_song == None:
                        #print("원곡 " + origin_song.text.replace('\n',""))
                        origin.append(origin_song.text.replace('\n',""))
                    else:
                        #print("번역 " + trans_song.text.replace('\n',""))
                        #print("원곡 " + origin_song.text.replace('\n',""))
                        origin.append(origin_song.text.replace('\n',""))
                        trans.append(trans_song.text.replace('\n',""))
                    #print(origin)
                    #print(trans)
                if origin == [] or trans == []:
                    break
                row.append([uuid.uuid4().hex, ' '.join(origin), ' '.join(trans)])
       

with open('train6.csv', 'w', newline='', encoding = "utf-8") as f:
    write = csv.writer(f)
    write.writerows(row)
    