Debmonitor Client Changelog
---------------------------

`v0.5.0`_ (2025-06-26)
^^^^^^^^^^^^^^^^^^^^^^

CLI breaking changes
""""""""""""""""""""

* CLI: the --update CLI argument has been removed. The script is not capable of self-updating anymore as the feature
  was never really used and the canonical way to update it is via its Debian package.

New features
""""""""""""

* config and CLI arguments: allow to specify multiple servers to send the report to more than one Debmonitor server.
  For the configuration the servers must be specified as comma-separated. For the CLI the -s/--server argument can be
  specified multiple times.

`v0.4.1`_ (2025-05-22)
^^^^^^^^^^^^^^^^^^^^^^

Minor improvements
""""""""""""""""""

*  Add support for Debian trixie and Python versions up to 3.13.

`v0.4.0`_ (2024-06-24)
^^^^^^^^^^^^^^^^^^^^^^

CLI breaking changes
""""""""""""""""""""
* The OS/Distribution name reported by the CLI is more granular from now on,
  since it contains the Distribution name (like Debian) and its version-id
  number. Check the new features section for more info.

New features
""""""""""""

* cli: modify get_distro_name to return the version id.
  Debmonitor is now being used to track hosts and Docker images,
  and having more granularity in the reported OS distribution
  name is surely beneficial to ease security reviews.
  The OS name is now going to be reported with its version id
  (as reported in /etc/os-release).

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
.. _`v0.4.0`: https://github.com/wikimedia/operations-software-debmonitor-client/releases/tag/v0.4.0
.. _`v0.4.1`: https://github.com/wikimedia/operations-software-debmonitor-client/releases/tag/v0.4.1
.. _`v0.5.0`: https://github.com/wikimedia/operations-software-debmonitor-client/releases/tag/v0.5.0
