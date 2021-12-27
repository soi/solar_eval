#! /bin/bash

for zip_id in *.zip
do
	id=${zip_id%.*}
	unzip -d $id $zip_id
	cat $id/* | cut -d , -f 6 | grep -v Power | egrep -v '(^$|^0$)' > $id/$id.csv
done
