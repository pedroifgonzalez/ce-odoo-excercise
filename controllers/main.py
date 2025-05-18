from odoo import http, _
from odoo.http import request


class CustomerPromotion(http.Controller):
    def _build_customer_domain(self, search=""):
        """Build domain for customer search

        Args:
            search: Search term to filter customers

        Returns:
            List of domain criteria for partner search
        """
        domain = [("is_company", "=", True), ("customer_rank", ">", 0)]

        # Add search criteria if provided
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

        return domain

    def _create_customer_pager(self, domain, page=0, search="", env=None):
        """Create pager for customer page

        Args:
            domain: Domain for partner search
            page: Current page number
            search: Search term used
            env: Environment to use, defaults to request.env

        Returns:
            Pager dict for pagination
        """
        # Use provided env or request.env
        env = env or request.env
        website = env["website"] if env else request.website

        # Count total partners for pagination
        partner_count = env["res.partner"].sudo().search_count(domain)

        # Create pager
        return website.pager(
            url="/our-customers",
            url_args={"search": search},
            total=partner_count,
            page=page,
            step=12,
        )

    def _get_customer_partners(self, domain, pager, env=None):
        """Get partner records based on domain and pager

        Args:
            domain: Domain for partner search
            pager: Pager dict with offset information
            env: Environment to use, defaults to request.env

        Returns:
            Recordset of res.partner
        """
        # Use provided env or request.env
        env = env or request.env

        return (
            env["res.partner"]
            .sudo()
            .search(domain, order="name asc", limit=12, offset=pager["offset"])
        )

    def _prepare_customer_values(self, partners, pager, search=""):
        """Prepare values for template rendering

        Args:
            partners: Partner recordset to display
            pager: Pager dict for pagination
            search: Search term used

        Returns:
            Dict of values for template rendering
        """
        return {
            "partners": partners,
            "pager": pager,
            "search": search,
        }

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
        # Build domain with search criteria
        domain = self._build_customer_domain(search)

        # Create pager for pagination
        pager = self._create_customer_pager(domain, page, search)

        # Get partner records
        partners = self._get_customer_partners(domain, pager)

        # Prepare template values
        values = self._prepare_customer_values(partners, pager, search)

        # Render template
        return request.render("ce_odoo_excercise.customers_page", values)
