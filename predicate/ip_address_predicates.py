from ipaddress import IPv4Network

from predicate.property_predicate import PropertyPredicate

is_global = PropertyPredicate(getter=IPv4Network.is_global)
is_multicast = PropertyPredicate(getter=IPv4Network.is_multicast)
is_private = PropertyPredicate(getter=IPv4Network.is_private)
is_loopback = PropertyPredicate(getter=IPv4Network.is_loopback)
is_reserved = PropertyPredicate(getter=IPv4Network.is_reserved)
is_link_local = PropertyPredicate(getter=IPv4Network.is_link_local)
is_unspecified = PropertyPredicate(getter=IPv4Network.is_unspecified)
