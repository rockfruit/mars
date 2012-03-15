#-*- coding: utf-8 -*-
#  mars http://www.naturalsciences.be/metamars/products/
#  Archetypes implementation of the MARS core types based on ATContentTypes
#  Copyright (c) 2003-2007 MARS development team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""

"""
__author__  = 'David Convent <david.convent@naturalsciences.be>'
__docformat__ = 'restructuredtext'


from api import *
from config import PROJECTNAME
from schemata import *

SiteSchema = MarsFolderSchema.copy()
SiteSchema += Schema((
    LinesField('synonyms',
        required=False,
        searchable=False,
        widget=LinesWidget(label='Alternate Site Names',
            label_msgid='label_site_synonyms',
            description="Synonyms, different spellings or local names of the sites name",
            description_msgid='help_site_synonyms',
            domain='mars',
            ),
        ),

    MarscatField('siteType',
        required=True,
        searchable=False,
        relationship='isSiteType',
        widget=MarscatWidget(
            label='Type',
            label_msgid='label_site_type',
            description='Select what kind of type this site is.',
            description_msgid='help_site_type',
            domain='mars',
            startup_directory='/marscategories/site',
            ),
        schemata='description',
        ),

    TextField(
        'detailedDescription',
        required=False,
        searchable=False,
        #default_content_type='text/plain',
        allowable_content_types = ('text/plain',
                                   'text/structured',
                                   'text/html',),
        default_output_type='text/x-html-safe',
        widget=RichWidget(label='Site Details',
            label_msgid='label_detailed_description',
            description='Describe more details about the type and layout of the site.',
            description_msgid='help_detailed_description',
            domain='mars',
            ),
        schemata='description',
        ),

    ))

SiteSchema += LocationSchema.copy()
SiteSchema += ChronologySchema.copy()
SiteSchema += DiscoverySchema.copy()
SiteSchema['discoverySite'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}
finalizeMarsSchema(SiteSchema, folderish=True,
                    delFields=('stratigraphicalLayer','discoveryPlace'))

class MarsSite(ATFolder, MarsMixin):
    """Archeological Site"""
    implements(
        (IFilesAndImagesContainer,)+tuple([a for a in implementedBy(ATFolder)])
    )
    schema = SiteSchema
    portal_type = "Site"
    archetype_name = "Site"


registerATCT(MarsSite, PROJECTNAME)