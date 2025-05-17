# Odoo CRM Social Networks Extension

## Requirements

1. **CRM Module Extension**
   - [X] Implement an extension that allows registering URLs for the following social accounts for each customer:
     - [X] Facebook
     - [X] LinkedIn
     - [X] Twitter

2. **Social Networks Tab**
   - [X] Display social networks in a separate tab in the customer profile
   - [X] Each social network should have its corresponding icon

3. **Completed Profile Indicator**
   - [X] When a customer has all social networks registered, mark it as a "completed profile"
   - [X] Show an image with a checkmark "Profile complete"
   - [X] This information should be visible from all customer views

4. **Profile Filtering**
   - [X] Add a filter that shows "Profile incomplete" customers

5. **Customer Promotion Page**
   - Add a website page dedicated to promoting customers
   - Show a list of customers with brief information about each one
   - Include their social accounts data

6. **Search Functionality**
   - Implement search on the promotion page
   - Allow finding customers by name and social accounts

7. **Compatibility**
   - Must be compatible with Odoo 13+

## Installation

1. Download the module and place it in your addons folder
2. Update the module list in Odoo
3. Install the module 'CRM Social Networks'
4. Restart the Odoo server

## Important Notes

Before using this module in production, you need to:

1. Add proper images for the module:
   - `/static/description/icon.png` - Module icon
   - `/static/description/check.png` - Checkmark icon for complete profiles

2. Test the module with your specific Odoo version to ensure compatibility

## Features

- Add social network fields to partners
- Display social networks in a separate tab with icons
- Show completed profile indicator
- Filter partners by profile completion status
- Provide a website page to promote customers with their social accounts
- Search functionality for customers by name and social accounts
