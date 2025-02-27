=================================
Resource Work Time From Contracts
=================================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-coopiteasy%2Faddons-lightgray.png?logo=github
    :target: https://github.com/coopiteasy/addons/tree/12.0/resource_work_time_from_contracts
    :alt: coopiteasy/addons

|badge1| |badge2| |badge3| 

Take the contracts of an employee into account when computing work time per
day.

When this module is installed, the number of hours an employee is supposed to
work is only computed from their contracts. Without contracts, the work time
per day is 0, instead of using the default company’s working hours.

The start and end dates of contracts are taken into account, but the status
(state) of contracts are ignored.

For this module to work properly, the company’s working hours should encompass
all possible work days (including weekend days if there are contracts with
weekend days), and each day should have working hours that correspond to the
working hours used in all contracts. This is because the company’s working
hours are used to compute leaves, and the number of hours per day is computed
from it.

For example, if the company working hours define 8 hours per day, from 8 to 12
and 13 to 17, all contracts’ working hours should be set from 8 to 12 and/or
from 13 to 17 for the corresponding days. Half days are thus supported.

If there are contracts with working hours that don’t match the company’s
working hours, the number of days for leaves will be computed incorrectly.

This module also makes the working hours (resource calendar) of an employee
always equal to the company’s working hours, and hides its field on the
employee form view.

**Table of contents**

.. contents::
   :local:

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/coopiteasy/addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/coopiteasy/addons/issues/new?body=module:%20resource_work_time_from_contracts%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Coop IT Easy SCRLfs

Contributors
~~~~~~~~~~~~

* `Coop IT Easy SCRLfs <https://coopiteasy.be>`_:

  * hugues de keyzer

Maintainers
~~~~~~~~~~~

This module is part of the `coopiteasy/addons <https://github.com/coopiteasy/addons/tree/12.0/resource_work_time_from_contracts>`_ project on GitHub.

You are welcome to contribute.
