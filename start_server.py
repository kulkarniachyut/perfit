import os
from subprocess import call

os.environ['FLASK_APP'] = 'run.py'
os.environ['FLASK_CONFIG'] = 'development'
call(["flask", "run"])
