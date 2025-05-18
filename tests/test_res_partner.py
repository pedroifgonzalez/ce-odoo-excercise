from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):
    """Test cases for the ResPartner model extensions"""

    def setUp(self):
        super(TestResPartner, self).setUp()
        # Create a test partner
        self.test_partner = self.env["res.partner"].create(
            {
                "name": "Test Company",
                "is_company": True,
            }
        )

    def test_social_fields_exist(self):
        """Test that social network fields exist on partner model"""
        self.assertTrue(hasattr(self.test_partner, "social_facebook"))
        self.assertTrue(hasattr(self.test_partner, "social_linkedin"))
        self.assertTrue(hasattr(self.test_partner, "social_twitter"))
        self.assertTrue(hasattr(self.test_partner, "has_complete_profile"))

    def test_complete_profile_computation(self):
        """Test the computation of has_complete_profile field"""
        # Initially, profile should be incomplete
        self.assertFalse(self.test_partner.has_complete_profile)

        # Fill in one social network
        self.test_partner.social_facebook = "https://facebook.com/testcompany"
        self.test_partner.flush_recordset()
        self.assertFalse(self.test_partner.has_complete_profile)

        # Fill in second social network
        self.test_partner.social_linkedin = "https://linkedin.com/company/testcompany"
        self.test_partner.flush_recordset()
        self.assertFalse(self.test_partner.has_complete_profile)

        # Fill in all social networks
        self.test_partner.social_twitter = "https://twitter.com/testcompany"
        self.test_partner.flush_recordset()
        self.assertTrue(self.test_partner.has_complete_profile)

        # Remove one social network
        self.test_partner.social_facebook = False
        self.test_partner.flush_recordset()
        self.assertFalse(self.test_partner.has_complete_profile)

    def test_url_validation(self):
        """Test URL validation for social networks"""
        # Valid URLs should not raise errors
        self.test_partner.social_facebook = "https://facebook.com/testcompany"
        self.test_partner.social_linkedin = "https://linkedin.com/company/testcompany"
        self.test_partner.social_twitter = "https://twitter.com/testcompany"

        self.test_partner.flush_recordset()

        # Test with www prefix
        self.test_partner.social_facebook = "https://www.facebook.com/testcompany"
        self.test_partner.social_linkedin = "https://www.linkedin.com/in/testuser"
        self.test_partner.social_twitter = "https://www.twitter.com/testcompany"

        self.test_partner.flush_recordset()

        with self.assertRaises(UserError):
            self.test_partner.social_facebook = "invalid_url"
            self.test_partner.flush_recordset()
