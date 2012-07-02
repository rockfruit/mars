#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='mars',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone mars migration zope archaeology',
      author='Mathieu Le Marec - Pasquet',
      author_email='kiorky@cryptelium.net',
      url='http://www.naturalsciences.be',
      license='GPL',
      namespace_packages=['mars', 'marsapp'],
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'bibliograph.core',
          'bibliograph.parsing',
          'bibliograph.rendering',
          'collective.bibliocustomviews',
          'collective.ckeditor',
          'collective.js.datatables',
          'collective.testcaselayer',
          'collective.uploadify',
          'collective.zipfiletransport',
          'demjson',
          'eea.facetednavigation',
          'ordereddict',
          'Plomino',
          'plomino.tinymce',
          'plone.app.testing',
          'plone.formwidget.datetime',
          #'plone.reload',
          'Products.ATVocabularyManager',
          'Products.CMFBibliographyAT',
          'Products.contentmigration',
          'Products.csvreplicata',
          'Products.Maps',
          'Products.RefBiblioParser',
          'setuptools',
          'z3c.autoinclude',
          'z3c.form[test]',
          'zc.buildout',
          'zope.component',
          'zope.interface',
          'zope.testing',
      ] ,
      entry_points = {
          'z3c.autoinclude.plugin': [
              'target = plone',
          ],
      },
      extras_require={'test': ['IPython', 'zope.testing', 'mocker']},
     )
