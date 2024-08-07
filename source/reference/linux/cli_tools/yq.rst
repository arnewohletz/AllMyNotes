yq
==

Update values
-------------
Update multiple values (using environment variables)

.. code-block:: bash

    $ yq --indent 4 ".ntis.ntis_repository_volume_name = \"${NTIS_REPOSITORY_VOLUME_NAME}\" | .data.volume_name = \"${DATA_VOLUME_NAME}\"" -i "${NTTS_PRODUCT_PREFIX_SUFFIX}_run_tags.yaml"

* preserve the double-quotes: ``\"${NTIS_REPOSITORY_VOLUME_NAME}\"``
