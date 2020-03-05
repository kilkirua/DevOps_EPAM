#!/bin/bash

function main()  {
if [[ -n $1 ]] ; then
	echo "Параметр не пустой"
   if [[ -e $1 ]] then
	echo "Файл или каталог сущесвует"
        else
        echo "Ошибка!"
        exit 1
   fi
fi

template = $1
result = $2

if [[ -z "$template" ]]; then
	echo "Не указан параметр --template"
	exit 2
elif [[ -z "$result" ]]; then
	echo "Не указан параметр --result"
	exit 2
fi

regex='\{\%[[:space:]]*([0-9A-Za-z_\-]+)[[:space:]]*\%\}*'

cat $template | while read new_line; do
    while [[ "$new_line" =~ $regex ]]; do
        var1="${BASH_REMATCH[1]}"
	var2="${BASH_REMATCH[0]}"
        new_line=${new_line//${var2}/${!var1}}
    done
    echo $new_line >> "$result"
done
}
