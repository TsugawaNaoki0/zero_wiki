sudo apt update

sudo apt upgrade

apt install python3-pip

pip3 install beautifulsoup4

apt-get install apache2



-------------------------------------------------------


cd /var/www

rm -rf html

mkdir html

cd html

cd zero_wiki

git clone https://github.com/TsugawaNaoki0/zero_wiki.git

chmod 777 zero_wiki/data/*

while true; do python3 zero_wiki/zeroWiki.py; sleep 60s; done
