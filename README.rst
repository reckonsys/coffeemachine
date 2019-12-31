coffeemachine
=============

Optimizing Coffee Machine Utilization

Method 1
--------

Don't use a Coffee Machine

Method 2
--------

Install these tools in your **coffeemachine**

- `Gogs <https://gogs.io/>`_
- `Taiga <https://taiga.io/>`_
- `Odoo <https://www.odoo.com/>`_
- `OpenSteer <https://https://github.com/reckonsys/opensteer>`_

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


OpenVPN
-------


If docker fails to start after installing openvpn, uninstall openvpn, install docker-ce, make sure docker daemon is running and the re install openvpn again. Everything should work now.

Have a look into `openvpn` folder to install openvpn
