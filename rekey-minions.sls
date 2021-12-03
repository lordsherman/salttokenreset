script:
  cmd.script:
    - name: salt://rekey-minion.sh
    - env:
       - PKI_DIR: {{ salt['config.get']('pki_dir') }}
