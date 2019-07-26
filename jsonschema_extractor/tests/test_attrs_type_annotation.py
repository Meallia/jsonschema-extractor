import attr
from typing import Optional


@attr.s
class Example_explicit(object):
    integer = attr.ib(type=int)
    optional = attr.ib(type=Optional[str])
    string = attr.ib(type=str, default="foo")
    
@attr.s
class Example_implicit(object):
    integer : int = attr.ib()
    optional : Optional[str]  = attr.ib()
    string : str = attr.ib(default="foo")

@pytest.mark.parametrized("example_class", [Example_explicit, Example_implicit])
def test_extract_cattrs(extractor, example_class):
    assert extractor.extract(example_class) == {
        "type": "object",
        "title": example_class.__name__,
        "properties": {
            "string": {"type": "string"},
            "integer": {"type": "integer"},
            "optional": {"anyOf":
                [
                    {"type": "string"},
                    {"type": "null"}
                ]
            }
        },
        "required": ["integer", "optional"]
    }
