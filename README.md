# Validator initial server configuration

This repository contains ansible playbooks to setup Cosmos SDK based infrastructure.

## Minimum requirements

* Debian 10 "Buster";
* Access to root using ssh by pub key or password;
* Ansible > 2.9

## Initial configuration

Before you will start using this software it is required to provide initial configuration to the roles.
First of all you will need to copy content of the `.sample` files in the project root (`inventory.sample`) and `groups_vars` directories to the appropriate names without extensions. In most cases it is enough to set variables in the `group_vars/all` and add IP address of the server to the `invenotory` file into `bootstrap` group.

## Running

- Init python virual environment with all dependencies: `source setup_venv.sh`

## Keys special directory

`vars/` directory should contain additional variables for different purposes. Also please use directory to store Ansible Vault files.

## Documentation

Most of the variable uses self explanatory names , but in some cases additional comments added to the sources.

Please note that prior production usage you should test those scripts on available testnets. For this you need to create separate clone of this repo and configure it to use testnet of the supported networks.

## Examples

### Initial hosts configuration

```
$ ansible-playbook playbooks/bootstrap.yml
```

This command will install all required software, services and users to operate infrastructure hosts.

# Testing

## Required software

- Docker

