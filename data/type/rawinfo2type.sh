#!/bin/bash

# parameters
INF=$1
TMP=$1.tmp
TYP=$2

# detect parameters
if [ -z "$2" ]; then
    echo "Usage: ./rawinfo2type.sh [/path/to/file.txt] [/path/to/file.csv]"
    echo "type.csv will be generated by info.txt"
    exit
fi

# example
#
#   title = 蝙蝠俠：開戰時刻
#   EN_title = BATMAN BEGINS
#   intro = 克里斯多夫諾蘭  經典作品 ...
#   主要演員：克里斯多福諾蘭,克里斯汀貝爾,米高肯恩,蓋瑞歐德曼,凱蒂荷姆絲,摩根費里曼,連恩尼遜
#   影片類型：動作
# ->
#   蝙蝠俠：開戰時刻,動作

# generate a temp txt
cp $INF $TMP

# remove unnessarys
`sed -i '/EN_title/ d' $TMP`
`sed -i '/intro/ d' $TMP`
`sed -i '/主要演員/ d' $TMP`
`sed -i '/---/ d' $TMP`
`sed -i 's/\.//g' $TMP`

# fix
`sed -i '1 s/title = //' $TMP`
`sed -i -e ':a' -e 'N' -e '$!ba' -e 's/\n//g' $TMP`
`sed -i 's/title = /\'$'\n/g' $TMP`
`sed -i 's/影片類型：/,/g' $TMP`

# generate csv file and add attribute name to first line
`touch $TYP`
`echo "name,type" > $TYP`
`sort $TMP | uniq >> $TYP`
rm $TMP
