# Python USPS API Tools

This project is a Python implementation of [USPS API Tools](https://www.usps.com/business/web-tools-apis/documentation-updates.htm).

Implemented in this library:

  - [Price Calculator APIs](https://www.usps.com/business/web-tools-apis/rate-calculator-api_files/rate-calculator-api.htm) (_Domestic Price Calculator_ and _International Price Calculator_)

Only a portion of the USPS API has been implemented. Contributions are welcome.

# Installation

Download these sources into your project, then:

```shell
pip install ./usps-tools
```

Or install directly into your project (note to update the tag reference, in this case `0.1.0`):

```shell
pip install git+https://github.com/pedrovagner/usps-tools@0.1.0#egg=usps-tools
```

# Usage

```python
import usps_tools as usps

usps_user_id = '<user id here>'
```

International freight:

```python
# Create a package
package = usps.Package(
    unique_id=1,
    weight=1,
    width=1,
    length=1,
    height=1,
    value_of_contents=1,
    country='Brazil',
    origin_zip='33337',
)

# Convert to dict
package_dict = package.to_dict()

# Creating a package from dict (and validate)
try:
    package = usps.Package.get_instance(package_dict)
except usps.ValidationError as e:
    print(e.origin.messages)

try:
    package_services = usps.PriceCalculator.get_package_services(usps_user_id, package)
except usps.ConnectionFail as e:
    # Catch only connection error
    print(e)
    raise e
except usps.Timeout as e:
    # Catch only timeout connection error
    print(e)
    raise e
except usps.XmlLoadError as e:
    # Catch only xml parse error
    print(e)
    raise e
except usps.XmlResponseError as e:
    # Catch only xml response error
    print(e)
    raise e
except usps.UspsToolsException as e:
    # Catch any error
    print(e)
    raise e

if package_services.error_message:
    print(package_services.error_message)
    print(package_services.error_dict)

for service in package_services.services:
    print(service.name, service.rate)
```

Domestic freight:

```python
# Create a package
package = usps.Package(
    unique_id=1,
    weight=1,
    width=1,
    length=1,
    height=1,
    value_of_contents=1,
    country='United States',
    zip_origination='33337',
    zip_destination='19716',
)

try:
    package_services = usps.PriceCalculator.get_package_services(usps_user_id, package)
except usps.UspsToolsException as e:
    # Catch any error
    print(e)
    raise e

if package_services.error_message:
    print(package_services.error_message)
    print(package_services.error_dict)

for service in package_services.services:
    print(service.name, service.rate)
```

# Translation

Update translation files (development purposes only):

```shell
pip install Babel

python setup.py extract_messages
# Execute when creating a new language translation directory
# python setup.py init_catalog --locale pt_BR
python setup.py update_catalog
python setup.py compile_catalog
```

# Contribution

Any contribution are welcome. This project follows [Semantic Versioning](https://semver.org/).

# License

See the [LICENSE](./LICENSE.md) file for license rights and limitations (MIT).
