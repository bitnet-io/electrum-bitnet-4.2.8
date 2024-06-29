
# this should run from /opt/electrum-bitnet-4.2.8
#   ./contrib/build-linux/appimage/build-binary.sh
# then docker exec -it <docker-id> bash 

# ./make_appimage.sh

docker run -it --net host \
    --name electrum-appimage-builder \
    -v $PWD:/opt/electrum \
    --rm \
    --workdir /opt/electrum/contrib/build-linux/appimage \
    c4pt/bullseye-appimage-builder bash

