#!/bin/bash
docker run -it \
    --name electrum-appimage-builder-cont2 \
    -v /home/c4pt000/opt/ELECTRUM-URANIUMX-04-13-2024/electrum-uraniumx:/opt/electrum \
    --rm \
    --workdir /opt/electrum/contrib/build-linux/appimage \
    electrum-appimage-buster bash \
    ./make_appimage.sh

