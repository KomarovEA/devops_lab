# snapshot utility 
(C)Com 2019


Script written in Python 3.7.5
Retrieve information of the system state each <timeinterval> and write snapshots outputs in the file on text or JSON formats.

Each snapshot includes:
    ● Snapshot #
    ● TimeStamp
    ● Overall CPU load
    ● Overall memory usage
    ● Overall virtual memory usage
    ● IO information
    ● Network information.
        
Outputs writes in file on text or JSON formats.
Paramerers  <timeinterval> and <Output file type> are configurable thrue snapshop.ini file in current directory.


### Installation

Snapshot requires [psutil](https://pypi.org/project/psutil/) and [pip](https://pip.pypa.io/en/stable/installing/)

```sh
$ pip install .
$ python
$ import snapshot
```
### Usage
To start collecting data:
$ shapshot.start()
Output file will appear in the same folder which utility rezides.
