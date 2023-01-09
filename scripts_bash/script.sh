#!/bin/bash
# created by Brewal Guyon
# last modification 17-11-22

location='/proc/meminfo'

res=`cat $location | grep -E "^(Mem|Swap)"`

IFS=$'\n'

echo -n `date +'%s'`, >> /root/Documents/sae15/data.csv

for d in $res:
do
   line=$line`echo $d | tr -s ' ' | tr -d ':' |  cut -d ' ' -f 2-3`,
done

echo -n ${line::-1} >> /root/Documents/sae15/data.csv

echo "" >> /root/Documents/sae15/data.csv

# tr -s -> replace multiple -s into one | tr -s -> remove all (: because there is : everywhere

exit 0