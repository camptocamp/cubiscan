# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
"""Contains Base Response definitions as expected by the cubiscan."""

from cubiscan import helpers

PREFIX = [

    {'key': 'start', 'length': 1, 'converter': None},
    {'key': 'command', 'length': 1, 'converter': helpers.decode},
    {'key': 'acknowledge', 'length': 1, 'converter': helpers.ack_to_bool},

]

SUFIX = [
    {'key': 'end', 'length': 1, 'converter': None},
    {'key': 'cr', 'length': 1, 'converter': None},
    {'key': 'lf', 'length': 1, 'converter': None}
]

MEASURE = [
    {'key': 'origin', 'length': 1, 'converter': helpers.decode},
    {'key': 'location', 'length': 6, 'converter': helpers.decode},
    {'key': 'length', 'length': 6, 'converter': helpers.extract_measure},
    {'key': 'width', 'length': 6, 'converter': helpers.extract_measure},
    {'key': 'height', 'length': 6, 'converter': helpers.extract_measure},
    {'key': 'space_metric', 'length': 1, 'converter': helpers.dim_to_bool},
    {'key': 'weight', 'length': 7, 'converter': helpers.extract_measure},
    {'key': 'dim_weight', 'length': 7, 'converter': helpers.extract_measure},
    {'key': 'weight_metric', 'length': 1, 'converter': helpers.dim_to_bool},
    {'key': 'factor', 'length': 5, 'converter': helpers.extract_factor},
    {'key': 'intl_unit', 'length': 1, 'converter': helpers.dom_intl_to_bool},
]
NEG_MEASURE = [
    {'key': 'origin', 'length': 1, 'converter': helpers.decode},
    {'key': 'error', 'length': 1, 'converter': helpers.get_error},
]

DIM_CALIBRATION = [
    {'key': 'identifier', 'length': 2, 'converter': int},
]

WEIGHT_CALIBRATION = [
    {'key': 'identifier', 'length': 2, 'converter': int},
]

TEST = [
    {'key': 'identifier', 'length': 2, 'converter': int},
]

REPORT_UNITS = [
    {'key': 'space_metric', 'length': 1, 'converter': helpers.dim_to_bool},
    {'key': 'weight_metric', 'length': 1, 'converter': helpers.dim_to_bool},
    {'key': 'intl_unit', 'length': 1, 'converter': helpers.dom_intl_to_bool},
    {'key': 'factor', 'length': 4, 'converter': int},
    {'key': 'location', 'length': 6, 'converter': helpers.decode},
]
