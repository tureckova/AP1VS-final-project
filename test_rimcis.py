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
    assert convert_num_to_rn(5) == 'V'
    assert convert_num_to_rn(10) == 'X'
    assert convert_num_to_rn(50) == 'L'
    assert convert_num_to_rn(100) == 'C'
    assert convert_num_to_rn(500) == 'D'
    assert convert_num_to_rn(1000) == 'M'
    assert convert_num_to_rn(3999) == 'MMMCMXCIX'
    assert convert_num_to_rn(36) == 'XXXVI'
    assert convert_num_to_rn(254) == 'CCLIV'
    assert convert_num_to_rn(1847) == 'MDCCCXLVII'
    assert convert_num_to_rn(2840) == 'MMDCCCXL'

    # Expected results of convert_rn_to_num
    assert convert_rn_to_num('I') == 1
    assert convert_rn_to_num('V') == 5
    assert convert_rn_to_num('X') == 10
    assert convert_rn_to_num('L') == 50
    assert convert_rn_to_num('C') == 100
    assert convert_rn_to_num('D') == 500
    assert convert_rn_to_num('M') == 1000
    assert convert_rn_to_num('MMMCMXCIX') == 3999
    assert convert_rn_to_num('LXVIII') == 68
    assert convert_rn_to_num('CMXCIX') == 999
    assert convert_rn_to_num('MCMLXXXIV') == 1984
    assert convert_rn_to_num('MMMDXLVIII') == 3548

    # Possible raised TypeErrors
    with pytest.raises(TypeError):
        generate_result(16)

    with pytest.raises(TypeError):
        generate_result(True)

    with pytest.raises(TypeError):
        convert_num_to_rn(150.15)

    with pytest.raises(TypeError):
        convert_num_to_rn(False)

    with pytest.raises(TypeError):
        convert_num_to_rn([20, 190, 708])

    with pytest.raises(TypeError):
        convert_rn_to_num(500)

    with pytest.raises(TypeError):
        convert_rn_to_num(True)

    with pytest.raises(TypeError):
        convert_rn_to_num(['XXI', 'MCIV', 'DCC'])

    # Possible raised ValueErrors
    with pytest.raises(ValueError):
        generate_result('IV80_plus3')

    with pytest.raises(ValueError):
        generate_result('MM10001000CCM')

    with pytest.raises(ValueError):
        convert_num_to_rn(4000)

    with pytest.raises(ValueError):
        convert_num_to_rn(0)

    with pytest.raises(ValueError):
        convert_rn_to_num('MMCBXIAA')  # Vstup obsahuje ne-římské číslice

    with pytest.raises(ValueError):
        convert_rn_to_num('MCXXXXIV')  # > 3x Opakující se symboly

    with pytest.raises(ValueError):
        convert_rn_to_num('MDDLVII')  # Opakující se pětkové symboly

    with pytest.raises(ValueError):
        convert_rn_to_num('CIXXVII')  # Opakování po předponě
        
    with pytest.raises(ValueError):
        convert_rn_to_num('MCMCMXIV')  # Opakování po předponě

    with pytest.raises(ValueError):
        convert_rn_to_num('IXII')  # Ostatní chyby

    with pytest.raises(ValueError):
        convert_rn_to_num('XDMCL')  # Špatné seřazení
