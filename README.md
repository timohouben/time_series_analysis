# time_series_gap_filling.py
Script to fill gaps in time series and interpolate with different methods.
This script is tailored to the following file type:

```
6335820  ID from GRDC discharge database; (Abfluss) DAILY
nodata   -9999.000
n       1 measurement per day [1, 1440]
start   1951 01 01 00 00 (YYYY MM DD HH MM)
end     2017 12 31 00 00 (YYYY MM DD HH MM)
1985 11 03 00 00       1.060
1985 11 04 00 00       0.826
1985 11 05 00 00       1.380
1985 11 06 00 00       3.230
1985 11 07 00 00       1.250
1985 11 08 00 00       1.200
1985 11 09 00 00       1.560
1985 11 10 00 00       2.390
1985 11 11 00 00       1.640
1985 11 12 00 00       1.230
        .                .
        .                .
        .                .
```

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

## Installation (for Mac)

Install python3.6 on your system. To check if python3.6 is already available open a terminal and type:
```
which python3
```
It should display the current version of python3.6. If not, you need to install python3.

When you have succesfully installed python3 open a terminal and install virtualenv:
```
python3.6 -m pip install virtualenv
```
We are about to create a virtual environment with the requirements listed above. A virtual environment ensures that the script is executed always with the same versions of required packages. Change the directory to a location where you want to store the virtual environment.
```
cd DIRECTORY/WHERE/YOU/WANT/TO/STORE/THE/VIRTUAL/ENVIRONMENT
```
Now make a virtualenv with you python3 installation:
```
virtualenv -p python3.6 gap_filling_env_py3
```
Activate this environment.
```
source gap_filling_env_py3/bin/activate
```
Your command line should be headed with (gap_filling_env_p3).

Download the requirements.txt:
```
curl -O https://github.com/timohouben/time_series_analysis/blob/master/requirements.txt
```
Install the requirements:
```
pip install -r requirements.txt
```

Now you are ready to run the script.
Change directory where you want to save the script:
```
cd DIRECTORY/SAVE/SCRIPT
```
Download the script:
```
curl -O https://github.com/timohouben/time_series_analysis/blob/master/time_series_gap_filling.py
```

# Run
Please read the header of the script first.

ALWAYS activate the created environment from above before you run the script:
```
source PATH/TO/THE/ENVIRONEMNT/bin/activate
```
Run the script:
```
python3 time_series_gap_filling.py PATH/TO/SOURCE/FILES
```
