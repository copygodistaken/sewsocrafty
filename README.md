# SewSoCrafty
Fully functional website with products, admin panel and (one day) online payment methods

The wife "needs" a website, and I need practice/experience with python/flask development, so here we go...

## Goals:
Fully functional website with an admin panel in which the wife can add products/services, update pricing, etc.
Admin account will be able to add additional administrators for future expansion of the "business".
I'd like 90% of the information to be editable from the Admin panel, leaving me to work on additional stuff instead of managing a website.
Contact information from the website will be able to be texted (Twilio) and/or emailed to the admin list

## Plan
With the initial commit I've got most of the page rendering working, but still need to work the content development and backend development.
1. ~~Create admin account (hard-coded user/pass for now)~~ to:
   1. Add products
   1. Remove products
   1. Edit products
   1. Edit landing page contents
   1. Add additional admin accounts
1. Convert password to database storage (salted bcrypt hash)
1. Add password update via email token
1. Store/Retrieve/Edit product data from database
1. Create secure method to set up initial Admin account upon deployment (email token from config.py MAIL_USERNAME to MAIL_USERNAME?)
1. Store/Retrieve/Edit product data from database
1. Search capability built in, not sure if I'll use something like ElasticSearch or add "meta" tags in the DB and search that way.
1. Add contact capability (Text/Email) to contact pages

## Expected DB setup
#### Users
* user_id (prikey)
* user_name
* password (bcrypt hash w/salt)
* first_name
* last_name
* email
* phone_num
* picture

#### Products
* prod_id (prikey)
* prod_name
* prod_desc
* prod_price
* prod_labor
* prod_cost
* date_added
* date_updated
* tags
* image(s) (min1, max5)
* user_id (key)

I'm sure there's plenty of roadblocks that I haven't yet anticipated, but this gives me a bit of a "digital roadmap" apart from the notes I've taken in a composition book...

# v0.04 updates:
Discovered {% include %} for templates, reduced file size of HTML products for better modularization

Added /admin section:
1. Hardcoded test admin account (admin/password)
1. Login/logout/register pages, admin landing page template set up
1. More adjustments to CSS styles to kludge together Bulma into working with WTForms (I'm not an expert!)

# v0.05 updates:
Fixed a few things that should have been caught in v0.04, but I needed to push what I had written to the master...
1. Flash messages ("you didn't submit a username between two and thirty characters") weren't working.
1. Form validation wasn't working
1. Changed wtforms.validators.DataRequred() to InputRequired()
1. Cleaned up registration form layout and inline error messages
1. Added templates/includes/flash_messages.html to centralize flash message display in bulma
1. Updated admin.html to fit site formatting
1. Got the database working (for basic login/registration)
1. Fixed formatting/linking issues with includes/sidebar.html
1. Set up LoginManager for user session management
1. Changed mymethods.py back to models.py, still learning!



