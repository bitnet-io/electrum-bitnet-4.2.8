docker run -it --net host \
    --name electrum-wine-builder-cont \
    -v $PWD:/opt/wine64/drive_c/electrum \
    --rm \
    --workdir /opt/wine64/drive_c/electrum/contrib/build-wine \
    electrum-wine-builder-img bash \
