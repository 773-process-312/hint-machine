#!/usr/bin/env python3
from scapy.all import IP, ICMP, send
import csv
from sys import exit
from datetime import datetime, timedelta
import time

TIME_FORMAT="%H:%M:%S-%d/%m/%y"
FIELDNAMES = ['release-time', 'chall', 'hint']


class HintMachine():
    def __init__(self, broadcast='255.255.255.255', icmpType=8):
        assert(type(icmpType) is type(int()))

        self.l2 = IP(dst=broadcast)
        self.l3 = ICMP(type=icmpType)

        self.hints = []
        self.message=b""
    
    def showHints(self):
        print('Loaded %d hints:' % len(self.hints))
        for hint in self.hints:
            for field in hint:
                print(field['release-time'],' - ' ,field['chall'], ' - ',field['hint'])

    def broadcastHints(self):
        self.l3.payload = self.message
        pkt = self.l2/self.l3
        send(pkt,verbose=False)
    
    def importFromCsv(self, filename):
        with open(filename, 'r') as f:
            reader = csv.DictReader(f, delimiter=';', quotechar='"',fieldnames=FIELDNAMES)
            for row in reader:
                self.hints.append([row])

            print("Successfully loaded hints from %s." % filename)


    def start(self, duration=0, releaseFreq=10):
        '''
        Start the Hint machine.
        Once the machine has loaded the csv file containing all the hints with release time, this function will automatically send new hints when needed !
        The machine will keep running during X seconds according to the specified "duration"
        '''
        assert(type(duration) is type(int()))
        assert(type(releaseFreq) is type(int()))

        print("-"*10)
        print("Starting the hint-machine for %d seconds !" % duration)
        print("-"*10)

        duration = timedelta(duration)

        start = datetime.now()

        while True:
            now = datetime.now()
            print(now)
            for hint in self.hints:
                for field in hint :
                    moment = datetime.strptime(field['release-time'], TIME_FORMAT)
                    if now >= moment:
                        print('Broadcasting hint %s for chall %s' % (field['hint'], field['chall']))
                        self.message += b"Chall '%s' : %s\n" % (field['chall'].encode(), field['hint'].encode())

            try:
                self.broadcastHints()
            except:
                print("Unable to broadcast hints. Abort.")
                exit()

            x = now - start
            if x > duration and duration != timedelta(-1):
                print("Duration reached. Stopping the hint-machine...")
                break
            else:
                time.sleep(releaseFreq)
                print("-"*5)
                self.message = b""


if __name__ == '__main__':
    
    machine = HintMachine()
    machine.importFromCsv('hints-examples.csv')
    machine.showHints()
    machine.start(duration=0, releaseFreq=60)
    #machine.addHint(myhint)
    #machine.broadcastHints()




