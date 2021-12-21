regen_minion_keys:
  module.run:
    - name: saltutil.regen_keys
  cmd.run:
    - name: 'sleep 120; salt-call service.restart salt-minion'
    - bg: True
    - order: last
