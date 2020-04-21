Scripts to fill gaps in time series and interpolate with different methods.
Both scripts are tailored to different file types. Please read the header of the corresponding file.

## Requirements

Python3.6.4

```
DateTime==4.3
matplotlib==3.2.1
numpy==1.18.2
pandas==1.0.3
scipy==1.4.1
```

## Installation (for Mac)

Install python3.6 on your system. To check if python3.6 is already available open a terminal and type:
```
which python3.6
```
It should display the current version of python3.6. If not, you need to install python3.

When you have succesfully installed python3.6 open a terminal and install virtualenv:
```
python3.6 -m pip install virtualenv
```
We are about to create a virtual environment with the requirements listed above. A virtual environment ensures that the script is executed always with the same versions of required packages. Change the directory to a location where you want to store the virtual environment.
```
cd DIRECTORY/WHERE/YOU/WANT/TO/STORE/THE/VIRTUAL/ENVIRONMENT
```
Now make a virtualenv with you python3.6 installation:
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
curl -O https://github.com/timohouben/time_series_analysis/blob/master/TheScriptYouWantToDownload.py
```

# Run
Please read the header of the script first.

ALWAYS activate the created environment from above before you run the script:
```
source PATH/TO/THE/ENVIRONEMNT/bin/activate
```
Run the script:
```
python3 TheScriptYouWantToRun.py PATH/TO/SOURCE/FILES
```
