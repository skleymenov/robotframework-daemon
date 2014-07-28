.. rfdaemon documentation master file, created by
   sphinx-quickstart on Mon Jul 28 13:13:05 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to rfdaemon's documentation!
====================================

Contents:

.. toctree::
   :maxdepth: 2

Overview
========
The *rfdaemon* is a web service with the RESTful API, that provides feature full set of functions allowing to run, monitor the Robot Framework test suites and store and review corresponding results.

RESTful API
===========

/suite
------
Controls suites version, provides detailed suite description and a set of methods to run, queue and cancel a suite execution.

Methods
^^^^^^^
* **GET** Returns a list of suites available.

/suite/__version
----------------
Methods
^^^^^^^
* **GET** Returns version info, including author and date of last commit.
* **POST** Requests to do a git pull from a corresponding repository. **TBD**

/suite/{id}
-----------
Methods
^^^^^^^
* **GET** Returns detailed information about corresponding test suite

/suite/{id}/run
---------------
Methods
^^^^^^^
* **PUT** Runs the corresponding test suite immediately.

/suite/{id}/queue
-----------------
Methods
^^^^^^^
* **PUT** Adds the corresponding test suite into the run queue.

Contribute
==========
* Issue Tracker: http://github.com/skleymenov/rfdaemon/issues
* Source Code: http://github.com/skleymenov/rfdaemon

License
=======

The project is licensed under the `Apache 2.0 license <http://www.apache.org/licenses/LICENSE-2.0>`_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

