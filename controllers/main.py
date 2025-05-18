from odoo import http, _
from odoo.http import request


class CustomerPromotion(http.Controller):
    @http.route(
        [
            "/our-customers",
            "/our-customers/page/<int:page>",
        ],
        type="http",
        auth="public",
        website=True,
    )
    def customers(self, page=0, search="", **kw):
        """Display the customers promotion page with search functionality"""
        domain = [("is_company", "=", True), ("customer_rank", ">", 0)]

        # Search functionality
        if search:
            domain += [
                "|",
                "|",
                "|",
                ("name", "ilike", search),
                ("social_facebook", "ilike", search),
                ("social_linkedin", "ilike", search),
                ("social_twitter", "ilike", search),
            ]

        # Count for pager
        partner_count = request.env["res.partner"].sudo().search_count(domain)

        # Pager
        pager = request.website.pager(
            url="/our-customers",
            url_args={"search": search},
            total=partner_count,
            page=page,
            step=12,
        )

        # Get partners
        partners = (
            request.env["res.partner"]
            .sudo()
            .search(domain, order="name asc", limit=12, offset=pager["offset"])
        )

        values = {
            "partners": partners,
            "pager": pager,
            "search": search,
        }

        return request.render("ce-odoo-excercise.customers_page", values)
