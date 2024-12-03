from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network

from predicate import FnPredicate
from predicate.predicate import Predicate
from predicate.property_predicate import PropertyPredicate

is_ipv4_address_global_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_global)
is_ipv4_address_multicast_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_multicast)
is_ipv4_address_private_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_private)
is_ipv4_address_loopback_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_loopback)
is_ipv4_address_reserved_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_reserved)
is_ipv4_address_link_local_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_link_local)
is_ipv4_address_unspecified_p: Predicate[IPv4Address] = PropertyPredicate(getter=IPv4Address.is_unspecified)

is_ipv6_address_global_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_global)
is_ipv6_address_multicast_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_multicast)
is_ipv6_address_private_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_private)
is_ipv6_address_loopback_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_loopback)
is_ipv6_address_reserved_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_reserved)
is_ipv6_address_link_local_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_link_local)
is_ipv6_address_unspecified_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_unspecified)
is_ipv6_address_site_local_p: Predicate[IPv6Address] = PropertyPredicate(getter=IPv6Address.is_site_local)

is_ipv4_global_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_global)
is_ipv4_multicast_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_multicast)
is_ipv4_private_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_private)
is_ipv4_loopback_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_loopback)
is_ipv4_reserved_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_reserved)
is_ipv4_link_local_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_link_local)
is_ipv4_unspecified_p: Predicate[IPv4Network] = PropertyPredicate(getter=IPv4Network.is_unspecified)

is_ipv6_global_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_global)
is_ipv6_multicast_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_multicast)
is_ipv6_private_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_private)
is_ipv6_loopback_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_loopback)
is_ipv6_reserved_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_reserved)
is_ipv6_link_local_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_link_local)
is_ipv6_unspecified_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_unspecified)
is_ipv6_site_local_p: Predicate[IPv6Network] = PropertyPredicate(getter=IPv6Network.is_site_local)


def subnet_of_p(value: IPv4Network | IPv6Network) -> Predicate[IPv4Network | IPv6Network]:
    return FnPredicate(lambda network: network.subnet_of(value))  # type: ignore


def supernet_of_p(value: IPv4Network | IPv6Network) -> Predicate[IPv4Network | IPv6Network]:
    return FnPredicate(lambda network: network.supernet_of(value))  # type: ignore
