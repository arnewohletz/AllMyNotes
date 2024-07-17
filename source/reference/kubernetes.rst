Kubectl
=======

Kubernetes consists of clusters, nodes and pods.

* Cluster: A group of nodes, which have the same location and accessed via the same Cloud Provider's API
* Nodes: A worker, mostly a separate machine, consisting of various pods
* Pod: Smallest unit in Kubernetes, defines a service, consists of one or more containers

A *namespace* bundles multiple *pods*, which may also be located on different *nodes* together.


Config
------
Get current config (from ``~/.kube/config``)

.. prompt:: bash

    kubectl config view



Cluster
-------
Get info about the cluster:

.. prompt:: bash

    kubectl cluster-info


Node
----
Get all nodes in current cluster

.. prompt:: bash

    kubectl get nodes

Describe node (shows included namespaces)

.. prompt::

    kubectl describe node <NODE>


Namespace
---------
A namespace is a space which separates resources and workloads.

Get all namespaces in current cluster:

.. prompt:: bash

    kubectl get namespaces

.. note::

    **Predefined namespaces:**

    * ``default``: The default namespace for objects with no other namespace
    * ``kube-node-lease``: This namespace holds Lease objects associated with each node.
      Node leases allow the kubelet to send heartbeats so that the control plane can detect node failure.
    * ``kube-public``: This namespace is created automatically and is readable by all users
      (including those not authenticated). This namespace is mostly reserved for cluster usage,
      in case that some resources should be visible and readable publicly throughout the whole cluster.
      The public aspect of this namespace is only a convention, not a requirement.
    * ``kube-system``: The namespace for objects created by the Kubernetes system.

Describe a namespace:

.. prompt:: bash

    kubectl describe namespace <NAMESPACE>

Create a namespace:

.. prompt:: bash

    kubectl apply -f <path/to/namespace.yaml>

.. hint::

    An example ``namespace.yaml`` for a development namespace:

    .. code-block:: yaml

        apiVersion: v1
        kind: Namespace
        metadata:
          name: development

Delete a namespace (all namespaces defined in ``namespace.yaml``:

.. prompt:: bash

    kubectl delete -f <path/to/namespace.yaml>


Deployment
----------
A deployment is a resource which manages an application on the cluster. It handles
the creation of the defined pods (and possible replicas) and ensures the application
runs in the desired state.

**Create**

Deploy an application from a single Docker image (uses single node)

.. prompt:: bash

    kubectl create deployment <DEPLOYMENT_NAME> --image=<IMAGE_URL:TAG>

**Describe**

Get detailed information about a deployment

.. prompt:: bash

    kubectl describe deployment <DEPLOYMENT_NAME>

**Scaling**

A deployment may have multiple replica pods running the same container to ensure
the constant availability of the application or to distribute incoming traffic
to multiple nodes.

Scale deployment to 4 replicas

.. prompt:: bash

    kubectl scale deployments/<DEPLOYMENT_NAME> --replicas=4

**Update image version**

Update the used Docker image version for a deployment, initiating a rolling update:
new pods using new images are created. When those running, the olds ones are
terminated

.. prompt:: bash

    kubectl set image deployments/<DEPLOYMENT_NAME> <IMAGE_NAME:TAG>

Check rollout status of deployment (e.g. after updating image version)

.. prompt:: bash

    kubectl rollout status deployments/<DEPLOYMENT_NAME>

Revert latest rollout  of deployment (e.g. a failed image version update)

.. prompt:: bash

    kubectl rollout undo deployments/<DEPLOYMENT_NAME>


Services
--------
A service is a load balancer and transfers traffic to pods. It exposes an
application deployment to external traffic providing a port.

Create a new service exposing a deployment under port 8001

.. prompt::

    kubectl expose deployments/<DEPLOYMENT_NAME> --type="NodePort" --port 8001

Get all services within a namespace

.. prompt:: bash

    kubectl get services -n <NAMESPACE>

**Describe a service**

Show detailed info on all services within the namespace

.. prompt:: bash

    kubectl describe services -n <NAMESPACE>

Show detailed info on specific services within the namespace

.. prompt:: bash

    kubectl describe service <SERVICE_NAME> -n <NAMESPACE>

**Delete a service**

Delete a single service (this does not affect the application deployment which
uses the service)

.. prompt:: bash

    kubectl delete service <SERVICE_NAME> -n <NAMESPACE>


Pod
---
A pod is a abstraction which represents one or more application containers.

Get names all pods of a namespace:

.. prompt:: bash

    kubectl get pods -n <NAMESPACE>

Get names of all pods in all namespaces

.. prompt:: bash

    kubectl get pods -A

Get wide output format of all pods of a namespace (includes cluster-internal IP address)

.. prompt:: bash

    kubectl get pods -o wide

Get names of all pods using a specific label name

.. prompt:: bash

    kubectl get pods -l <LABEL_NAME>

**Describe a pod**

Shows the containers, running inside the pod among other information.

Describe single pod within a namespace:

.. prompt:: bash

    kubectl describe pod <POD> -n <NAMESPACE>

Describe all pods within a namespace:

.. prompt:: bash

    kubectl describe pods -n <NAMESPACE>


**Get logs**

Print the latest logs of a running container inside a log (if pod only runs a single
container, ``-c <CONTAINER>``  must not be specified):

.. prompt:: bash

    kubectl logs -n <NAMESPACE> <POD> -c <CONTAINER>


**Labels**

Labels are used to tag one or multiple pods

Add another label name to a pod

.. prompt:: bash

    kubectl label pod <POD_NAME> <LABEL_NAME=VALUE>

Delete a label from a pod

.. prompt:: bash

    kubectl label pod <POD_NAME> <LABEL_NAME>-


ReplicaSet
----------

A ReplicaSet is a resource, which ensures that a specific number of pod replicas
are running at any given time. Commonly deployments are used to manage ReplicaSets,
so it is not recommended to use them directly.

**Get replica sets**

Get all ReplicaSets within the namespace which manage pods containing a certain label

.. prompt:: bash

    kubectl get replicaset -l <LABEL_NAME> -n <NAMESPACE>

