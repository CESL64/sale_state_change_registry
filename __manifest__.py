{
    "name": "Sale State Change Registry",
    "version": "18.0.1.0.0",
    "summary": "Registro de cambios de estado para ventas",
    "description": "Hereda sale.order para registrar cambios en state.",
    "author": "Prueba Tecnica",
    "license": "LGPL-3",
    "category": "Sales",
    "depends": [
        "sale",
        "state_change_registry",
    ],
    "data": [
        "views/sale_order_views.xml",
        "views/state_change_registry_views.xml",
    ],
    "installable": True,
    "application": False,
}
