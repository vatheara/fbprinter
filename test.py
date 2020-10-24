import subprocess
import os
cd = os.system('%cd%')
subprocess.call("explorer %cd%" ,shell=True)

