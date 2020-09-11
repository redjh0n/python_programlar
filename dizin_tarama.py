import requests

print("*"*5,"DİZİN TARAMA PROGRAMI","*"*5,"\nSite Sonuna '/'' koymayı unutmayınız!","Örnek: https://site.com/")

site = input("Site Giriniz: ")
wordlist = input("Wordlist Dosyasını Giriniz: ")

file = open(wordlist,"r")
word = file.readlines()

liste = []


for i in word:
    yeni = i.replace("\n", "")
    liste.append(yeni)

for dizin in liste:
    
    tam_site = site+dizin
    
    istek = requests.get(tam_site)
    
    get = istek.status_code
    if get == 200:
        print("Dizin:",dizin,"--","Status Code:",istek.status_code)
        
    elif get == 301:
        print("Dizin:",dizin,"--","Status Code:",istek.status_code)
        
    else:
        print("Dizin:",dizin,"--","Status Code:",istek.status_code)
        
file.close()