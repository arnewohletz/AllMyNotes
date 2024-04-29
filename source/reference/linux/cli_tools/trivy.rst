trivy
=====
``trivy`` is a scanner for vulnerabilities in container images, file systems,
and Git repositories, as well as for configuration issues and hard-coded secrets.

Scan Docker image
-----------------
Scan a Docker image from a repository URL

.. prompt:: bash

    trivy image <URL>

for example:  ``trivy image artifactory.prod.cre.az-eastus2.hosting.nuautoco.com/cli-docker/calllog-sidecar-master:0.0.7``

Scan a local Docker image

.. prompt:: bash

    trivy image <IMAGE_ID>