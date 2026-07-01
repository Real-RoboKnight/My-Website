# My Website

This is the code that runs the [website that I develop](www.dylan-shah.com). 

When I create .env files, I will try to remember to commit a template 
version of the env file, that states the names of required secrets, 
to allow you to easily add them.

.env files:

- ./.env
  - `PORT` This is the port on the host computer that my website will be on.
  - `SECRET_KEY` This should be a long and secure key that the server will use. When rotated, will sign out of all sessions, etc.
  - `EMAIL_HOST` URL of the SMTP email server
  - `EMAIL_HOST_USER` Username for email server
  - `EMAIL_HOST_PASSWORD` The password for the email server
  - `TURNSTILE_SECRET_KEY` A secret key for [cloudflare turnstile](www.cloudflare.com/products/turnstile/)
  - `TURNSTILE_PUBLIC_KEY` A public key for [cloudflare turnstile](www.cloudflare.com/products/turnstile/)

Also, you will want to go to ./nginx/nginx.conf:45 and change the host name for the website.
Same with allowed hosts at `home_page/django/main/settings.py`
`localhost` is provided already if you are not planning to publish this site to the wider internet.

To run it, install docker, and run the docker compose file.

If there are any errors or suggestions, feel free to create a pull request or issue on Github, 
or email me at [website.errors@dylan-shah.com](mailto:website.errors@dylan-shah.com)

## License

The source code in this repository is licensed under the [GNU Affero General Public License v3.0 (AGPL-3.0)](LICENSE), with the **explicit exception** of any front end django/jinja templates.

All django/jinja templates located anywhere are proprietary and confidential and are not subject to the AGPL. These are typically in `templates` directories, however anything that is not a django/jinja template in these directories are licensed under the AGPL-3.0. Permission is granted to run these templates locally as part of this application, but you may not redistribute, modify, or sublicense these templates without explicit written permission.

