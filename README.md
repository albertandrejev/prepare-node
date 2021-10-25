# Cosmostation Validator Operations Repository

This repository contains ansible roles to control and setup Cosmostation validator infrastructure.

## Minimum requirements

* Debian 10 "Buster";
* Access via ssh by pub key;
* Ansible 2.9

## Installation of the additional roles

In order to install dependent roles you should perform following command: `ansible-galaxy install --roles-path ./roles -r requirements.yml`

## Initial configuration

Before you will start using this software it is required to provide initial configuration to the roles. First of all you will need to copy content of the `.sample` files in the project root (`inventory.sample`), `host_vars` and `groups_vars` directories to the appropriate names without extensions. In most cases it is enough to set variables in the `group_vars/all` and in `group_vars/network` as well as in the `host_vars/<node IP address or domain name>` (see samples).

## Keys special directory

`vars/` directory should contain additional variables for different purposes. Also please use directory to store Ansible Vault files.

## Documentation

Most of the variable uses self explanatory names , but in some cases additional comments added to the sources.

Please note that prior production usage you should test those scripts on available testnets. For this you need to create separate clone of this repo and configure it to use testnet of the supported networks.


# Testing

## Required software

- Docker

## Ansible environment installation

- Init python virual environment: `python3 -m venv molecule-venv`
- Activate environment: `source molecule-venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- 

## Examples

### Initial hosts configuration

```
$ ansible-playbook playbooks/bootstrap.yml
```

This command will install all required software, services and users to operate infrastructure hosts.
