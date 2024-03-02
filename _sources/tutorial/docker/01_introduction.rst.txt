01 - Introduction
=================
Pros to Docker
--------------
**Very few resources / saves money**

    * Isolate application from its environment
    * Virtual machines do the same, but waste a lot of resources (e.g. vagrant)
    * Docker shares common dependencies between multiple applications
    * Server services are charged by computation. Using VMs requires lots of resources
      for your applications overhead
    * Docker containers starts in milliseconds (~ 8 applications in 2 seconds)

**Portability**

    * Getting applications working on a device can require lots of dependencies
    * Application is stored inside a docker file, which is then executable on various machines
    * A docker file is a controlled environment

**Picking the right tool for the job**

    * No installation complications when trying new, not familiar technologies
    * Installation of these tools is managed by docker
    * Implementing micro-services for applications is much easier as each service can run
      in its own docker
