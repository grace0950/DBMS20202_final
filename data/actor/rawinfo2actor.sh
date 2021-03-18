#!/bin/bash

# parameters
INF=$1
TMP=$1.tmp
ACT=$2

# detect parameters
if [ -z "$2" ]; then
    echo "Usage: ./rawinfo2actor.sh [/path/to/file.txt] [/path/to/file.txt]"
    echo ".txt will be generated based on .txt"
    exit
fi

# example
#
#   title = 蝙蝠俠：開戰時刻
#   EN_title = BATMAN BEGINS
#   影片類型：動作
#   url = ????
#   intro = 克里斯多夫諾蘭  經典作品 ...
#   主要演員：克里斯多福諾蘭,克里斯汀貝爾,米高肯恩,蓋瑞歐德曼,凱蒂荷姆絲,摩根費里曼,連恩尼遜
# ->
#   克里斯多福諾蘭
#   克里斯汀貝爾
#   米高肯恩
#   蓋瑞歐德曼
#   凱蒂荷姆絲
#   摩根費里曼
#   連恩尼遜

# generate a temp csv
cp $INF $TMP

# remove unnessarys
`sed -i 's/\s//g' $TMP`
`sed -i '/title/ d' $TMP`
`sed -i '/EN_title/ d' $TMP`
`sed -i '/url/ d' $TMP`
`sed -i '/intro/ d' $TMP`
`sed -i 's/影片類型.*/,/g' $TMP`
`sed -i 's/主要演員：//g' $TMP`
`sed -i '/---/ d' $TMP`
`sed -i 's/\.//g' $TMP`

# fix
`sed -i -e ':a' -e 'N' -e '$!ba' -e 's/\n//g' $TMP`
`sed -i 's/,\+/,/g' $TMP`
`sed -i 's/,/\'$'\n/g' $TMP`
`sed -i '$ d' $TMP`
`sed -i '/^$/ d' $TMP`

# sort and uniq
`sort $TMP | uniq > $ACT`
rm $TMP
