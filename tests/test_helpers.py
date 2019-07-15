# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from cubiscan import helpers


def test_decode():
    res = helpers.decode(bytes('TEST', 'ascii'))
    assert isinstance(res, str)


def test_base_extract():
    res = helpers.base_extract(bytes('L0323', 'ascii'))
    assert res[0] == '0323'
    assert res[1] is None

    res = helpers.base_extract(bytes('L-0323', 'ascii'))
    assert res[0] == '0323'
    assert res[1] == 'low_precision'

    res = helpers.base_extract(bytes('L_0323', 'ascii'))
    assert res[0] == '0323'
    assert res[1] == 'low'

    res = helpers.base_extract(bytes('L~0323', 'ascii'))
    assert res[0] == '0323'
    assert res[1] == 'over'


def test_dim_to_bool():
    res = helpers.dim_to_bool(bytes('E', 'ascii'))
    assert not res

    res = helpers.dim_to_bool(bytes('M', 'ascii'))
    assert res


def test_extract_factor():
    res = helpers.extract_factor(bytes('L0323', 'ascii'))
    assert res == 323


def test_extract_measure():
    res = helpers.extract_measure(bytes('L03.23', 'ascii'))
    assert res[0] == 3.23


def test_dom_intl_to_bool():
    res = helpers.dom_intl_to_bool(bytes('I', 'ascii'))
    assert res is True

    res = helpers.dom_intl_to_bool(bytes('F', 'ascii'))
    assert res is False


def test_get_error():
    res = helpers.get_error(bytes('C', 'ascii'))
    assert res == 'corner_sensor'

    res = helpers.get_error(bytes('M', 'ascii'))
    assert res == 'measure_error'

    res = helpers.get_error(bytes('Z', 'ascii'))
    assert res == 'zeroing_error'


def test_ack_to_bool():
    res = helpers.ack_to_bool(bytes('A', 'ascii'))
    assert res is True

    res = helpers.ack_to_bool(bytes('N', 'ascii'))
    assert res is False
