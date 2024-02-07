Debmonitor Client Changelog
---------------------------

`v0.3.5`_ (2024-02-07)
^^^^^^^^^^^^^^^^^^^^^^

Bug fixes
"""""""""

* setup.py: actually set ``install_requires`` in the call to ``setup()``.

  * Do not set ``apt`` as a dependency as it's not shipped in PyPi.org. It needs to be installed from the debian
    package ``python3-apt``.
  * Add setuptools as an explicit dependency, required for `pkg_resources`.

`v0.3.4`_ (2024-01-24)
^^^^^^^^^^^^^^^^^^^^^^

Miscellanea
"""""""""""

* setup.py: remove dependency on the deprecated and archived ``pytest-runner``.

`v0.3.3`_ (2024-01-11)
^^^^^^^^^^^^^^^^^^^^^^

Miscellanea
"""""""""""

* Initial version in its own standalone repository.
* .wmfconfig: updated configuration for releases to adapt to the new repository.
* Use ``setuptools_scm`` for handling the client version.


.. _`v0.3.3`: https://github.com/wikimedia/operations-software-debmonitor-client/releases/tag/v0.3.3
.. _`v0.3.4`: https://github.com/wikimedia/operations-software-debmonitor-client/releases/tag/v0.3.4
.. _`v0.3.5`: https://github.com/wikimedia/operations-software-debmonitor-client/releases/tag/v0.3.5
