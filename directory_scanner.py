import requests
import sys

print("""***********SITE DIRECTORY SEARCH TOOL***********""")

if len(sys.argv) < 2:
    print("Type 'python3 directory_scanner.py --help' to find out how the program works")

elif sys.argv[1] == "--help":
    print("""          
python3 directory_scanner.py http://site.com/ wordlist.txt

#Don't forget to put "/" at the end of the site address.
#Write the Wordlist file with the file extension(txt,md).
""")

else:
    
    site = sys.argv[1]
    wordlist = sys.argv[2]

    file = open(wordlist,"r")
    word = file.readlines()

    dir_list = []


    for i in word:
        new_word = i.replace("\n", "")
        dir_list.append(new_word)

    for directory in dir_list:
    
        full_site = site+directory
    
        request = requests.get(full_site)
    
        get = request.status_code
    
        if get == 200:
            print("Directory:",directory,"--","Status Code:",request.status_code)
        
        elif get == 301:
            print("Directory:",directory,"--","Status Code:",request.status_code)
        
        else:
            print("Directory:",directory,"--","Status Code:",request.status_code)
        
    file.close()