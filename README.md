# GriNwaLetTGbOt

Install python3.7 
debian: 
(https://linuxize.com/post/how-to-install-python-3-7-on-debian-9/)
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar -xf Python-3.7.3.tar.xz
cd Python-3.7.3
./configure --enable-optimizations
make -j 8
sudo make altinstall
python3.7 --version
UBUNTU:
(https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
python3.7 --version
>>> Python 3.7.5

Install  pip

sudo apt install python3-pip

Check
pip3 --version
>>> pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)

After this install - Install the package for Telegram.
python3.7 -m pip install aiogram
python3.7 -m pip install asyncio
python3.7 -m pip install requests


After all installation move the bot.py file to grin/grin-wallet and picture grin.png 
Open file bot.py  and change:

TOKEN = "1056341881:AAEKYEkс-QVtKIмtzSgIFL06ahUIOnkPemo"   
 > Here is the bot token that you receive from botFather
password = 'Zalupa9563'                                    
 > Here is the password for the grin-wallet
admin_id = [771844687, 730668]                            
 > Here is your telegram ID from @get_id_bot
grin_pass_api = 'zijvVcc6GH5BYgznbR6K'                     
 > Enter the contents of the file here /root/.grin/main/.api_secret


After that we save the changed script on the server 


Start ssh.
sudo apt install screen
 
screen -S tg_bot
cd
cd grin/grin-wallet
python3.7 bot.py


If everything is fine you will see the inscription "starting"

Press CTRL + A + D and in this way we exit screen

To restart the bot you need to go into the screen -x tg_bot
ctrl+c
python3.7 bot.py 
CTRL+A+D

# GRIN1LOVE 

