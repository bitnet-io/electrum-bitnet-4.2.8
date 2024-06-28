rm -rf ps-tx.txt*
 ps ax | grep run_elec > ps-tx.txt
 cat ps-tx.txt | cut -c1-8 > ps-tx.txt2
 sed -i 's/^/kill -9 /g' ps-tx.txt2 
 chmod +x ps-tx.txt2
 ./ps-tx.txt2 
 python3 run_electrum
