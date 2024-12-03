from ipaddress import IPv4Network

from predicate.ip_address_predicates import (
    is_global,
    is_link_local,
    is_loopback,
    is_multicast,
    is_private,
    is_reserved,
    is_unspecified,
)


def test_ipv4_network_is_global():
    assert not is_global(IPv4Network("100.64.0.0/10"))
    assert not is_global(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_multicast():
    assert not is_multicast(IPv4Network("127.0.0.0/29"))
    assert is_multicast(IPv4Network("224.0.0.0/4"))


def test_ipv4_network_is_private():
    assert not is_private(IPv4Network("100.64.0.0/10"))
    assert is_private(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_loopback():
    assert is_loopback(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_reserved():
    assert is_reserved(IPv4Network("240.0.0.0/4"))
    assert not is_reserved(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_link_local():
    assert is_link_local(IPv4Network("169.254.0.0/16"))
    assert not is_link_local(IPv4Network("127.0.0.0/29"))


def test_ipv4_network_is_unspecified():
    assert not is_unspecified(IPv4Network("127.0.0.0/29"))
