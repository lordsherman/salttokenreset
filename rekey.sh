rm -r $PKI_DIR
systemctl stop salt-minion
systemctl start salt-minion
sleep 8
salt-call service.restart salt-minion
