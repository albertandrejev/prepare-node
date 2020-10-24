import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mutt_installed(host):
    mutt = host.package("mutt")
    assert mutt.is_installed

def test_lynis_installed_properly(host):
    lynis_installation = host.file("/opt/lynis")
    assert lynis_installation.is_directory

def test_lynis_cron_script_installed(host):
    lynis_cron = host.file("/etc/cron.daily/lynis")
    assert lynis_cron.contains('^EMAIL_TO=sysadmin@email.org$')
    assert lynis_cron.contains('^LYNIS_DIR=/opt/lynis$')
    assert lynis_cron.contains('^LYNIS=${LYNIS_DIR}/lynis$')
    assert lynis_cron.contains('^${LYNIS} audit system --auditor "${AUDITOR}" --cronjob > ${REPORT}$')
    assert lynis_cron.contains('^    echo "$EMAIL_MSG"|mutt "$EMAIL_TO" -s "Lynis vulnerabilities report (${HOST})" -a "${REPORT}";$')
