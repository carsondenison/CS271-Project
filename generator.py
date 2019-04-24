from idioms import *
from gen_init import *

for cmd in cmds:
	strToFunc[cmd[0]](strToTemplate[cmd[0]], cmd[1], cmd[2])