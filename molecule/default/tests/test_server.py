import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('molecule-gocd-server')


def test_server_container(host):
    # 'host' now binds to the container
    assert host.check_output('docker ps -f "name=gocd-server" -f '
                             '"status=running" --format '
                             '{{ "{{.Names}}" }}') == 'gocd-server'


def test_traefik_container(host):
    # 'host' now binds to the container
    command = ('docker ps -f "name=traefik_traefik_1" -f "status=running" '
               '--format {{ "{{.Names}}" }}')
    assert host.check_output(command) == 'traefik_traefik_1'
