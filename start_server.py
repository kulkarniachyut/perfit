# export FLASK_APP=run.py
import os
from subprocess import call
# call(["ls", "-l"])

os.environ['FLASK_APP'] = 'run.py'
os.environ['FLASK_CONFIG'] = 'development'
call(["flask", "run"])
