rm -r $PKI_DIR
systemctl stop salt-minion
sleep 5
systemctl start salt-minion
sleep 60
