sed
===

Update value in file
--------------------

.. code-block::

    export NTTS_PRODUCT_PREFIX_SUFFIX=cntts
    export PROMOTED_METAPACKAGE_VERSION=24.03.0

.. prompt:: bash

    sed -i "s/crnc-tts-neuraltts.products.${NTTS_PRODUCT_PREFIX_SUFFIX}==.*/crnc-tts-neuraltts.products.${NTTS_PRODUCT_PREFIX_SUFFIX}==${PROMOTED_METAPACKAGE_VERSION}\"/g" "${NTTS_PRODUCT_PREFIX_SUFFIX}_run_environment.yaml"

* ``-i`` defines that the file in-place is edited (no backup suffix provided)
* ``s/`` marks the begin of the regular expression, the single ``/`` marks its end
* the ``/g`` at the end, defines to perform global substitution, where the match
  for the regular expression is replaces by the string between ``/`` and ``/g``
* the filename argument (at the end) defines the file to be edited

.. code-block::

    sed -i "s/[pattern]/[replacement]/g <filename>"

.. hint::

    For macOS, use the following pattern for the in-place replacement:

    .. code-block::

        sed -i "" "s/[pattern]/[replacement]/g <filename>"