Rekey Salt Minion:
  cmd.script:
    - name: salt://rekey.sh
    - env:
      - PKI_DIR: {{ salt['config.get']('pki_dir') }}
