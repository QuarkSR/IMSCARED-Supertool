import time
import urllib2
import os
from pathlib import Path
zipFile="https://uploads-from-an-external-server.weebly.com/uploads/1/1/6/2/116274509/imscared.zip"
sevenzaLink="https://uploads-from-an-external-server.weebly.com/uploads/1/1/6/2/116274509/7za.exe"
def download(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        #print status,
    f.close()
print"=====IMSCARED (2016) Supertool=====\n\nWritten by Parzival Wolfram in Python 2\n\nI wish people still put their heart and soul into their programs...\nI miss the DOS days. And I wasn't even alive yet at that time!"
time.sleep(3.5)
print"\n\nAlright, enough dicking around! Let's get to it!\n\n"
restartFlag = False
global restartFlag
def begin():
    if restartFlag:
        ""
    else:
        userInput=""
    print"Enter a number corresponding to an option below:\n\n1 - Download and extract the filled \"imscared\" folder. Will extract with a downloaded tool. \n(Recommend dropping this program on the desktop first!)\n2 - Time-set script! Use this to automatically set the time to the Lucky Ticket times automatically!\n3 - Reset your progress (for set up of a new run)\n4 - Patch the revolver! INFINITE AMMO!\n\n0 - Exit"
    userInput=int(raw_input("Input>"))
    if userInput == 0:
        exit()
    elif userInput == 1:
        print"\n\n\nAlright, here goes!\n\nDownloading folder...\n"
        download(zipFile)
        print"\n\nDownloading 7-Zip temporary utility...\n"
        download(sevenzaLink)
        print"\n\nExtracting...\n"
        os.system("7za x imscared.zip")
        print"Did it work? Checking..."
        try:
            my_file = Path(str(os.getcwd())+"\\imscared\\revolver.ini")
            my_abs_path = my_file.resolve()
        except FileNotFoundError:
            print"No. No it didn't. Cleaning up, then bailing..."
            os.system("del imscared.zip /f")
            os.system("del 7za.exe /f")
            time.sleep(5)
            exit()
        else:
            print"Yes. Yes it did."
            print"Cleaning up..."
            os.system("del imscared.zip /f")
            os.system("del 7za.exe /f")
            print"Alright, looping back to the start of the program! (mainly because I've coded this very lazily...)"
            restart()
    elif userInput == 2:
        print"Alright, let's do it! Setting clock to first ticket's time..."
        os.system("time 7:45:00 AM")
        print"Set! Next ticket time will be set in 5 seconds..."
        time.sleep(5)
        print"Setting to second ticket time..."
        os.system("time 8:23:00 PM")
        print"Set! Next ticket time will be set in 5 seconds..."
        time.sleep(5)
        print"Setting to metro ticket time..."
        os.system("time 12:00:00 AM")
        print"Set! Time will be restored from the Internet in 5 seconds..."
        time.sleep(5)
        from urllib2 import urlopen
        res = urlopen('http://just-the-time.appspot.com/')
        time_str = res.read().strip()
        os.system("time " + str(time_str[11:]))
        print"Time restored! If it isn't actually fixed, you can manually reset it, I guess."
        print"Alright, looping back to the start of the program! (mainly because I've coded this very lazily...)"
        restart()
    elif userInput == 3:
        print"Alright, let's do it! Erasing saved data..."
        batchOut=open("temp.bat","w")
        batchOut.write("@echo off\ncd %%APPDATA%%\\IMSCARED\ntaskkill /im imscared.exe /f\ndel white.ini /f\ndel workshop.ini /f\n\n\nexit")
        batchOut.flush()
        batchOut.close()
        os.system("call temp.bat")
        os.system("del temp.bat /f")
        print"Erased!"
        print"Alright, looping back to the start of the program! (mainly because I've coded this very lazily...)"
        restart()
    elif userInput == 4:
        print"Alright, let's do it! Patching..."
        axfilOut=open("temp.axfil","w")
        axfilOut.write("[revolver]\nbullets=\"6.000000\"")
        axfilOut.flush()
        axfilOut.close()
        batchOut=open("temp.bat","w")
        batchOut.write("@echo off\ntaskkill /im IMSCARED.exe /f\ndel %%APPDATA%%\\IMSCARED\\revolver.ini /f\ncopy temp.axfil %%APPDATA%%\\IMSCARED\\revolver.ini\nattrib %%APPDATA%%\\IMSCARED\\revolver.ini +r\ndel temp.axfil\ndel temp.bat")
        batchOut.flush()
        batchOut.close()
        os.system("call temp.bat")
        print"Patched!"
        print"Alright, looping back to the start of the program! (mainly because I've coded this very lazily...)"
        restart()
    else:
        begin()
    begin()
def restart():
    print"Restarting, please wait..."
    time.sleep(10)
    print"\n\n"
    time.sleep(0.01)
    restartFlag=True
    begin()
begin()
