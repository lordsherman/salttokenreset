Rekey Salt Minion:
  file.absent:
    - name: {{ salt['confi.get']('pki_dir') }}

Restart Salt Minion:
  cmd.run:
    - name: 'salt-call service.restart salt-minion'
    - bg: True
    - order: last
