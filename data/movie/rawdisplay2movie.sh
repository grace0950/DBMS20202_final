#!/bin/bash

# parameters
TXT=$1
TMP=$1.tmp
CSV=$2

# detect parameters
if [ -z "$2" ]; then
    echo "Usage: ./rawdisplay2csv.sh [/path/to/file.txt] [/path/to/csv]"
    echo ".csv will be generated based on .txt"
    exit
fi

# example
#
#   title = 國賓電影網站入口 - 國賓影城 - 國賓大戲院 - 電影 - 現正熱映 - 1/2的魔法
#   date = 05/23
#   theater = 國賓大戲院
#   time = 11:10
#   ting = 2廳 116席
# ->
#   1/2的魔法, 國賓大戲院, 台北市成都路88號

# generate a temp txt
cp $TXT $TMP

# remove unnessary data
`sed -i 's/國賓電影網站入口 - 國賓影城 - 國賓大戲院 - 電影 - 現正熱映 - //g' $TMP`
`sed -i '/---/ d' $TMP`
`sed -i '/ting = / d' $TMP`

# title/theater/ting
`sed -i '1 s/title = //g' $TMP`
`sed -i '/date/ d' $TMP`
`sed -i 's/theater = /,/g' $TMP`
`sed -i '/time/ d' $TMP`

# remove newline
`sed -i -e ':a' -e 'N' -e '$!ba' -e 's/\n//g' $TMP`

# fix
`sed -i 's/title = /\'$'\n/g' $TMP`
`sed -i 's/\s//g' $TMP`

# add location after theater(fixed theater-location pair)
`sed -i 's/國賓大戲院/&,台北市成都路88號/g' $TMP`
`sed -i 's/國賓影城@中和環球購物中心/&,新北市中和區中山路三段122號4樓/g' $TMP`
`sed -i 's/國賓影城@台北長春廣場/&,台北市中山區長春路176號/g' $TMP`
`sed -i 's/國賓影城@台北微風廣場/&,台北市復興南路一段39號7樓/g' $TMP`
`sed -i 's/國賓影城@林口昕境廣場/&,新北市林口區文化三路一段402巷2號4F/g' $TMP`
`sed -i 's/國賓影城@淡水禮萊廣場/&,新北市淡水區中正路一段2號/g' $TMP`
`sed -i 's/國賓影城@新莊晶冠廣場/&,新北市新莊區五工路66號3樓/g' $TMP`
`sed -i 's/國賓影城@八德廣豐新天地/&,桃園市八德區介壽路一段728號/g' $TMP`
`sed -i 's/國賓影城@台南國賓廣場/&,台南市中華東路一段66號/g' $TMP`
`sed -i 's/國賓影城@高雄大魯閣草衙道/&,高雄市前鎮區中山四路100號3樓/g' $TMP`
`sed -i 's/國賓影城@高雄義大世界/&,高雄市大樹區學城路一段12號3樓/g' $TMP`
`sed -i 's/國賓影城@屏東環球購物中心/&,屏東市仁愛路90號6樓/g' $TMP`
`sed -i 's/國賓影城@金門昇恆昌金湖廣場/&,金門縣金湖鎮太湖路二段198號6樓/g' $TMP`

# generate csv file and add attribute name to first line
`touch $CSV`
`echo "title,theater,location" > $CSV`

# sort and remove duplicates
sort $TMP | uniq >> $CSV

rm $TMP
