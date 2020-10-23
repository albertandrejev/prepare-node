import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_password_and_root_login_disabled(host):
    sshd_config = host.file("/etc/ssh/sshd_config")
    assert sshd_config.contains("PasswordAuthentication no")
    assert sshd_config.contains("PermitRootLogin no")

def test_sshd_is_running_and_enabled(host):
    sshd = host.service("sshd")
    assert sshd.is_running
    assert sshd.is_enabled
