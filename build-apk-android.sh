sleep 2s
echo './contrib/android/make_apk'
echo 'exit back out with exit'
echo 'then apk debug is in dist/'
echo 'cp -rf dist/Bitnet*here*apk .'
echo 'adjust create-keystore to your local apksigner from 29.0.3 or 33.0.1   FROM ANDROID-SDK on local machine command line tools or otherwise or from the docker-android builder in /opt/android/android-sdk'
echo './create-keystore-and-sign.sh'

docker pull c4pt/electrum-android-build-apks

docker run -it -d --net host --rm --user root \
    -v $PWD:/home/user/wspace/electrum \
    -v $PWD/.buildozer/.gradle:/home/user/.gradle \
    --workdir /home/user/wspace/electrum \
    c4pt/electrum-android-build-apks
