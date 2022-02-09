07 - Dockerizing your web applications
======================================

**General Tips**

Always add and use these file to all your web applications for dockerization:

    * Dockerfile
    * .dockerignore
    * docker-compose.yml
    * .env

"The secret to change is to focus all of your energy not on fighting the old
but on building the new"

-> force you to design your apps in a scale-able way, even if you are not scaling
beyond one host

**Logging**

Issue

    * Ruby write log messages in a /tmp folder by default
    * Hence, they are written into the container
    * All log files are lost when restarting the container, since volumes are not
      used during production

Solution

    * Redirect your log to STOUT (Flask does this automatically)
    * Logs are then managed by docker at the host level, not the container level (web
      app level)
    * What happens with the log file is then defined on the host level

**Use ENV variables**

* Use your own env variables even if your application uses its own config files
* That way separate environments will have separate environment files (e.g. dev and
  production)
* Remember: docker-compose can load multiple env files in a specified order

**Keep your apps stateless**

Issue

    * Keep them as stupid as possible
    * Don't store important data inside your app
    * If webapp get restarted, all data is lost

Solution

    * Use redis (or similar tools) to store data between requests
    * In reality those data is often stored on the client site as signed cookies
    * To store them on the server side, use redis to save them at the backend

-> See the "Twelve-Factor App" for a guide to design web applications (https://12factor.net/)
