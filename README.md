for ElectrumX uraniumX (BIT) server
https://github.com/c4pt000/ElectrumX-server-UraniumX

# for androi
# https://drive.google.com/file/d/1WByxyLy0Y4ygmjHLlqBtHQubZLyQa1mr/view?usp=sharing


```
cd /usr/bin
wget https://github.com/c4pt000/electrum-bitnet/releases/download/electrum-bitnet/electrum-bitnet.tar.gz
tar -xvf electrum-bitnet.tar.gz
```
![s1](https://raw.githubusercontent.com/c4pt000/electrum-bitnet/main/ascii-art.png)
![s1](https://raw.githubusercontent.com/c4pt000/electrum-bitnet/main/history.png)
![s1](https://raw.githubusercontent.com/c4pt000/electrum-bitnet/main/payto.png)
![s1](https://raw.githubusercontent.com/c4pt000/electrum-bitnet/main/paytoconfirm.png)
![s1](https://raw.githubusercontent.com/c4pt000/electrum-bitnet/main/paytoconfirm-sent.png)


# macOS (requires python3 , xcode command line tools)
```
cd electrum-bitnet
python3 -m pip install --upgrade pip
python3 -m pip install .
python3 -m pip install PyQt5
cd contrib
sh build-macos-automake.sh
sh make_libsecp256k1.sh
cd ..
./run_electrum
```
