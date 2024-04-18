# build for windows setup.exe, portable.exe (wine builder) requires docker

```
cd contrib/build-wine
docker build -t electrum-wine-builder-img .
./build-binary.sh

enter the docker guest

cd /opt/wine64/drive_c/electrum
./make_win.sh

```

# macOS python3.10 , xcode command line tools)

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
# macos dmg builder (requires intel macOS (arm64 hybrid fails...suggest BigSur)
