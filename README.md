# 07-01-2024 improvements to the QR code

![s1](https://github.com/c4pt000/a-PROTECTED_QR_CODE-QR-code-Encryption-layer-for-QR-codes-in-plainsight-and-machine-vision-and-crypt/releases/download/gif/new-QR-electrum-bitnet-4.2.8.gif)


# how to restore kivy framework revert to -> python3.8
# with python3.8 installed
```
 wget https://bootstrap.pypa.io/get-pip.py
 python3.8 get-pip.py 
 python3.8 -m pip install kivy==2.0.0rc2
 python3.8 -m pip install .
 python3.8 -m pip install cryptography
 python3.8 -m pip install aiorpcx==0.18.7 cryptography requests PyQt5 protobuf==3.20.0
 python3.8 run_electrum -g kivy
```

# requires older python3 aiorpcx == 0.18.7 and libsecp256k1.so.0 or wont work
```
git clone https://github.com/bitnet-io/electrum-bitnet-4.2.8
cd electrum-bitnet-4.2.8
python3 -m pip install .
python3 -m pip install aiorpcx==0.18.7 cryptography requests PyQt5 protobuf==3.20.0

./contrib/make_libsecp256k1.sh
python3 run_electrum
```

# build for windows setup.exe, portable.exe (wine builder) requires docker
```
git clone https://github.com/bitnet-io/electrum-bitnet-4.2.8
cd electrum-bitnet-4.2.8

cd contrib/build-wine
docker build -t electrum-wine-builder-img .
cd ../../
./contrib/build-wine/build-binary.sh
cd /opt/wine64/drive_c/electrum
./make_win.sh
```

# Linux AppImage (requires docker)
```

git clone https://github.com/bitnet-io/electrum-bitnet-4.2.8
cd electrum-bitnet-4.2.8

cd contrib/build-linux-appimage
docker build -t electrum-appimage-builder-img .
cd ../../../
./contrib/build-linux/appimage/build-binary.sh

./make_appimage.sh 
```

# building for android (requires docker + java11 + nodejs + apksigner to sign the debug.apk)

```
git clone https://github.com/bitnet-io/electrum-bitnet-4.2.8
cd electrum-bitnet-4.2.8

sh android-builder-docker.sh

enter the docker guest

┌─[root@nwstrtrj01 04-18-2024-17:24:30] ]─[/home/c4pt000/opt/ELECTRUM-URANIUMX-04-13-2024/electrum-bitnet-4.1.5]
└──╼ # sh android-builder-docker.sh 
eb6180cefd0a6f14756557e7f8cd2dfd7b3f80eb905e266a5f614dec178feffb

docker exec -it eb6 bash

hit crtl-C a few times to stop .bashrc scripts from running

run make_apk then hit "Y" for Yes

./contrib/android/make_apk

should build the apk into dist/

exit

cp -rf dist/Bitnet-4.2.8.0-arm64-v8a-debug.apk .

in order to "sign" the apk with a cert you need apksigner from android build-tools installed with your host

/Android/Sdk/build-tools/34.0.0/apksigner

adjust this script to your path to apksigner create-keystore-and-sign.sh

then run the script to sign the debug .apk

sh create-keystore-and-sign.sh

script will output a signed apk

Bitnet-4.2.8.0-arm64-v8a-signed.apk

```






# macOS python3.10 , xcode command line tools)

```
git clone https://github.com/bitnet-io/electrum-bitnet-4.2.8
cd electrum-bitnet-4.2.8

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
macos dmg builder (requires intel macOS (arm64 hybrid fails...suggest BigSur)


# running this in terminal directly with ncurses graphics instead of QT or Kivy

```./run_electrum -g text```
```./Electrum-AppImage_x86_64 -g text```

![s1](https://github.com/bitnet-io/electrum-bitnet-4.2.8/releases/download/4.2.8/run_electrum-g-text.gif)
