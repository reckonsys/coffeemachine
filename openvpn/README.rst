OpenVPN
-------

If docker fails to start after installing openvpn, uninstall openvpn, install docker-ce, make sure docker daemon is running and the re install openvpn again. Everything should work now.

::

    docker-compose build openvpn

    # Initialize the configuration files and certificates
    docker-compose run --rm openvpn ovpn_genconfig -u udp://VPN.SERVERNAME.COM
    docker-compose run --rm openvpn ovpn_initpki

    docker-compose up -d openvpn

    # CLIENTNAME='peter'
    # Generate Client Certs
    docker-compose run --rm openvpn easyrsa build-client-full $CLIENTNAME nopass

    # Retrieve the client configuration with embedded certificates
    docker-compose run --rm openvpn ovpn_getclient $CLIENTNAME > ovpn/$CLIENTNAME.ovpn

    # Revoke a client certificate
    docker-compose run --rm openvpn ovpn_revokeclient $CLIENTNAME remove

- https://github.com/kylemanna/docker-openvpn/blob/master/docs/docker-compose.md
- https://github.com/jessfraz/dockerfiles/blob/master/coredns/Dockerfile
