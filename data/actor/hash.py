import hashlib
import codecs
import sys
import os

# change stdout to utf-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# get current directory
f = open(os.getcwd()+"/data/actor/names.txt", encoding="utf-8")
#f = open("names.txt", encoding="utf-8")

for line in f:
    hashid = int(hashlib.md5(line.encode('utf-8')).hexdigest(), 16)
    sex = hashid % 2
    if(sex == 0):
        sex = "男"
    elif(sex == 1):
        sex = "女"
    name = line.rstrip("\n")
    print(f"{name},{hashid},{sex}")

f.close()
