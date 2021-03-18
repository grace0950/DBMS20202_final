#!/bin/bash
PWD=`pwd`

# remove additional parameter for sed -i (if have)
sed -i '' "s/-i \'\'/-i/g" $PWD/data/actor/rawinfo2actor.sh
sed -i '' "s/-i \'\'/-i/g" $PWD/data/acts/rawinfo2act.sh
sed -i '' "s/-i \'\'/-i/g" $PWD/data/display/display_txt2csv.sh
sed -i '' "s/-i \'\'/-i/g" $PWD/data/movie/rawdisplay2movie.sh
sed -i '' "s/-i \'\'/-i/g" $PWD/data/type/rawinfo2type.sh
sed -i '' "s/-i \'\'/-i/g" $PWD/update_all_data.sh
sed -i '' "s/-i \'\'/-i/g" $PWD/update_no_merge.sh

# add additional parameter for sed -i
sed -i '' "s/-i/& \'\'/g" $PWD/data/actor/rawinfo2actor.sh
sed -i '' "s/-i/& \'\'/g" $PWD/data/acts/rawinfo2act.sh
sed -i '' "s/-i/& \'\'/g" $PWD/data/display/display_txt2csv.sh
sed -i '' "s/-i/& \'\'/g" $PWD/data/movie/rawdisplay2movie.sh
sed -i '' "s/-i/& \'\'/g" $PWD/data/type/rawinfo2type.sh
sed -i '' "s/-i/& \'\'/g" $PWD/update_all_data.sh
sed -i '' "s/-i/& \'\'/g" $PWD/update_no_merge.sh
