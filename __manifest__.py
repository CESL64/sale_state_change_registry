{
    "name": "Sale State Change Registry",
    "version": "18.0.1.0.0",
    "summary": "Registro de cambios de estado para ventas",
    "description": "Hereda sale.order para registrar cambios en state.",
    "author": "Carlos Eduardo Salinas Honduras",
    "license": "LGPL-3",
    "category": "Sales",
    "depends": [
        "sale_management",
        "state_change_registry",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/mail_template_data.xml",
        "views/sale_order_views.xml",
        "views/state_change_registry_views.xml",
        "wizard/state_change_registry_report_wizard_views.xml",
        "views/menus.xml",
        "reports/sale_order_state_change_registry_report_inherit.xml",
    ],
    "installable": True,
    "application": False,
}
