
proxies = {'https':'85.25.95.117:9999',
           'https':'190.145.200.126:9999' ,
           'https':'20.47.108.204:9999' ,
           'https':'54.36.176.76:9999' ,
           'https':'167.114.174.168:9999' ,
           'https':'24.14.225.100:9999' ,
           'https':'212.129.15.88:9999' ,
           'https':'5.189.184.6:9999' ,
           'https':'103.232.215.194:9999' ,
           
          }


import csv 
import random
import time
import requests
import uuid
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/a/chromedriver.exe')
index = 0
row = []
i = random.choice(list(proxies.values()))
for num in range (1,3): # 페이지 번호 
    print("page:" + str(num))
    url = 'https://kgasa.com/lyrics/korean/page/'+str(num)
    #print(url)
    result = requests.get(url, i)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    content = bs_obj.findAll("a", {"class":"entry-title-link"})
    #song_link = content.find(attr = ['href'])
    #print(content)
    #announcement1s = content.findAll("td", {"class" : "ltsearch-songtitle"})
    #print(announcement1s)
    #announcement2s = content.findAll("td", {"class" : "ltsearch-translatelanguages"})
    

    for item in (content):
        breaker = False
        song_link = item.attrs['href'] 
        #print(song_link)
        time.sleep(1)
        linkResult = requests.get(song_link)
        subpage = BeautifulSoup(linkResult.content, "html.parser")
        hangul = subpage.find("div", {"class": "entry-content"})
        #print(hangul)
        driver.get(song_link)
        
  
        
        hangul_start = 0
        trans_start = 0
        trans_end = 0
        #hangul_lyrics = driver.find_elements_by_tag_name("h3"|"p")
        hangul_lyrics = driver.find_elements_by_xpath('//*[@id="genesis-content"]/article/div//h3|//p' )
        name = subpage.find("h1", {"class": "entry-title"})
        print(name.text)
        for k in range(0,len(hangul_lyrics) ):
            #print(hangul_lyrics[k].text)
            drop = False
            if hangul_lyrics[k].text == "HANGUL" :
                hangul_start = k+1
            if hangul_lyrics[k].text == "ENGLISH TRANSLATION" :
                trans_start = k+1
            if hangul_lyrics[k].text == "we are working on it!" :
                breaker = True
                break
            if "Filed Under: " in hangul_lyrics[k].text :
                trans_end = k+1
                
        if breaker == False:
            '''
            for j in range(hangul_start,trans_start-1):
                origin_lyrics.append(hangul_lyrics[j].text.replace('\n'," "))
            for l in range(trans_start,(trans_start + (trans_start-1-hangul_start))):
                trans_lyrics.append(hangul_lyrics[l].text.replace('\n'," ")) 
            '''    
            for j in range(0, trans_start-1-hangul_start):
                #if hangul_lyrics[trans_start + j].text == "© 2019–2022 kgasa.com | Powered by WordPress and Genesis | Log in" :
                if not ((trans_start - 1) - hangul_start) == ((trans_end - 1) - trans_start):
                    drop == True
                    break
                if drop == False:
                    origin_lyrics = []
                    trans_lyrics = []
                    origin_lyrics.append(hangul_lyrics[hangul_start + j].text.replace('\n'," "))
                    trans_lyrics.append(hangul_lyrics[trans_start + j].text.replace('\n'," "))
                    row.append([uuid.uuid4().hex, ' '.join(origin_lyrics), ' '.join(trans_lyrics)])
                
        #print(origin_lyrics)
        #print(trans_lyrics)
        
        
with open('121.csv', 'w', newline='', encoding = "utf-8") as f:
    write = csv.writer(f)
    write.writerows(row)
    

    '''
            for k in range(1, len(hangul_lyrics)) :
                if hangul_lyrics[k].text == "HANGUL" :
                    print(hangul_lyrics[k].text)
            '''  
'''
        atag = item.find("a")['href']
        
        english_only = lang.find("td", {"class" : "ltsearch-translatelanguages"})
        #print(atag)
        #print(lang.text)

   
        link = "https://lyricstranslate.com/" + atag
        #print("https://lyricstranslate.com/" + atag)
        linkResult = requests.get(link)
        subpage = BeautifulSoup(linkResult.content, "html.parser")
        
        if lang.text == "Korean → English":
            #print("correct")
            index += 1
            print(index)
            original = subpage.find("div", {"class" : "song-node-text"})
            translate = subpage.find("div", {"class" : "translate-node-text"})
            #print(original)
            #print(translate)
            #artist = subpage.find("li", {"class" : "song-node-info-artist"})
            #artist_site = artist.find("a")['href']
            song_name = subpage.find("li", {"class" : "song-node-info-album"})
            if song_name == None:
                continue
            #print(song_name)
            song_url_name = song_name.find("a")['href']
            print(song_url_name)
            #print(artist_site)
            #artist_site = artist_site.replace("-lyrics.html","")
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
       

with open('11~20.csv', 'w', newline='', encoding = "utf-8") as f:
    write = csv.writer(f)
    write.writerows(row)

driver = webdriver.Chrome('C:/Users/a/chromedriver.exe')

driver.get('https://kgasa.com/lyrics/korean/')

driver.find_element_by_link_text('BIG Naughty – Beyond Love (Feat. 10CM) Lyrics').click()

allmusicElement = driver.find_elements_by_css_selector(
    "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")

driver.find_element_by_tag_name('p').text
        '''