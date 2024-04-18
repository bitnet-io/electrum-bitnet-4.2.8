docker run -it --net host \
    --name electrum-appimage-builder-cont \
    -v $PWD:/opt/electrum \
    --rm \
    --workdir /opt/electrum/contrib/build-linux/appimage \
    electrum-appimage-builder-img bash

