# Token Info

Script for getting token info about Hive-engine tokens, targetted towards the data needs of @cryptosimplify on Hive.

*Please note that this software is in early Beta stage, and that you need to know what you are doing to use it.*

For Ubuntu and Debian install these packages:
```
sudo apt-get install python3-pip build-essential libssl-dev python3-dev python3-setuptools python3-gmpy2
```

### Install Python Packages

Install needed packages by (you may need to replace pip3 by pip):
```
sudo pip3 install -U beem hiveengine pandas
```

Clone the Github repository to your home directory:
```
cd ~
git clone https://github.com/flaxz/tokeninfo
```

Make the bash files executable:
```
cd ~/tokeninfo
chmod u+x getinfo.sh
```

Run the script to get data.

```
cd ~/tokeninfo
./getinfo.sh
```

The data will be printed on screen.

Coders: 
@flaxz on Hive
