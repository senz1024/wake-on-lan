import telnetlib

ROUTER='192.168.1.1'
USERPASS=open('userpass').readline().strip()
ROOTPASS=open('rootpass').readline().strip()
MAC=open('mac').readline().strip()

tn = telnetlib.Telnet(ROUTER)

print('login...')
tn.read_until('Password: ')
tn.write(USERPASS+'\n')
tn.read_until('>')
print('login success')
tn.write('administrator'+'\n')
tn.read_until('Password: ')
tn.write(ROOTPASS+'\n')
tn.read_until('# ')
print('root success')
tn.write('wol send lan1 '+MAC+'\n')
print('wake on lan!')

