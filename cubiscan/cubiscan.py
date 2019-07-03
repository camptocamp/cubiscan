# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

import socket

from cubiscan.command import get_command_registry

EXCLUDED = ['start', 'end', 'cr', 'lf']


class CubiScan(object):

    ip_address = None
    port = None
    timeout = None

    def __init__(self, ip_address, port, timeout=30):
        self.ip_address = ip_address
        self.port = port
        self.timeout = timeout

    def _make_request(self, command, param=None):
        command_string = get_command_registry().build_command_string(
            command, param
        )
        conn = socket.create_connection((self.ip_address, self.port))
        conn.send(command_string)
        conn.settimeout(self.timeout)
        try:
            data = conn.recv()
        finally:
            conn.close()
        return self._parse_response(data)

    def _parse_response(self, command, data):
        mapping, neg_mapping = get_command_registry().get_response_for(command)
        used_map = mapping
        index = 0
        res_dict = {}
        sections = data.split(bytes(',', 'ascii'))
        for section in sections:
            start = 0
            while start < len(section):
                key = used_map[index]['key']
                length = used_map[index]['length']
                converter = used_map[index]['converter']
                if key in EXCLUDED:
                    start += length
                    index += 1
                    continue
                end = start + length
                value = section[start:end]
                res_dict[key] = converter(value) if converter else value
                start = end
                index += 1
                if key == 'acknowledge' and not res_dict[key]:
                    used_map = neg_mapping
        return res_dict

    def continuous_measure(self):
        return self._make_request('continous_measure')

    def calibrate_dimension(self):
        return self._make_request('dim_calibration')

    def set_dimension_unit(self, metric=True):
        param = None
        if metric:
            param = bytes('M', 'ascii')
        else:
            param = bytes('E', 'ascii')
        return self._make_request('dim_unit', param)

    def set_factor(self, intl=True):
        param = None
        if intl:
            param = bytes('I', 'ascii')
        else:
            param = bytes('D', 'ascii')
        return self._make_request('set_factor', param)

    def set_location(self, location):
        if len(location) < 6:
            location = ' ' * (6 - len(location)) + location
        return self._make_request('location', location)

    def measure(self):
        return self._make_request('measure')

    def calibrate_scale(self, weight):
        if not weight > 50 and weight < 100:
            raise ValueError(
                "Weight is not in specified range for calibration"
            )
        value = format(weight, '.2f')
        if len(value) < 6:
            value = '0' * (6 - len(value)) + value
        return self._make_request('weight_calibration', value)

    def test(self):
        return self._make_request('test')

    def report_units(self):
        return self._make_request('units')

    def set_weight_units(self, metric=True):
        param = None
        if metric:
            param = bytes('M', 'ascii')
        else:
            param = bytes('E', 'ascii')
        return self._make_request('weight_unit', param)

    def zero(self):
        self._make_request('zero')
