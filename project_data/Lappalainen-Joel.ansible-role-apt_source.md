Apt source
=========

[![Build Status](https://travis-ci.org/ajsalminen/ansible-role-apt_source.svg?branch=master)](https://travis-ci.org/ajsalminen/ansible-role-apt_source)


This role can be used to manage Apt package sources. It supports both regular
Debian and Ubuntu's PPA sources. The role provides an easy way to only pick the
packages you want to take priority over the ones in the base release via Apt
pinning.

Requirements
------------

python-apt has to be present on the server.

Role Variables
--------------

apt_source_config:

A list of dicts. Only supports a single item for now. The apt source is defined
in the item and has the key/value pairs described below.

      source: deb http://ppa.launchpad.net/nginx/stable/ubuntu {{ansible_lsb.codename}} main

A complete Debian package source string or a ppa name.

      key:
        url: http://www.dotdeb.org/dotdeb.gpg
        id: 89DF5277

A dict containing the URL and ID of the public key associated with the source
as accepted by the apt_key module.

      packages:
        - pattern: '*nginx*'
          absent: True
          filepath: /etc/apt/preferences.d/my_custom_file

A list of patterns for packages that should get the priority defined by
apt_source_high_priority. This for making the desired packages the primary
candidate for installation by apt. If absent is set, the pin will be removed.
The filepath can also be set if the defaults don't work because of overlapping
pins for example.

     apt_source_source_selector: "release o={{apt_source_release_origin}}"

This is the selector used when pinning packages. The role tries to set
reasonable defaults based on the other parameters but set this if needed. For
example the varnish repos need this to be set to o=varnish-cache.org while the
default value is o=repo.varnish-cache.org. Check with apt-cache policy.

     apt_source_state: absent

To remove a package source completely, set this parameter.

     apt_source_high_priority: 500

The priority set for packages that are picked from the source with
apt_source_packages.

     apt_source_default_pin:
       - pattern: "*"
         priority: 200
         filepath: "{{ apt_source_preferences_dir }}/100_{{ apt_source_preferences_name }}"

The default pin priority set for all packages in the source. You could change
this to pin them all to a different priority.

Example Playbook
----------------

    - hosts: servers
      roles:
          - role: ajsalminen.apt_source
            apt_source_config:
                - source: deb http://ppa.launchpad.net/nginx/stable/ubuntu {{ansible_lsb.codename}} main
                   key:
                        url: http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x00A6F0A3C300EE8C
                        id: C300EE8C
                   packages:
                        - pattern: '*nginx*'

License
-------

MIT/Simplified BSD license

Author Information
------------------

Role created by Antti J. Salminen in 2014.