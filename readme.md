blogsite
--------

Running server
--------------

```
venv\scripts\activate.bat
set FLASK_APP=run.py
flask run
```

Creating database
-----------------

```
venv\script\activate.bat
python
>>> from blogsite.models import db
>>> db.create_all()
```
