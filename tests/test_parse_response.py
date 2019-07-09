# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
import pytest

from cubiscan.cubiscan import CubiScan

# This only tests the parsing of the Response.
# We dont check the actual connection.


@pytest.fixture(scope="module")
def scanner_obj():
    return CubiScan('127.0.0.1', '1234')


def test_parse_positive_measure_response(scanner_obj):
    response_msg = bytes('\x02MAC004600,L020.0,W010.0,H030.0,'
                         'M,K500.50,D510.50,M,F0010,I\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('continous_measure', response_msg)
    assert response['command'] == 'M'
    assert response['acknowledge'] is True
    assert response['origin'] == 'C'
    assert response['location'] == '004600'
    assert response['length'] == (20.0, None)
    assert response['width'] == (10.0, None)
    assert response['height'] == (30.0, None)
    assert response['space_metric'] is True
    assert response['weight'] == (500.50, None)
    assert response['dim_weight'] == (510.50, None)
    assert response['weight_metric'] is True
    assert response['factor'] == 10
    assert response['intl_unit'] is True


def test_parse_neg_measure_response(scanner_obj):
    response_msg = bytes('\x02MNCZ\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('continous_measure', response_msg)
    assert response['command'] == 'M'
    assert response['acknowledge'] is False
    assert response['origin'] == 'C'
    assert response['error'] == 'zeroing_error'


def test_parse_no_core_response(scanner_obj):
    response_msg = bytes('\x02FA\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('set_factor', response_msg)
    assert response['command'] == 'F'
    assert response['acknowledge'] is True


def test_parse_no_core_response_neg(scanner_obj):
    response_msg = bytes('\x02FN\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('set_factor', response_msg)
    assert response['command'] == 'F'
    assert response['acknowledge'] is False


def test_parse_dim_calibration(scanner_obj):
    response_msg = bytes('\x02DA42\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('dim_calibration', response_msg)
    assert response['command'] == 'D'
    assert response['acknowledge'] is True
    assert response['identifier'] == 42


def test_parse_weight_calibration(scanner_obj):
    response_msg = bytes('\x02SA42\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('weight_calibration', response_msg)
    assert response['command'] == 'S'
    assert response['acknowledge'] is True
    assert response['identifier'] == 42


def test_parse_test(scanner_obj):
    response_msg = bytes('\x02TA42\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('test', response_msg)
    assert response['command'] == 'T'
    assert response['acknowledge'] is True
    assert response['identifier'] == 42


def test_report_unit(scanner_obj):
    response_msg = bytes('\x02UAMMI0010004600\x03\x0D\x0A', 'ascii')
    response = scanner_obj._parse_response('units', response_msg)
    assert response['command'] == 'U'
    assert response['acknowledge'] is True
    assert response['space_metric'] is True
    assert response['weight_metric'] is True
    assert response['intl_unit'] is True
    assert response['location'] == '004600'
