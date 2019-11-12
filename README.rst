coffeemachine
=============

Optimizing Coffee Machine Utilization

Method 1
--------

Don't use a Coffee Machine

Method 2
--------

Install these tools in your **coffeemachine**

- OpenSteer
- GitLab
- `Taiga <https://github.com/docker-taiga/taiga/>`_
- Zulip
- Odoo

How to install those?
---------------------

::

    docker-machine create coffeemachine
    eval $(docker-machine env coffeemachine)
    docker-compose build
    docker-compose up


And that is how you optimize your Coffee Machine.


bigga
-----

Detailed installation docs available here: https://github.com/reckonsys/bigga
