# Copyright 2024 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "sale_usability_misc",
    "version": "16.0.1.0.1",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Elabore",
    "license": "AGPL-3",
    "category": "Sales",
    "summary": "Various improves for Sales app",
    # any module necessary for this one to work correctly
    "depends": [
        "base","sale","sales_team","sale_crm",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/sale_order_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}