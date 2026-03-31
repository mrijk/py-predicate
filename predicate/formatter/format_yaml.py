import yaml

from predicate.formatter.format_json import to_json
from predicate.predicate import Predicate


def to_yaml(predicate: Predicate) -> str:
    """Format predicate as yaml."""
    return yaml.dump(to_json(predicate), default_flow_style=False)
