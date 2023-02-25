# Introducing Arike
<b>"Arike"</b> is a project that aims to improve the palliative care system for patients who need constant or specialized medical attention. The word "Arike" comes from Malayalam and translates to "Alongside" or "Besides" in English.

In India, palliative care is provided by a team of specialized nurses who visit patients under their Panchayat/Municipality/Corporation to relieve their suffering and provide them with the best possible quality of life. However, the current system is paper-based, making it inefficient and prone to errors.

Our capstone project is to build a system that automates and streamlines the palliative care process, making it more efficient and accurate.

## Basics of Arike
In palliative care, there are "Primary Health Centers" (PHC) and "Community Health Centers" (CHC) that reside in a ward belonging to one of the many LSGs (Local Self-Government) in a district. Primary nurses visit patients locality-wise every month, go through their case sheets, and provide them with the care they need. If a patient needs expert care, they are referred to a specialist nurse from the CHC.

The main users of Arike are:

<b>Primary Nurse:</b> responsible for maintaining all health records for a patient under their PHC.

<b>Secondary Nurse:</b> specialist nurses from the CHC who provide special care for a patient when referred by a primary nurse.

<b>District Admin:</b> responsible for accessing records under the user's district. This user has full access to the data and can create and delete Primary or Secondary nurses.

## Main Entities
<b> Facility Provider: </b> can be a PHC or CHC.
<b> Patient: </b> registered in a PHC and referred to a CHC. They are the object whose data we deal with in the system.

#### Login Details:
You can log in to the system using the following credentials:

```makefile
Username: distadmin 
Password: distadmin
UserType: District Admin

Username: primarynurse
Password: primarynurse
UserType: Primary Nurse

Username: secondarynurse
Password: secondarynurse
UserType: Secondary Nurse
```

## Purpose
The purpose of the Arike project is to build a Django-based web application as part of the GDC Fellow Program for Coronasafe, with the goal of digitalizing healthcare. The project is focused on improving the current system of palliative care in India, where specialized medical staff provide care to patients directly in their homes or communities.

The current system is paper-based, which leads to inefficiencies and errors in the treatment process. The Arike project aims to automate and streamline this process, making it more efficient and accurate.

The main users of the Arike web application are primary and secondary nurses, who are responsible for maintaining health records and providing care to patients, and district administrators, who have full access to the data and can create or delete nurses.

By digitizing healthcare in this way, Arike can help improve the quality of life for patients under palliative care, reduce hospital capacity burden, and increase overall efficiency in the healthcare system.


## For Local Development

### 1. Install Packages

```
bundle
yarn
```

### 2. Configure application environment variables

1. Copy `example.env` to `.env`.

   ```
   cp example.env .env
   ```

2. Update the values of `DB_USERNAME` and `DB_PASSWORD` in the new `.env` file.

   Use the same values from the previous step. The username should be `postgres`, and the password will be whatever value you've set.

The `.env` file contains environment variables that are used to configure the application. The file contains documentation explaining where you should source its values from. If you're just starting out, you shouldn't have to change any variables other than the ones listed above.

### Basic Commands

#### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

   ```py
   python manage.py createsuperuser
   ```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

#### Setting up your database

To apply **migrations**, use this command:

```py
python manage.py makemirgations users
python manage.py makemirgations facility
python manage.py makemigrations sites
python manage.py migrate
```

#### Running tests with pytest

```py
pytest
```

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd arike
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

### Deployment

The following details how to deploy this application.

#### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

#### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
