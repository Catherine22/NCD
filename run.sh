#!/bin/bash

# python pyncd.py assets/fileClasses/class1.bin assets/g5/1b439405f8628b2fc7c894fda0370552.bin

FILE="result"

getFileName() {
    local args="${@}"
    args=${args##*/}
    echo "${args%.*}"
}

if [[ -f "${FILE}" ]]
then
    rm ${FILE}
fi
touch ${FILE}

for x in $(ls assets/x/*.bin)
do
    for y in $(ls assets/y/*.bin)
    do 
        echo "$(python pyncd.py $x $y >> ${FILE})" >> ${FILE}
    done
done  
echo 'done'
