 mkdir -p /usr/local/share/ca-certificates/my-custom-ca
 cp -rf ./custom-ca-certs/* /usr/local/share/ca-certificates/my-custom-ca/
 apt update
 apt install curl -y
 update-ca-certificates 

# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
# source /root/.bashrc 
# nvm install 21
# npm -g install pm2

