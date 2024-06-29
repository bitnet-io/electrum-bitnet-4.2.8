#apt update > /dev/null && apt install --yes --no-install-recommends \
#    ca-certificates

apt-get update 
# pin the distro packages
#cp -rf apt.sources.list /etc/apt/sources.list
#cp -rf apt.preferences /etc/apt/preferences.d/snapshot

apt-get update && \
    apt-get install -y  \
	ca-certificates \
        sudo \
        git \
        wget \
        make \
	python3 \
        autotools-dev \
        autoconf \
        libtool \
        autopoint \
        pkg-config \
        xz-utils \
        libssl-dev \
        libssl1.1 \
        openssl \
        zlib1g-dev \
        libffi-dev \
        libncurses5-dev \
        libncurses5 \
        libtinfo-dev \
        libtinfo5 \
        libsqlite3-dev \
        libusb-1.0-0-dev \
        libudev-dev \
        libudev1 \
        gettext \
        libdbus-1-3 \
        xutils-dev \
        libxkbcommon0 \
        libxkbcommon-x11-0 \
        libxcb1-dev \
        libxcb-xinerama0 \
        libxcb-randr0 \
        libxcb-render0 \
        libxcb-shm0 \
        libxcb-shape0 \
        libxcb-sync1 \
        libxcb-xfixes0 \
        libxcb-xkb1 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-util0-dev \
        libxcb-render-util0 \
        libx11-xcb1 \
        libc6-dev \
        libc6 \
        libc-dev-bin \
        libv4l-dev \
        libjpeg62-turbo-dev \
        libx11-dev \
        && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean

        #libxcb-util1 \
