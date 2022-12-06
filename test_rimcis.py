"""
Rimcis related testing.

This file's goal is to always ensure proper results, and to create
a warning when these results deviate from expectations.
"""
from rimcis import convert_num_to_rn
from rimcis import convert_rn_to_num
from rimcis import generate_result
import pytest


def test_rimcis():
    """
    Test use cases and edge cases of rimcis.

    Tests that the possible cases, that can arise while using rimcis,
    always return correct values.
    """
    # Expected results of generate_result
    assert generate_result('XVI') == 16
    assert generate_result('16') == 'XVI'

    # Expected results of convert_num_to_rn
    assert convert_num_to_rn(1) == 'I'
    assert convert_num_to_rn(10) == 'X'
    assert convert_num_to_rn(1000) == 'M'
    assert convert_num_to_rn(3999) == 'MMMCMXCIX'
    assert convert_num_to_rn(36) == 'XXXVI'
    assert convert_num_to_rn(254) == 'CCLIV'
    assert convert_num_to_rn(1847) == 'MDCCCXLVII'
    assert convert_num_to_rn(2840) == 'MMDCCCXL'

    # Expected results of convert_rn_to_num
    assert convert_rn_to_num('I') == 1
    assert convert_rn_to_num('X') == 10
    assert convert_rn_to_num('M') == 1000
    assert convert_rn_to_num('MMMCMXCIX') == 3999
    assert convert_rn_to_num('LXVIII') == 68
    assert convert_rn_to_num('CMXCIX') == 999
    assert convert_rn_to_num('MCMLXXXIV') == 1984
    assert convert_rn_to_num('MMMDXLVIII') == 3548

    # Possible raised TypeErrors
    with pytest.raises(TypeError):
        generate_result(16)
        generate_result(True)

    # Possible raised ValueErrors
    with pytest.raises(ValueError):
        generate_result('IV80_plus3')
        generate_result('MM10001000CCM')
