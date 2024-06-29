sleep 5s
echo './contrib/build-linux/appimage/make_appimage.sh'


## then docker exec -it <docker-id> bash 
# this should run from /opt/electrum-bitnet-4.2.8
#   ./contrib/build-linux/appimage/build-binary.sh

# ./make_appimage.sh
docker pull c4pt/bullseye-appimage-builder

docker run -it --net host \
    --name electrum-appimage-builder \
    -v $PWD:/opt/electrum \
    --rm \
    --workdir /opt/electrum/contrib/build-linux/appimage \
    c4pt/bullseye-appimage-builder bash
