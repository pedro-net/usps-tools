# import enum


# @enum.unique
# class DomesticServiceName(enum.Enum):
#     """
#     RateV4 SERVICE ID values
#     https://www.usps.com/business/web-tools-apis/rate-calculator-api_files/rate-calculator-api.htm#_Toc57794300
#     """
#     FIRST_CLASS_MAIL_LETTER = 0
#     PRIORITY_MAIL = 1
#     PRIORITY_MAIL_EXPRESS_HOLD_FOR_PICKUP = 2
#     PRIORITY_MAIL_EXPRESS = 3
#     STANDARD_POST = 4
#     MEDIA_MAIL = 6
#     LIBRARY_MAIL = 7
#     PRIORITY_MAIL_EXPRESS_FLAT_RATE_ENVELOPE = 13
#     FIRST_CLASS_MAIL_LARGE_POSTCARDS = 15
#     PRIORITY_MAIL_FLAT_RATE_ENVELOPE = 16
#     PRIORITY_MAIL_MEDIUM_FLAT_RATE_BOX = 17
#     PRIORITY_MAIL_LARGE_FLAT_RATE_BOX = 22
#     PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY = 23
#     PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_FLAT_RATE_ENVELOPE = 25
#     PRIORITY_MAIL_EXPRESS_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 27
#     PRIORITY_MAIL_SMALL_FLAT_RATE_BOX = 28
#     PRIORITY_MAIL_PADDED_FLAT_RATE_ENVELOPE = 29
#     PRIORITY_MAIL_EXPRESS_LEGAL_FLAT_RATE_ENVELOPE = 30
#     PRIORITY_MAIL_EXPRESS_LEGAL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 31
#     PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_LEGAL_FLAT_RATE_ENVELOPE = 32
#     PRIORITY_MAIL_HOLD_FOR_PICKUP = 33
#     PRIORITY_MAIL_LARGE_FLAT_RATE_BOX_HOLD_FOR_PICKUP = 34
#     PRIORITY_MAIL_MEDIUM_FLAT_RATE_BOX_HOLD_FOR_PICKUP = 35
#     PRIORITY_MAIL_SMALL_FLAT_RATE_BOX_HOLD_FOR_PICKUP = 36
#     PRIORITY_MAIL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 37
#     PRIORITY_MAIL_GIFT_CARD_FLAT_RATE_ENVELOPE = 38
#     PRIORITY_MAIL_GIFT_CARD_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 39
#     PRIORITY_MAIL_WINDOW_FLAT_RATE_ENVELOPE = 40
#     PRIORITY_MAIL_WINDOW_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 41
#     PRIORITY_MAIL_SMALL_FLAT_RATE_ENVELOPE = 42
#     PRIORITY_MAIL_SMALL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 43
#     PRIORITY_MAIL_LEGAL_FLAT_RATE_ENVELOPE = 44
#     PRIORITY_MAIL_LEGAL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 45
#     PRIORITY_MAIL_PADDED_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 46
#     PRIORITY_MAIL_REGIONAL_RATE_BOX_A = 47
#     PRIORITY_MAIL_REGIONAL_RATE_BOX_A_HOLD_FOR_PICKUP = 48
#     PRIORITY_MAIL_REGIONAL_RATE_BOX_B = 49
#     PRIORITY_MAIL_REGIONAL_RATE_BOX_B_HOLD_FOR_PICKUP = 50
#     FIRST_CLASS_PACKAGE_SERVICE_HOLD_FOR_PICKUP = 53
#     PRIORITY_MAIL_EXPRESS_FLAT_RATE_BOXES = 55
#     PRIORITY_MAIL_EXPRESS_FLAT_RATE_BOXES_HOLD_FOR_PICKUP = 56
#     PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_FLAT_RATE_BOXES = 57
#     PRIORITY_MAIL_REGIONAL_RATE_BOX_C = 58
#     PRIORITY_MAIL_REGIONAL_RATE_BOX_C_HOLD_FOR_PICKUP = 59
#     FIRST_CLASS_PACKAGE_SERVICE = 61
#     PRIORITY_MAIL_EXPRESS_PADDED_FLAT_RATE_ENVELOPE = 62
#     PRIORITY_MAIL_EXPRESS_PADDED_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP = 63
#     PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_PADDED_FLAT_RATE_ENVELOPE = 64
#
#     def __init__(self, *args):
#         """
#         :param args:
#         """
#         display_name = {
#             'FIRST_CLASS_MAIL_LETTER': "First-Class Mail; Letter",
#             'PRIORITY_MAIL': "Priority Mail",
#             'PRIORITY_MAIL_EXPRESS_HOLD_FOR_PICKUP': "Priority Mail Express; Hold For Pickup",
#             'PRIORITY_MAIL_EXPRESS': "Priority Mail Express",
#             'STANDARD_POST': "Standard Post",
#             'MEDIA_MAIL': "Media Mail",
#             'LIBRARY_MAIL': "Library Mail",
#             'PRIORITY_MAIL_EXPRESS_FLAT_RATE_ENVELOPE': "Priority Mail Express; Flat Rate Envelope",
#             'FIRST_CLASS_MAIL_LARGE_POSTCARDS': "First-Class Mail; Large Postcards",
#             'PRIORITY_MAIL_FLAT_RATE_ENVELOPE': "Priority Mail; Flat Rate Envelope",
#             'PRIORITY_MAIL_MEDIUM_FLAT_RATE_BOX': "Priority Mail; Medium Flat Rate Box",
#             'PRIORITY_MAIL_LARGE_FLAT_RATE_BOX': "Priority Mail; Large Flat Rate Box",
#             'PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY': "Priority Mail Express; Sunday/Holiday Delivery",
#             'PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_FLAT_RATE_ENVELOPE': "Priority Mail Express; Sunday/Holiday Delivery Flat Rate Envelope",
#             'PRIORITY_MAIL_EXPRESS_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail Express; Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_SMALL_FLAT_RATE_BOX': "Priority Mail; Small Flat Rate Box",
#             'PRIORITY_MAIL_PADDED_FLAT_RATE_ENVELOPE': "Priority Mail; Padded Flat Rate Envelope",
#             'PRIORITY_MAIL_EXPRESS_LEGAL_FLAT_RATE_ENVELOPE': "Priority Mail Express; Legal Flat Rate Envelope",
#             'PRIORITY_MAIL_EXPRESS_LEGAL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail Express; Legal Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_LEGAL_FLAT_RATE_ENVELOPE':
#                 "Priority Mail Express; Sunday/Holiday Delivery Legal Flat Rate Envelope",
#             'PRIORITY_MAIL_HOLD_FOR_PICKUP': "Priority Mail; Hold For Pickup",
#             'PRIORITY_MAIL_LARGE_FLAT_RATE_BOX_HOLD_FOR_PICKUP': "Priority Mail; Large Flat Rate Box Hold For Pickup",
#             'PRIORITY_MAIL_MEDIUM_FLAT_RATE_BOX_HOLD_FOR_PICKUP': "Priority Mail; Medium Flat Rate Box Hold For Pickup",
#             'PRIORITY_MAIL_SMALL_FLAT_RATE_BOX_HOLD_FOR_PICKUP': "Priority Mail; Small Flat Rate Box Hold For Pickup",
#             'PRIORITY_MAIL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail; Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_GIFT_CARD_FLAT_RATE_ENVELOPE': "Priority Mail; Gift Card Flat Rate Envelope",
#             'PRIORITY_MAIL_GIFT_CARD_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail; Gift Card Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_WINDOW_FLAT_RATE_ENVELOPE': "Priority Mail; Window Flat Rate Envelope",
#             'PRIORITY_MAIL_WINDOW_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail; Window Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_SMALL_FLAT_RATE_ENVELOPE': "Priority Mail; Small Flat Rate Envelope",
#             'PRIORITY_MAIL_SMALL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail; Small Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_LEGAL_FLAT_RATE_ENVELOPE': "Priority Mail; Legal Flat Rate Envelope",
#             'PRIORITY_MAIL_LEGAL_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail; Legal Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_PADDED_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail; Padded Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_REGIONAL_RATE_BOX_A': "Priority Mail; Regional Rate Box A",
#             'PRIORITY_MAIL_REGIONAL_RATE_BOX_A_HOLD_FOR_PICKUP': "Priority Mail; Regional Rate Box A Hold For Pickup",
#             'PRIORITY_MAIL_REGIONAL_RATE_BOX_B': "Priority Mail; Regional Rate Box B",
#             'PRIORITY_MAIL_REGIONAL_RATE_BOX_B_HOLD_FOR_PICKUP': "Priority Mail; Regional Rate Box B Hold For Pickup",
#             'FIRST_CLASS_PACKAGE_SERVICE_HOLD_FOR_PICKUP': "First-Class; Package Service Hold For Pickup",
#             'PRIORITY_MAIL_EXPRESS_FLAT_RATE_BOXES': "Priority Mail Express; Flat Rate Boxes",
#             'PRIORITY_MAIL_EXPRESS_FLAT_RATE_BOXES_HOLD_FOR_PICKUP': "Priority Mail Express; Flat Rate Boxes Hold For Pickup",
#             'PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_FLAT_RATE_BOXES': "Priority Mail Express; Sunday/Holiday Delivery Flat Rate Boxes",
#             'PRIORITY_MAIL_REGIONAL_RATE_BOX_C': "Priority Mail; Regional Rate Box C",
#             'PRIORITY_MAIL_REGIONAL_RATE_BOX_C_HOLD_FOR_PICKUP': "Priority Mail; Regional Rate Box C Hold For Pickup",
#             'FIRST_CLASS_PACKAGE_SERVICE': "First-Class; Package Service",
#             'PRIORITY_MAIL_EXPRESS_PADDED_FLAT_RATE_ENVELOPE': "Priority Mail Express; Padded Flat Rate Envelope",
#             'PRIORITY_MAIL_EXPRESS_PADDED_FLAT_RATE_ENVELOPE_HOLD_FOR_PICKUP': "Priority Mail Express; Padded Flat Rate Envelope Hold For Pickup",
#             'PRIORITY_MAIL_EXPRESS_SUNDAY_HOLIDAY_DELIVERY_PADDED_FLAT_RATE_ENVELOPE':
#                 "Priority Mail Express; Sunday/Holiday Delivery Padded Flat Rate Envelope",
#         }
#         self.display_name = display_name[self.name]


# @enum.unique
# class InternationalServiceName(enum.Enum):
#     """
#     IntlRateV2 CLASSID values
#     https://www.usps.com/business/web-tools-apis/rate-calculator-api_files/rate-calculator-api.htm#_Toc57794300
#     """
#     PRIORITY_MAIL_EXPRESS_INTERNATIONAL = 1
#     PRIORITY_MAIL_INTERNATIONAL = 2
#     GLOBAL_EXPRESS_GUARANTEED_GXG = 4
#     GLOBAL_EXPRESS_GUARANTEED_DOCUMENT = 5
#     GLOBAL_EXPRESS_GUARANTEE_NON_DOCUMENT_RECTANGULAR = 6
#     GLOBAL_EXPRESS_GUARANTEED_NON_DOCUMENT_NON_RECTANGULAR = 7
#     PRIORITY_MAIL_INTERNATIONAL_FLAT_RATE_ENVELOPE = 8
#     PRIORITY_MAIL_INTERNATIONAL_MEDIUM_FLAT_RATE_BOX = 9
#     PRIORITY_MAIL_EXPRESS_INTERNATIONAL_FLAT_RATE_ENVELOPE = 10
#     PRIORITY_MAIL_INTERNATIONAL_LARGE_FLAT_RATE_BOX = 11
#     USPS_GXG_ENVELOPES = 12
#     FIRST_CLASS_MAIL_INTERNATIONAL_LETTER = 13
#     FIRST_CLASS_MAIL_INTERNATIONAL_LARGE_ENVELOPE = 14
#     FIRST_CLASS_PACKAGE_INTERNATIONAL_SERVICE = 15
#     PRIORITY_MAIL_INTERNATIONAL_SMALL_FLAT_RATE_BOX = 16
#     PRIORITY_MAIL_EXPRESS_INTERNATIONAL_LEGAL_FLAT_RATE_ENVELOPE = 17
#     PRIORITY_MAIL_INTERNATIONAL_GIFT_CARD_FLAT_RATE_ENVELOPE = 18
#     PRIORITY_MAIL_INTERNATIONAL_WINDOW_FLAT_RATE_ENVELOPE = 19
#     PRIORITY_MAIL_INTERNATIONAL_SMALL_FLAT_RATE_ENVELOPE = 20
#     FIRST_CLASS_MAIL_INTERNATIONAL_POSTCARD = 21
#     PRIORITY_MAIL_INTERNATIONAL_LEGAL_FLAT_RATE_ENVELOPE = 22
#     PRIORITY_MAIL_INTERNATIONAL_PADDED_FLAT_RATE_ENVELOPE = 23
#     PRIORITY_MAIL_INTERNATIONAL_DVD_FLAT_RATE_PRICED_BOX = 24
#     PRIORITY_MAIL_INTERNATIONAL_LARGE_VIDEO_FLAT_RATE_PRICED_BOX = 25
#     PRIORITY_MAIL_EXPRESS_INTERNATIONAL_PADDED_FLAT_RATE_ENVELOPE = 27
#
#     def __init__(self, *args):
#         """
#         :param args:
#         """
#         display_name = {
#             'PRIORITY_MAIL_EXPRESS_INTERNATIONAL': "Priority Mail Express International",
#             'PRIORITY_MAIL_INTERNATIONAL': "Priority Mail International",
#             'GLOBAL_EXPRESS_GUARANTEED_GXG': "Global Express Guaranteed; (GXG)",
#             'GLOBAL_EXPRESS_GUARANTEED_DOCUMENT': "Global Express Guaranteed; Document",
#             'GLOBAL_EXPRESS_GUARANTEE_NON_DOCUMENT_RECTANGULAR': "Global Express Guarantee; Non-Document Rectangular",
#             'GLOBAL_EXPRESS_GUARANTEED_NON_DOCUMENT_NON_RECTANGULAR': "Global Express Guaranteed; Non-Document Non-Rectangular",
#             'PRIORITY_MAIL_INTERNATIONAL_FLAT_RATE_ENVELOPE': "Priority Mail International; Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_MEDIUM_FLAT_RATE_BOX': "Priority Mail International; Medium Flat Rate Box",
#             'PRIORITY_MAIL_EXPRESS_INTERNATIONAL_FLAT_RATE_ENVELOPE': "Priority Mail Express International; Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_LARGE_FLAT_RATE_BOX': "Priority Mail International; Large Flat Rate Box",
#             'USPS_GXG_ENVELOPES': "USPS GXG; Envelopes",
#             'FIRST_CLASS_MAIL_INTERNATIONAL_LETTER': "First-Class Mail; International Letter",
#             'FIRST_CLASS_MAIL_INTERNATIONAL_LARGE_ENVELOPE': "First-Class Mail; International Large Envelope",
#             'FIRST_CLASS_PACKAGE_INTERNATIONAL_SERVICE': "First-Class Package International Service",
#             'PRIORITY_MAIL_INTERNATIONAL_SMALL_FLAT_RATE_BOX': "Priority Mail International; Small Flat Rate Box",
#             'PRIORITY_MAIL_EXPRESS_INTERNATIONAL_LEGAL_FLAT_RATE_ENVELOPE': "Priority Mail Express International; Legal Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_GIFT_CARD_FLAT_RATE_ENVELOPE': "Priority Mail International; Gift Card Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_WINDOW_FLAT_RATE_ENVELOPE': "Priority Mail International; Window Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_SMALL_FLAT_RATE_ENVELOPE': "Priority Mail International; Small Flat Rate Envelope",
#             'FIRST_CLASS_MAIL_INTERNATIONAL_POSTCARD': "First-Class Mail; International Postcard",
#             'PRIORITY_MAIL_INTERNATIONAL_LEGAL_FLAT_RATE_ENVELOPE': "Priority Mail International; Legal Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_PADDED_FLAT_RATE_ENVELOPE': "Priority Mail International; Padded Flat Rate Envelope",
#             'PRIORITY_MAIL_INTERNATIONAL_DVD_FLAT_RATE_PRICED_BOX': "Priority Mail International; DVD Flat Rate priced box",
#             'PRIORITY_MAIL_INTERNATIONAL_LARGE_VIDEO_FLAT_RATE_PRICED_BOX': "Priority Mail International; Large Video Flat Rate priced box",
#             'PRIORITY_MAIL_EXPRESS_INTERNATIONAL_PADDED_FLAT_RATE_ENVELOPE': "Priority Mail Express International; Padded Flat Rate Envelope",
#         }
#         self.display_name = display_name[self.name]
