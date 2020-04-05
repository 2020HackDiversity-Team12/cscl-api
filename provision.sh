echo 'apt-get updating...'
sudo apt-get update -y

echo 'installing python 3 & pip...'
sudo apt-get install -y python3-pip

echo 'installing git...'
sudo apt-get install -y git

echo 'installing mongodb server...'
sudo apt-get install -y mongodb

echo 'installing pipenv...'
sudo pip3 install pipenv