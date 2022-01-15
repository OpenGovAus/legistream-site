# legistream (legistream-site)

![Legistream Screenshot](/.github/img/f11-ss.png)

Legistream is the easiest way to stream Australian parliaments live. Legistream bypasses the need to use the often slow and outdated state/territory parliament websites, streamlining the experience. Legistream also bypasses the need to use a Flash player on both the NT and QLD websites, offering a more secure viewing option for people interested in those jurisdictions.

Legistream uses our Python package [legistream-backend](https://github.com/OpenGovAus/legistream-backend) to gather stream URLs and metadata from the parliament sites.

- We also plan to integrate [Aus-Bills](https://github.com/OpenGovAus/Aus-Bills) in some form in the future.

# Setup

## Install RabbitMQ

You can find instructions for different hosts [here](https://www.rabbitmq.com/download.html).

## Poetry

Install `poetry` with `pip`:

    ```sh
    pip3 install poetry
    ```

## Install Dependencies

    ```sh
    poetry update
    ```

## Create secrets.py

In `legistream_site/`, make a file called `secrets.py`. Inside it, create these two constants:

```python
ADMIN_PATH = 'your server admin path'
SECRET_KEY = 'your server secret key' # Look at the Django docs for more info
```

The application will work if you just throw in random garbage, but **do not leave ADMIN_PATH blank!**

## Set DEBUG = True

In `legistream_site/settings.py` change the line:

```python
DEBUG = False
```

to

```python
DEBUG = True
```

# Running Legistream

On first run:

```sh
poetry run python3 manage.py makemigrations legistream
```

```sh
poetry run python3 manage.py migrate
```

Clear pending tasks:

```sh
poetry run celery -A legistream_site purge
```

Start the Celery worker:

```sh
poetry run celery -A legistream_site worker -l info --pool=solo
```

Start Celery Beat:

```sh
poetry run celery -A legistream_site beat -l info
```

To run the server, use this command:

```sh
poetry run python3 manage.py runserver --insecure
```

If you get any errors, make sure you've set up your virtual environment correctly and that you've installed all the required dependencies.

You should now be able to access Legistream by going to `localhost:8000` in your browser.
