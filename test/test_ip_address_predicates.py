from ipaddress import IPv4Network

from predicate.ip_address_predicates import (
    is_ipv4_network_global_p,
    is_ipv4_network_link_local_p,
    is_ipv4_network_loopback_p,
    is_ipv4_network_multicast_p,
    is_ipv4_network_private_p,
    is_ipv4_network_reserved_p,
    is_ipv4_network_unspecified_p,
    subnet_of_p,
    supernet_of_p,
)


def test_ipv4_network_is_global():
    assert not is_ipv4_network_global_p(IPv4Network("100.64.0.0/10"))
    assert not is_ipv4_network_global_p(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_multicast():
    assert not is_ipv4_network_multicast_p(IPv4Network("127.0.0.0/29"))
    assert is_ipv4_network_multicast_p(IPv4Network("224.0.0.0/4"))


def test_ipv4_network_is_private():
    assert not is_ipv4_network_private_p(IPv4Network("100.64.0.0/10"))
    assert is_ipv4_network_private_p(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_loopback():
    assert is_ipv4_network_loopback_p(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_reserved():
    assert is_ipv4_network_reserved_p(IPv4Network("240.0.0.0/4"))
    assert not is_ipv4_network_reserved_p(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_link_local():
    assert is_ipv4_network_link_local_p(IPv4Network("169.254.0.0/16"))
    assert not is_ipv4_network_link_local_p(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_unspecified():
    assert not is_ipv4_network_unspecified_p(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_subnet_of():
    predicate = subnet_of_p(IPv4Network("192.168.1.0/24"))

    assert predicate(IPv4Network("192.168.1.128/30"))


def test_ipv4_network_is_supernet_of():
    predicate = supernet_of_p(IPv4Network("192.168.1.128/30"))

    assert predicate(IPv4Network("192.168.1.0/24"))
