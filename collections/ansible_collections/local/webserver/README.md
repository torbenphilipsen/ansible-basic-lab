# Local Webserver Collection

This collection contains roles and modules for web server automation.

## Included Roles

- `nginx_install`: Install and configure Nginx web server
- `nginx_vhost`: Configure Nginx virtual hosts

## Installation

Install the collection:

    ansible-galaxy collection install -p ./collections local.webserver

## Usage

Example playbook using the collection:

    ---
    - hosts: webservers
      collections:
        - local.webserver

      roles:
        - nginx_install

## License

GPL-3.0-or-later