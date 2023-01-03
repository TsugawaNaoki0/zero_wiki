cd /var/www

rm -rf html

mkdir html

cd html

git clone https://github.com/TsugawaNaoki0/zero_wiki.git

mv zero_wiki/* ./

chmod 666 data/quake_data.txt

while true; do python3 quake.py; sleep 3s; done
