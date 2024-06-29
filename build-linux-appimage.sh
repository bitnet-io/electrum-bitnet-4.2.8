sleep 5s
echo './make_appimage.sh'

docker pull c4pt/bullseye-appimage-builder
./contrib/build-linux/appimage/build-binary.sh
