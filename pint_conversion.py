
#! Have to run pint module from a pipenv shell command line in this case it is python3 pint_convsersion.py
import pint

ureg = pint.UnitRegistry()

result = 3 * ureg.meter + 4 * ureg.centimeter

print(result)
print(result.to(ureg.meter))
print(result.to(ureg.centimeter))