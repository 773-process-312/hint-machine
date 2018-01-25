# ICMP Hinter

This is a simple tool initially created to send periodically CTF hints through ICMP broadcasted messages.

## Usage 


### hints.csv
The tool loads the hints from a CSV file, according ot the following format :
''''
17:30:25-25/01/18";"Chall name";"Hint description"
...
''''

And that's basically everything you need to know !


### hint-machine

The hint-machine can be used as follow :
''''
machine = HintMachine()
machine.importFromCsv('hints-examples.csv')
machine.showHints()
machine.start(duration=-1, releaseFreq=60)
''''




