from .. import code
import pytest

def test_get_name():
    with pytest.raises(ValueError) as e:
        code.get_name(None)
    assert str(e.value) == 'value is none'