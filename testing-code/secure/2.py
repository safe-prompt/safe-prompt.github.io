import yaml
import pytest

def test_safe_yaml_load():
    unsafe_yaml = "!!python/object/apply:os.system ['echo unsafe']"
    with pytest.raises(yaml.constructor.ConstructorError):
        yaml.safe_load(unsafe_yaml)
    safe_yaml = "a: 1\nb: 2"
    data = yaml.safe_load(safe_yaml)
    assert data == {'a': 1, 'b': 2}
