{
    "name": "CRM Social Networks",
    "version": "1.0",
    "category": "CRM",
    "summary": "Add social network fields to CRM partners",
    "description": """
        This module extends the CRM functionality to:
        - Add social network fields (Facebook, LinkedIn, Twitter) to partners
        - Display social networks in a separate tab with icons
        - Show completed profile indicator
        - Filter partners by profile completion status
        - Provide a website page to promote customers with their social accounts
    """,
    "author": "Pedro Iván Fernández González",
    "website": "",
    "depends": [
        "crm",
        "website",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/templates.xml",
    ],
    "qweb": [],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
