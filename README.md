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

git clone https://github.com/TsugawaNaoki0/zero_wiki.git

chmod 777 zero_wiki/data/*

cd zero_wiki

while true; do python3 zeroWiki.py; sleep 60s; done
