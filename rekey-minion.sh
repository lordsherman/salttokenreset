rm -r $PKI_DIR
systemctl stop salt-minion
sleep 15
systemctl start salt-minion
