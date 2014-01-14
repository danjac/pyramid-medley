**pyramid-medley** is an opinionated Pyramid scaffold to help you get going quickly with a new project.

It includes:

* SQLAlchemy
* Jinja2
* WTForms
* Twitter Bootstrap

The scaffolding also includes some extra goodies for example:

* Templated emails 
* Basic User model
* Caching and sessions (Redis)
* Simple cronjobs

This scaffold is probably more than is required for most projects : it's just a ton of patterns and ideas I've picked up playing 
around with the Pyramid stack. 


Quick install
-------------

1. git clone https://github.com/danjac/pyramid-medley.git
2. cd pyramid-medley
3. python setup.py develop

Making a new project
--------------------

First make a virtualenv...

1. pcreate -t medley myproject
2. cd myproject 
3. python setup.py install


