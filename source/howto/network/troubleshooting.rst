Troubleshooting
===============

Linux: Unable to resolve host (domain name)
-------------------------------------------

:Problem:

    When accessing a host via its name, for example via ``curl "my.host.name"``,
    it is not resolved to a network address:

    .. code-block:: none

        curl: (6) Could not resolve host: my.host.name

:Cause:

    The DNS server, responsible to resolve host names to IP addresses, is either

    * not reachable (maybe due to a Firewall configuration of the Linux machines network)
    * does not have a configuration for this host name

:Solution:

    In case, your inside a company network, contact IT to help resolve the issue
    on either the DNS server or the Firewall.

    As a workaround, adapt the ``/etc/hosts`` file on the Linux system by adding
    the mapping (adapt the IP to the real IP of the host):

    .. code-block:: none

        # Example
        254.132.24.1        my.host.name
