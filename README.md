# COMP3278 Project: Face Recognition

Face recognition using python and mysql.

## Installation

### Environment

Create virtual environment using Anaconda.
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```

### Extract model

```
cd app/cv_backend
tar -xvzf train.tar.gz
```

### MySQL Install

[Mac](https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html)

[Ubuntu](https://dev.mysql.com/doc/mysql-linuxunix-excerpt/5.7/en/linux-installation.html)

[Windows](https://dev.mysql.com/downloads/installer/)

You'll obtain an account and password after installation, then you should modify the appropiate files in `cv_backend/*.py`, with the corresponding username and password:

```py
# create database connection
myconn = mysql.connector.connect(host="localhost", user="root", passwd="xxxxx", database="facerecognition")
```

### Database credentials setup

Change `db_user`, `db_passwd`, `db_name` in `app/config.yml` accordingly.

### Email setup

This app uses the gmail SMTP server. To use the "send to my email" feature, change the credentials in `app/config.yaml`. 

You also need to enable "Less secure app access" in gmail: See https://myaccount.google.com/lesssecureapps.

## Login Interface

```
python app/Welcome_code.py
```

The camera will be activated and recognize your face using the pretrained model.
