# Copyright 2022 Elabore
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale show CRM opportunity",
    "version": "14.0.1.0.0",
    "author": "Elabore",
    "website": "https://github.com/elabore-coop/sale-tools",
    "maintainer": "Laetitia Da Costa",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "The field linking a quote to an opportunity is always visible, not only in developper mode",
    "description": """
   :image: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
=================
sale_show_crm_opportunity
=================

    * The field linking a quote to an opportunity is always visible (not only in developper mode)

Installation
============

Install ``sale_show_crm_opportunity``, all dependencies will be installed by default.

Known issues / Roadmap
======================

None yet.

Bug Tracker
===========

Bugs are tracked on `our issues website
<https://github.com/elabore-coop/sale-tools/issues>`_. In case of
trouble, please check there if your issue has already been
reported. If you spotted it first, help us smashing it by providing a
detailed and welcomed feedback.

Credits
=======

Images
------

* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=f3db262>`_.

Funders
-------

The development of this module has been financially supported by:
* Elabore (https://elabore.coop)


Maintainer
----------
This module is maintained by Elabore.

""",
    # any module necessary for this one to work correctly
    "depends": [
        "sale",
        "sale_crm"
    ],
    "data": [
        "views/sale_order_views.xml",        
    ],
    "installable": True,
    "application": False,
}
