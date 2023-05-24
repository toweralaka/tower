# Tower

## Setting up a development environment

1. Have Python 3
2. Create a virtualenv:
   ```console
   $ python3 -m venv towerenv
   ```
3. Activate the venv:
   ```console
   $ . towerenv/bin/activate  # or a Windows alternative
   ```
   *Note that you have to run this every time you start a new
   terminal shell session.*
4. Run the following to have the same requirements installed in your local virtualenv you've just activated:
   ```console
   $ pip install -r requirements.txt
   ```
5. Set up "dotenv" by copying the example file and altering the values:
   ```console
   $ cp -v .env.example
   $ code .env  # edit stuff at this step
   ```
   `DEBUG` may remain `True`, it only controls how much helpful info
   Django will show to you on errors. `DJANGO_SECRET_KEY` should be set
   to any random string, don't copy this value from production, use your
   own. 
   
   *It is safe to add secrets to `.env` — it's gitignored, it's not safe
   to do this with `.env.example`, though.*
6. Populate your database with the tables according to
   the app models: 
   ```console
   $ ./manage.py migrate
   ```
7. With the following, you'll start a Python server instance:
   ```console
   $ ./manage.py runserver
   ```
   You may open http://127.0.0.1:8000/ to view this project.
   Keep the process running for as long as you're doing the development
   work.

