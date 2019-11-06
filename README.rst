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
- Taiga
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

Detailed installation docs available here: https://github.com/reckonsys/bigga


OpenVPN
-------

::

    docker-compose build openvpn

    # Initialize the configuration files and certificates
    docker-compose run --rm openvpn ovpn_genconfig -u udp://VPN.SERVERNAME.COM
    docker-compose run --rm openvpn ovpn_initpki

    docker-compose up -d openvpn

    # CLIENTNAME='peter'
    # Generate Client Certs
    docker-compose run --rm openvpn easyrsa build-client-full $CLIENTNAME

    # Retrieve the client configuration with embedded certificates
    docker-compose run --rm openvpn ovpn_getclient $CLIENTNAME > $CLIENTNAME.ovpn

    # Revoke a client certificate
    docker-compose run --rm openvpn ovpn_revokeclient $CLIENTNAME remove

- https://github.com/kylemanna/docker-openvpn/blob/master/docs/docker-compose.md
