import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_journald_syslogd_forwarding_set(host):
    sshd_config = host.file("/etc/systemd/journald.conf")
    assert sshd_config.contains("^ForwardToSyslog=yes$")
