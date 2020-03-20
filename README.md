# time_series_gap_filling.py
Script to fill gaps in time series and interpolate with different methods.

## Requirements

Python3.6.4

```
cycler==0.10.0
DateTime==4.3
kiwisolver==1.1.0
matplotlib==3.2.1
numpy==1.18.2
pandas==1.0.3
pyparsing==2.4.6
python-dateutil==2.8.1
pytz==2019.3
scipy==1.4.1
six==1.14.0
zope.interface==5.0.0
```

## Installation

1. Install python3 on your system
2. Install virtualenv
3. Change

Install python3 on your system.
For Mac: open a terminal and install virtualenv:

```
pip install virtualenv
```

We are about to create a virtualenv with the requirements listed above. A virtual environment ensures that the script is executed always with the same versions of required packages. Change the directory to a location where you want to store the virtual environment.

```
cd directory/where/you/want/to/store/your/virtualenv
```

Now make a virtualenv with you python3 installation:
```
virtualenv -p python3 gap_filling_env_py3
```

Activate this environent.
```
source gap_filling_env_py3/bin/activate
```
Install requirements
