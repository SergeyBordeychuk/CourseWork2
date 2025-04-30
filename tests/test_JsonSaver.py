import pytest


def test_json_saver(json_saver):
    with pytest.raises(AttributeError):
        a = json_saver.file_name
        print(a)