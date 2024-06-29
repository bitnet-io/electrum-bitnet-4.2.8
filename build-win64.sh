sleep 2s
echo './contrib/build-wine/make_win.sh'
docker pull c4pt/electrum-wine-builder-img
docker run -it --net host \
    --name electrum-wine-builder-cont \
    -v $PWD:/opt/wine64/drive_c/electrum \
    --rm \
    --workdir /opt/wine64/drive_c/electrum/contrib/build-wine \
    c4pt/electrum-wine-builder-img bash \
