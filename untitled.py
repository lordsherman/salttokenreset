import salt.config
import salt.loader
import salt.runner
import salt.client
import os
import time
import subprocess
import sys

opts = salt.config.master_config('/etc/salt/master')
local = salt.client.LocalClient()

#cmd_async will return a Job ID that we can then use to check if it completed succesfully.
#Without this the script will error and time out if any minions dont respond.
pingJID = local.cmd_async('*', 'test.ping')

#Returns a dictionary list of all minions and if they respond to ping or not.
runner = salt.runner.RunnerClient(opts)
pinglist = runner.cmd('jobs.exit_success',[pingJID])

#Checking if all minions responded or not.  Exits script if not all respond.
res = True
for i in pinglist:
	if not pinglist[i]:
		res = False
		break

if res == False:
	print('Not All Minions Responded... Aborting Script')
	sys.exit(1)
else:
	print('All Minions Responded... Proceeding')

#Generate list of cached minions to accept individually.
#This is important to ensure we are not accepting any unwanted minions.
#One possible issue is the time it may take to individually accept all 3k~ minions.

cachedMinionsDirectory = '/var/cache/salt/master/minions'
cachedMinionList = os.listdir(cachedMinionsDirectory)

#Send command to minions to rekey.  Runs Rekey-minion.sh
print('Sending Rekey State to Minions')
local.cmd('*', 'state.sls', ['rekey-minions'])
time.sleep(60)

#Rekey Salt-Master
print('Rekeying Salt Master')
PKI_DIR = '/etc/salt/pki/master'
subprocess.run(['rm', '-rf', PKI_DIR])
subprocess.run(['systemctl', 'restart', 'salt-master'])
time.sleep(5)

#Have Script Sleep for 2 minutes to give Minions time to send auth requests
print('Pausing to give time for minion key exchange')
time.sleep(120)
print('Time to Accept these Minions')
#Accept each cached minions key from our cached list

for i in range(len(cachedMinionList)):
	subprocess.run(['salt-key', '-a', cachedMinionList[i], '-y'])
print('Did this work?')

#Might need to restart salt-minions after key acceptance due to weird failure issues

#Run cleanup state on minions
