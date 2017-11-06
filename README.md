# DRF Shop
Written only for training. \
Rest API for shop. \
Have products and tags. \
Unauthorised users can only read api data. Superusers can post/update/delete data. \
Filtering by product title and tag slug.

# How to run from Docker
Project have 3 management command for create testing data:
- `make_admin` - create admin user with login `Admin` and password `adm1n`.
- `make_tags` - create tags for products.
- `make_products` - create products with random tags.

Example:
```
$ docker-compose build
$ docker-compose run web python3 /dj_shop/manage.py migrate
$ docker-compose run web python3 /dj_shop/manage.py make_admin
$ docker-compose run web python3 /dj_shop/manage.py make_tags
$ docker-compose run web python3 /dj_shop/manage.py make_products
$ docker-compose up
```

Then, go to `0.0.0.0:8000`. 
