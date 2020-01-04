import os
import subprocess

ad = input("Kapatılması istenen program :")

cmd = "tasklist /v /fo csv | findstr /i \"{}\"".format(ad)

ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

output = ps.communicate()[0]
print(output)



ouTput = str(output)

say = 0
yaz=""
for i in ouTput:
    if(i=="\""):
        say+=1
    if(say<4 and say>2):
        yaz += i
    if(say==4):
        break
cikti = ""
for i in yaz:
    try:
        if(int(i)!=str):
            cikti += i
    except:
        pass

PID = cikti

os.system("TASKKILL /PID {} ".format(cikti))