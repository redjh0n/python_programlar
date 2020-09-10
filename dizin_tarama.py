import requests

print("*"*5,"DİZİN TARAMA PROGRAMI","*"*5,"\nSite Sonuna '/'' koymayı unutmayınız!","Örnek: https://site.com/")

file = open("wordlist.txt","r")
word = file.readlines()

liste = []

site = input("Site Giriniz: ")

for i in word:
    yeni = i.replace("\n", "")
    liste.append(yeni)

for dizin in liste:
    
    tam_site = site+dizin
    
    istek = requests.get(tam_site)
    
    get = istek.status_code
    if get == 200:
        print("Dizin:",dizin,"Status Code:",istek.status_code)
        
    else:
        continue
file.close()