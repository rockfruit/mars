#-*- coding: utf-8 -*-
from zope.interface import Interface

from Products.ATContentTypes.interface import IATDocument

class IMarsCollectionObject(IATDocument):
    """MarsCollectionObject marker interface
    """
    pass

class ISchemataViewletEnabled(Interface):
    """Marker Interface for schemata display viewlet
    """


class IFilesAndImagesContainer(Interface):
    """Marker interface for folders and images container object"""
