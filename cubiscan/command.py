# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
"""Defines a Registry for Commands and their Responses."""

from cubiscan import base_responses

COMMAND_REGISTRY = None


class CommandRegistry(object):

    command_bits = None
    response_mappings = None

    def __init__(self):
        self.command_bits = {}
        self.response_mappings = {}
        self.init_base_mappings()

    def init_base_mappings(self):
        """Register the base commands."""
        self.add_command(
            'continous_measure', bytes('C', 'ascii'),
            base_responses.MEASURE, base_responses.NEG_MEASURE
        )
        self.add_command(
            'dim_calibration', bytes('D', 'ascii'),
            base_responses.DIM_CALIBRATION, []
        )
        self.add_command('dim_unit', bytes('"', 'ascii'), [], [])
        self.add_command('set_factor', bytes('F', 'ascii'), [], [])
        self.add_command('location', bytes('L', 'ascii'), [], [])
        self.add_command(
            'measure', bytes('M', 'ascii'),
            base_responses.MEASURE, base_responses.NEG_MEASURE
        )
        self.add_command(
            'weight_calibration', bytes('S', 'ascii'),
            base_responses.WEIGHT_CALIBRATION, []
        )
        self.add_command(
            'test', bytes('T', 'ascii'), base_responses.TEST, []
        )
        self.add_command(
            'units', bytes('U', 'ascii'), base_responses.REPORT_UNITS, []
        )
        self.add_command('weight_unit', bytes('#', 'ascii'), [], [])
        self.add_command('zero', bytes('Z', 'ascii'), [], [])

    def add_command(self, name, command_bit, response, neg_response):
        """
        Add the bit inidicating the command the positive response and the
        negative response to the dicts.
        """
        self.command_bits[name] = command_bit
        self.response_mappings[name] = (response, neg_response)

    def build_command_string(self, name, params=None):
        """Wrap command and params with the base stuff arround it.
        """
        # All commands always have the following format
        # <STX><COMMAND><DATA><ETX><CR><LF>
        # STX = start of text
        # Command = The command you want to execute usually one ascii char
        # Data = Additional data required but in a lot of cases this isnt given
        # ETX = end of text
        # CR = Carriage return
        # LF = Line Feed

        byte = self.command_bits[name]
        command = bytes.fromhex('02') + byte
        if params:
            command += params
        command += bytes.fromhex('030D0A')
        return command

    def get_response_for(self, name):
        """Get the Responses for a command and append the prefix and suffix."""
        specific_resp, specific_neg_resp = \
            self.response_mappings.get(name, ([], []))
        complete_resp = (base_responses.PREFIX +
                         specific_resp + base_responses.SUFIX)
        complete_neg_resp = (base_responses.PREFIX +
                             specific_neg_resp + base_responses.SUFIX)

        return (complete_resp, complete_neg_resp)


def get_command_registry():
    """
    Get the registry and always return same instance to allow for extension.
    """
    global COMMAND_REGISTRY
    if not COMMAND_REGISTRY:
        COMMAND_REGISTRY = CommandRegistry()
    return COMMAND_REGISTRY
