import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('usps-tools', localedir, fallback=True)
_ = translate.gettext
