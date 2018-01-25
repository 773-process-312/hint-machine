# ICMP Hinter

This is a simple tool initially created to send periodically CTF hints through ICMP broadcasted messages.

![](https://i.imgur.com/W3wyHTH.jpg)

## Usage

### hints.csv
The tool loads the hints from a CSV file, according ot the following format :

```
17:30:25-25/01/18";"Chall name";"Hint description"
...
```

And that's basically everything you need to know !


### hint-machine

The hint-machine can be used as follow :

```
machine = HintMachine()
machine.importFromCsv('hints-examples.csv')
machine.showHints()
machine.start(duration=-1, releaseFreq=60)
```



## Documentation

### HintMachine

Create the hintmachine object \o/

| argument | description |
| --- | --- |
| broadcast | Specify the broadcast destination IP address to use to send ICMP packets |
| icmpType | Specify which type of ICMP packets to use  |


#### hintmachine.importFromCsv()

Import hints from a CSV file

| argument | description |
| --- | --- |
| filename | Specify the CSV file containing the hints list  |

#### hintmachine.start()

Start the machine once all hints has been loaded.

| argument | description |
| --- | --- |
| duration | Specify for how long (in seconds) the Hint-machine will keep running  |
| releaseFreq | Specify the frequency of hints releasing |
