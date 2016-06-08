#-*-coding=utf-8-*-
import subprocess
import time
import re
def nvflash():
    wait_device_cmd=['adb','wait-for-device']

    result=subprocess.Popen(wait_device_cmd,stdout=subprocess.PIPE)
    result.wait()


    forced_recovery_cmd=['adb','reboot','forced-recovery']
    result=subprocess.Popen(forced_recovery_cmd,stdout=subprocess.PIPE)
    result.wait()

    print "Going to flash"


    cmd=['./shell_script.sh']
    result=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    result.wait()
    print result.stdout.read()

    result=subprocess.Popen(wait_device_cmd,stdout=subprocess.PIPE)
    result.wait()

    dmesg_cmd=['adb','shell','dmesg']
    result=subprocess.Popen(dmesg_cmd,stdout=subprocess.PIPE)
    result.wait()
    dmesg_string=result.stdout.read()
    if re.search(r'nvhdcp: link integrity check passed',dmesg_cmd):
        print "Passed"
        return True
    else:
        print "Failed"
        return False


def main():
    pass_count=0
    total_count=50
    for i in range(total_count):
        time.sleep(5)
        print "*"*20
        if nvflash():
            pass_count=pass_count+1

        print "Pass count %d/%d" %(pass_count,total_count)

