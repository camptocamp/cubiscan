CUBISCAN
========

Provides an interface to a cubiscan devices (https://cubiscan.com/).
These devices are used to measure and weigh objects. 

Usage
-----

``
from cubiscan.cubiscan import CubiScan


obj = CubiScan(ip, port, timeout=timeout)

obj.measure()
``

Functions
---------

Following Functions of a Cubiscan are covered:

- Continuous measure
- Dimension calibration
- Dimension units
- Factor Toggle
- Location/City id
- Measure
- Scale calibration
- Test
- Units
- Weight units
- Zero
- 
