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

            .. code-block:: bash

                $ ln -s </path/to/my/application>/nginx.conf /usr/local/etc/nginx/init.d/<doc_project_name>.conf

        .. group-tab:: Linux

            .. code-block:: bash

                $ ln -s </path/to/my/application>/nginx.conf /etc/nginx/sites-enabled/<doc_project_name>.conf

#. Restart nginx

    .. tabs::
        .. group-tab:: macOS

            .. code-block:: bash

                $ nginx -c /usr/local/etc/nginx/nginx.conf

            or restart as brew service via

            .. code-block:: bash

                $ brew services restart nginx

        .. group-tab:: Linux

            .. code-block:: bash

                $ nginx /etc/init.d/nginx restart

#. Open ``https://127.0.0.1:<PORT>``, using the port specified in your configuration, in your browser.


Host documentation on GitHub Pages
----------------------------------
`GitHub Pages`_ is an alternative to host a Sphinx documentation, making it available
from anywhere. GitHub provides the service for free for public repositories (make sure,
the repository, containing the documentation, is publicly available).

Deploy from branch
``````````````````
#. Log into your GitHub account and open the documentation repository.
#. Create a new, empty branch (:menuselection:`View all branches --> New branch`),
   named ``gh-pages`` and push it to the remote (here: ``origin``):

    .. code-block:: bash

        $ git switch --orphan gh-pages
        $ git commit --allow-empty "initial commit"
        $ git push origin gh-pages

#. Select :menuselection:`Actions --> New Workflow`. Here, select to *set up a workflow yourself*.
#. A new file (default: ``main.yml``) is created under ``.github/workflows/`` and presented
   in the editor. Change the name to a proper name, for example ``build_publish_html.yml``.
#. In the editor, enter the action's workflow. This shows a working example:

    .. code-block:: yaml
        :linenos:

        name: "Pull Request Docs Build"
        on: [pull_request, push]

        jobs:
          docs:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v4
            - uses: actions/setup-python@v5
              with:
                python-version: '3.11'
            - name: Install dependencies
              run: |
                pip install -r requirements.txt
                sudo apt-get update
                sudo apt-get install -y pandoc
                python -m sphinx build -b html source build
            - uses: actions/upload-artifact@v1
              with:
                name: github-pages
                path: /home/runner/work/AllMyNotes/AllMyNotes/build/
            - name: Commit HTML output to gh-pages
              run: |
                  git clone https://github.com/horsewithnoname1985/AllMyNotes.git --branch gh-pages --single-branch gh-pages
                  cp -r ./build/* gh-pages/
                  cd gh-pages
                  touch .nojekyll
                  git config --local user.email "action@github.com"
                  git config --local user.name "GitHub Action"
                  git add .
                  git commit -m "Update documentation" -a || true
            - name: Push changes
              uses: ad-m/github-push-action@master
              with:
                branch: gh-pages
                directory: gh-pages
                github_token: ${{ secrets.GITHUB_TOKEN }}

    Adapt the workflow to your needs. In the upper form, it executes the following
    steps on a Linux virtual machine:

        * Checks out the repo's sources
        * Installs Python 3.11
        * Install Python dependencies and *pandoc*
        * Build the documentation as HTML
        * Upload the HTML output as build artifact to this run
        * Commit and the HTML output to the ``gh-pages`` branch

#. Select :guilabel:`Commit changes...` to commit the workflow file. As the workflow
   defines, that a runs is triggered on every push, this will trigger a workflow run.
#. Go to :guilabel:`Actions` and check the workflow (here: *Pull Request Docs Build*)
   completes successfully.
#. If so, go back :guilabel:`Code` and select the *gh-pages* branch, which should contain
   all HTML output files.
#. Select :menuselection:`Settings --> Code and automation --> Pages`.
#. Under :menuselection:`Build and deployment --> Source`, select ``Deploy from a branch``.
   Below, under *Branch*, make sure the ``gh-branch`` is selected and ``/ (root)`` is
   used as the pages parent directory (as ``index.html`` is on the branches root
   directory) and save the selection.
#. Refresh the page. On the top, there should now appear a box, containing the
   message ``Your site is live at ...``. If not, enter the following URL into your browser:

    .. code-block:: none

        https://<github_username>.github.io/<repository_name>/

   This should open your documentation.


.. _GitHub Pages: https://pages.github.com/
