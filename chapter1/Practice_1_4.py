# Section 1.4.1


def pressure(v, t, n):
    """Compute the pressure in pascals of an ideal gas.

    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v


help(pressure)
# Help on function pressure in module __main__:
#
# pressure(v, t, n)
#     Compute the pressure in pascals of an ideal gas.
#    
#     Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law
#    
#     v -- volume of gas, in cubic meters
#     t -- absolute temperature in degrees kelvin
#     n -- particles of gas

# Section 1.4.2


def pressure(v, t, n=6.023e23):
    """Compute the pressure in pascals of an ideal gas.

    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    >>> pressure(1, 273, 1)
    273.0
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v


pressure(1, 273.15)
# 2270.351781

pressure(1, 273.15, 3 * 6.023e23)
# 6811.055342999999
