from typing import List
from xml.etree import ElementTree
import requests
from . import exceptions, models
from .i18n import _


class PriceCalculator:
    """
    https://www.usps.com/business/web-tools-apis/rate-calculator-api_files/rate-calculator-api.htm
    """

    @staticmethod
    def _get_api_url():
        """
        API Signature: https://www.usps.com/business/web-tools-apis/rate-calculator-api_files/rate-calculator-api.htm#_Toc57794294
        :param api:
        :param xml:
        :return:
        """
        return 'https://secure.shippingapis.com/ShippingAPI.dll'

    @staticmethod
    def get_package_services(api_user_id, package: models.Package) -> models.PackageServices:
        """
        :param api_user_id:
        :param package:
        :return:
        :raise ConnectionFail: Erro de conexão.
        :raise XmlLoadError: Não foi possível instanciar o JSON da resposta.
        :raise XmlResponseError: Resposta não retornou um JSON válido.
        :raise Timeout: Requisição demorou muito para responder.
        :raise ValidationError: Erro de validação.
        """
        return PriceCalculator.get_packages_services(api_user_id, [package])[0]

    @staticmethod
    def get_packages_services(api_user_id, packages: List[models.Package]) -> List[models.PackageServices]:
        """
        :return:
        """
        result = []
        domestic_packages = []
        international_packages = []

        for package in packages:

            error = package.validate()
            if error:
                result.append(models.PackageServices(package=package, error_message=str(error), error_dict=error))
                continue
            if package.check_is_domestic_shipping():
                domestic_packages.append(package)
            else:
                international_packages.append(package)
        if domestic_packages:
            result += PriceCalculator.get_domestic_packages_services(api_user_id, domestic_packages)
        if international_packages:
            result += PriceCalculator.get_international_packages_services(api_user_id, international_packages)
        return result

    @staticmethod
    def get_domestic_packages_services(api_user_id, packages: List[models.Package]) -> List[models.PackageServices]:
        """
        USPS Domestic Price Calculator API (RateV4): https://www.usps.com/business/web-tools-apis/rate-calculator-api.htm#_Toc487632557
        Domestic freight means package sent to United State.
        :param api_user_id:
        :param packages:
        :return:
        """
        xml_data = PriceCalculator.get_xml_domestic(api_user_id, packages)
        try:
            response = requests.post(PriceCalculator._get_api_url(), data={'API': 'RateV4', 'XML': xml_data})
        except requests.exceptions.Timeout as e:
            raise exceptions.Timeout(origin=e)
        except requests.exceptions.ConnectionError as e:
            raise exceptions.ConnectionFail(origin=e)
        try:
            xml_root = ElementTree.fromstring(response.content)
        except ValueError as e:
            raise exceptions.XmlResponseError(origin=e)
        if not response.ok:
            raise exceptions.ValidationError(_("Fail to get USPS domestic freight."))
        if xml_root.tag == 'Error':
            raise exceptions.ValidationError(xml_root.find('Description').text)
        result = []
        for pack in xml_root:

            package = next(filter(lambda item: item.unique_id == int(pack.attrib['ID']), packages))
            services = []

            error = pack.find('Error')
            if error is not None:
                if error.find('Number').text == '-2147219497':
                    result.append(models.PackageServices(package=package, error_message=_("Please enter a valid ZIP Code for the destination.")))
                if error.find('Number').text == '-2147219385':
                    result.append(models.PackageServices(package=package, error_message=_("The entered weight must be less than 16 ounces.")))
                else:
                    result.append(models.PackageServices(package=package, error_message=error.find('Description').text))
                    continue
            for pack_service in pack.findall('Postage'):
                try:
                    class_id = int(pack_service.attrib['CLASSID'])
                    services.append(models.Service.get_instance({
                        'unique_id': class_id,
                        'name': pack_service.find('MailService').text,
                        'is_international': False,
                        'rate': pack_service.find('Rate').text,
                    }))
                except ValueError as e:
                    raise exceptions.XmlLoadError(origin=e)
            result.append(models.PackageServices(
                package=package,
                # Sort by increasing rate
                services=sorted(services, key=lambda service: service.rate),
            ))
        return result

    @staticmethod
    def get_xml_domestic(api_user_id, packages: List[models.Package]):
        xml_packages = ''
        for package in packages:
            xml_packages += PriceCalculator.generate_xml_domestic_package(package)
        return """
            <RateV4Request USERID="{api_user_id}">
                <Revision>2</Revision>
                {xml_packages}
            </RateV4Request>
        """.format(api_user_id=api_user_id, xml_packages=xml_packages)

    @staticmethod
    def generate_xml_domestic_package(package: models.Package):
        return """
            <Package ID="{package.unique_id}">
                <Service>ALL</Service>
                <ZipOrigination>{package.zip_origination}</ZipOrigination>
                <ZipDestination>{package.zip_destination}</ZipDestination>
                <Pounds>{package.weight}</Pounds>
                <Ounces>0</Ounces>
                <Container>RECTANGULAR</Container>
                <Size>LARGE</Size>
                <Width>{package.width}</Width>
                <Length>{package.length}</Length>
                <Height>{package.height}</Height>
                <Machinable>true</Machinable>
            </Package>
        """.format(package=package)

    @staticmethod
    def get_international_packages_services(api_user_id, packages: List[models.Package]) -> List[models.PackageServices]:
        """
        USPS International Price Calculator API (IntlRateV2):
        https://www.usps.com/business/web-tools-apis/rate-calculator-api_files/rate-calculator-api.htm#_Toc57794292

        International freight means package sent to outside United State.
        :return:
        """
        xml_data = PriceCalculator.get_xml_international(api_user_id, packages)
        try:
            response = requests.post(PriceCalculator._get_api_url(), data={'API': 'IntlRateV2', 'XML': xml_data})
        except requests.exceptions.Timeout as e:
            raise exceptions.Timeout(origin=e)
        except requests.exceptions.ConnectionError as e:
            raise exceptions.ConnectionFail(origin=e)
        try:
            xml_root = ElementTree.fromstring(response.content)
        except ValueError as e:
            raise exceptions.XmlResponseError(origin=e)
        if not response.ok:
            raise exceptions.ValidationError(_("Fail to get USPS international freight."))
        if xml_root.tag == 'Error':
            raise exceptions.ValidationError(xml_root.find('Description').text)
        result = []
        for pack in xml_root:

            package = next(filter(lambda item: item.unique_id == int(pack.attrib['ID']), packages))
            services = []

            error = pack.find('Error')
            if error is not None:
                result.append(models.PackageServices(package=package, error_message=error.find('Description').text))
                continue
            for pack_service in pack.findall('Service'):
                extra_services = []
                for extra_services_root in pack_service.findall('ExtraServices'):
                    for extra_service in extra_services_root.findall('ExtraService'):
                        extra_services.append({
                            'unique_id': int(extra_service.find('ServiceID').text),
                            'name': extra_service.find('ServiceName').text,
                            'available': extra_service.find('Available').text,
                            'price': extra_service.find('Price').text,
                        })
                try:
                    service_id = int(pack_service.attrib['ID'])
                    services.append(models.Service.get_instance({
                        'unique_id': service_id,
                        'name': pack_service.find('SvcDescription').text,
                        'rate': pack_service.find('Postage').text,
                        'is_international': True,
                        'extra_services': extra_services,
                    }))
                except ValueError as e:
                    raise exceptions.XmlLoadError(origin=e)
            result.append(models.PackageServices(
                package=package,
                # Sort by increasing rate
                services=sorted(services, key=lambda service: service.rate),
            ))
        return result

    @staticmethod
    def get_xml_international(api_user_id, packages: List[models.Package]):
        xml_packages = ''
        for package in packages:
            xml_packages += PriceCalculator.generate_xml_international_package(package)
        return """
            <IntlRateV2Request USERID="{api_user_id}">
                <Revision>2</Revision>
                {xml_packages}
            </IntlRateV2Request>
        """.format(api_user_id=api_user_id, xml_packages=xml_packages)

    @staticmethod
    def generate_xml_international_package(package: models.Package):
        """
        :param package:
        :return:
        """
        result = """
            <Package ID="{package.unique_id}">
                <Pounds>{package.weight}</Pounds>
                <Ounces>0</Ounces>
                <Machinable>True</Machinable>
                <MailType>Package</MailType>
                <GXG>
                <POBoxFlag>Y</POBoxFlag>
                <GiftFlag>Y</GiftFlag>
                </GXG>
                <ValueOfContents>{package.value_of_contents}</ValueOfContents>
                <Country>{package.country}</Country>
                <Container>RECTANGULAR</Container>
                <Size>LARGE</Size>
                <Width>{package.width}</Width>
                <Length>{package.length}</Length>
                <Height>{package.height}</Height>
                <Girth>0</Girth>
                <OriginZip>{package.origin_zip}</OriginZip>
                <CommercialFlag>N</CommercialFlag>
        """.format(package=package)
        if package.acceptance_date_time and package.destination_postal_code:
            result += """
                <AcceptanceDateTime>{acceptance_date_time}</AcceptanceDateTime>
            """.format(acceptance_date_time=package.acceptance_date_time.replace(microsecond=0).isoformat())
        if package.destination_postal_code:
            result += """
                <DestinationPostalCode>{package.destination_postal_code}</DestinationPostalCode>
            """.format(package=package)
        return result + """
            </Package>
        """
