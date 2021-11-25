#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv
import pathlib

if __name__ == "__main__":
    DOT_ENV_PATH = pathlib.Path()
    if DOT_ENV_PATH.exists():
        #dotenv.read.dotenv()
        load_dotenv()
    else:
        print('make sure .env file exist')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "judonazim.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
