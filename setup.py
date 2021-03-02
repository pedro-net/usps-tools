from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


class InstallWithCompile(build_py):
    def run(self):
        self.run_command('compile_catalog')
        super().run()


setup(name='usps-tools',
      version='0.1.0',
      description="Python implementation of USPS API Tools <https://www.usps.com/business/web-tools-apis/documentation-updates.htm>",
      url='https://github.com/pedrovagner/usps-tools',
      author='PedroVagner.com',
      python_requires='~=3.5',  # new in Python 3.5: import typing (function annotations)
      install_requires=['requests ~= 2.0', 'marshmallow >= 3.*, < 4.*'],
      cmdclass={
          'build_py': InstallWithCompile,
      },
      setup_requires=['Babel'],
      packages=find_packages(),
      include_package_data=True,
      package_data={
          '': [
              'locale/*/*/*.mo',
              'locale/*/*/*.po',
          ]
      },
      )
