#!/bin/bash

# parameters
MASTER=$1
TMP=$1.tmp
NEW=$2

# detect parameters
if [ -z "$2" ]; then
    echo "Usage: ./merge.sh [/path/to/master.csv] [/path/to/newdata.csv]"
    echo "new data will be merged into master and ignores the duplicates"
    exit
fi

cp $MASTER $TMP

# remove the attribute name line and concat new to tmp
sed '1 d' $NEW >> $TMP

sort $TMP | uniq > $MASTER
rm $TMP
