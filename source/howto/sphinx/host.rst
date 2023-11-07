Host documentation on localhost (with nginx)
--------------------------------------------
#. :ref:`Install and setup nginx <install_setup_nginx>`.
#. Create a configuration file (for example *nginx.conf*) in your project root directory.
#. Add the following content:

    .. code-block:: none
        :linenos:

        server {
            listen                  1050;
            server_name             localhost;
            charset                 utf-8;
            client_max_body_size    75M;
            root                    "/path/to/project/_build";
            index                   index.html;
        }

#. Adjust the port (line 2), the root path (line 6; which is where the index.html of your
   build output resides).
#. Create a symlink of your configuration to your nginx configuration directory:

    .. tabs::
        .. group-tab:: macOS

            .. prompt:: bash

                ln -s </path/to/my/application>/nginx.conf /usr/local/etc/nginx/init.d/<doc_project_name>.conf

        .. group-tab:: Linux

            .. prompt:: bash

                ln -s </path/to/my/application>/nginx.conf /etc/nginx/sites-enabled/<doc_project_name>.conf

#. Restart nginx

    .. tabs::
        .. group-tab:: macOS

            .. prompt:: bash

                nginx -c /usr/local/etc/nginx/nginx.conf

            or restart as brew service via

            .. prompt:: bash

                brew services restart nginx

        .. group-tab:: Linux

            .. prompt:: bash

                nginx /etc/init.d/nginx restart

#. Open ``https://127.0.0.1:<PORT>``, using the port specified in your configuration, in your browser.
