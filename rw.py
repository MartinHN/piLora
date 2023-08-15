import os
import subprocess

isPi="armv7" in str(subprocess.check_output(["uname", "-m"]))

def isRW():
    try:
        return os.system("mount | grep 'type ext4' | grep rw") == 0
    except:
        print("can't check rw mode")
    return False

bootedRW = isRW()
    
def setRW(b):
    global bootedRW
    global isPi
    if not isPi:
        print('ignoring rw on non pi platforms')
        return

    if bootedRW:
        print('ignoring as booted in rw')
        return
 
    rwStr="rw" if b else "ro"
    if  os.system(f"sudo mount -o remount,{rwStr} /") != 0:
        print("!!!!!!   could not set RW/RO correctly")


    



