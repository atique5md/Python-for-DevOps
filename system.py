import os

# print(os.system('wmic logicaldisk get size'))

def checkram(command):
    print(os.system(command))

cmd = 'systeminfo | find "system Boot Time"'

checkram(cmd)
