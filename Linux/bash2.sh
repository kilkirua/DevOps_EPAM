#!/bin/bash

function cheak() {

if [ -e "$1" ]&&[ -r "$1" ] ; then
  echo "Файл или директория доступны" 
else
  echo "Ошибка доступа!" 
  exit 1
fi
 
}

function main() {

lock_file=~/bash2.lock

if [ -f ${lock_file} ]; then
	echo  "$(date +'%d.%m.%Y %H:%M:%S') : Скрипт уже запущен!" >> $LOGFILENAME
        exit 1
else
        touch ${lock_file}
        for file in "$SOURCEDIR"/*; do
	    name=$(awk 'BEGIN{FS="\t"} NR==1 {print $1}' "$1")
            date=$(awk 'BEGIN{FS="\t"} NR==1 {print $2}' "$1")
	    cur_date=$(date +'%d.%m.%Y %H:%M:%S')
	    UUID=$(awk 'END{if (/^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}/) print $1}' "$1")
		if [ ! -z "$UUID" ];  then
			new_name="${name} ${date} ${cur_date}"
			mv $file $TARGETDIR/$new_name
			echo "$(date +'%d.%m.%Y %H:%M:%S') : файл $file перемещен в $TARGETDIR/$new_name" >> $LOGFILENAME
			rm -rf ${lock_file}
		else
			continue
		fi
        done
fi 
}
