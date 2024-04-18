docker run -it \
    --name electrum-wine-builder-cont \
    -v /home/c4pt000/opt/ELECTRUM-URANIUMX-04-13-2024/electrum-bitnet:/opt/wine64/drive_c/electrum \
    --rm \
    --workdir /opt/wine64/drive_c/electrum/contrib/build-wine \
    electrum-wine-builder-img bash \
