import sys

# 26 col
column = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# 20 row
row = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

theaters = []
seat = []
movies = []
all_in_web = []

date = "0627-0704"

with open(date + "csvs/type_data" + date + ".csv", encoding="utf-8") as types:
    data = types.readlines()
    # remove first line
    data = data[1:]
    for line in data:
        line = line.strip()
        features = line.split(",")
        movie = features[0]
        all_in_web.append(movie)
    types.close()

with open(date + "csvs/display_data" + date + ".csv", encoding="utf-8") as display:
    data = display.readlines()
    # remove first line
    data = data[1:]
    for line in data:
        line = line.strip()
        features = line.split(",")
        movie = features[0]
        theater = features[2]
        dated = features[1]
        time = features[4]
        TT = [movie, theater, dated, time]
        if theater not in theaters:
            theaters.append(theater)
        if movie not in movies:
            movies.append(movie)
        if TT not in seat:
            seat.append(TT)
    display.close()


for S in seat:
    for C in column:
        for R in row:
            print(f"{S[0]},{S[1]},{S[2]},{S[3]},{C},{R},0")

for M in all_in_web:
    if M not in movies:
        for T in theaters:
            for C in column:
                for R in row:
                    print(f"{M},{T},NULL,NULL,{C},{R},0")


