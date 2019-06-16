# Order System
Designing an order system in Django Framework. Include login/register/logout/admin functionality, as well as Product/Order/ProductOrder relational database implementation.

# Before you get started
- Basic understanding of Django (forms, urls, models, templates, jinja)
- Understanding of many to many and one to many database design principles

# Available Routes
- `http://localhost:8000/register` The registeration page.
- `http://localhost:8000/login` The login page. Redirects to home page if user is authenticated.
- `http://localhost:8000/` The home page with products. Requires authentication.
- `http://localhost:8000/order` The order summary page. Requires authentication.
- `http://localhost:8000/confirm-order` The confirm order route. Allows user to mark their order as confirmed, so that it can be flagged for delivery/shipping by administrator. Requires authentication.
- `http://localhost:8000/add-to-cart/<slug>/` Called from the home page, used to add items to users order. Requires authentication.

# Setup
**How to obtain this repository:**
```sh
git clone https//link.to.this.projects.git-repo
```

**Modules/dependencies:**
- `django`
- `python3`

# Tests
- Adding items to order summary
- Confirmation of orders (flips flags (confirmed/order_status) on orders and orderproduct items)
- Aggregate total order and unconfirmed order items in ProductOrder model for Summary

# Todo 
- Add delete from cart functionality


# Contributors
- Daniel Corcoran

# Sources
- [Django Docs](https://docs.djangoproject.com/en/2.2/)