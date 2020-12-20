# legistream (legistream-site)

![Legistream Screenshot](/gh-images/f11-ss.png)

Legistream is the easiest way to stream Australian parliaments live. Legistream bypasses the need to use the often slow and outdated state/territory parliament websites, streamlining the experience. Legistream also bypasses the need to use a Flash player on both the NT and QLD websites, offering a more secure viewing option for people interested in those jurisdictions.

Legistream uses our Python package [legistream-backend](https://github.com/OpenGovAus/legistream-backend) to gather stream URLs and metadata from the parliament sites.

- We also plan to integreate [Aus-Bills](https://github.com/OpenGovAus/Aus-Bills) in some form in the future.

# Setup

## Virtual Environment

Begin by setting up a virtual environment:

```sh
pip3 install virtualenv
```
```sh
virtualenv legistr_venv
```

##### Windows

```sh
legistr_venv/Scripts/activate
```

##### Linux/MacOS

```sh
source legistr_venv/bin/activate
```

You should now be loaded into the virtual environment, and your terminal should look like this:

```
(legistr_venv) /.../git/legistream-site/ >
```

## Install Dependencies

```sh
pip3 install -r requirements.txt
```

## Create secrets.py

In `legistream_site/`, make a file called `secrets.py`. Inside it, create these two constants:

```python
ADMIN_PATH = 'your server admin path'
SECRET_KEY = 'your server secret key' # Look at the Django docs for more info
```

The application will work if you just throw in random garbage, but **do not leave ADMIN_PATH blank!**

# Running Legistream

To run the server, use this command:

```sh
python3 manage.py runserver
```

If you get any errors, make sure you've set up your virtual environment correctly and that you've installed all the required dependencies.

You should now be able to access Legistream by going to `localhost:8000` in your browser.

# Contributing

- Do not submit pull requests that contain code for the actual parliament streams, please have a look at [legistream-backend](https://github.com/OpenGovAus/legistream-backend) if you wish to change things related to getting stream URLs and statuses.

Submit a pull request when you've finished working on your desired feature, issue, or optimisation.

Your request won't be merged until at least two of us have had a look through your PR and approved it.

If you submit anything that deliberately opens up security risks, **don't expect to be submitting anything else in the future**.