import pytest


def test_head_hunter_api(head_hunter_api):
    with pytest.raises(AttributeError):
        a = head_hunter_api.url
        print(a)