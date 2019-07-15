# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from cubiscan.command import get_command_registry


def test_command_string_without_param():
    registry = get_command_registry()
    command = registry.build_command_string('continous_measure')
    assert command == bytes('\x02C\x03\x0D\x0A', 'ascii')


def test_command_string_with_param():
    registry = get_command_registry()
    command = registry.build_command_string('dim_unit', bytes('M', 'ascii'))
    assert command == bytes('\x02"M\x03\x0D\x0A', 'ascii')
