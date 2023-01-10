
typing = {
        "Normal": 0,
        "Fire": 1,
        "Water": 2,
        "Grass": 3,
        "Electric": 4,
        "Ice": 5,
        "Fighting": 6,
        "Poison": 7,
        "Ground": 8,
        "Flying": 9,
        "Psychic": 10,
        "Bug": 11,
        "Rock": 12,
        "Ghost": 13,
        "Dark": 14,
        "Dragon": 15,
        "Steel": 16,
        "Fairy": 17,
        "None": 18
    }

typing_back = {
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

#[N,F,W,G,E,I,FG,P,G,F,PY,B,R,G,Dra,D,S,F]
# From https://codegolf.stackexchange.com/questions/105331/pokemon-type-chart-and-dual-type-chart
type_weakness = [[1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,2,1,1,.5,.5,1,1,1,1,1,1,2,1,1,.5,2],
[1,.5,1,1,0,2,.5,1,1,1,1,.5,2,1,2,1,1,1],
[1,.5,1,.5,2,1,.5,1,1,1,1,.5,1,2,1,1,1,.5],
[1,1,1,.5,1,.5,1,1,1,1,2,2,0,1,2,1,1,1],
[.5,2,.5,.5,2,1,1,1,2,.5,2,2,1,1,1,1,1,1],
[1,.5,2,1,.5,2,1,1,1,2,1,.5,1,1,1,1,1,1],
[0,0,1,.5,1,1,.5,2,1,1,1,1,1,1,1,1,2,1],
[.5,2,.5,0,2,.5,.5,1,.5,2,1,.5,1,.5,.5,.5,1,.5],
[1,1,1,1,2,2,.5,1,.5,.5,2,.5,1,1,.5,1,1,.5],
[1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,1],
[1,1,2,2,.5,1,2,1,1,2,.5,.5,.5,1,2,1,1,1],
[1,1,.5,1,2,1,1,1,.5,1,1,1,.5,1,1,1,1,1],
[1,.5,1,1,1,1,2,2,1,1,1,1,1,.5,1,1,2,1],
[1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,1],
[1,1,1,1,1,1,1,1,1,.5,.5,.5,.5,1,2,2,1,2],
[1,2,1,1,1,1,2,.5,1,1,1,1,1,0,1,1,.5,2],
[1,.5,1,2,1,1,.5,1,2,1,1,1,1,1,1,0,.5,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


def weakness(index, name, type1, type2):
    print()

    print(index, ":",name)
    print(type1, type2)
    print()

    #weakness 1
    for i in range(17):
        final_weakness = type_weakness[typing[type1]][i] * type_weakness[typing[type2]][i]
        print(typing_back[i], ":", final_weakness)


def main():

    pokeData = open("PokeData.txt")

    data= [[0]*3]*906

    for i in pokeData:
        #print(i[0])
        temp = i.split(" ")
        #print(int(temp[0]))

        temp[3] = temp[3].strip()

        data[int(temp[0])] = temp[1],temp[2],temp[3]

        #print(data[int(temp[0])])

        #data[int(temp[0])][0] = temp[1]
        #print(data[int(i[0])][0])

        #data[int(temp[0])][1] = temp[2]
        #print(data[int(i[0])][1])

        #data[int(temp[0])][2] = temp[3]
        #print(data[int(i[0])][2])


    while(1):

        print()
        print("Please enter the index of the pokemon you want to see type weakness of")
        x = input("Enter here: ")


        index = 0
        for i in data:
            #print(x, index)
            if int(x) == index:
                weakness(index, i[0], i[1], i[2])
            index += 1


main()

