Rekey Salt Minion:
  file.absent:
    - name: '/etc/salt/pki/minion'

Restart Salt Minion:
  cmd.run:
    - name: 'salt-call service.restart salt-minion'
    - bg: True
    - order: last
