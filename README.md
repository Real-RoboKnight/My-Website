# My Website

This is the code that runs the [website that I develop](www.dylan-shah.com). 

When I create .env files, I will try to remember to commit a template 
version of the env file, that states the names of required secrets, 
to allow you to easily add them.

.env files:

- ./.env
  - `PORT:3000` This is the port on the host computer that my website will be on.
  - `SECRET_KEY` This should be a long and secure key that the server will use. When rotated, will sign out of all sessions, etc.
  - `EMAIL_HOST_PASSWORD` The password for the email service

Also, you will want to go to ./nginx/nginx.conf:45 and change the host name for the website.
Same with allowed hosts at `home_page/django/main/settings.py`
`localhost` is provided already if you are not planning to publish this site to the wider internet.

To run it, install docker, and run the docker compose file.

If there are any errors or suggestions, feel free to create a pull request or issue on Github, 
or email me at [website.errors@dylan-shah.com](mailto:website.errors@dylan-shah.com)