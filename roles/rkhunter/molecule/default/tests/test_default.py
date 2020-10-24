import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rkhunter_config_properly_set(host):
    rkhunter = host.file("/etc/default/rkhunter")
    assert rkhunter.contains('^CRON_DAILY_RUN="true"$')
    assert rkhunter.contains('^CRON_DB_UPDATE="true"$')
    assert rkhunter.contains('^DB_UPDATE_EMAIL="true"$')
    assert rkhunter.contains('^REPORT_EMAIL="sysadmin@email.org"$')
    assert rkhunter.contains('^APT_AUTOGEN="true"$')

def test_rkhunter_local_config_properly_set(host):
    rkhunter_local = host.file("/etc/rkhunter.conf.local")
    assert rkhunter_local.contains('^ALLOWHIDDENDIR=/tmp$')
    assert rkhunter_local.contains('^ALLOWHIDDENFILE=/tmp/file1$')
    assert rkhunter_local.contains('^ALLOWDEVFILE=/dev/sdb1$')
    assert rkhunter_local.contains('^SCRIPTWHITELIST=/root/some_script$')
    assert rkhunter_local.contains('^PWDLESS_ACCOUNTS=myself$')
    assert rkhunter_local.contains('^SCANROOTKITMODE=THOROUGH$')
