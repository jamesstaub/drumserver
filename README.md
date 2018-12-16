# drumserver
a simple api endpoint to navigate a large directory of drum samples to power web audio apps.

the /static folder contains a copy of the directory structure in an s3 bucket. 
this app uses python `os` to traverse the directories but the files in this repo have no data. 
The purpose is solely to provide a folder navigation UI, not to actaully serve the audio files.


to run:
`python3 -m venv env`
`source env/bin/activate`
`python app/__init__.py`