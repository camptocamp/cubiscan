.. image:: https://travis-ci.com/camptocamp/cubiscan.svg?branch=master
    :target: https://travis-ci.com/camptocamp/cubiscan

CUBISCAN
========

Provides an interface to cubiscan devices (https://cubiscan.com/).
These devices are used to measure and weigh objects. 

Usage
-----

.. code:: python

  from cubiscan.cubiscan import CubiScan


  obj = CubiScan(ip, port, timeout=timeout)
  obj.measure()

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
