COFFEEMACHINE_IP=192.168.255.10
docker-machine create --driver generic --generic-ip-address $COFFEEMACHINE_IP  --generic-ssh-user coffeemachine coffeemachine
