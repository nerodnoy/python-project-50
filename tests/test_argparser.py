import os


def test_help():
    exit_status = os.system('gendiff -h')
    assert exit_status == 0
