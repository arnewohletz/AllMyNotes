How to use Docsearch + Algolia for searching Spinx documentation
================================================================

Set up Algolia DocSearch
------------------------

#. Create an free `Algolia`_ account at https://dashboard.algolia.com/users/sign_up.
#. Log into the created account and create a new application.
#. For this new application (which has a unique ID, like ``XDNC7OV40H``), which
   must be selected,

    #. create an new API key (select the *API Keys* link), which will be used by
       crawler (needs writing access). Go to :menuselection:`All API Keys --> New API Key`,
       give it a description (like: *for scraping, has writing access*), add the *ACL*
       (Access Control List) ``addObject``, ``editSettings`` and ``deleteIndex`` rights
       and save the key.
    #. create a new index (e.g. 'documentation_search'), which will be used to store
       the documenation page's records, which will be used for searching. Got to
       :menuselection:`Search --> Configure --> Index --> New... --> Index`. Give
       it an expressive name (like: *documentation_search*).

Set up the Sphinx documentation
-------------------------------
#. Install both the extensions `sphinx-sitemap`_ and `sphinx-docsearch`_.

    .. prompt:: bash

        pip install sphinx-sitemap sphinx-docsearch

#. Add both extensions to your ``conf.py`` file:

    .. code-block:: python

        extensions = [ ...
            'sphinx_sitemap',
            'sphinx_docsearch',
            ...
            ]

#. For *sphinx-sitemap*. also add these variables to your ``conf.py`` file:

    .. code-block:: python

        html_baseurl = '<HOST_ADDRESS_AND_PORT>'
        sitemap_filename = "sitemap.xml"
        sitemap_url_scheme = "{link}"
        sitemap_locales = [None]

    where ``<HOST_ADDRESS_AND_PORT>`` is the URL under which your documentation
    is hosted (zt is also possible to host it locally (e.g. via nginx,
    here serving the documentation at ``http://127.0.0.1:xxxxx/``, where ``xxxxx``
    is the used port).

#. For *sphinx-docsearch*, also add these variables to your ``conf.py`` file:

    .. code-block:: python

        docsearch_app_id = "<DOCSEARCH_APP_ID>"
        docsearch_api_key = "<DOCSEARCH_SEARCH_API_KEY>"
        docsearch_index_name = "<DOCSEARCH_INDEX_NAME>"

    where

        * ``<DOCSEARCH_APP_ID>`` is the ID of your application, created in the last section
        * ``<DOCSEARCH_SEARCH_API_KEY>`` is the API key used for searching only (not the one,
          we created, as only reading rights are required)
        * ``<DOCSEARCH_INDEX_NAME>`` is the name of the index of the application, we created

Set up DocSearch Scraper
------------------------
First, the documentation needs needs to be scraped and the results published to the index
in your Algolia application. As the current v3 of DocSearch only allows to be used for
publicly available web pages, the legacy v2 must be used. It must be self-hosted, which is
best done via the Docker image, provided on https://hub.docker.com/r/algolia/docsearch-scraper.

#. `Install Docker`_.
#. Install `jq`_.
#. Inside the documentation project's root, create an ``.env`` file, which contains the
   Algolia application ID and the API key which has writing rights (which we previously created).
   An example:

    .. code-block:: ini

        APPLICATION_ID=XDNC7OV40H
        API_KEY=e68cf0191685750ebe30574473b0016e
        MAX_API_KEY_LENGTH=32

    Set the ``MAX_API_KEY_LENGTH`` variable value to the length of your ``API_KEY``.

#. Also create a `DocSearch config`_ JSON file in the documentation's root directory,
   for instance ``docsearch_crawler_settings.json``. It will contains the configuration
   for the crawler, for example:

    .. code-block:: json

        {
          "index_name": "documentation_search",
          "sitemap_urls": ["http://trn-srvtts-gpu03.cerence.net:8321/sitemap.xml"],
          "sitemap_enabled": true,
          "stop_urls": [],
          "selectors": {
            "lvl0": ".document h1",
            "lvl1": {
              "selector": ".document h2, .document li"
            },
            "lvl2": ".document h3",
            "lvl3": ".document h4",
            "text": ".document p, .document li, .document pre, .document li"
          },
          "selectors_exclude": [
            ".search-exclude"
          ]
        }

    It it important to align the configuration values to your specific documentation in
    order to successfully crawl the data.

    * ``index_name``: the name of the application's index (here: ``documentation_search``)
    * ``sitemap_urls``: the URL of the documentation's ``sitemap.xml`` (we will create it
      later during building the documentation, placing it at the root URLs, here:
      ``["http://trn-srvtts-gpu03.cerence.net:8321/sitemap.xml"]``)
    * ``sitemap_enabled``: define that the sitemap.xml is supposed to be used by the
      crawler to retrieve all individual URLs of the documentation (here: ``true``)
    * ``stop_urls``: list of all URLs which are not supposed to be crawled (here: empty)
    * ``selectors``: lists all CSS selectors whose matching elements are crawled and
      assigned to the associated targets. There are seven targets, ``lvl0``, ``lvl1``,
      ``lvl2``, ``lvl3``, ``lvl4``, ``lvl5`` and ``text``. The first six refer to the
      different titles, where ``lvl0`` is the highest in hierarchy and ``lvl5`` is the
      lowest. Though only ``lvl0`` is required, it is recommended to define at least the
      first three. The ``text`` target contains all CSS selectors matching text elements
      which are supposed to be considered for the search. The selectors are depending
      on the documentation's HTML structure and should be inspected in a running instance
      of it. If the crawler reveals incorrect or missing records, it mostly comes from
      incorrectly defined selectors, in which case those need to be adapted and the
      crawler to be executed again
      More info under https://docsearch.algolia.com/docs/legacy/config-file#selectors
    * ``selectors_exclude``: list of all element selectors, which should be excluded
      from the crawling records (here: ``.search-exclude``, any element of class="search-exclude",
      which must be done in the Sphinx documentation, using a `class`_ name)

    .. important::

        Don't use ``start_urls`` option, if your want all your pages inside ``sitemap.xml``
        to be searched. In this case, it was observed, that the sitemap is ignored.


Execute the crawler
-------------------
#. Rebuild the documentation to create or update the ``sitemap.xml``.
#. Make sure, the documentation is hosted under the specified address (you may also
   check that the ``sitemap.xml`` is available under <HOST_ADDRESS_AND_PORT>/sitemap.xml)
#. From the documentations sources root directory (where ``.env`` and
   ``docsearch_crawler_settings.json`` are located), run the Docker image like this:

    .. prompt:: bash

        docker run -it --env-file=.env -e "CONFIG=$(cat docsearch_crawler_settings.json | jq -r tostring)" algolia/docsearch-scraper

    .. important::

        It has been observed, that ZScaler is blocking the connection from the Docker
        container towards the hosted documentation. If you see *Host unreachable* errors
        reported, switch off ZScaler while the container is running.

    .. hint::

        It has been observed, that the version ``v1.13.0`` of *algolia/docsearch-scraper*
        shows more log output. In case, you want to debug a failing execution, you may
        defer to this image via ``algolia/docsearch-scraper:v1.13.0``.

#. After the documentation has been crawled, you may visit the *index* of your Algolia
   application, to check, if the amount of records, reported by DocSearch at the end of
   the run, are all available.
#. Visit the hosted documentation and try using the search bar. The displayed results
   should now display the information according the previously extracted records.


Further documentation
---------------------

Aloglia DocSearch GitHub: https://github.com/algolia/docsearch
Algolia DocSearch for Sphinx: https://sphinx-docsearch.readthedocs.io/en/latest/index.html#
Algolia Dashboard: https://dashboard.algolia.com/
Algolia Config File: https://docsearch.algolia.com/docs/legacy/config-file/
Algolia self run DocSearch: https://docsearch.algolia.com/docs/legacy/run-your-own/

Use a sitemap.xml: https://docsearch.algolia.com/docs/legacy/tips/
Tutorial: https://brunoscheufler.com/blog/2021-08-08-setting-up-algolia-docsearch-with-nextjs
Tutorial 2: https://www.howtocode.io/posts/algolia/how-to-setup-algolia-doc-search

Maybe switch to v3: https://docsearch.algolia.com/docs/what-is-docsearch/



.. _Algolia: https://www.algolia.com/
.. _sphinx-sitemap: https://sphinx-sitemap.readthedocs.io/en/latest/index.html
.. _sphinx-docsearch: https://sphinx-docsearch.readthedocs.io/en/latest/
.. _Install Docker: https://docs.docker.com/engine/install/
.. _DocSearch config: https://docsearch.algolia.com/docs/legacy/config-file/
.. _class: https://docutils.sourceforge.io/docs/ref/rst/directives.html#class-option
.. _jq: https://github.com/jqlang/jq