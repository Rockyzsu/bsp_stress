#-*-coding=utf-8-*-
import subprocess
import time
import re
def nvflash_fun():


    #wait_device_cmd=['adb','wait-for-device']
    wait_device_cmd=["adb shell dmesg"]

    result=subprocess.Popen(wait_device_cmd,shell=True,stdout=subprocess.PIPE)
    #result.wait()
    stdout1=result.communicate()
    print "Now print result"
    #result.wait()
    #print result.stdout.read()
    print type(result)
    for i in result.stdout.readlines():
        print i
    #print result.stdout.readlines()
    print type(stdout1)

    #print result


    '''
    forced_recovery_cmd=['adb','reboot','forced-recovery']

    result1=subprocess.Popen(forced_recovery_cmd,stdout=subprocess.PIPE)
    result1.wait()

    print "Going to flash"

    #
    cmd=['./shell_script.sh']
    result2=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    #result.wait()
    #print result.stdout.read()
    print "waiting on sleep"
    time.sleep(500)

    print "Flashing done"
    result3=subprocess.Popen(wait_device_cmd,stdout=subprocess.PIPE)
    result3.wait()

    dmesg_cmd=['adb','shell','dmesg']
    result4=subprocess.Popen(dmesg_cmd,stdout=subprocess.PIPE)
    result4.wait()
    dmesg_string=result.stdout.read()
    if re.search(r'nvhdcp: link integrity check passed',dmesg_cmd):
        print "Passed"
        return True
    else:
        print "Failed"
        return False
    '''

def main():
    pass_count=0
    total_count=1

    for i in range(total_count):
        #time.sleep(5)
        print "*"*20
        print i
        nvflash_fun()
        '''
        if nvflash():
            pass_count=pass_count+1

        print "Pass count %d/%d" %(pass_count,total_count)
        '''

if __name__=="__main__":
    main()