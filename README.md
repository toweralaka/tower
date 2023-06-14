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

# To activate scheduler so schedules are performed
1. Go to scheduled tasks model under the DJANGO Q application in the admin(https://{domain_name}/admin/django_q/schedule)
2. Create scheduled tasks:
   * Task to send prescription reminder emails
      * 'Name' = any arbitrary value
      * 'Func' = 'tracker.tasks.send_recent_reminder'
      * Indicate how often you want the schedule to run:
         e.g: ('Schedule type' = 'minutes', 'Minutes' = '2') means every 2 munites, django_q will look for active prescriptions and send those that are due
      * Leave other default values and submit
3. 
   * IN DEVELOPMENT:
      * open a new console
      * start qcluster
      ```console
      $ ./manage.py start qcluster.service
      ```
   * IN PRODUCTION:
      * Create a service for qcluster
         * Open qcluster.service file
         ```console
         $ sudo nano /etc/systemd/system/qcluster.service
         ```
         * Edit service as follows:

            [Unit]

            Description=qcluster runner

            After=network.target


            [Service]

            User=user

            WorkingDirectory=/home/user/path_to_project

            ExecStart=/home/user/path_to_project_env/bin/python manage.py qcluster


            [Install]

            WantedBy=multi-user.target
      * Enable the service:
         ```console
         sudo systemctl enable qcluster.service
         ```
      * Start the service:
         ```console
         sudo systemctl start qcluster.service
         ```