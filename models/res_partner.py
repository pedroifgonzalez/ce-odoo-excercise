import re

from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    social_facebook = fields.Char(string="Facebook URL")
    social_linkedin = fields.Char(string="LinkedIn URL")
    social_twitter = fields.Char(string="Twitter URL")

    has_complete_profile = fields.Boolean(
        string="Has Complete Profile",
        compute="_compute_has_complete_profile",
        store=True,
        help="Indicates if the partner has all social networks filled",
    )

    @api.depends("social_facebook", "social_linkedin", "social_twitter")
    def _compute_has_complete_profile(self):
        """Compute if the partner has all social networks filled"""
        for partner in self:
            partner.has_complete_profile = all(
                [
                    partner.social_facebook,
                    partner.social_linkedin,
                    partner.social_twitter,
                ]
            )

    @api.onchange("social_facebook", "social_linkedin", "social_twitter")
    def _validate_social_network_url(self):
        # Define regex patterns for each social network URL
        for value, regex, network_name in zip(
            (self.social_facebook, self.social_linkedin, self.social_twitter),
            (
                r"^https?://(www\.)?(facebook|fb)\.com/[a-zA-Z0-9.\-_]+/?$",  # Facebook pattern
                r"^https?://(www\.)?linkedin\.com/(in|company)/[a-zA-Z0-9.\-_]+/?$",  # LinkedIn pattern
                r"^https?://(www\.)?(twitter|x)\.com/[a-zA-Z0-9_]+/?$",  # Twitter/X pattern
            ),
            ("Facebook", "LinkedIn", "Twitter/X"),
        ):
            if not value:
                continue
            if not re.match(regex, value):
                raise UserError(
                    f"Invalid URL format for {network_name}: {value}\n\n"
                    f"Please enter a valid {network_name} URL."
                )
