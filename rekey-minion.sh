rm -r $PKI_DIR
salt-call --local service.restart salt-minion && salt-call --local service.start salt-minion

