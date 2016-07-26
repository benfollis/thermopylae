from setuptools import setup
setup(name='thermopylae',
      version="0.1",
      description="A python module to read 1 wire thermometers and present thier results via rest"
      url="https://github.com/benfollis/thermopylae",
      author="Ben Follis",
      license="GPLv3",
      packages=['thermopylae', 'thermopylae.busdrivers', 'thermopylae.config', 'thermopylae.web']
      zip_safe=False,
      scripts=['bin/thermopylae_rest']
