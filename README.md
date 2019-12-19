# drumserver
a simple api endpoint to navigate a large directory of drum samples to power web audio apps.

the /static folder contains a copy of the directory structure in an s3 bucket. 
this app uses python `os` to traverse the directories but the files in this repo have no data. 
The purpose is solely to provide a folder navigation UI, not to actaully serve the audio files.




## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

Create an environment
```sh
$ python3 -m venv env
$ pip install -r requirements.txt

$ createdb drumserver

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

or activate existing environment
sh
```
virtualenv env
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
