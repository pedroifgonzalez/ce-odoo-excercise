from odoo.tests.common import TransactionCase
from ..controllers.main import CustomerPromotion


class TestCustomerPromotion(TransactionCase):
    """Test cases for the customer promotion page controllers"""

    def setUp(self):
        super(TestCustomerPromotion, self).setUp()
        # Create test partners with social networks
        self.partner1 = self.env["res.partner"].create(
            {
                "name": "Test Company 1",
                "is_company": True,
                "customer_rank": 1,
                "social_facebook": "https://facebook.com/testcompany1",
                "social_linkedin": "https://linkedin.com/company/testcompany1",
                "social_twitter": "https://twitter.com/testcompany1",
            }
        )

        self.partner2 = self.env["res.partner"].create(
            {
                "name": "Test Company 2",
                "is_company": True,
                "customer_rank": 1,
                "social_facebook": "https://facebook.com/testcompany2",
            }
        )

        # Initialize controller
        self.controller = CustomerPromotion()

    def test_build_customer_domain(self):
        """Test the domain building method"""
        # Test without search term
        domain = self.controller._build_customer_domain()
        self.assertEqual(domain, [("is_company", "=", True), ("customer_rank", ">", 0)])

        # Test with search term
        domain = self.controller._build_customer_domain("testcompany1")
        self.assertIn(("name", "ilike", "testcompany1"), domain)
        self.assertIn(("social_facebook", "ilike", "testcompany1"), domain)
        self.assertIn(("social_linkedin", "ilike", "testcompany1"), domain)
        self.assertIn(("social_twitter", "ilike", "testcompany1"), domain)

    def test_create_customer_pager(self):
        """Test the pager creation method"""
        # Create a test domain
        domain = [("is_company", "=", True), ("customer_rank", ">", 0)]

        # Create pager with environment
        pager = self.controller._create_customer_pager(
            domain, page=0, search="test", env=self.env
        )

        # Check pager structure
        self.assertIn("page_count", pager)
        self.assertIn("offset", pager)
        self.assertEqual(pager["page"], {"url": "/our-customers?search=test", "num": 1})

    def test_get_customer_partners(self):
        """Test the partner fetching method"""
        # Create a test domain and mock pager
        domain = [("is_company", "=", True), ("customer_rank", ">", 0)]
        mock_pager = {"offset": 0}

        # Get partners - pass the environment
        partners = self.controller._get_customer_partners(
            domain, mock_pager, env=self.env
        )

        # Check if both test partners are returned
        self.assertIn(self.partner1.id, partners.ids)
        self.assertIn(self.partner2.id, partners.ids)

        # Test with search domain
        search_domain = domain + [("social_facebook", "ilike", "testcompany2")]
        partners = self.controller._get_customer_partners(
            search_domain, mock_pager, env=self.env
        )

        # Should only contain partner2
        self.assertNotIn(self.partner1.id, partners.ids)
        self.assertIn(self.partner2.id, partners.ids)

    def test_prepare_customer_values(self):
        """Test the values preparation method"""
        # Create test data
        partners = self.env["res.partner"].browse([self.partner1.id, self.partner2.id])
        mock_pager = {"page": 1, "offset": 0}
        search_term = "test"

        # Get template values
        values = self.controller._prepare_customer_values(
            partners, mock_pager, search_term
        )

        # Check values
        self.assertEqual(values["partners"], partners)
        self.assertEqual(values["pager"], mock_pager)
        self.assertEqual(values["search"], search_term)
