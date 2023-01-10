import requests
from bs4 import BeautifulSoup

def main(URL, dex, file):

    typing = {
        0: "Normal",
        1: "Fire",
        2: "Water",
        3: "Grass",
        4: "Electric",
        5: "Ice",
        6: "Fighting",
        7: "Poison",
        8: "Ground",
        9: "Flying",
        10: "Psychic",
        11: "Bug",
        12: "Rock",
        13: "Ghost",
        14: "Dark",
        15: "Dragon",
        16: "Steel",
        17: "Fairy",
    }

    #URL = "https://bulbapedia.bulbagarden.net/wiki/Charizard_(Pokémon)"
    #URL = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pokémon)"
    page = requests.get(URL)

    #print(page.text)

    soup = BeautifulSoup(page.content, "html.parser")

    #soup = soup.prettify()

    title = soup.title.string
    title = title.split(" ")
    #print(title[0])

    type = soup.find_all("b")

    poktype = ["None", "None"]

    for i in type[0:5]:
        temp = str(i)
        #print(temp)
        for a in range(18):
            if(temp.find(typing[a]) > 0):
                if poktype[0] == "None":
                    poktype[0] = typing[a]
                elif poktype[1] == "None":
                    poktype[1] = typing[a]

    #print(poktype)

    temp_url = soup.find_all("a")

    a = 93
    natdex = ""
    forward = False
    for i in temp_url[93:105]:
        if not forward:

            i = str(i)

            natdex = i[i.find("#")+8:i.find("#")+11]
            #print(natdex)


            try:
                if int(natdex) == int(dex)+1:
                    #print(a,i)
                    forward = True
            except ValueError:
                forward = False

            a+=1

    temp_url = str(temp_url[a])

    #print((temp_url[temp_url.find('\"')+1:]))
    temp_url = temp_url[temp_url.find('\"')+1:]
    temp_url = temp_url[:temp_url.find('\"')]
    URL = "https://bulbapedia.bulbagarden.net" + temp_url

    file.write(str(dex))
    file.write(" ")

    try:
        file.write(str(title[0]))
    except ValueError:
        temp_title = str(title[0][0:len(str(title[0]))-1])
        file.write(temp_title)

    file.write(" ")
    file.write(str(poktype[0]))
    file.write(" ")
    file.write(str(poktype[1]))
    file.write("\n")

    dex = str(int(dex)+1)

    print(URL)

    return URL, dex


URL = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pokémon)"
#URL = "https://bulbapedia.bulbagarden.net/wiki/Chansey_(Pokémon)"
dex = "001"

file = open("PokeData.txt", "a")
#file.write("\n")

for a in range(906):
    URL,dex = main(URL,dex, file)

file.close()