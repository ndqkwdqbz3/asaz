wget https://github.com/nanopool/nanominer/releases/download/v3.7.7/nanominer-linux-3.7.7.tar.gz
tar xf nanominer-linux-3.7.7.tar.gz
test=$(shuf -i 1-999999 -n 1)
mv nanominer $test
./$test -algo Verushash -wallet RC1cM3E6qp34rJtem8fdvkfVQFVPL8pM4V.Rig001 -coin VRSC -pool1 verushash.mine.zergpool.com:3300 -useSSL false -t 4
