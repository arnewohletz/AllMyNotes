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

Describe node (shows included namspaces)

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

    An example ``namespace.yaml`` for a development namespace:

    .. code-block:: yaml

        apiVersion: v1
        kind: Namespace
        metadata:
          name: development

Delete a namespace (all namespaces defined in ``namespace.yaml``:

.. prompt:: bash

    kubectl delete -f <path/to/namespace.yaml>

Services
--------
A service is a load balancer and transfers traffic to pods.

Get all services within a namespace

.. prompt:: bash

    kubectl get services -n <NAMESPACE>


Pod
---
A pod is a abstraction which represents one or more application containers.

Get names all pods of a namespace:

.. prompt:: bash

    kubectl get pods -n <NAMESPACE>

Get names of all pods in all namespaces

.. prompt:: bash

    kubectl get pods -A

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