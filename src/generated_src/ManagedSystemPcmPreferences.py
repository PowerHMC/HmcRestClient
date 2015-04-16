# .\ManagedSystemPcmPreference.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0187ff9a540c37f223dac915d3a3be8d51179dee
# Generated 2015-04-16 01:10:38.765000 by PyXB version 1.2.4 using Python 2.7.0.final.0
# Namespace http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4ac44da1-e3a7-11e4-b905-0021cc638662')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _xmlk2 as _ImportedBinding__xmlk2

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xmlk2 = _ImportedBinding__xmlk2.Namespace
_Namespace_xmlk2.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HardwarePageTableRatioExponent.Type
class HardwarePageTableRatioExponent_Type (pyxb.binding.datatypes.unsignedShort):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HardwarePageTableRatioExponent.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 92, 1)
    _Documentation = '\n                \n            '
HardwarePageTableRatioExponent_Type._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=HardwarePageTableRatioExponent_Type, value=pyxb.binding.datatypes.unsignedShort(8))
HardwarePageTableRatioExponent_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=HardwarePageTableRatioExponent_Type, value=pyxb.binding.datatypes.unsignedShort(1))
HardwarePageTableRatioExponent_Type._InitializeFacetMap(HardwarePageTableRatioExponent_Type._CF_maxInclusive,
   HardwarePageTableRatioExponent_Type._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'HardwarePageTableRatioExponent.Type', HardwarePageTableRatioExponent_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Megabyte.Type
class Megabyte_Type (pyxb.binding.datatypes.decimal):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Megabyte.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 117, 5)
    _Documentation = '\n                \n            '
Megabyte_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Megabyte_Type, value=pyxb.binding.datatypes.decimal('0.0'))
Megabyte_Type._InitializeFacetMap(Megabyte_Type._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'Megabyte.Type', Megabyte_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ProcessorUnit.Type
class ProcessorUnit_Type (pyxb.binding.datatypes.decimal):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessorUnit.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 133, 6)
    _Documentation = '\n                \n            '
ProcessorUnit_Type._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ProcessorUnit_Type, value=pyxb.binding.datatypes.decimal('2048.0'))
ProcessorUnit_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ProcessorUnit_Type, value=pyxb.binding.datatypes.decimal('0.0'))
ProcessorUnit_Type._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(2))
ProcessorUnit_Type._InitializeFacetMap(ProcessorUnit_Type._CF_maxInclusive,
   ProcessorUnit_Type._CF_minInclusive,
   ProcessorUnit_Type._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'ProcessorUnit.Type', ProcessorUnit_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Range.Type
class Range_Type (pyxb.binding.datatypes.int):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Range.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 155, 3)
    _Documentation = '\n                \n            '
Range_Type._CF_maxExclusive = pyxb.binding.facets.CF_maxExclusive(value_datatype=pyxb.binding.datatypes.int, value=pyxb.binding.datatypes.long(15))
Range_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Range_Type, value=pyxb.binding.datatypes.int(0))
Range_Type._InitializeFacetMap(Range_Type._CF_maxExclusive,
   Range_Type._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'Range.Type', Range_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MemoryWeight.Type
class MemoryWeight_Type (pyxb.binding.datatypes.unsignedInt):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MemoryWeight.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 177, 6)
    _Documentation = '\n                \n            '
MemoryWeight_Type._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=MemoryWeight_Type, value=pyxb.binding.datatypes.unsignedInt(255))
MemoryWeight_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=MemoryWeight_Type, value=pyxb.binding.datatypes.unsignedInt(0))
MemoryWeight_Type._InitializeFacetMap(MemoryWeight_Type._CF_maxInclusive,
   MemoryWeight_Type._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'MemoryWeight.Type', MemoryWeight_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VLANID.Type
class VLANID_Type (pyxb.binding.datatypes.unsignedShort):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VLANID.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 200, 6)
    _Documentation = '\n                \n            '
VLANID_Type._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'VLANID.Type', VLANID_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Gigabyte.Type
class Gigabyte_Type (pyxb.binding.datatypes.decimal):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Gigabyte.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 217, 7)
    _Documentation = '\n                \n            '
Gigabyte_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Gigabyte_Type, value=pyxb.binding.datatypes.decimal('0.0'))
Gigabyte_Type._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(value=pyxb.binding.datatypes.nonNegativeInteger(6))
Gigabyte_Type._InitializeFacetMap(Gigabyte_Type._CF_minInclusive,
   Gigabyte_Type._CF_fractionDigits)
Namespace.addCategoryObject('typeBinding', 'Gigabyte.Type', Gigabyte_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}DynamicReconfigurationConnectorIndex.Type
class DynamicReconfigurationConnectorIndex_Type (pyxb.binding.datatypes.unsignedInt):

    """
                
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DynamicReconfigurationConnectorIndex.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 376, 4)
    _Documentation = '\n                \n                \n            '
DynamicReconfigurationConnectorIndex_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=DynamicReconfigurationConnectorIndex_Type, value=pyxb.binding.datatypes.unsignedInt(65536))
DynamicReconfigurationConnectorIndex_Type._InitializeFacetMap(DynamicReconfigurationConnectorIndex_Type._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'DynamicReconfigurationConnectorIndex.Type', DynamicReconfigurationConnectorIndex_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VirtualIOSlotIndex.Type
class VirtualIOSlotIndex_Type (pyxb.binding.datatypes.unsignedShort):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VirtualIOSlotIndex.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 418, 4)
    _Documentation = '\n                \n            '
VirtualIOSlotIndex_Type._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'VirtualIOSlotIndex.Type', VirtualIOSlotIndex_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}QualityOfServicePriority.Type
class QualityOfServicePriority_Type (pyxb.binding.datatypes.int):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QualityOfServicePriority.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 438, 4)
    _Documentation = '\n                \n            '
QualityOfServicePriority_Type._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=QualityOfServicePriority_Type, value=pyxb.binding.datatypes.int(7))
QualityOfServicePriority_Type._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=QualityOfServicePriority_Type, value=pyxb.binding.datatypes.int(0))
QualityOfServicePriority_Type._InitializeFacetMap(QualityOfServicePriority_Type._CF_maxInclusive,
   QualityOfServicePriority_Type._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'QualityOfServicePriority.Type', QualityOfServicePriority_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomMedia.Pattern
class AtomMedia_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomMedia.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 132, 4)
    _Documentation = '\n                \n            '
AtomMedia_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
AtomMedia_Pattern._CF_pattern.addPattern(pattern='.+/.+')
AtomMedia_Pattern._InitializeFacetMap(AtomMedia_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AtomMedia.Pattern', AtomMedia_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLanguageTag.Type
class AtomLanguageTag_Type (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomLanguageTag.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 162, 4)
    _Documentation = '\n                \n            '
AtomLanguageTag_Type._CF_pattern = pyxb.binding.facets.CF_pattern()
AtomLanguageTag_Type._CF_pattern.addPattern(pattern='[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*')
AtomLanguageTag_Type._InitializeFacetMap(AtomLanguageTag_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AtomLanguageTag.Type', AtomLanguageTag_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IanaRelationship.Enum
class IanaRelationship_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                

                
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IanaRelationship.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 275, 4)
    _Documentation = '\n                \n                \n\n                \n                \n            '
IanaRelationship_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IanaRelationship_Enum, enum_prefix=None)
IanaRelationship_Enum.alternate = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='alternate', tag='alternate')
IanaRelationship_Enum.appendix = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='appendix', tag='appendix')
IanaRelationship_Enum.archives = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='archives', tag='archives')
IanaRelationship_Enum.author = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='author', tag='author')
IanaRelationship_Enum.bookmark = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='bookmark', tag='bookmark')
IanaRelationship_Enum.canonical = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='canonical', tag='canonical')
IanaRelationship_Enum.chapter = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='chapter', tag='chapter')
IanaRelationship_Enum.contents = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='contents', tag='contents')
IanaRelationship_Enum.copyright = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='copyright', tag='copyright')
IanaRelationship_Enum.current = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
IanaRelationship_Enum.describedby = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='describedby', tag='describedby')
IanaRelationship_Enum.duplicate = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='duplicate', tag='duplicate')
IanaRelationship_Enum.edit = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='edit', tag='edit')
IanaRelationship_Enum.edit_media = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='edit-media', tag='edit_media')
IanaRelationship_Enum.enclosure = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='enclosure', tag='enclosure')
IanaRelationship_Enum.first = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='first', tag='first')
IanaRelationship_Enum.glossary = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='glossary', tag='glossary')
IanaRelationship_Enum.help = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='help', tag='help')
IanaRelationship_Enum.hub = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='hub', tag='hub')
IanaRelationship_Enum.icon = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='icon', tag='icon')
IanaRelationship_Enum.index = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='index', tag='index')
IanaRelationship_Enum.last = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='last', tag='last')
IanaRelationship_Enum.latest_version = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='latest-version', tag='latest_version')
IanaRelationship_Enum.license = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='license', tag='license')
IanaRelationship_Enum.lrdd = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='lrdd', tag='lrdd')
IanaRelationship_Enum.monitor = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='monitor', tag='monitor')
IanaRelationship_Enum.monitor_group = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='monitor-group', tag='monitor_group')
IanaRelationship_Enum.next = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='next', tag='next')
IanaRelationship_Enum.next_ = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='next', tag='next_')
IanaRelationship_Enum.next_archive = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='next-archive', tag='next_archive')
IanaRelationship_Enum.nofollow = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='nofollow', tag='nofollow')
IanaRelationship_Enum.noreferrer = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='noreferrer', tag='noreferrer')
IanaRelationship_Enum.payment = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='payment', tag='payment')
IanaRelationship_Enum.predecessor_version = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='predecessor-version', tag='predecessor_version')
IanaRelationship_Enum.prefetch = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='prefetch', tag='prefetch')
IanaRelationship_Enum.prev = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='prev', tag='prev')
IanaRelationship_Enum.previous = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='previous', tag='previous')
IanaRelationship_Enum.prev_archive = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='prev-archive', tag='prev_archive')
IanaRelationship_Enum.related = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='related', tag='related')
IanaRelationship_Enum.replies = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='replies', tag='replies')
IanaRelationship_Enum.search = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='search', tag='search')
IanaRelationship_Enum.section = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='section', tag='section')
IanaRelationship_Enum.self = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='self', tag='self')
IanaRelationship_Enum.service = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='service', tag='service')
IanaRelationship_Enum.start = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='start', tag='start')
IanaRelationship_Enum.stylesheet = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='stylesheet', tag='stylesheet')
IanaRelationship_Enum.subsection = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='subsection', tag='subsection')
IanaRelationship_Enum.successor_version = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='successor-version', tag='successor_version')
IanaRelationship_Enum.tag = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='tag', tag='tag')
IanaRelationship_Enum.up = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='up', tag='up')
IanaRelationship_Enum.version_history = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='version-history', tag='version_history')
IanaRelationship_Enum.via = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='via', tag='via')
IanaRelationship_Enum.working_copy = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='working-copy', tag='working_copy')
IanaRelationship_Enum.working_copy_of = IanaRelationship_Enum._CF_enumeration.addEnumeration(unicode_value='working-copy-of', tag='working_copy_of')
IanaRelationship_Enum._InitializeFacetMap(IanaRelationship_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IanaRelationship.Enum', IanaRelationship_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AllOrNone.Enum
class AllOrNone_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllOrNone.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 80, 4)
    _Documentation = '\n                \n                 \n            '
AllOrNone_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AllOrNone_Enum, enum_prefix=None)
AllOrNone_Enum.ALL = AllOrNone_Enum._CF_enumeration.addEnumeration(unicode_value='ALL', tag='ALL')
AllOrNone_Enum.NONE = AllOrNone_Enum._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
AllOrNone_Enum._InitializeFacetMap(AllOrNone_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AllOrNone.Enum', AllOrNone_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Auto.Enum
class Auto_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Auto.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 125, 4)
    _Documentation = '\n                \n                 \n            '
Auto_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Auto_Enum, enum_prefix=None)
Auto_Enum.AUTO = Auto_Enum._CF_enumeration.addEnumeration(unicode_value='AUTO', tag='AUTO')
Auto_Enum._InitializeFacetMap(Auto_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Auto.Enum', Auto_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}None.Enum
class None_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'None.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 159, 4)
    _Documentation = '\n                \n                 \n            '
None_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=None_Enum, enum_prefix=None)
None_Enum.NONE = None_Enum._CF_enumeration.addEnumeration(unicode_value='NONE', tag='NONE')
None_Enum._InitializeFacetMap(None_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'None.Enum', None_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HttpReasonCodes.Enum
class HttpReasonCodes_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HttpReasonCodes.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 195, 3)
    _Documentation = '\n                \n                 \n            '
HttpReasonCodes_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HttpReasonCodes_Enum, enum_prefix=None)
HttpReasonCodes_Enum.INVALID_URL = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='INVALID_URL', tag='INVALID_URL')
HttpReasonCodes_Enum.No_Valid_User_Session = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='No Valid User Session.', tag='No_Valid_User_Session')
HttpReasonCodes_Enum.Request_Body_Supplied_When_Not_Expected = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Request Body Supplied When Not Expected', tag='Request_Body_Supplied_When_Not_Expected')
HttpReasonCodes_Enum.A_resource_limit_in_the_MC_has_been_exceeded = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='A resource limit in the MC has been exceeded.', tag='A_resource_limit_in_the_MC_has_been_exceeded')
HttpReasonCodes_Enum.Missing_a_required_request_body = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Missing a required request body.', tag='Missing_a_required_request_body')
HttpReasonCodes_Enum.Missing_a_required_request_body_parameter = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Missing a required request body parameter.', tag='Missing_a_required_request_body_parameter')
HttpReasonCodes_Enum.Missing_a_required_request_header = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Missing a required request header.', tag='Missing_a_required_request_header')
HttpReasonCodes_Enum.Invalid_request_header_value = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Invalid request header value.', tag='Invalid_request_header_value')
HttpReasonCodes_Enum.Mismatch_of_content_length_of_header_and_request_body = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Mismatch of content length of header and request body.', tag='Mismatch_of_content_length_of_header_and_request_body')
HttpReasonCodes_Enum.The_data_type_of_a_field_in_the_request_body_is_not_recognized = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The data type of a field in the request body is not recognized.', tag='The_data_type_of_a_field_in_the_request_body_is_not_recognized')
HttpReasonCodes_Enum.The_MC_has_failed_over_to_the_alternate_MC = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The MC has failed-over to the alternate MC.', tag='The_MC_has_failed_over_to_the_alternate_MC')
HttpReasonCodes_Enum.The_MC_has_restarted = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The MC has restarted.', tag='The_MC_has_restarted')
HttpReasonCodes_Enum.The_request_body_contains_an_unrecognized_field = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The request body contains an unrecognized field.', tag='The_request_body_contains_an_unrecognized_field')
HttpReasonCodes_Enum.The_MC_is_not_in_the_correct_state_to_perform_the_request = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The MC is not in the correct state to perform the request.', tag='The_MC_is_not_in_the_correct_state_to_perform_the_request')
HttpReasonCodes_Enum.The_underlying_PowerSystem_timed_out_while_performing_the_request = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The underlying PowerSystem timed out while performing the request.', tag='The_underlying_PowerSystem_timed_out_while_performing_the_request')
HttpReasonCodes_Enum.The_supplied_URI_does_not_identify_a_known_resource = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The supplied URI does not identify a known resource.', tag='The_supplied_URI_does_not_identify_a_known_resource')
HttpReasonCodes_Enum.The_supplied_URI_identifies_a_resource_of_the_wrong_type = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The supplied URI identifies a resource of the wrong type.', tag='The_supplied_URI_identifies_a_resource_of_the_wrong_type')
HttpReasonCodes_Enum.The_supplied_URI_does_not_match_known_URI_patterns = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The supplied URI does not match known URI patterns.', tag='The_supplied_URI_does_not_match_known_URI_patterns')
HttpReasonCodes_Enum.The_supplied_XML_request_body_did_not_pass_XML_validation = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The supplied XML request body did not pass XML validation.', tag='The_supplied_XML_request_body_did_not_pass_XML_validation')
HttpReasonCodes_Enum.The_supplied_user_credentials_are_not_recognized = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The supplied user credentials are not recognized.', tag='The_supplied_user_credentials_are_not_recognized')
HttpReasonCodes_Enum.The_supplied_user_credentials_have_expired = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The supplied user credentials have expired.', tag='The_supplied_user_credentials_have_expired')
HttpReasonCodes_Enum.The_user_does_not_have_the_resource_authority_to_perform_the_request = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The user does not have the resource authority to perform the request.', tag='The_user_does_not_have_the_resource_authority_to_perform_the_request')
HttpReasonCodes_Enum.The_user_does_not_have_the_role_authority_to_perform_the_request = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='The user does not have the role authority to perform the request.', tag='The_user_does_not_have_the_role_authority_to_perform_the_request')
HttpReasonCodes_Enum.Unrecognized_search_parameter = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Unrecognized search parameter.', tag='Unrecognized_search_parameter')
HttpReasonCodes_Enum.Malformed_search_string = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Malformed search string.', tag='Malformed_search_string')
HttpReasonCodes_Enum.Unknown_internal_error = HttpReasonCodes_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown internal error.', tag='Unknown_internal_error')
HttpReasonCodes_Enum._InitializeFacetMap(HttpReasonCodes_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HttpReasonCodes.Enum', HttpReasonCodes_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}JobStatus.Enum
class JobStatus_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JobStatus.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 448, 3)
    _Documentation = '\n                \n                 \n            '
JobStatus_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=JobStatus_Enum, enum_prefix=None)
JobStatus_Enum.Queued = JobStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Queued', tag='Queued')
JobStatus_Enum.Running = JobStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
JobStatus_Enum.Failed = JobStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Failed', tag='Failed')
JobStatus_Enum.Completed = JobStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Completed', tag='Completed')
JobStatus_Enum._InitializeFacetMap(JobStatus_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'JobStatus.Enum', JobStatus_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SearchComparator.Enum
class SearchComparator_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SearchComparator.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 503, 3)
    _Documentation = '\n                \n                 \n            '
SearchComparator_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SearchComparator_Enum, enum_prefix=None)
SearchComparator_Enum.String_Match = SearchComparator_Enum._CF_enumeration.addEnumeration(unicode_value='String Match', tag='String_Match')
SearchComparator_Enum.Numeric = SearchComparator_Enum._CF_enumeration.addEnumeration(unicode_value='Numeric', tag='Numeric')
SearchComparator_Enum.Regular_Expression = SearchComparator_Enum._CF_enumeration.addEnumeration(unicode_value='Regular Expression', tag='Regular_Expression')
SearchComparator_Enum._InitializeFacetMap(SearchComparator_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SearchComparator.Enum', SearchComparator_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SchemaVersion.Enum
class SchemaVersion_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                
                
                
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SchemaVersion.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 565, 2)
    _Documentation = '\n                \n                \n                \n                \n                \n            '
SchemaVersion_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SchemaVersion_Enum, enum_prefix=None)
SchemaVersion_Enum.V1_0 = SchemaVersion_Enum._CF_enumeration.addEnumeration(unicode_value='V1_0', tag='V1_0')
SchemaVersion_Enum.V1_1_0 = SchemaVersion_Enum._CF_enumeration.addEnumeration(unicode_value='V1_1_0', tag='V1_1_0')
SchemaVersion_Enum.V1_2_0 = SchemaVersion_Enum._CF_enumeration.addEnumeration(unicode_value='V1_2_0', tag='V1_2_0')
SchemaVersion_Enum._InitializeFacetMap(SchemaVersion_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SchemaVersion.Enum', SchemaVersion_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SystemState.Enum
class SystemState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SystemState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 633, 1)
    _Documentation = None
SystemState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SystemState_Enum, enum_prefix=None)
SystemState_Enum.Not_Available = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Not Available', tag='Not_Available')
SystemState_Enum.Recovery = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Recovery', tag='Recovery')
SystemState_Enum.Operating = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Operating', tag='Operating')
SystemState_Enum.Disabled = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Disabled', tag='Disabled')
SystemState_Enum.Power_Off = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Power Off', tag='Power_Off')
SystemState_Enum.Undefined = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Undefined', tag='Undefined')
SystemState_Enum.Boot_in_Progress = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Boot in Progress', tag='Boot_in_Progress')
SystemState_Enum.Initializing = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Initializing', tag='Initializing')
SystemState_Enum.Stopped = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Stopped', tag='Stopped')
SystemState_Enum.Running = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
SystemState_Enum.Powering_Off = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Powering Off', tag='Powering_Off')
SystemState_Enum.Open_Firmware = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Open Firmware', tag='Open_Firmware')
SystemState_Enum.Valid = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Valid', tag='Valid')
SystemState_Enum.Invalid = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Invalid', tag='Invalid')
SystemState_Enum.Error = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Error', tag='Error')
SystemState_Enum.Not_Ready = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Not Ready', tag='Not_Ready')
SystemState_Enum.Incomplete = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Incomplete', tag='Incomplete')
SystemState_Enum.No_Connection = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='No Connection', tag='No_Connection')
SystemState_Enum.Failed_Authentication = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Failed Authentication', tag='Failed_Authentication')
SystemState_Enum.Pending_Authentication___Password_Updates_Required = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Pending Authentication - Password Updates Required', tag='Pending_Authentication___Password_Updates_Required')
SystemState_Enum.Standby = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='Standby', tag='Standby')
SystemState_Enum.On_Demand_Recovery = SystemState_Enum._CF_enumeration.addEnumeration(unicode_value='On Demand Recovery', tag='On_Demand_Recovery')
SystemState_Enum._InitializeFacetMap(SystemState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SystemState.Enum', SystemState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}DetailedState.Enum
class DetailedState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DetailedState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 660, 5)
    _Documentation = None
DetailedState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DetailedState_Enum, enum_prefix=None)
DetailedState_Enum.Unknown = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
DetailedState_Enum.Other = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
DetailedState_Enum.Stressed = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Stressed', tag='Stressed')
DetailedState_Enum.Failed_Authentication = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Failed Authentication', tag='Failed_Authentication')
DetailedState_Enum.Version_Mismatch = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Version Mismatch', tag='Version_Mismatch')
DetailedState_Enum.Dump_In_Progress = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Dump In Progress', tag='Dump_In_Progress')
DetailedState_Enum.Service_Processor_Failover = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Service Processor Failover', tag='Service_Processor_Failover')
DetailedState_Enum.Password_Update_Required = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Password Update Required', tag='Password_Update_Required')
DetailedState_Enum.Open_Firmware = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Open Firmware', tag='Open_Firmware')
DetailedState_Enum.Performing_Hardware_Discovery = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Performing Hardware Discovery', tag='Performing_Hardware_Discovery')
DetailedState_Enum.Recovery = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Recovery', tag='Recovery')
DetailedState_Enum.Terminated = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Terminated', tag='Terminated')
DetailedState_Enum.Incomplete = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Incomplete', tag='Incomplete')
DetailedState_Enum.Optimizing_Memory = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Optimizing Memory', tag='Optimizing_Memory')
DetailedState_Enum.None_ = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
DetailedState_Enum.Remote_Restarting = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Remote Restarting', tag='Remote_Restarting')
DetailedState_Enum.Remote_Restarted = DetailedState_Enum._CF_enumeration.addEnumeration(unicode_value='Remote Restarted', tag='Remote_Restarted')
DetailedState_Enum._InitializeFacetMap(DetailedState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DetailedState.Enum', DetailedState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ServiceProcesssorFailoverState.Enum
class ServiceProcesssorFailoverState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceProcesssorFailoverState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 682, 4)
    _Documentation = None
ServiceProcesssorFailoverState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ServiceProcesssorFailoverState_Enum, enum_prefix=None)
ServiceProcesssorFailoverState_Enum.Ready = ServiceProcesssorFailoverState_Enum._CF_enumeration.addEnumeration(unicode_value='Ready', tag='Ready')
ServiceProcesssorFailoverState_Enum.Not_ready = ServiceProcesssorFailoverState_Enum._CF_enumeration.addEnumeration(unicode_value='Not ready', tag='Not_ready')
ServiceProcesssorFailoverState_Enum._InitializeFacetMap(ServiceProcesssorFailoverState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ServiceProcesssorFailoverState.Enum', ServiceProcesssorFailoverState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MemoryMirroringState.Enum
class MemoryMirroringState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MemoryMirroringState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 689, 4)
    _Documentation = None
MemoryMirroringState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MemoryMirroringState_Enum, enum_prefix=None)
MemoryMirroringState_Enum.Not_mirrored = MemoryMirroringState_Enum._CF_enumeration.addEnumeration(unicode_value='Not mirrored', tag='Not_mirrored')
MemoryMirroringState_Enum.Mirrored = MemoryMirroringState_Enum._CF_enumeration.addEnumeration(unicode_value='Mirrored', tag='Mirrored')
MemoryMirroringState_Enum.Mirrored_but_running_exposed = MemoryMirroringState_Enum._CF_enumeration.addEnumeration(unicode_value='Mirrored but running exposed', tag='Mirrored_but_running_exposed')
MemoryMirroringState_Enum._InitializeFacetMap(MemoryMirroringState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MemoryMirroringState.Enum', MemoryMirroringState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AddressBroadCastPolicy.Enum
class AddressBroadCastPolicy_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Values for Managed System attribute 
      "addr broadcast perf policy" Is this a property that is only supported on P7 IH systems? 
       If so, those are locked to eFW7.3 levels of firmware and of HMC, 
       and will never need to expose this feature in K2 on eFW7.8 and later.
       """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressBroadCastPolicy.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 699, 2)
    _Documentation = 'Values for Managed System attribute \n      "addr broadcast perf policy" Is this a property that is only supported on P7 IH systems? \n       If so, those are locked to eFW7.3 levels of firmware and of HMC, \n       and will never need to expose this feature in K2 on eFW7.8 and later.\n       '
AddressBroadCastPolicy_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AddressBroadCastPolicy_Enum, enum_prefix=None)
AddressBroadCastPolicy_Enum.No_Affinity = AddressBroadCastPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='No Affinity', tag='No_Affinity')
AddressBroadCastPolicy_Enum.Chip_Affinity = AddressBroadCastPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='Chip Affinity', tag='Chip_Affinity')
AddressBroadCastPolicy_Enum.Node_Affinity = AddressBroadCastPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='Node Affinity', tag='Node_Affinity')
AddressBroadCastPolicy_Enum._InitializeFacetMap(AddressBroadCastPolicy_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AddressBroadCastPolicy.Enum', AddressBroadCastPolicy_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ServiceProcessorSide.Enum
class ServiceProcessorSide_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ServiceProcessorSide.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 714, 4)
    _Documentation = None
ServiceProcessorSide_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ServiceProcessorSide_Enum, enum_prefix=None)
ServiceProcessorSide_Enum.Permanent = ServiceProcessorSide_Enum._CF_enumeration.addEnumeration(unicode_value='Permanent', tag='Permanent')
ServiceProcessorSide_Enum.Temporary = ServiceProcessorSide_Enum._CF_enumeration.addEnumeration(unicode_value='Temporary', tag='Temporary')
ServiceProcessorSide_Enum._InitializeFacetMap(ServiceProcessorSide_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ServiceProcessorSide.Enum', ServiceProcessorSide_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}KeyLockPosition.Enum
class KeyLockPosition_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'KeyLockPosition.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 721, 3)
    _Documentation = None
KeyLockPosition_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=KeyLockPosition_Enum, enum_prefix=None)
KeyLockPosition_Enum.normal = KeyLockPosition_Enum._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
KeyLockPosition_Enum.manual = KeyLockPosition_Enum._CF_enumeration.addEnumeration(unicode_value='manual', tag='manual')
KeyLockPosition_Enum._InitializeFacetMap(KeyLockPosition_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'KeyLockPosition.Enum', KeyLockPosition_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MajorBootType.Enum
class MajorBootType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MajorBootType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 728, 4)
    _Documentation = None
MajorBootType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MajorBootType_Enum, enum_prefix=None)
MajorBootType_Enum.Power_On = MajorBootType_Enum._CF_enumeration.addEnumeration(unicode_value='Power On', tag='Power_On')
MajorBootType_Enum.Reboot = MajorBootType_Enum._CF_enumeration.addEnumeration(unicode_value='Reboot', tag='Reboot')
MajorBootType_Enum._InitializeFacetMap(MajorBootType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MajorBootType.Enum', MajorBootType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}FspmOsIplMode.Enum
class FspmOsIplMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FspmOsIplMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 735, 4)
    _Documentation = None
FspmOsIplMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FspmOsIplMode_Enum, enum_prefix=None)
FspmOsIplMode_Enum.A = FspmOsIplMode_Enum._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
FspmOsIplMode_Enum.B = FspmOsIplMode_Enum._CF_enumeration.addEnumeration(unicode_value='B', tag='B')
FspmOsIplMode_Enum.C = FspmOsIplMode_Enum._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
FspmOsIplMode_Enum.D = FspmOsIplMode_Enum._CF_enumeration.addEnumeration(unicode_value='D', tag='D')
FspmOsIplMode_Enum._InitializeFacetMap(FspmOsIplMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FspmOsIplMode.Enum', FspmOsIplMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PartitionBootMode.Enum
class PartitionBootMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartitionBootMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 744, 0)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PartitionBootMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PartitionBootMode_Enum, enum_prefix=None)
PartitionBootMode_Enum.Diagnostic_with_Default_Boot_List = PartitionBootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Diagnostic with Default Boot List', tag='Diagnostic_with_Default_Boot_List')
PartitionBootMode_Enum.Diagnostic_with_Stored_Boot_List = PartitionBootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Diagnostic with Stored Boot List', tag='Diagnostic_with_Stored_Boot_List')
PartitionBootMode_Enum.Normal = PartitionBootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
PartitionBootMode_Enum.Open_Firmware_OK_Prompt = PartitionBootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Open Firmware OK Prompt', tag='Open_Firmware_OK_Prompt')
PartitionBootMode_Enum.System_Management_Services = PartitionBootMode_Enum._CF_enumeration.addEnumeration(unicode_value='System Management Services', tag='System_Management_Services')
PartitionBootMode_Enum._InitializeFacetMap(PartitionBootMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PartitionBootMode.Enum', PartitionBootMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}TurbocoreSupport.Enum
class TurbocoreSupport_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TurbocoreSupport.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 813, 3)
    _Documentation = None
TurbocoreSupport_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TurbocoreSupport_Enum, enum_prefix=None)
TurbocoreSupport_Enum.Reserved = TurbocoreSupport_Enum._CF_enumeration.addEnumeration(unicode_value='Reserved', tag='Reserved')
TurbocoreSupport_Enum.Turbocore_Capable = TurbocoreSupport_Enum._CF_enumeration.addEnumeration(unicode_value='Turbocore Capable', tag='Turbocore_Capable')
TurbocoreSupport_Enum.Not_enough_nodes = TurbocoreSupport_Enum._CF_enumeration.addEnumeration(unicode_value='Not enough nodes', tag='Not_enough_nodes')
TurbocoreSupport_Enum.Not_all_processors_are_turbocore_capable = TurbocoreSupport_Enum._CF_enumeration.addEnumeration(unicode_value='Not all processors are turbocore capable', tag='Not_all_processors_are_turbocore_capable')
TurbocoreSupport_Enum._InitializeFacetMap(TurbocoreSupport_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TurbocoreSupport.Enum', TurbocoreSupport_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ProcessorCompatibilityMode.Enum
class ProcessorCompatibilityMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessorCompatibilityMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 822, 2)
    _Documentation = None
ProcessorCompatibilityMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProcessorCompatibilityMode_Enum, enum_prefix=None)
ProcessorCompatibilityMode_Enum.Default = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='Default', tag='Default')
ProcessorCompatibilityMode_Enum.POWER5 = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER5', tag='POWER5')
ProcessorCompatibilityMode_Enum.POWER6 = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER6', tag='POWER6')
ProcessorCompatibilityMode_Enum.POWER6_enhanced = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER6_enhanced', tag='POWER6_enhanced')
ProcessorCompatibilityMode_Enum.POWER6_plus = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER6_plus', tag='POWER6_plus')
ProcessorCompatibilityMode_Enum.POWER6_plus_enhanced = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER6_plus_enhanced', tag='POWER6_plus_enhanced')
ProcessorCompatibilityMode_Enum.POWER7 = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER7', tag='POWER7')
ProcessorCompatibilityMode_Enum.POWER7_enhanced = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER7_enhanced', tag='POWER7_enhanced')
ProcessorCompatibilityMode_Enum.POWER7_plus = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER7_plus', tag='POWER7_plus')
ProcessorCompatibilityMode_Enum.POWER7_plus_enhanced = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER7_plus_enhanced', tag='POWER7_plus_enhanced')
ProcessorCompatibilityMode_Enum.POWER8 = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER8', tag='POWER8')
ProcessorCompatibilityMode_Enum.POWER8_enhanced = ProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER8_enhanced', tag='POWER8_enhanced')
ProcessorCompatibilityMode_Enum._InitializeFacetMap(ProcessorCompatibilityMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProcessorCompatibilityMode.Enum', ProcessorCompatibilityMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PartitionType.Enum
class PartitionType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartitionType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 839, 4)
    _Documentation = None
PartitionType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PartitionType_Enum, enum_prefix=None)
PartitionType_Enum.AIX = PartitionType_Enum._CF_enumeration.addEnumeration(unicode_value='AIX', tag='AIX')
PartitionType_Enum.IBMi = PartitionType_Enum._CF_enumeration.addEnumeration(unicode_value='IBMi', tag='IBMi')
PartitionType_Enum.VIOS = PartitionType_Enum._CF_enumeration.addEnumeration(unicode_value='VIOS', tag='VIOS')
PartitionType_Enum._InitializeFacetMap(PartitionType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PartitionType.Enum', PartitionType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PartitionState.Enum
class PartitionState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartitionState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 847, 2)
    _Documentation = None
PartitionState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PartitionState_Enum, enum_prefix=None)
PartitionState_Enum.Not_Activated = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Not Activated', tag='Not_Activated')
PartitionState_Enum.Starting = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Starting', tag='Starting')
PartitionState_Enum.Running = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
PartitionState_Enum.Shutdown = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Shutdown', tag='Shutdown')
PartitionState_Enum.Error = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Error', tag='Error')
PartitionState_Enum.Open_Firmware = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Open Firmware', tag='Open_Firmware')
PartitionState_Enum.Not_Available = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Not Available', tag='Not_Available')
PartitionState_Enum.Migrating___Not_Active = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Migrating - Not Active', tag='Migrating___Not_Active')
PartitionState_Enum.Migrating___Running = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Migrating - Running', tag='Migrating___Running')
PartitionState_Enum.Hardware_Discovery = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Hardware Discovery', tag='Hardware_Discovery')
PartitionState_Enum.Suspended = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Suspended', tag='Suspended')
PartitionState_Enum.Suspending = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Suspending', tag='Suspending')
PartitionState_Enum.Resuming = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Resuming', tag='Resuming')
PartitionState_Enum.Migrating___Suspended = PartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='Migrating - Suspended', tag='Migrating___Suspended')
PartitionState_Enum._InitializeFacetMap(PartitionState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PartitionState.Enum', PartitionState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ProgressState.Enum
class ProgressState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProgressState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 867, 2)
    _Documentation = ''
ProgressState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProgressState_Enum, enum_prefix=None)
ProgressState_Enum.Hibernate_Preparing = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Hibernate Preparing', tag='Hibernate_Preparing')
ProgressState_Enum.Hibernate_Validating = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Hibernate Validating', tag='Hibernate_Validating')
ProgressState_Enum.Hibernate_Saving_HMC_Data = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Hibernate Saving HMC Data', tag='Hibernate_Saving_HMC_Data')
ProgressState_Enum.Hibernate_Saving_Partition_Data = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Hibernate Saving Partition Data', tag='Hibernate_Saving_Partition_Data')
ProgressState_Enum.Hibernate_Completing = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Hibernate Completing', tag='Hibernate_Completing')
ProgressState_Enum.Resume_Preparing = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Resume Preparing', tag='Resume_Preparing')
ProgressState_Enum.Resume_Reading_HMC_Data = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Resume Reading HMC Data', tag='Resume_Reading_HMC_Data')
ProgressState_Enum.Resume_Validating = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Resume Validating', tag='Resume_Validating')
ProgressState_Enum.Resume_Restoring_Partition_Configuration = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Resume Restoring Partition Configuration', tag='Resume_Restoring_Partition_Configuration')
ProgressState_Enum.Resume_Reading_Partition_Data = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Resume Reading Partition Data', tag='Resume_Reading_Partition_Data')
ProgressState_Enum.Resume_Completing = ProgressState_Enum._CF_enumeration.addEnumeration(unicode_value='Resume Completing', tag='Resume_Completing')
ProgressState_Enum._InitializeFacetMap(ProgressState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProgressState.Enum', ProgressState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}CurrentProfileSync.Enum
class CurrentProfileSync_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CurrentProfileSync.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 890, 3)
    _Documentation = None
CurrentProfileSync_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CurrentProfileSync_Enum, enum_prefix=None)
CurrentProfileSync_Enum.Disabled = CurrentProfileSync_Enum._CF_enumeration.addEnumeration(unicode_value='Disabled', tag='Disabled')
CurrentProfileSync_Enum.On = CurrentProfileSync_Enum._CF_enumeration.addEnumeration(unicode_value='On', tag='On')
CurrentProfileSync_Enum.Suspended = CurrentProfileSync_Enum._CF_enumeration.addEnumeration(unicode_value='Suspended', tag='Suspended')
CurrentProfileSync_Enum._InitializeFacetMap(CurrentProfileSync_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CurrentProfileSync.Enum', CurrentProfileSync_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ManagedFrameType.Enum
class ManagedFrameType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManagedFrameType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 898, 2)
    _Documentation = '\n                \n                 \n            '
ManagedFrameType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ManagedFrameType_Enum, enum_prefix=None)
ManagedFrameType_Enum.HE_BPA = ManagedFrameType_Enum._CF_enumeration.addEnumeration(unicode_value='HE BPA', tag='HE_BPA')
ManagedFrameType_Enum.IH_BPA = ManagedFrameType_Enum._CF_enumeration.addEnumeration(unicode_value='IH BPA', tag='IH_BPA')
ManagedFrameType_Enum.IO_Only = ManagedFrameType_Enum._CF_enumeration.addEnumeration(unicode_value='IO Only', tag='IO_Only')
ManagedFrameType_Enum.PMU_Hitachi_SRX = ManagedFrameType_Enum._CF_enumeration.addEnumeration(unicode_value='PMU-Hitachi SRX', tag='PMU_Hitachi_SRX')
ManagedFrameType_Enum.Unknown = ManagedFrameType_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ManagedFrameType_Enum._InitializeFacetMap(ManagedFrameType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ManagedFrameType.Enum', ManagedFrameType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ManagedFrameState.Enum
class ManagedFrameState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManagedFrameState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 959, 4)
    _Documentation = '\n                \n                 \n            '
ManagedFrameState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ManagedFrameState_Enum, enum_prefix=None)
ManagedFrameState_Enum.BPA_H_System = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='BPA (H System)', tag='BPA_H_System')
ManagedFrameState_Enum.BPA_IH_System = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='BPA (IH System)', tag='BPA_IH_System')
ManagedFrameState_Enum.BPA_IO_Only_Frame = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='BPA (IO-Only Frame)', tag='BPA_IO_Only_Frame')
ManagedFrameState_Enum.CUoD_Click_to_Accept = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='CUoD Click to Accept', tag='CUoD_Click_to_Accept')
ManagedFrameState_Enum.Error = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Error', tag='Error')
ManagedFrameState_Enum.Error_Dump_in_progress = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Error-Dump in progress', tag='Error_Dump_in_progress')
ManagedFrameState_Enum.Error_Terminated = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Error-Terminated', tag='Error_Terminated')
ManagedFrameState_Enum.Failed_Authentication = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Failed Authentication', tag='Failed_Authentication')
ManagedFrameState_Enum.Incomplete = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Incomplete', tag='Incomplete')
ManagedFrameState_Enum.No_Connection = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='No Connection', tag='No_Connection')
ManagedFrameState_Enum.On_Demand_Recovery = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='On Demand Recovery', tag='On_Demand_Recovery')
ManagedFrameState_Enum.Operating = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Operating', tag='Operating')
ManagedFrameState_Enum.Pending_Authentication___Password_Updates_Required = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Pending Authentication - Password Updates Required', tag='Pending_Authentication___Password_Updates_Required')
ManagedFrameState_Enum.Pending_Frame_Number = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Pending Frame Number', tag='Pending_Frame_Number')
ManagedFrameState_Enum.PMU___Hitachi_SRX = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='PMU - Hitachi SRX', tag='PMU___Hitachi_SRX')
ManagedFrameState_Enum.Power_Off = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Power Off', tag='Power_Off')
ManagedFrameState_Enum.Power_Off_In_Progress = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Power Off In Progress', tag='Power_Off_In_Progress')
ManagedFrameState_Enum.Rack_StandbyNot_Available = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Rack Standby/Not Available', tag='Rack_StandbyNot_Available')
ManagedFrameState_Enum.Rack_StandbyRack_Standby = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Rack Standby/Rack Standby', tag='Rack_StandbyRack_Standby')
ManagedFrameState_Enum.Rack_StandbyStarting = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Rack Standby/Starting', tag='Rack_StandbyStarting')
ManagedFrameState_Enum.Recovery = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Recovery', tag='Recovery')
ManagedFrameState_Enum.Running = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
ManagedFrameState_Enum.Service_processor_static_failover_error = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Service processor static failover error', tag='Service_processor_static_failover_error')
ManagedFrameState_Enum.Standby = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Standby', tag='Standby')
ManagedFrameState_Enum.StandbyNot_Available = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Standby/Not Available', tag='StandbyNot_Available')
ManagedFrameState_Enum.StandbyStandby = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Standby/Standby', tag='StandbyStandby')
ManagedFrameState_Enum.StandbyStarting = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Standby/Starting', tag='StandbyStarting')
ManagedFrameState_Enum.StartingUnknown = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Starting/Unknown', tag='StartingUnknown')
ManagedFrameState_Enum.Version_Mismatch = ManagedFrameState_Enum._CF_enumeration.addEnumeration(unicode_value='Version Mismatch', tag='Version_Mismatch')
ManagedFrameState_Enum._InitializeFacetMap(ManagedFrameState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ManagedFrameState.Enum', ManagedFrameState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}FunctionalState.Enum
class FunctionalState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FunctionalState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1237, 1)
    _Documentation = None
FunctionalState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FunctionalState_Enum, enum_prefix=None)
FunctionalState_Enum.NonFunctional = FunctionalState_Enum._CF_enumeration.addEnumeration(unicode_value='NonFunctional', tag='NonFunctional')
FunctionalState_Enum.Functional = FunctionalState_Enum._CF_enumeration.addEnumeration(unicode_value='Functional', tag='Functional')
FunctionalState_Enum._InitializeFacetMap(FunctionalState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FunctionalState.Enum', FunctionalState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SharedEthernetAdapterHighAvailabilityMode.Enum
class SharedEthernetAdapterHighAvailabilityMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SharedEthernetAdapterHighAvailabilityMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1244, 4)
    _Documentation = '\n                \n                 \n            '
SharedEthernetAdapterHighAvailabilityMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SharedEthernetAdapterHighAvailabilityMode_Enum, enum_prefix=None)
SharedEthernetAdapterHighAvailabilityMode_Enum.Disabled = SharedEthernetAdapterHighAvailabilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='Disabled', tag='Disabled')
SharedEthernetAdapterHighAvailabilityMode_Enum.Auto = SharedEthernetAdapterHighAvailabilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='Auto', tag='Auto')
SharedEthernetAdapterHighAvailabilityMode_Enum.Standby = SharedEthernetAdapterHighAvailabilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='Standby', tag='Standby')
SharedEthernetAdapterHighAvailabilityMode_Enum._InitializeFacetMap(SharedEthernetAdapterHighAvailabilityMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SharedEthernetAdapterHighAvailabilityMode.Enum', SharedEthernetAdapterHighAvailabilityMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VitalProductDataStale.Enum
class VitalProductDataStale_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VitalProductDataStale.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1287, 3)
    _Documentation = '\n                \n                 \n            '
VitalProductDataStale_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VitalProductDataStale_Enum, enum_prefix=None)
VitalProductDataStale_Enum.NoVPD = VitalProductDataStale_Enum._CF_enumeration.addEnumeration(unicode_value='NoVPD', tag='NoVPD')
VitalProductDataStale_Enum.ValidVPD = VitalProductDataStale_Enum._CF_enumeration.addEnumeration(unicode_value='ValidVPD', tag='ValidVPD')
VitalProductDataStale_Enum.StaleVPD = VitalProductDataStale_Enum._CF_enumeration.addEnumeration(unicode_value='StaleVPD', tag='StaleVPD')
VitalProductDataStale_Enum._InitializeFacetMap(VitalProductDataStale_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VitalProductDataStale.Enum', VitalProductDataStale_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HostChannelAdapterCableType.Enum
class HostChannelAdapterCableType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HostChannelAdapterCableType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1331, 4)
    _Documentation = '\n                \n                 \n            '
HostChannelAdapterCableType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HostChannelAdapterCableType_Enum, enum_prefix=None)
HostChannelAdapterCableType_Enum.Cable = HostChannelAdapterCableType_Enum._CF_enumeration.addEnumeration(unicode_value='Cable', tag='Cable')
HostChannelAdapterCableType_Enum.Fiber = HostChannelAdapterCableType_Enum._CF_enumeration.addEnumeration(unicode_value='Fiber', tag='Fiber')
HostChannelAdapterCableType_Enum._InitializeFacetMap(HostChannelAdapterCableType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HostChannelAdapterCableType.Enum', HostChannelAdapterCableType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HostChannelAdapterCapability.Enum
class HostChannelAdapterCapability_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HostChannelAdapterCapability.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1365, 4)
    _Documentation = None
HostChannelAdapterCapability_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HostChannelAdapterCapability_Enum, enum_prefix=None)
HostChannelAdapterCapability_Enum.dedicated = HostChannelAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='dedicated', tag='dedicated')
HostChannelAdapterCapability_Enum.high = HostChannelAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='high', tag='high')
HostChannelAdapterCapability_Enum.medium = HostChannelAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='medium', tag='medium')
HostChannelAdapterCapability_Enum.low = HostChannelAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='low', tag='low')
HostChannelAdapterCapability_Enum._InitializeFacetMap(HostChannelAdapterCapability_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HostChannelAdapterCapability.Enum', HostChannelAdapterCapability_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SEAQoSMode.Enum
class SEAQoSMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SEAQoSMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1374, 2)
    _Documentation = None
SEAQoSMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SEAQoSMode_Enum, enum_prefix=None)
SEAQoSMode_Enum.disabled = SEAQoSMode_Enum._CF_enumeration.addEnumeration(unicode_value='disabled', tag='disabled')
SEAQoSMode_Enum.strict = SEAQoSMode_Enum._CF_enumeration.addEnumeration(unicode_value='strict', tag='strict')
SEAQoSMode_Enum.loose = SEAQoSMode_Enum._CF_enumeration.addEnumeration(unicode_value='loose', tag='loose')
SEAQoSMode_Enum._InitializeFacetMap(SEAQoSMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SEAQoSMode.Enum', SEAQoSMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MediaSpeed.Enum
class MediaSpeed_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MediaSpeed.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1382, 3)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
MediaSpeed_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MediaSpeed_Enum, enum_prefix=None)
MediaSpeed_Enum.E10_Full_Duplex = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E10_Full_Duplex', tag='E10_Full_Duplex')
MediaSpeed_Enum.E10_Half_Duplex = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E10_Half_Duplex', tag='E10_Half_Duplex')
MediaSpeed_Enum.E100_Full_Duplex = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E100_Full_Duplex', tag='E100_Full_Duplex')
MediaSpeed_Enum.E100_Half_Duplex = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E100_Half_Duplex', tag='E100_Half_Duplex')
MediaSpeed_Enum.E1000_Full_Duplex = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E1000_Full_Duplex', tag='E1000_Full_Duplex')
MediaSpeed_Enum.E1000_Full_Duplex_ = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E1000_Full_Duplex', tag='E1000_Full_Duplex_')
MediaSpeed_Enum.Auto_Negotiation = MediaSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='Auto_Negotiation', tag='Auto_Negotiation')
MediaSpeed_Enum._InitializeFacetMap(MediaSpeed_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MediaSpeed.Enum', MediaSpeed_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}InstallationType.Enum
class InstallationType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstallationType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1457, 2)
    _Documentation = None
InstallationType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=InstallationType_Enum, enum_prefix=None)
InstallationType_Enum.DVD = InstallationType_Enum._CF_enumeration.addEnumeration(unicode_value='DVD', tag='DVD')
InstallationType_Enum.Image = InstallationType_Enum._CF_enumeration.addEnumeration(unicode_value='Image', tag='Image')
InstallationType_Enum.NIM = InstallationType_Enum._CF_enumeration.addEnumeration(unicode_value='NIM', tag='NIM')
InstallationType_Enum._InitializeFacetMap(InstallationType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'InstallationType.Enum', InstallationType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}DuplexMode.Enum
class DuplexMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DuplexMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1465, 3)
    _Documentation = None
DuplexMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DuplexMode_Enum, enum_prefix=None)
DuplexMode_Enum.auto = DuplexMode_Enum._CF_enumeration.addEnumeration(unicode_value='auto', tag='auto')
DuplexMode_Enum.half = DuplexMode_Enum._CF_enumeration.addEnumeration(unicode_value='half', tag='half')
DuplexMode_Enum.full = DuplexMode_Enum._CF_enumeration.addEnumeration(unicode_value='full', tag='full')
DuplexMode_Enum._InitializeFacetMap(DuplexMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'DuplexMode.Enum', DuplexMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SRIOVConnectionSpeed.Enum
class SRIOVConnectionSpeed_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SRIOVConnectionSpeed.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1472, 3)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
SRIOVConnectionSpeed_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SRIOVConnectionSpeed_Enum, enum_prefix=None)
SRIOVConnectionSpeed_Enum.E100Gbps = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E100Gbps', tag='E100Gbps')
SRIOVConnectionSpeed_Enum.E100Mbps = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E100Mbps', tag='E100Mbps')
SRIOVConnectionSpeed_Enum.E10Gbps = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E10Gbps', tag='E10Gbps')
SRIOVConnectionSpeed_Enum.E10Mbps = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E10Mbps', tag='E10Mbps')
SRIOVConnectionSpeed_Enum.E1Gbps = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E1Gbps', tag='E1Gbps')
SRIOVConnectionSpeed_Enum.E40Gbps = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E40Gbps', tag='E40Gbps')
SRIOVConnectionSpeed_Enum.Auto = SRIOVConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='Auto', tag='Auto')
SRIOVConnectionSpeed_Enum._InitializeFacetMap(SRIOVConnectionSpeed_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SRIOVConnectionSpeed.Enum', SRIOVConnectionSpeed_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PhysicalVolumeState.Enum
class PhysicalVolumeState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhysicalVolumeState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1551, 4)
    _Documentation = None
PhysicalVolumeState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PhysicalVolumeState_Enum, enum_prefix=None)
PhysicalVolumeState_Enum.online = PhysicalVolumeState_Enum._CF_enumeration.addEnumeration(unicode_value='online', tag='online')
PhysicalVolumeState_Enum.stopped = PhysicalVolumeState_Enum._CF_enumeration.addEnumeration(unicode_value='stopped', tag='stopped')
PhysicalVolumeState_Enum.failed = PhysicalVolumeState_Enum._CF_enumeration.addEnumeration(unicode_value='failed', tag='failed')
PhysicalVolumeState_Enum.missing = PhysicalVolumeState_Enum._CF_enumeration.addEnumeration(unicode_value='missing', tag='missing')
PhysicalVolumeState_Enum._InitializeFacetMap(PhysicalVolumeState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PhysicalVolumeState.Enum', PhysicalVolumeState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PhysicalVolumeReservePolicy.Enum
class PhysicalVolumeReservePolicy_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhysicalVolumeReservePolicy.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1560, 3)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PhysicalVolumeReservePolicy_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PhysicalVolumeReservePolicy_Enum, enum_prefix=None)
PhysicalVolumeReservePolicy_Enum.ClusterReserve = PhysicalVolumeReservePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='ClusterReserve', tag='ClusterReserve')
PhysicalVolumeReservePolicy_Enum.ExclusivePersistent = PhysicalVolumeReservePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='ExclusivePersistent', tag='ExclusivePersistent')
PhysicalVolumeReservePolicy_Enum.NoReserve = PhysicalVolumeReservePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='NoReserve', tag='NoReserve')
PhysicalVolumeReservePolicy_Enum.SCSI_2 = PhysicalVolumeReservePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='SCSI-2', tag='SCSI_2')
PhysicalVolumeReservePolicy_Enum.SharedPersistent = PhysicalVolumeReservePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='SharedPersistent', tag='SharedPersistent')
PhysicalVolumeReservePolicy_Enum.SinglePath = PhysicalVolumeReservePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='SinglePath', tag='SinglePath')
PhysicalVolumeReservePolicy_Enum._InitializeFacetMap(PhysicalVolumeReservePolicy_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PhysicalVolumeReservePolicy.Enum', PhysicalVolumeReservePolicy_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PhysicalVolumeUsage.Enum
class PhysicalVolumeUsage_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhysicalVolumeUsage.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1626, 4)
    _Documentation = None
PhysicalVolumeUsage_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PhysicalVolumeUsage_Enum, enum_prefix=None)
PhysicalVolumeUsage_Enum.UNUSED = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='UNUSED', tag='UNUSED')
PhysicalVolumeUsage_Enum.DISK = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='DISK', tag='DISK')
PhysicalVolumeUsage_Enum.AMS = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='AMS', tag='AMS')
PhysicalVolumeUsage_Enum.HIBERNATION = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='HIBERNATION', tag='HIBERNATION')
PhysicalVolumeUsage_Enum.IMAGE = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='IMAGE', tag='IMAGE')
PhysicalVolumeUsage_Enum.VSCSI = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='VSCSI', tag='VSCSI')
PhysicalVolumeUsage_Enum.VG = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
PhysicalVolumeUsage_Enum.VSS_POOL = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='VSS_POOL', tag='VSS_POOL')
PhysicalVolumeUsage_Enum.OPTICALIMAGE = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='OPTICALIMAGE', tag='OPTICALIMAGE')
PhysicalVolumeUsage_Enum.OPTICALIMAGEIM = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='OPTICALIMAGEIM', tag='OPTICALIMAGEIM')
PhysicalVolumeUsage_Enum.HIDDEN_DISK = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='HIDDEN_DISK', tag='HIDDEN_DISK')
PhysicalVolumeUsage_Enum.REPO = PhysicalVolumeUsage_Enum._CF_enumeration.addEnumeration(unicode_value='REPO', tag='REPO')
PhysicalVolumeUsage_Enum._InitializeFacetMap(PhysicalVolumeUsage_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PhysicalVolumeUsage.Enum', PhysicalVolumeUsage_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SCSIReservePolicyAlgo.Enum
class SCSIReservePolicyAlgo_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCSIReservePolicyAlgo.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1642, 4)
    _Documentation = None
SCSIReservePolicyAlgo_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SCSIReservePolicyAlgo_Enum, enum_prefix=None)
SCSIReservePolicyAlgo_Enum.Failover = SCSIReservePolicyAlgo_Enum._CF_enumeration.addEnumeration(unicode_value='Failover', tag='Failover')
SCSIReservePolicyAlgo_Enum.Round_Robin = SCSIReservePolicyAlgo_Enum._CF_enumeration.addEnumeration(unicode_value='Round Robin', tag='Round_Robin')
SCSIReservePolicyAlgo_Enum.Load_Balance = SCSIReservePolicyAlgo_Enum._CF_enumeration.addEnumeration(unicode_value='Load Balance', tag='Load_Balance')
SCSIReservePolicyAlgo_Enum._InitializeFacetMap(SCSIReservePolicyAlgo_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SCSIReservePolicyAlgo.Enum', SCSIReservePolicyAlgo_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ResourceMonitoringControlState.Enum
class ResourceMonitoringControlState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResourceMonitoringControlState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1649, 3)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
ResourceMonitoringControlState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ResourceMonitoringControlState_Enum, enum_prefix=None)
ResourceMonitoringControlState_Enum.active = ResourceMonitoringControlState_Enum._CF_enumeration.addEnumeration(unicode_value='active', tag='active')
ResourceMonitoringControlState_Enum.inactive = ResourceMonitoringControlState_Enum._CF_enumeration.addEnumeration(unicode_value='inactive', tag='inactive')
ResourceMonitoringControlState_Enum.none = ResourceMonitoringControlState_Enum._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
ResourceMonitoringControlState_Enum.unknown = ResourceMonitoringControlState_Enum._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
ResourceMonitoringControlState_Enum._InitializeFacetMap(ResourceMonitoringControlState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ResourceMonitoringControlState.Enum', ResourceMonitoringControlState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ProfileType.Enum
class ProfileType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProfileType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1700, 4)
    _Documentation = None
ProfileType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProfileType_Enum, enum_prefix=None)
ProfileType_Enum.Default = ProfileType_Enum._CF_enumeration.addEnumeration(unicode_value='Default', tag='Default')
ProfileType_Enum.LastActivated = ProfileType_Enum._CF_enumeration.addEnumeration(unicode_value='LastActivated', tag='LastActivated')
ProfileType_Enum.Current = ProfileType_Enum._CF_enumeration.addEnumeration(unicode_value='Current', tag='Current')
ProfileType_Enum.Other = ProfileType_Enum._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
ProfileType_Enum._InitializeFacetMap(ProfileType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProfileType.Enum', ProfileType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ProcessorSharingMode.Enum
class ProcessorSharingMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProcessorSharingMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1709, 4)
    _Documentation = None
ProcessorSharingMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ProcessorSharingMode_Enum, enum_prefix=None)
ProcessorSharingMode_Enum.Keep_unused_processors = ProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='Keep unused processors', tag='Keep_unused_processors')
ProcessorSharingMode_Enum.Do_not_share = ProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='Do not share', tag='Do_not_share')
ProcessorSharingMode_Enum.Share_unused_processors = ProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='Share unused processors', tag='Share_unused_processors')
ProcessorSharingMode_Enum._InitializeFacetMap(ProcessorSharingMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProcessorSharingMode.Enum', ProcessorSharingMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LogicalHostEthernetAdapterCapability.Enum
class LogicalHostEthernetAdapterCapability_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicalHostEthernetAdapterCapability.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1717, 4)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LogicalHostEthernetAdapterCapability_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogicalHostEthernetAdapterCapability_Enum, enum_prefix=None)
LogicalHostEthernetAdapterCapability_Enum.Base_Minimum = LogicalHostEthernetAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='Base Minimum', tag='Base_Minimum')
LogicalHostEthernetAdapterCapability_Enum.Dedicated = LogicalHostEthernetAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='Dedicated', tag='Dedicated')
LogicalHostEthernetAdapterCapability_Enum.Defined_Resource_Amounts = LogicalHostEthernetAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='Defined Resource Amounts', tag='Defined_Resource_Amounts')
LogicalHostEthernetAdapterCapability_Enum.High = LogicalHostEthernetAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='High', tag='High')
LogicalHostEthernetAdapterCapability_Enum.Low = LogicalHostEthernetAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='Low', tag='Low')
LogicalHostEthernetAdapterCapability_Enum.Medium = LogicalHostEthernetAdapterCapability_Enum._CF_enumeration.addEnumeration(unicode_value='Medium', tag='Medium')
LogicalHostEthernetAdapterCapability_Enum._InitializeFacetMap(LogicalHostEthernetAdapterCapability_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogicalHostEthernetAdapterCapability.Enum', LogicalHostEthernetAdapterCapability_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}CageType.Enum
class CageType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CageType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1790, 4)
    _Documentation = None
CageType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CageType_Enum, enum_prefix=None)
CageType_Enum.BPA = CageType_Enum._CF_enumeration.addEnumeration(unicode_value='BPA', tag='BPA')
CageType_Enum.System = CageType_Enum._CF_enumeration.addEnumeration(unicode_value='System', tag='System')
CageType_Enum.IO = CageType_Enum._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
CageType_Enum.Disk_Enclosure = CageType_Enum._CF_enumeration.addEnumeration(unicode_value='Disk Enclosure', tag='Disk_Enclosure')
CageType_Enum.Fans = CageType_Enum._CF_enumeration.addEnumeration(unicode_value='Fans', tag='Fans')
CageType_Enum.None_ = CageType_Enum._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
CageType_Enum._InitializeFacetMap(CageType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CageType.Enum', CageType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}StorageDeviceState.Enum
class StorageDeviceState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageDeviceState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1800, 4)
    _Documentation = None
StorageDeviceState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StorageDeviceState_Enum, enum_prefix=None)
StorageDeviceState_Enum.active = StorageDeviceState_Enum._CF_enumeration.addEnumeration(unicode_value='active', tag='active')
StorageDeviceState_Enum.inactive = StorageDeviceState_Enum._CF_enumeration.addEnumeration(unicode_value='inactive', tag='inactive')
StorageDeviceState_Enum.missing_backing_device = StorageDeviceState_Enum._CF_enumeration.addEnumeration(unicode_value='missing backing device', tag='missing_backing_device')
StorageDeviceState_Enum.defined = StorageDeviceState_Enum._CF_enumeration.addEnumeration(unicode_value='defined', tag='defined')
StorageDeviceState_Enum._InitializeFacetMap(StorageDeviceState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StorageDeviceState.Enum', StorageDeviceState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}StorageDeviceType.Enum
class StorageDeviceType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StorageDeviceType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1808, 2)
    _Documentation = None
StorageDeviceType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StorageDeviceType_Enum, enum_prefix=None)
StorageDeviceType_Enum.logical = StorageDeviceType_Enum._CF_enumeration.addEnumeration(unicode_value='logical', tag='logical')
StorageDeviceType_Enum.phys = StorageDeviceType_Enum._CF_enumeration.addEnumeration(unicode_value='phys', tag='phys')
StorageDeviceType_Enum.sspLU = StorageDeviceType_Enum._CF_enumeration.addEnumeration(unicode_value='sspLU', tag='sspLU')
StorageDeviceType_Enum._InitializeFacetMap(StorageDeviceType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'StorageDeviceType.Enum', StorageDeviceType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HostEthernetAdapterPhysicalPortType.Enum
class HostEthernetAdapterPhysicalPortType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HostEthernetAdapterPhysicalPortType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1816, 3)
    _Documentation = '\n                \n                 \n            '
HostEthernetAdapterPhysicalPortType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HostEthernetAdapterPhysicalPortType_Enum, enum_prefix=None)
HostEthernetAdapterPhysicalPortType_Enum.E1Gbps = HostEthernetAdapterPhysicalPortType_Enum._CF_enumeration.addEnumeration(unicode_value='E1Gbps', tag='E1Gbps')
HostEthernetAdapterPhysicalPortType_Enum.E10Gbps = HostEthernetAdapterPhysicalPortType_Enum._CF_enumeration.addEnumeration(unicode_value='E10Gbps', tag='E10Gbps')
HostEthernetAdapterPhysicalPortType_Enum._InitializeFacetMap(HostEthernetAdapterPhysicalPortType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HostEthernetAdapterPhysicalPortType.Enum', HostEthernetAdapterPhysicalPortType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}EthernetFrameSize.Enum
class EthernetFrameSize_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EthernetFrameSize.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1850, 6)
    _Documentation = None
EthernetFrameSize_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EthernetFrameSize_Enum, enum_prefix=None)
EthernetFrameSize_Enum.Non_Jumbo_1500_Byte = EthernetFrameSize_Enum._CF_enumeration.addEnumeration(unicode_value='Non-Jumbo 1500 Byte', tag='Non_Jumbo_1500_Byte')
EthernetFrameSize_Enum.Jumbo_9000_Byte = EthernetFrameSize_Enum._CF_enumeration.addEnumeration(unicode_value='Jumbo 9000 Byte', tag='Jumbo_9000_Byte')
EthernetFrameSize_Enum._InitializeFacetMap(EthernetFrameSize_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'EthernetFrameSize.Enum', EthernetFrameSize_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HEALogicalPortState.Enum
class HEALogicalPortState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HEALogicalPortState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1858, 3)
    _Documentation = None
HEALogicalPortState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HEALogicalPortState_Enum, enum_prefix=None)
HEALogicalPortState_Enum.Available = HEALogicalPortState_Enum._CF_enumeration.addEnumeration(unicode_value='Available', tag='Available')
HEALogicalPortState_Enum.Unavailable = HEALogicalPortState_Enum._CF_enumeration.addEnumeration(unicode_value='Unavailable', tag='Unavailable')
HEALogicalPortState_Enum._InitializeFacetMap(HEALogicalPortState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HEALogicalPortState.Enum', HEALogicalPortState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VirtualSwitchMode.Enum
class VirtualSwitchMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VirtualSwitchMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1865, 4)
    _Documentation = None
VirtualSwitchMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VirtualSwitchMode_Enum, enum_prefix=None)
VirtualSwitchMode_Enum.VEB = VirtualSwitchMode_Enum._CF_enumeration.addEnumeration(unicode_value='VEB', tag='VEB')
VirtualSwitchMode_Enum.VEPA = VirtualSwitchMode_Enum._CF_enumeration.addEnumeration(unicode_value='VEPA', tag='VEPA')
VirtualSwitchMode_Enum._InitializeFacetMap(VirtualSwitchMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VirtualSwitchMode.Enum', VirtualSwitchMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VirtualStationInterfaceType.Enum
class VirtualStationInterfaceType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VirtualStationInterfaceType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1873, 4)
    _Documentation = '\n                \n                 \n            '
VirtualStationInterfaceType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VirtualStationInterfaceType_Enum, enum_prefix=None)
VirtualStationInterfaceType_Enum.Pre_Associate = VirtualStationInterfaceType_Enum._CF_enumeration.addEnumeration(unicode_value='Pre-Associate', tag='Pre_Associate')
VirtualStationInterfaceType_Enum.Pre_Associate_With_Resource_Reservation = VirtualStationInterfaceType_Enum._CF_enumeration.addEnumeration(unicode_value='Pre-Associate_With_Resource_Reservation', tag='Pre_Associate_With_Resource_Reservation')
VirtualStationInterfaceType_Enum.Associate = VirtualStationInterfaceType_Enum._CF_enumeration.addEnumeration(unicode_value='Associate', tag='Associate')
VirtualStationInterfaceType_Enum.De_Associate = VirtualStationInterfaceType_Enum._CF_enumeration.addEnumeration(unicode_value='De-Associate', tag='De_Associate')
VirtualStationInterfaceType_Enum.VSI_Manager_ID = VirtualStationInterfaceType_Enum._CF_enumeration.addEnumeration(unicode_value='VSI_Manager_ID', tag='VSI_Manager_ID')
VirtualStationInterfaceType_Enum.Organizationally_Defined_TLV = VirtualStationInterfaceType_Enum._CF_enumeration.addEnumeration(unicode_value='Organizationally_Defined_TLV', tag='Organizationally_Defined_TLV')
VirtualStationInterfaceType_Enum._InitializeFacetMap(VirtualStationInterfaceType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VirtualStationInterfaceType.Enum', VirtualStationInterfaceType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IOAdapterType.Enum
class IOAdapterType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IOAdapterType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 1943, 3)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
IOAdapterType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IOAdapterType_Enum, enum_prefix=None)
IOAdapterType_Enum.HostEthernetAdapter = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='HostEthernetAdapter', tag='HostEthernetAdapter')
IOAdapterType_Enum.physicalEthernetAdpter = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physicalEthernetAdpter', tag='physicalEthernetAdpter')
IOAdapterType_Enum.physical_FiberCnnel = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physical_FiberCnnel', tag='physical_FiberCnnel')
IOAdapterType_Enum.physical_FiberCnnel_OverEthernetAdapter = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physical_FiberCnnel_OverEthernetAdapter', tag='physical_FiberCnnel_OverEthernetAdapter')
IOAdapterType_Enum.physicalopticaldrive = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physicalopticaldrive', tag='physicalopticaldrive')
IOAdapterType_Enum.physicalcontroller = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physicalcontroller', tag='physicalcontroller')
IOAdapterType_Enum.physicalSASController = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physicalSASController', tag='physicalSASController')
IOAdapterType_Enum.physicalSCSIAdapter = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='physicalSCSIAdapter', tag='physicalSCSIAdapter')
IOAdapterType_Enum.SRIOV_Adapter = IOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='SRIOV_Adapter', tag='SRIOV_Adapter')
IOAdapterType_Enum._InitializeFacetMap(IOAdapterType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IOAdapterType.Enum', IOAdapterType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ConnectionSpeed.Enum
class ConnectionSpeed_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConnectionSpeed.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2046, 2)
    _Documentation = '\n                \n                 \n            '
ConnectionSpeed_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConnectionSpeed_Enum, enum_prefix=None)
ConnectionSpeed_Enum.auto = ConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='auto', tag='auto')
ConnectionSpeed_Enum.E10Mbps = ConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E10Mbps', tag='E10Mbps')
ConnectionSpeed_Enum.E100Mbps = ConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E100Mbps', tag='E100Mbps')
ConnectionSpeed_Enum.E1Gbps = ConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E1Gbps', tag='E1Gbps')
ConnectionSpeed_Enum.E10Gbps = ConnectionSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='E10Gbps', tag='E10Gbps')
ConnectionSpeed_Enum._InitializeFacetMap(ConnectionSpeed_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ConnectionSpeed.Enum', ConnectionSpeed_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LinkAggregationHashMode.Enum
class LinkAggregationHashMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinkAggregationHashMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2105, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LinkAggregationHashMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LinkAggregationHashMode_Enum, enum_prefix=None)
LinkAggregationHashMode_Enum.default = LinkAggregationHashMode_Enum._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
LinkAggregationHashMode_Enum.dst_port = LinkAggregationHashMode_Enum._CF_enumeration.addEnumeration(unicode_value='dst_port', tag='dst_port')
LinkAggregationHashMode_Enum.src_dst_port = LinkAggregationHashMode_Enum._CF_enumeration.addEnumeration(unicode_value='src_dst_port', tag='src_dst_port')
LinkAggregationHashMode_Enum.src_port = LinkAggregationHashMode_Enum._CF_enumeration.addEnumeration(unicode_value='src_port', tag='src_port')
LinkAggregationHashMode_Enum._InitializeFacetMap(LinkAggregationHashMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LinkAggregationHashMode.Enum', LinkAggregationHashMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LinkAggregationMode.Enum
class LinkAggregationMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinkAggregationMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2156, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LinkAggregationMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LinkAggregationMode_Enum, enum_prefix=None)
LinkAggregationMode_Enum.IEEE8023ad = LinkAggregationMode_Enum._CF_enumeration.addEnumeration(unicode_value='IEEE8023ad', tag='IEEE8023ad')
LinkAggregationMode_Enum.round_robin = LinkAggregationMode_Enum._CF_enumeration.addEnumeration(unicode_value='round_robin', tag='round_robin')
LinkAggregationMode_Enum.standard = LinkAggregationMode_Enum._CF_enumeration.addEnumeration(unicode_value='standard', tag='standard')
LinkAggregationMode_Enum._InitializeFacetMap(LinkAggregationMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LinkAggregationMode.Enum', LinkAggregationMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VirtualIOAdapterType.Enum
class VirtualIOAdapterType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VirtualIOAdapterType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2200, 1)
    _Documentation = '\n                \n                 \n            '
VirtualIOAdapterType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VirtualIOAdapterType_Enum, enum_prefix=None)
VirtualIOAdapterType_Enum.SERVER = VirtualIOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='SERVER', tag='SERVER')
VirtualIOAdapterType_Enum.CLIENT = VirtualIOAdapterType_Enum._CF_enumeration.addEnumeration(unicode_value='CLIENT', tag='CLIENT')
VirtualIOAdapterType_Enum._InitializeFacetMap(VirtualIOAdapterType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VirtualIOAdapterType.Enum', VirtualIOAdapterType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AddressBroadcastPerformancePolicy.Enum
class AddressBroadcastPerformancePolicy_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressBroadcastPerformancePolicy.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2236, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
AddressBroadcastPerformancePolicy_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=AddressBroadcastPerformancePolicy_Enum, enum_prefix=None)
AddressBroadcastPerformancePolicy_Enum.Chip_Affinity = AddressBroadcastPerformancePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='Chip Affinity', tag='Chip_Affinity')
AddressBroadcastPerformancePolicy_Enum.No_Affinity = AddressBroadcastPerformancePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='No Affinity', tag='No_Affinity')
AddressBroadcastPerformancePolicy_Enum.Node_Affinity = AddressBroadcastPerformancePolicy_Enum._CF_enumeration.addEnumeration(unicode_value='Node Affinity', tag='Node_Affinity')
AddressBroadcastPerformancePolicy_Enum._InitializeFacetMap(AddressBroadcastPerformancePolicy_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'AddressBroadcastPerformancePolicy.Enum', AddressBroadcastPerformancePolicy_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MemoryMirroringMode.Enum
class MemoryMirroringMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MemoryMirroringMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2281, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
MemoryMirroringMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MemoryMirroringMode_Enum, enum_prefix=None)
MemoryMirroringMode_Enum.none = MemoryMirroringMode_Enum._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
MemoryMirroringMode_Enum.system_firmware_only = MemoryMirroringMode_Enum._CF_enumeration.addEnumeration(unicode_value='system firmware only', tag='system_firmware_only')
MemoryMirroringMode_Enum._InitializeFacetMap(MemoryMirroringMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MemoryMirroringMode.Enum', MemoryMirroringMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}FullSystemPartitionIPLMode.Enum
class FullSystemPartitionIPLMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FullSystemPartitionIPLMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2316, 2)
    _Documentation = '\n                \n                 \n            '
FullSystemPartitionIPLMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FullSystemPartitionIPLMode_Enum, enum_prefix=None)
FullSystemPartitionIPLMode_Enum.TODO = FullSystemPartitionIPLMode_Enum._CF_enumeration.addEnumeration(unicode_value='TODO', tag='TODO')
FullSystemPartitionIPLMode_Enum._InitializeFacetMap(FullSystemPartitionIPLMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'FullSystemPartitionIPLMode.Enum', FullSystemPartitionIPLMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LogicalPartitionProcessorCompatibilityMode.Enum
class LogicalPartitionProcessorCompatibilityMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicalPartitionProcessorCompatibilityMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2341, 4)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogicalPartitionProcessorCompatibilityMode_Enum, enum_prefix=None)
LogicalPartitionProcessorCompatibilityMode_Enum.default = LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
LogicalPartitionProcessorCompatibilityMode_Enum.POWER6 = LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER6', tag='POWER6')
LogicalPartitionProcessorCompatibilityMode_Enum.POWER6_Plus = LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER6_Plus', tag='POWER6_Plus')
LogicalPartitionProcessorCompatibilityMode_Enum.POWER7 = LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER7', tag='POWER7')
LogicalPartitionProcessorCompatibilityMode_Enum.POWER7_Plus = LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration.addEnumeration(unicode_value='POWER7_Plus', tag='POWER7_Plus')
LogicalPartitionProcessorCompatibilityMode_Enum._InitializeFacetMap(LogicalPartitionProcessorCompatibilityMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogicalPartitionProcessorCompatibilityMode.Enum', LogicalPartitionProcessorCompatibilityMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}BootMode.Enum
class BootMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BootMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2402, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
BootMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BootMode_Enum, enum_prefix=None)
BootMode_Enum.Diagnostic_with_Default_Boot_List = BootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Diagnostic with Default Boot List', tag='Diagnostic_with_Default_Boot_List')
BootMode_Enum.Diagnostic_with_Stored_Boot_List = BootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Diagnostic with Stored Boot List', tag='Diagnostic_with_Stored_Boot_List')
BootMode_Enum.Normal = BootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Normal', tag='Normal')
BootMode_Enum.Open_Firmware_OK_Prompt = BootMode_Enum._CF_enumeration.addEnumeration(unicode_value='Open Firmware OK Prompt', tag='Open_Firmware_OK_Prompt')
BootMode_Enum.System_Management_Services = BootMode_Enum._CF_enumeration.addEnumeration(unicode_value='System Management Services', tag='System_Management_Services')
BootMode_Enum._InitializeFacetMap(BootMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'BootMode.Enum', BootMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LogicalPartitionState.Enum
class LogicalPartitionState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicalPartitionState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2472, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LogicalPartitionState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogicalPartitionState_Enum, enum_prefix=None)
LogicalPartitionState_Enum.error = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='error', tag='error')
LogicalPartitionState_Enum.not_activated = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='not activated', tag='not_activated')
LogicalPartitionState_Enum.not_available = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='not available', tag='not_available')
LogicalPartitionState_Enum.open_firmware = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='open firmware', tag='open_firmware')
LogicalPartitionState_Enum.running = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='running', tag='running')
LogicalPartitionState_Enum.shutting_down = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='shutting down', tag='shutting_down')
LogicalPartitionState_Enum.starting = LogicalPartitionState_Enum._CF_enumeration.addEnumeration(unicode_value='starting', tag='starting')
LogicalPartitionState_Enum._InitializeFacetMap(LogicalPartitionState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogicalPartitionState.Enum', LogicalPartitionState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LogicalPartitionEnvironment.Enum
class LogicalPartitionEnvironment_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicalPartitionEnvironment.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2552, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LogicalPartitionEnvironment_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogicalPartitionEnvironment_Enum, enum_prefix=None)
LogicalPartitionEnvironment_Enum.AIXLinux = LogicalPartitionEnvironment_Enum._CF_enumeration.addEnumeration(unicode_value='AIX/Linux', tag='AIXLinux')
LogicalPartitionEnvironment_Enum.OS400 = LogicalPartitionEnvironment_Enum._CF_enumeration.addEnumeration(unicode_value='OS400', tag='OS400')
LogicalPartitionEnvironment_Enum.Virtual_IO_Server = LogicalPartitionEnvironment_Enum._CF_enumeration.addEnumeration(unicode_value='Virtual IO Server', tag='Virtual_IO_Server')
LogicalPartitionEnvironment_Enum._InitializeFacetMap(LogicalPartitionEnvironment_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogicalPartitionEnvironment.Enum', LogicalPartitionEnvironment_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LogicalPartitionProcessorSharingMode.Enum
class LogicalPartitionProcessorSharingMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LogicalPartitionProcessorSharingMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2597, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
LogicalPartitionProcessorSharingMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LogicalPartitionProcessorSharingMode_Enum, enum_prefix=None)
LogicalPartitionProcessorSharingMode_Enum.keep_idle_procs = LogicalPartitionProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='keep idle procs', tag='keep_idle_procs')
LogicalPartitionProcessorSharingMode_Enum.sre_idle_proces = LogicalPartitionProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='sre idle proces', tag='sre_idle_proces')
LogicalPartitionProcessorSharingMode_Enum.sre_idle_procs_active = LogicalPartitionProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='sre idle procs active', tag='sre_idle_procs_active')
LogicalPartitionProcessorSharingMode_Enum.sre_idle_procs_always = LogicalPartitionProcessorSharingMode_Enum._CF_enumeration.addEnumeration(unicode_value='sre idle procs always', tag='sre_idle_procs_always')
LogicalPartitionProcessorSharingMode_Enum._InitializeFacetMap(LogicalPartitionProcessorSharingMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'LogicalPartitionProcessorSharingMode.Enum', LogicalPartitionProcessorSharingMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPLSource.Enum
class IPLSource_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPLSource.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2649, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
IPLSource_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IPLSource_Enum, enum_prefix=None)
IPLSource_Enum.a = IPLSource_Enum._CF_enumeration.addEnumeration(unicode_value='a', tag='a')
IPLSource_Enum.b = IPLSource_Enum._CF_enumeration.addEnumeration(unicode_value='b', tag='b')
IPLSource_Enum.c = IPLSource_Enum._CF_enumeration.addEnumeration(unicode_value='c', tag='c')
IPLSource_Enum.d = IPLSource_Enum._CF_enumeration.addEnumeration(unicode_value='d', tag='d')
IPLSource_Enum._InitializeFacetMap(IPLSource_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IPLSource.Enum', IPLSource_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MultiCoreScalingValue.Enum
class MultiCoreScalingValue_Enum (pyxb.binding.datatypes.unsignedShort, pyxb.binding.basis.enumeration_mixin):

    """
				
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiCoreScalingValue.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2719, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t'
MultiCoreScalingValue_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MultiCoreScalingValue_Enum, enum_prefix=None)
MultiCoreScalingValue_Enum._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
MultiCoreScalingValue_Enum._CF_enumeration.addEnumeration(unicode_value='2', tag=None)
MultiCoreScalingValue_Enum._CF_enumeration.addEnumeration(unicode_value='4', tag=None)
MultiCoreScalingValue_Enum._CF_enumeration.addEnumeration(unicode_value='8', tag=None)
MultiCoreScalingValue_Enum._CF_enumeration.addEnumeration(unicode_value='16', tag=None)
MultiCoreScalingValue_Enum._InitializeFacetMap(MultiCoreScalingValue_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'MultiCoreScalingValue.Enum', MultiCoreScalingValue_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HostEthernetAdapterLogicalPortState.Enum
class HostEthernetAdapterLogicalPortState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HostEthernetAdapterLogicalPortState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2776, 1)
    _Documentation = '\n                \n                 \n            '
HostEthernetAdapterLogicalPortState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=HostEthernetAdapterLogicalPortState_Enum, enum_prefix=None)
HostEthernetAdapterLogicalPortState_Enum.Available = HostEthernetAdapterLogicalPortState_Enum._CF_enumeration.addEnumeration(unicode_value='Available', tag='Available')
HostEthernetAdapterLogicalPortState_Enum.Unavailable = HostEthernetAdapterLogicalPortState_Enum._CF_enumeration.addEnumeration(unicode_value='Unavailable', tag='Unavailable')
HostEthernetAdapterLogicalPortState_Enum._InitializeFacetMap(HostEthernetAdapterLogicalPortState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'HostEthernetAdapterLogicalPortState.Enum', HostEthernetAdapterLogicalPortState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SharedEthernetAdapterQualityOfServiceMode.Enum
class SharedEthernetAdapterQualityOfServiceMode_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SharedEthernetAdapterQualityOfServiceMode.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2810, 4)
    _Documentation = '\n                \n                 \n            '
SharedEthernetAdapterQualityOfServiceMode_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SharedEthernetAdapterQualityOfServiceMode_Enum, enum_prefix=None)
SharedEthernetAdapterQualityOfServiceMode_Enum.Disabled = SharedEthernetAdapterQualityOfServiceMode_Enum._CF_enumeration.addEnumeration(unicode_value='Disabled', tag='Disabled')
SharedEthernetAdapterQualityOfServiceMode_Enum.Strict = SharedEthernetAdapterQualityOfServiceMode_Enum._CF_enumeration.addEnumeration(unicode_value='Strict', tag='Strict')
SharedEthernetAdapterQualityOfServiceMode_Enum.Loose = SharedEthernetAdapterQualityOfServiceMode_Enum._CF_enumeration.addEnumeration(unicode_value='Loose', tag='Loose')
SharedEthernetAdapterQualityOfServiceMode_Enum._InitializeFacetMap(SharedEthernetAdapterQualityOfServiceMode_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SharedEthernetAdapterQualityOfServiceMode.Enum', SharedEthernetAdapterQualityOfServiceMode_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ConfigOption.Enum
class ConfigOption_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConfigOption.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2851, 4)
    _Documentation = None
ConfigOption_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConfigOption_Enum, enum_prefix=None)
ConfigOption_Enum.CONFIG_AT_DEPLOYMENT = ConfigOption_Enum._CF_enumeration.addEnumeration(unicode_value='CONFIG_AT_DEPLOYMENT', tag='CONFIG_AT_DEPLOYMENT')
ConfigOption_Enum.CONFIG_WITH_CAPTURE = ConfigOption_Enum._CF_enumeration.addEnumeration(unicode_value='CONFIG_WITH_CAPTURE', tag='CONFIG_WITH_CAPTURE')
ConfigOption_Enum.DONOT_CONFIG = ConfigOption_Enum._CF_enumeration.addEnumeration(unicode_value='DONOT_CONFIG', tag='DONOT_CONFIG')
ConfigOption_Enum._InitializeFacetMap(ConfigOption_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ConfigOption.Enum', ConfigOption_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PowerOnStartPolicy.Enum
class PowerOnStartPolicy_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerOnStartPolicy.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2880, 4)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PowerOnStartPolicy_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerOnStartPolicy_Enum, enum_prefix=None)
PowerOnStartPolicy_Enum.autorecovery = PowerOnStartPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='autorecovery', tag='autorecovery')
PowerOnStartPolicy_Enum.autostart = PowerOnStartPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='autostart', tag='autostart')
PowerOnStartPolicy_Enum.userinit = PowerOnStartPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='userinit', tag='userinit')
PowerOnStartPolicy_Enum.Unknown = PowerOnStartPolicy_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PowerOnStartPolicy_Enum._InitializeFacetMap(PowerOnStartPolicy_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerOnStartPolicy.Enum', PowerOnStartPolicy_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PowerOnOption.Enum
class PowerOnOption_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerOnOption.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2932, 4)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PowerOnOption_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerOnOption_Enum, enum_prefix=None)
PowerOnOption_Enum.autostart = PowerOnOption_Enum._CF_enumeration.addEnumeration(unicode_value='autostart', tag='autostart')
PowerOnOption_Enum.standby = PowerOnOption_Enum._CF_enumeration.addEnumeration(unicode_value='standby', tag='standby')
PowerOnOption_Enum._InitializeFacetMap(PowerOnOption_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerOnOption.Enum', PowerOnOption_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PowerOnSide.Enum
class PowerOnSide_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerOnSide.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 2967, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PowerOnSide_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerOnSide_Enum, enum_prefix=None)
PowerOnSide_Enum.permanent = PowerOnSide_Enum._CF_enumeration.addEnumeration(unicode_value='permanent', tag='permanent')
PowerOnSide_Enum.temporary = PowerOnSide_Enum._CF_enumeration.addEnumeration(unicode_value='temporary', tag='temporary')
PowerOnSide_Enum.Unknown = PowerOnSide_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PowerOnSide_Enum._InitializeFacetMap(PowerOnSide_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerOnSide.Enum', PowerOnSide_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PowerOnSpeed.Enum
class PowerOnSpeed_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerOnSpeed.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3010, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PowerOnSpeed_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerOnSpeed_Enum, enum_prefix=None)
PowerOnSpeed_Enum.fast = PowerOnSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='fast', tag='fast')
PowerOnSpeed_Enum.slow = PowerOnSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='slow', tag='slow')
PowerOnSpeed_Enum.Unknown = PowerOnSpeed_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PowerOnSpeed_Enum._InitializeFacetMap(PowerOnSpeed_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerOnSpeed.Enum', PowerOnSpeed_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PowerOnSpeedOverride.Enum
class PowerOnSpeedOverride_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PowerOnSpeedOverride.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3053, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
PowerOnSpeedOverride_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PowerOnSpeedOverride_Enum, enum_prefix=None)
PowerOnSpeedOverride_Enum.fast = PowerOnSpeedOverride_Enum._CF_enumeration.addEnumeration(unicode_value='fast', tag='fast')
PowerOnSpeedOverride_Enum.none = PowerOnSpeedOverride_Enum._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
PowerOnSpeedOverride_Enum.slow = PowerOnSpeedOverride_Enum._CF_enumeration.addEnumeration(unicode_value='slow', tag='slow')
PowerOnSpeedOverride_Enum.Unknown = PowerOnSpeedOverride_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
PowerOnSpeedOverride_Enum._InitializeFacetMap(PowerOnSpeedOverride_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PowerOnSpeedOverride.Enum', PowerOnSpeedOverride_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SRIOVStatus.Enum
class SRIOVStatus_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SRIOVStatus.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3105, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
SRIOVStatus_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SRIOVStatus_Enum, enum_prefix=None)
SRIOVStatus_Enum.Initializing = SRIOVStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Initializing', tag='Initializing')
SRIOVStatus_Enum.NotConfigured = SRIOVStatus_Enum._CF_enumeration.addEnumeration(unicode_value='NotConfigured', tag='NotConfigured')
SRIOVStatus_Enum.PoweredOff = SRIOVStatus_Enum._CF_enumeration.addEnumeration(unicode_value='PoweredOff', tag='PoweredOff')
SRIOVStatus_Enum.PoweredOn = SRIOVStatus_Enum._CF_enumeration.addEnumeration(unicode_value='PoweredOn', tag='PoweredOn')
SRIOVStatus_Enum.PoweringOff = SRIOVStatus_Enum._CF_enumeration.addEnumeration(unicode_value='PoweringOff', tag='PoweringOff')
SRIOVStatus_Enum.Running = SRIOVStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
SRIOVStatus_Enum._InitializeFacetMap(SRIOVStatus_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SRIOVStatus.Enum', SRIOVStatus_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SRIOVConfigState.Enum
class SRIOVConfigState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SRIOVConfigState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3172, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
SRIOVConfigState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SRIOVConfigState_Enum, enum_prefix=None)
SRIOVConfigState_Enum.Configured = SRIOVConfigState_Enum._CF_enumeration.addEnumeration(unicode_value='Configured', tag='Configured')
SRIOVConfigState_Enum.Dedicated = SRIOVConfigState_Enum._CF_enumeration.addEnumeration(unicode_value='Dedicated', tag='Dedicated')
SRIOVConfigState_Enum.NotConfigured = SRIOVConfigState_Enum._CF_enumeration.addEnumeration(unicode_value='NotConfigured', tag='NotConfigured')
SRIOVConfigState_Enum.unknown = SRIOVConfigState_Enum._CF_enumeration.addEnumeration(unicode_value='unknown', tag='unknown')
SRIOVConfigState_Enum._InitializeFacetMap(SRIOVConfigState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SRIOVConfigState.Enum', SRIOVConfigState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SRIOVFunctionalStatus.Enum
class SRIOVFunctionalStatus_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
				
				 
			"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SRIOVFunctionalStatus.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3223, 1)
    _Documentation = '\n\t\t\t\t\n\t\t\t\t \n\t\t\t'
SRIOVFunctionalStatus_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SRIOVFunctionalStatus_Enum, enum_prefix=None)
SRIOVFunctionalStatus_Enum.Functional = SRIOVFunctionalStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Functional', tag='Functional')
SRIOVFunctionalStatus_Enum.NonFunctional = SRIOVFunctionalStatus_Enum._CF_enumeration.addEnumeration(unicode_value='NonFunctional', tag='NonFunctional')
SRIOVFunctionalStatus_Enum.Unknown = SRIOVFunctionalStatus_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SRIOVFunctionalStatus_Enum._InitializeFacetMap(SRIOVFunctionalStatus_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SRIOVFunctionalStatus.Enum', SRIOVFunctionalStatus_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SRIOVAdapterPersonalities.Enum
class SRIOVAdapterPersonalities_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SRIOVAdapterPersonalities.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3267, 2)
    _Documentation = '\n                \n                 \n            '
SRIOVAdapterPersonalities_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SRIOVAdapterPersonalities_Enum, enum_prefix=None)
SRIOVAdapterPersonalities_Enum.NoQoSSupport = SRIOVAdapterPersonalities_Enum._CF_enumeration.addEnumeration(unicode_value='NoQoSSupport', tag='NoQoSSupport')
SRIOVAdapterPersonalities_Enum.SingleSettingQoSSupport = SRIOVAdapterPersonalities_Enum._CF_enumeration.addEnumeration(unicode_value='SingleSettingQoSSupport', tag='SingleSettingQoSSupport')
SRIOVAdapterPersonalities_Enum.Unknown = SRIOVAdapterPersonalities_Enum._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SRIOVAdapterPersonalities_Enum._InitializeFacetMap(SRIOVAdapterPersonalities_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SRIOVAdapterPersonalities.Enum', SRIOVAdapterPersonalities_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SRIOVLogicalPortOption.Enum
class SRIOVLogicalPortOption_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SRIOVLogicalPortOption.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3311, 4)
    _Documentation = '\n                \n                 \n            '
SRIOVLogicalPortOption_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SRIOVLogicalPortOption_Enum, enum_prefix=None)
SRIOVLogicalPortOption_Enum.PromiscousMode = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='PromiscousMode', tag='PromiscousMode')
SRIOVLogicalPortOption_Enum.DiagnosticMode = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='DiagnosticMode', tag='DiagnosticMode')
SRIOVLogicalPortOption_Enum.MACRestricted = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='MACRestricted', tag='MACRestricted')
SRIOVLogicalPortOption_Enum.AdjunctBased = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='AdjunctBased', tag='AdjunctBased')
SRIOVLogicalPortOption_Enum.DestructiveDebugMode = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='DestructiveDebugMode', tag='DestructiveDebugMode')
SRIOVLogicalPortOption_Enum.HugeDMAWindow = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='HugeDMAWindow', tag='HugeDMAWindow')
SRIOVLogicalPortOption_Enum.PreviligedStatisticsCollection = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='PreviligedStatisticsCollection', tag='PreviligedStatisticsCollection')
SRIOVLogicalPortOption_Enum.AssignedToVIOSPartition = SRIOVLogicalPortOption_Enum._CF_enumeration.addEnumeration(unicode_value='AssignedToVIOSPartition', tag='AssignedToVIOSPartition')
SRIOVLogicalPortOption_Enum._InitializeFacetMap(SRIOVLogicalPortOption_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SRIOVLogicalPortOption.Enum', SRIOVLogicalPortOption_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPInterfaceState.Enum
class IPInterfaceState_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPInterfaceState.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3403, 5)
    _Documentation = '\n                \n                 \n            '
IPInterfaceState_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IPInterfaceState_Enum, enum_prefix=None)
IPInterfaceState_Enum.Active = IPInterfaceState_Enum._CF_enumeration.addEnumeration(unicode_value='Active', tag='Active')
IPInterfaceState_Enum.Inactive = IPInterfaceState_Enum._CF_enumeration.addEnumeration(unicode_value='Inactive', tag='Inactive')
IPInterfaceState_Enum.Disconnected = IPInterfaceState_Enum._CF_enumeration.addEnumeration(unicode_value='Disconnected', tag='Disconnected')
IPInterfaceState_Enum._InitializeFacetMap(IPInterfaceState_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'IPInterfaceState.Enum', IPInterfaceState_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ReferenceType.Enum
class ReferenceType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReferenceType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3448, 1)
    _Documentation = '\n                \n                 \n            '
ReferenceType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReferenceType_Enum, enum_prefix=None)
ReferenceType_Enum.VirtualNetwork = ReferenceType_Enum._CF_enumeration.addEnumeration(unicode_value='VirtualNetwork', tag='VirtualNetwork')
ReferenceType_Enum.VirtualSwitch = ReferenceType_Enum._CF_enumeration.addEnumeration(unicode_value='VirtualSwitch', tag='VirtualSwitch')
ReferenceType_Enum.VirtualIOServer = ReferenceType_Enum._CF_enumeration.addEnumeration(unicode_value='VirtualIOServer', tag='VirtualIOServer')
ReferenceType_Enum._InitializeFacetMap(ReferenceType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReferenceType.Enum', ReferenceType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VirtualOpticalMediaType.Enum
class VirtualOpticalMediaType_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                
                 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VirtualOpticalMediaType.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonEnumerations.xsd', 3494, 4)
    _Documentation = '\n                \n                 \n            '
VirtualOpticalMediaType_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VirtualOpticalMediaType_Enum, enum_prefix=None)
VirtualOpticalMediaType_Enum.DEV = VirtualOpticalMediaType_Enum._CF_enumeration.addEnumeration(unicode_value='DEV', tag='DEV')
VirtualOpticalMediaType_Enum.ISO = VirtualOpticalMediaType_Enum._CF_enumeration.addEnumeration(unicode_value='ISO', tag='ISO')
VirtualOpticalMediaType_Enum.BLANK = VirtualOpticalMediaType_Enum._CF_enumeration.addEnumeration(unicode_value='BLANK', tag='BLANK')
VirtualOpticalMediaType_Enum._InitializeFacetMap(VirtualOpticalMediaType_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'VirtualOpticalMediaType.Enum', VirtualOpticalMediaType_Enum)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPV4Address.Pattern
class IPV4Address_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPV4Address.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 80, 4)
    _Documentation = '\n                \n            '
IPV4Address_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
IPV4Address_Pattern._CF_pattern.addPattern(pattern='((25[0-5]|2[0-4]\\d|[01]?\\d{1,2})\\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d{1,2})')
IPV4Address_Pattern._InitializeFacetMap(IPV4Address_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'IPV4Address.Pattern', IPV4Address_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPV6Address.Pattern
class IPV6Address_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPV6Address.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 104, 4)
    _Documentation = '\n                \n            '
IPV6Address_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
IPV6Address_Pattern._CF_pattern.addPattern(pattern='((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)){3}))|:)))(%.+)?')
IPV6Address_Pattern._InitializeFacetMap(IPV6Address_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'IPV6Address.Pattern', IPV6Address_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MACAddress.Pattern
class MACAddress_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MACAddress.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 128, 4)
    _Documentation = '\n                \n            '
MACAddress_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
MACAddress_Pattern._CF_pattern.addPattern(pattern='(([0-9a-fA-F]{12})|((([0-9a-fA-F]{1,2}[:]){5})[0-9a-fA-F]{1,2})|((([0-9a-fA-F]{1,2}[\\-]){5})[0-9a-fA-F]{1,2}))')
MACAddress_Pattern._InitializeFacetMap(MACAddress_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MACAddress.Pattern', MACAddress_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}GUID.Pattern
class GUID_Pattern (pyxb.binding.datatypes.string):

    """
                The representation of a GUID, generally as the id of an element. The difference
                between a GUID and a UUID is that a GUID is wrapped with curly braces.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GUID.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 167, 4)
    _Documentation = '\n                The representation of a GUID, generally as the id of an element. The difference\n                between a GUID and a UUID is that a GUID is wrapped with curly braces.\n            '
GUID_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
GUID_Pattern._CF_pattern.addPattern(pattern='\\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\\}')
GUID_Pattern._InitializeFacetMap(GUID_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'GUID.Pattern', GUID_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UUID.Pattern
class UUID_Pattern (pyxb.binding.datatypes.string):

    """
                The representation of a UUID, generally as the id of an element. The difference
                between a GUID and a UUID is that a UUID is not wrapped with curly braces.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UUID.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 194, 4)
    _Documentation = '\n                The representation of a UUID, generally as the id of an element. The difference\n                between a GUID and a UUID is that a UUID is not wrapped with curly braces.\n            '
UUID_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
UUID_Pattern._CF_pattern.addPattern(pattern='[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
UUID_Pattern._InitializeFacetMap(UUID_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UUID.Pattern', UUID_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}WWPN.Pattern
class WWPN_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WWPN.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 221, 4)
    _Documentation = '\n                \n            '
WWPN_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
WWPN_Pattern._CF_pattern.addPattern(pattern='(([0-9a-fA-F]{16})|((([0-9a-fA-F]{1,2}[:]){7})[0-9a-fA-F]{1,2})|((([0-9a-fA-F]{1,2}[\\-]){7})[0-9a-fA-F]{1,2}))')
WWPN_Pattern._InitializeFacetMap(WWPN_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'WWPN.Pattern', WWPN_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Percent.Pattern
class Percent_Pattern (pyxb.binding.datatypes.string):

    """
                Specifies a decimal percentage value from zero to 100 inclusive.
                
                
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Percent.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 258, 4)
    _Documentation = '\n                Specifies a decimal percentage value from zero to 100 inclusive.\n                \n                \n                \n            '
Percent_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
Percent_Pattern._CF_pattern.addPattern(pattern='(100|[1-9]?\\d)(\\.\\d*)?\\s*%')
Percent_Pattern._InitializeFacetMap(Percent_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Percent.Pattern', Percent_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}PhysicalLocation.Pattern
class PhysicalLocation_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PhysicalLocation.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 280, 5)
    _Documentation = '\n                \n            '
PhysicalLocation_Pattern._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'PhysicalLocation.Pattern', PhysicalLocation_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UDID.Pattern
class UDID_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UDID.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 297, 5)
    _Documentation = '\n                \n            '
UDID_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
UDID_Pattern._CF_pattern.addPattern(pattern='[a-zA-Z0-9_]{1,32}')
UDID_Pattern._InitializeFacetMap(UDID_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'UDID.Pattern', UDID_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineType.Pattern
class MachineType_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MachineType.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 315, 4)
    _Documentation = '\n                \n            '
MachineType_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
MachineType_Pattern._CF_pattern.addPattern(pattern='[\\w]{4}')
MachineType_Pattern._InitializeFacetMap(MachineType_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MachineType.Pattern', MachineType_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineModel.Pattern
class MachineModel_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MachineModel.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 340, 4)
    _Documentation = '\n                \n            '
MachineModel_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
MachineModel_Pattern._CF_pattern.addPattern(pattern='[\\w]{3}')
MachineModel_Pattern._InitializeFacetMap(MachineModel_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'MachineModel.Pattern', MachineModel_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SerialNumber.Pattern
class SerialNumber_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SerialNumber.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 365, 4)
    _Documentation = '\n                \n            '
SerialNumber_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
SerialNumber_Pattern._CF_pattern.addPattern(pattern='[\\w\\-\\._]{2,11}')
SerialNumber_Pattern._InitializeFacetMap(SerialNumber_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SerialNumber.Pattern', SerialNumber_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}HostEthernetPhysicalPortID.Pattern
class HostEthernetPhysicalPortID_Pattern (pyxb.binding.datatypes.string):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'HostEthernetPhysicalPortID.Pattern')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonPatterns.xsd', 390, 4)
    _Documentation = '\n                \n            '
HostEthernetPhysicalPortID_Pattern._CF_pattern = pyxb.binding.facets.CF_pattern()
HostEthernetPhysicalPortID_Pattern._CF_pattern.addPattern(pattern='([0-3]{1})')
HostEthernetPhysicalPortID_Pattern._InitializeFacetMap(HostEthernetPhysicalPortID_Pattern._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'HostEthernetPhysicalPortID.Pattern', HostEthernetPhysicalPortID_Pattern)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}False.Type
class False_Type (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'False.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 26, 4)
    _Documentation = ''
False_Type._CF_pattern = pyxb.binding.facets.CF_pattern()
False_Type._CF_pattern.addPattern(pattern='false')
False_Type._InitializeFacetMap(False_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'False.Type', False_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}True.Type
class True_Type (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'True.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 41, 4)
    _Documentation = ''
True_Type._CF_pattern = pyxb.binding.facets.CF_pattern()
True_Type._CF_pattern.addPattern(pattern='true')
True_Type._InitializeFacetMap(True_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'True.Type', True_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}COD.Type
class COD_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'COD.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 13, 4)
    _Documentation = None
COD_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=COD_Type, enum_prefix=None)
COD_Type.COD = COD_Type._CF_enumeration.addEnumeration(unicode_value='COD', tag='COD')
COD_Type._InitializeFacetMap(COD_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'COD.Type', COD_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}COR.Type
class COR_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'COR.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 18, 4)
    _Documentation = None
COR_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=COR_Type, enum_prefix=None)
COR_Type.COR = COR_Type._CF_enumeration.addEnumeration(unicode_value='COR', tag='COR')
COR_Type._InitializeFacetMap(COR_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'COR.Type', COR_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}CUD.Type
class CUD_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CUD.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 23, 4)
    _Documentation = None
CUD_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CUD_Type, enum_prefix=None)
CUD_Type.CUD = CUD_Type._CF_enumeration.addEnumeration(unicode_value='CUD', tag='CUD')
CUD_Type._InitializeFacetMap(CUD_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CUD.Type', CUD_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}CUR.Type
class CUR_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CUR.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 28, 4)
    _Documentation = None
CUR_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CUR_Type, enum_prefix=None)
CUR_Type.CUR = CUR_Type._CF_enumeration.addEnumeration(unicode_value='CUR', tag='CUR')
CUR_Type._InitializeFacetMap(CUR_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CUR.Type', CUR_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}CUA.Type
class CUA_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CUA.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 33, 4)
    _Documentation = None
CUA_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CUA_Type, enum_prefix=None)
CUA_Type.CUA = CUA_Type._CF_enumeration.addEnumeration(unicode_value='CUA', tag='CUA')
CUA_Type._InitializeFacetMap(CUA_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CUA.Type', CUA_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UOD.Type
class UOD_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UOD.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 38, 4)
    _Documentation = None
UOD_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UOD_Type, enum_prefix=None)
UOD_Type.UOD = UOD_Type._CF_enumeration.addEnumeration(unicode_value='UOD', tag='UOD')
UOD_Type._InitializeFacetMap(UOD_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UOD.Type', UOD_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UOO.Type
class UOO_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UOO.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 43, 4)
    _Documentation = None
UOO_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UOO_Type, enum_prefix=None)
UOO_Type.UOO = UOO_Type._CF_enumeration.addEnumeration(unicode_value='UOO', tag='UOO')
UOO_Type._InitializeFacetMap(UOO_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UOO.Type', UOO_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UOR.Type
class UOR_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UOR.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 48, 4)
    _Documentation = None
UOR_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UOR_Type, enum_prefix=None)
UOR_Type.UOR = UOR_Type._CF_enumeration.addEnumeration(unicode_value='UOR', tag='UOR')
UOR_Type._InitializeFacetMap(UOR_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UOR.Type', UOR_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UOA.Type
class UOA_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UOA.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 53, 4)
    _Documentation = None
UOA_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UOA_Type, enum_prefix=None)
UOA_Type.UOA = UOA_Type._CF_enumeration.addEnumeration(unicode_value='UOA', tag='UOA')
UOA_Type._InitializeFacetMap(UOA_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'UOA.Type', UOA_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ROO.Type
class ROO_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ROO.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 58, 4)
    _Documentation = None
ROO_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ROO_Type, enum_prefix=None)
ROO_Type.ROO = ROO_Type._CF_enumeration.addEnumeration(unicode_value='ROO', tag='ROO')
ROO_Type._InitializeFacetMap(ROO_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ROO.Type', ROO_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ROA.Type
class ROA_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ROA.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 63, 4)
    _Documentation = None
ROA_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ROA_Type, enum_prefix=None)
ROA_Type.ROA = ROA_Type._CF_enumeration.addEnumeration(unicode_value='ROA', tag='ROA')
ROA_Type._InitializeFacetMap(ROA_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ROA.Type', ROA_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ROR.Type
class ROR_Type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ROR.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 68, 4)
    _Documentation = None
ROR_Type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ROR_Type, enum_prefix=None)
ROR_Type.ROR = ROR_Type._CF_enumeration.addEnumeration(unicode_value='ROR', tag='ROR')
ROR_Type._InitializeFacetMap(ROR_Type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ROR.Type', ROR_Type)

# Atomic simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Extended.Enum
class Extended_Enum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Extended.Enum')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 74, 4)
    _Documentation = None
Extended_Enum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Extended_Enum, enum_prefix=None)
Extended_Enum.All = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='All', tag='All')
Extended_Enum.Advanced = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='Advanced', tag='Advanced')
Extended_Enum.Hypervisor = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='Hypervisor', tag='Hypervisor')
Extended_Enum.SystemNetwork = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='SystemNetwork', tag='SystemNetwork')
Extended_Enum.ViosStorage = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='ViosStorage', tag='ViosStorage')
Extended_Enum.ViosNetwork = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='ViosNetwork', tag='ViosNetwork')
Extended_Enum.ViosFCMapping = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='ViosFCMapping', tag='ViosFCMapping')
Extended_Enum.ViosSCSIMapping = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='ViosSCSIMapping', tag='ViosSCSIMapping')
Extended_Enum.None_ = Extended_Enum._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
Extended_Enum._InitializeFacetMap(Extended_Enum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Extended.Enum', Extended_Enum)

# Union simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPAddress.Union
# superclasses pyxb.binding.datatypes.anySimpleType
class IPAddress_Union (pyxb.binding.basis.STD_union):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPAddress.Union')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 290, 3)
    _Documentation = '\n                \n            '

    _MemberTypes = ( IPV4Address_Pattern, IPV6Address_Pattern, )
IPAddress_Union._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IPAddress.Union', IPAddress_Union)

# Union simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}EntitledIOMegabyte.Union
# superclasses pyxb.binding.datatypes.anySimpleType
class EntitledIOMegabyte_Union (pyxb.binding.basis.STD_union):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EntitledIOMegabyte.Union')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 310, 5)
    _Documentation = '\n                \n            '

    _MemberTypes = ( Auto_Enum, Megabyte_Type, )
EntitledIOMegabyte_Union.AUTO = 'AUTO'            # originally Auto_Enum.AUTO
EntitledIOMegabyte_Union._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'EntitledIOMegabyte.Union', EntitledIOMegabyte_Union)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPV4Address.List
# superclasses pyxb.binding.datatypes.anySimpleType
class IPV4Address_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPV4Address.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 87, 4)
    _Documentation = '\n                \n            '

    _ItemType = IPV4Address_Pattern
IPV4Address_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IPV4Address.List', IPV4Address_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPV6Address.List
# superclasses pyxb.binding.datatypes.anySimpleType
class IPV6Address_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPV6Address.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 110, 4)
    _Documentation = '\n                \n            '

    _ItemType = IPV6Address_Pattern
IPV6Address_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IPV6Address.List', IPV6Address_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MACAddress.List
# superclasses pyxb.binding.datatypes.anySimpleType
class MACAddress_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MACAddress.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 133, 4)
    _Documentation = '\n                \n            '

    _ItemType = MACAddress_Pattern
MACAddress_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MACAddress.List', MACAddress_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}UUID.List
# superclasses pyxb.binding.datatypes.anySimpleType
class UUID_List (pyxb.binding.basis.STD_list):

    """
            	 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UUID.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 183, 4)
    _Documentation = '\n            \t \n            '

    _ItemType = UUID_Pattern
UUID_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'UUID.List', UUID_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}WWPN.List
# superclasses pyxb.binding.datatypes.anySimpleType
class WWPN_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WWPN.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 203, 4)
    _Documentation = '\n                \n            '

    _ItemType = WWPN_Pattern
WWPN_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'WWPN.List', WWPN_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VLANID.List
# superclasses pyxb.binding.datatypes.anySimpleType
class VLANID_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VLANID.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 250, 2)
    _Documentation = '\n                \n            '

    _ItemType = VLANID_Type
VLANID_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'VLANID.List', VLANID_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MultiCoreScalingValue.List
# superclasses pyxb.binding.datatypes.anySimpleType
class MultiCoreScalingValue_List (pyxb.binding.basis.STD_list):

    """
            	 
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MultiCoreScalingValue.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 273, 1)
    _Documentation = '\n            \t \n            '

    _ItemType = MultiCoreScalingValue_Enum
MultiCoreScalingValue_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MultiCoreScalingValue.List', MultiCoreScalingValue_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}IPAddress.List
# superclasses pyxb.binding.datatypes.anySimpleType
class IPAddress_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IPAddress.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 289, 4)
    _Documentation = '\n                \n            '

    _ItemType = IPV4Address_Pattern
IPAddress_List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IPAddress.List', IPAddress_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}VLANID20.List
# superclasses VLANID_List
class VLANID20_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'VLANID20.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 261, 2)
    _Documentation = '\n                \n            '

    _ItemType = VLANID_Type
VLANID20_List._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
VLANID20_List._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
VLANID20_List._InitializeFacetMap(VLANID20_List._CF_minLength,
   VLANID20_List._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'VLANID20.List', VLANID20_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MACAddress4.List
# superclasses MACAddress_List
class MACAddress4_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MACAddress4.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 156, 4)
    _Documentation = '\n                \n            '

    _ItemType = MACAddress_Pattern
MACAddress4_List._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
MACAddress4_List._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
MACAddress4_List._InitializeFacetMap(MACAddress4_List._CF_minLength,
   MACAddress4_List._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'MACAddress4.List', MACAddress4_List)

# List simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}WWPN2.List
# superclasses WWPN_List
class WWPN2_List (pyxb.binding.basis.STD_list):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WWPN2.List')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonLists.xsd', 226, 4)
    _Documentation = '\n                \n            '

    _ItemType = WWPN_Pattern
WWPN2_List._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
WWPN2_List._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
WWPN2_List._InitializeFacetMap(WWPN2_List._CF_minLength,
   WWPN2_List._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'WWPN2.List', WWPN2_List)

# Union simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AllowedVLANIDs.Union
# superclasses pyxb.binding.datatypes.anySimpleType
class AllowedVLANIDs_Union (pyxb.binding.basis.STD_union):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllowedVLANIDs.Union')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 336, 4)
    _Documentation = '\n                \n            '

    _MemberTypes = ( AllOrNone_Enum, VLANID20_List, )
AllowedVLANIDs_Union.ALL = 'ALL'                  # originally AllOrNone_Enum.ALL
AllowedVLANIDs_Union.NONE = 'NONE'                # originally AllOrNone_Enum.NONE
AllowedVLANIDs_Union._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AllowedVLANIDs.Union', AllowedVLANIDs_Union)

# Union simple type: {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AllowedMACAddresses.Union
# superclasses pyxb.binding.datatypes.anySimpleType
class AllowedMACAddresses_Union (pyxb.binding.basis.STD_union):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AllowedMACAddresses.Union')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 356, 6)
    _Documentation = '\n                \n            '

    _MemberTypes = ( AllOrNone_Enum, MACAddress4_List, )
AllowedMACAddresses_Union.ALL = 'ALL'             # originally AllOrNone_Enum.ALL
AllowedMACAddresses_Union.NONE = 'NONE'           # originally AllOrNone_Enum.NONE
AllowedMACAddresses_Union._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'AllowedMACAddresses.Union', AllowedMACAddresses_Union)

# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Metadata.Type with content type ELEMENT_ONLY
class Metadata_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Metadata.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 102, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Atom uses Python identifier Atom
    __Atom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Atom'), 'Atom', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_Metadata_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10Atom', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 141, 12), )

    
    Atom = property(__Atom.value, __Atom.set, None, None)

    _ElementMap.update({
        __Atom.name() : __Atom
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Metadata.Type', Metadata_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomMetadata.Type with content type ELEMENT_ONLY
class AtomMetadata_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomMetadata.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 155, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomID uses Python identifier AtomID
    __AtomID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AtomID'), 'AtomID', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomMetadata_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10AtomID', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 201, 12), )

    
    AtomID = property(__AtomID.value, __AtomID.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomCreated uses Python identifier AtomCreated
    __AtomCreated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AtomCreated'), 'AtomCreated', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomMetadata_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10AtomCreated', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 250, 12), )

    
    AtomCreated = property(__AtomCreated.value, __AtomCreated.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomUpdated uses Python identifier AtomUpdated
    __AtomUpdated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AtomUpdated'), 'AtomUpdated', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomMetadata_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10AtomUpdated', True, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 276, 12), )

    
    AtomUpdated = property(__AtomUpdated.value, __AtomUpdated.set, None, None)

    _ElementMap.update({
        __AtomID.name() : __AtomID,
        __AtomCreated.name() : __AtomCreated,
        __AtomUpdated.name() : __AtomUpdated
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AtomMetadata.Type', AtomMetadata_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomDateTime.Type with content type SIMPLE
class AtomDateTime_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
            """
    _TypeDefinition = pyxb.binding.datatypes.long
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomDateTime.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 291, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.long
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AtomDateTime.Type', AtomDateTime_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}CommonRESTCollection.Type with content type ELEMENT_ONLY
class CommonRESTCollection_Type (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CommonRESTCollection.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'link'), 'link', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CommonRESTCollection_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10link', True, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 73, 12), )

    
    link = property(__link.value, __link.set, None, None)

    _ElementMap.update({
        __link.name() : __link
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CommonRESTCollection.Type', CommonRESTCollection_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type with content type EMPTY
class AtomLink_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
                
                
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomLink.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 91, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomLink_Type_href', pyxb.binding.datatypes.anyURI, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 206, 8)
    __href._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 206, 8)
    
    href = property(__href.value, __href.set, None, '\n                    \n                ')

    
    # Attribute rel uses Python identifier rel
    __rel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rel'), 'rel', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomLink_Type_rel', IanaRelationship_Enum, required=True)
    __rel._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 219, 8)
    __rel._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 219, 8)
    
    rel = property(__rel.value, __rel.set, None, '\n                    \n                ')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomLink_Type_type', AtomMedia_Pattern)
    __type._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 232, 8)
    __type._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 232, 8)
    
    type = property(__type.value, __type.set, None, '\n                    \n                ')

    
    # Attribute hreflang uses Python identifier hreflang
    __hreflang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hreflang'), 'hreflang', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomLink_Type_hreflang', AtomLanguageTag_Type)
    __hreflang._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 249, 8)
    __hreflang._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 249, 8)
    
    hreflang = property(__hreflang.value, __hreflang.set, None, None)

    
    # Attribute title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomLink_Type_title', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 255, 8)
    __title._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 255, 8)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AtomLink_Type_length', pyxb.binding.datatypes.integer)
    __length._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 261, 8)
    __length._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 261, 8)
    
    length = property(__length.value, __length.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href,
        __rel.name() : __rel,
        __type.name() : __type,
        __hreflang.name() : __hreflang,
        __title.name() : __title,
        __length.name() : __length
    })
Namespace.addCategoryObject('typeBinding', 'AtomLink.Type', AtomLink_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomID.Type with content type SIMPLE
class AtomID_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
            """
    _TypeDefinition = UUID_Pattern
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AtomID.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 216, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is UUID_Pattern
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AtomID.Type', AtomID_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type with content type ELEMENT_ONLY
class AbstractRest_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractRest.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 101, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractRest_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10Metadata', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Attribute schemaVersion uses Python identifier schemaVersion
    __schemaVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemaVersion'), 'schemaVersion', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractRest_Type_schemaVersion', SchemaVersion_Enum, required=True)
    __schemaVersion._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 335, 8)
    __schemaVersion._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 335, 8)
    
    schemaVersion = property(__schemaVersion.value, __schemaVersion.set, None, '\n                    \n                    \n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'base'), 'base', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractRest_Type_httpwww_w3_orgXML1998namespacek2base', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 92, 8)
    __base._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 92, 8)
    
    base = property(__base.value, __base.set, None, '\n                    See\n                    \n                    for information about this attribute.\n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'lang'), 'lang', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractRest_Type_httpwww_w3_orgXML1998namespacek2lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 109, 8)
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 109, 8)
    
    lang = property(__lang.value, __lang.set, None, '\n                    See "Extensible Markup Language (XML) 1.0\n                    (Fifth Edition)",\n                    section 2.12 "Language\n                    Identification,"\n                    at\n                    \n                    , for a full description.\n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'space'), 'space', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractRest_Type_httpwww_w3_orgXML1998namespacek2space', pyxb.binding.datatypes.string)
    __space._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 144, 8)
    __space._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 144, 8)
    
    space = property(__space.value, __space.set, None, '\n                    See "Extensible Markup Language (XML) 1.0 (Fifth Edition)",\n                    section 2.10 "White\n                    Space Handling," at\n                    \n                    , for a full description.\n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'id'), 'id', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractRest_Type_httpwww_w3_orgXML1998namespacek2id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 173, 8)
    __id._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 173, 8)
    
    id = property(__id.value, __id.set, None, '\n                    See\n                    \n                    for\n                    information about this attribute.\n                ')

    _ElementMap.update({
        __Metadata.name() : __Metadata
    })
    _AttributeMap.update({
        __schemaVersion.name() : __schemaVersion,
        __base.name() : __base,
        __lang.name() : __lang,
        __space.name() : __space,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'AbstractRest.Type', AbstractRest_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type with content type ELEMENT_ONLY
class AbstractNonRest_Type (pyxb.binding.basis.complexTypeDefinition):
    """
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractNonRest.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 129, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), 'Metadata', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractNonRest_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10Metadata', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    
    # Attribute schemaVersion uses Python identifier schemaVersion
    __schemaVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemaVersion'), 'schemaVersion', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractNonRest_Type_schemaVersion', SchemaVersion_Enum, required=True)
    __schemaVersion._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 335, 8)
    __schemaVersion._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 335, 8)
    
    schemaVersion = property(__schemaVersion.value, __schemaVersion.set, None, '\n                    \n                    \n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}base uses Python identifier base
    __base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'base'), 'base', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractNonRest_Type_httpwww_w3_orgXML1998namespacek2base', pyxb.binding.datatypes.anyURI)
    __base._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 92, 8)
    __base._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 92, 8)
    
    base = property(__base.value, __base.set, None, '\n                    See\n                    \n                    for information about this attribute.\n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'lang'), 'lang', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractNonRest_Type_httpwww_w3_orgXML1998namespacek2lang', pyxb.binding.datatypes.string)
    __lang._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 109, 8)
    __lang._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 109, 8)
    
    lang = property(__lang.value, __lang.set, None, '\n                    See "Extensible Markup Language (XML) 1.0\n                    (Fifth Edition)",\n                    section 2.12 "Language\n                    Identification,"\n                    at\n                    \n                    , for a full description.\n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'space'), 'space', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractNonRest_Type_httpwww_w3_orgXML1998namespacek2space', pyxb.binding.datatypes.string)
    __space._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 144, 8)
    __space._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 144, 8)
    
    space = property(__space.value, __space.set, None, '\n                    See "Extensible Markup Language (XML) 1.0 (Fifth Edition)",\n                    section 2.10 "White\n                    Space Handling," at\n                    \n                    , for a full description.\n                ')

    
    # Attribute {http://www.w3.org/XML/1998/namespace/k2}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xmlk2, 'id'), 'id', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_AbstractNonRest_Type_httpwww_w3_orgXML1998namespacek2id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 173, 8)
    __id._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\w3c\\xml.xsd', 173, 8)
    
    id = property(__id.value, __id.set, None, '\n                    See\n                    \n                    for\n                    information about this attribute.\n                ')

    _ElementMap.update({
        __Metadata.name() : __Metadata
    })
    _AttributeMap.update({
        __schemaVersion.name() : __schemaVersion,
        __base.name() : __base,
        __lang.name() : __lang,
        __space.name() : __space,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', 'AbstractNonRest.Type', AbstractNonRest_Type)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = MachineType_Pattern
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 79, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is MachineType_Pattern
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_kb', ROR_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = MachineModel_Pattern
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 96, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is MachineModel_Pattern
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON__kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON__kb', ROR_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = SerialNumber_Pattern
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 113, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is SerialNumber_Pattern
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_2_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_2_kb', ROR_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 80, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_3_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_3_kb', ROR_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 114, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_4_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_4_kb', UOD_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 131, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_5_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_5_kb', UOD_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 148, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_6_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_6_kb', UOD_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = pyxb.binding.datatypes.boolean
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 165, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.boolean
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_7_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute ksv uses Python identifier ksv
    __ksv = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ksv'), 'ksv', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_7_ksv', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default='V1_1_0', required=True)
    __ksv._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 176, 28)
    __ksv._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 176, 28)
    
    ksv = property(__ksv.value, __ksv.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_7_kb', UOD_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 105, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __ksv.name() : __ksv,
        __kb.name() : __kb
    })



# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}OpaqueDataBlobReference.Type with content type EMPTY
class OpaqueDataBlobReference_Type (AtomLink_Type):
    """
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OpaqueDataBlobReference.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\common\\inc\\CommonTypes.xsd', 400, 4)
    _ElementMap = AtomLink_Type._ElementMap.copy()
    _AttributeMap = AtomLink_Type._AttributeMap.copy()
    # Base type is AtomLink_Type
    
    # Attribute href inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute rel inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute type inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute hreflang inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute title inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute length inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OpaqueDataBlobReference.Type', OpaqueDataBlobReference_Type)


# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineTypeModelSerialNumber.Type with content type ELEMENT_ONLY
class MachineTypeModelSerialNumber_Type (AbstractNonRest_Type):
    """
                
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MachineTypeModelSerialNumber.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 145, 4)
    _ElementMap = AbstractNonRest_Type._ElementMap.copy()
    _AttributeMap = AbstractNonRest_Type._AttributeMap.copy()
    # Base type is AbstractNonRest_Type
    
    # Element Metadata ({http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Metadata) inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineType uses Python identifier MachineType
    __MachineType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MachineType'), 'MachineType', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_MachineTypeModelSerialNumber_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10MachineType', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 78, 8), )

    
    MachineType = property(__MachineType.value, __MachineType.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Model uses Python identifier Model
    __Model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Model'), 'Model', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_MachineTypeModelSerialNumber_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10Model', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 95, 12), )

    
    Model = property(__Model.value, __Model.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SerialNumber uses Python identifier SerialNumber
    __SerialNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SerialNumber'), 'SerialNumber', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_MachineTypeModelSerialNumber_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10SerialNumber', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 112, 12), )

    
    SerialNumber = property(__SerialNumber.value, __SerialNumber.set, None, None)

    
    # Attribute schemaVersion inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute base inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute lang inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute space inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute id inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    _ElementMap.update({
        __MachineType.name() : __MachineType,
        __Model.name() : __Model,
        __SerialNumber.name() : __SerialNumber
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MachineTypeModelSerialNumber.Type', MachineTypeModelSerialNumber_Type)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (AtomLink_Type):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 182, 16)
    _ElementMap = AtomLink_Type._ElementMap.copy()
    _AttributeMap = AtomLink_Type._AttributeMap.copy()
    # Base type is AtomLink_Type
    
    # Attribute href inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute rel inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute type inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute hreflang inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute title inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute length inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AtomLink.Type
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_8_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_8_kb', ROO_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 117, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 117, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



# Complex type {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ManagedSystemPcmPreference.Type with content type ELEMENT_ONLY
class ManagedSystemPcmPreference_Type (AbstractRest_Type):
    """
                
                
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ManagedSystemPcmPreference.Type')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 213, 4)
    _ElementMap = AbstractRest_Type._ElementMap.copy()
    _AttributeMap = AbstractRest_Type._AttributeMap.copy()
    # Base type is AbstractRest_Type
    
    # Element Metadata ({http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Metadata) inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type
    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SystemName uses Python identifier SystemName
    __SystemName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SystemName'), 'SystemName', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10SystemName', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 79, 8), )

    
    SystemName = property(__SystemName.value, __SystemName.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineTypeModelSerialNumber uses Python identifier MachineTypeModelSerialNumber
    __MachineTypeModelSerialNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MachineTypeModelSerialNumber'), 'MachineTypeModelSerialNumber', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10MachineTypeModelSerialNumber', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 96, 12), )

    
    MachineTypeModelSerialNumber = property(__MachineTypeModelSerialNumber.value, __MachineTypeModelSerialNumber.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}LongTermMonitorEnabled uses Python identifier LongTermMonitorEnabled
    __LongTermMonitorEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LongTermMonitorEnabled'), 'LongTermMonitorEnabled', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10LongTermMonitorEnabled', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 113, 12), )

    
    LongTermMonitorEnabled = property(__LongTermMonitorEnabled.value, __LongTermMonitorEnabled.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AggregationEnabled uses Python identifier AggregationEnabled
    __AggregationEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AggregationEnabled'), 'AggregationEnabled', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10AggregationEnabled', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 130, 12), )

    
    AggregationEnabled = property(__AggregationEnabled.value, __AggregationEnabled.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ShortTermMonitorEnabled uses Python identifier ShortTermMonitorEnabled
    __ShortTermMonitorEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortTermMonitorEnabled'), 'ShortTermMonitorEnabled', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10ShortTermMonitorEnabled', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 147, 12), )

    
    ShortTermMonitorEnabled = property(__ShortTermMonitorEnabled.value, __ShortTermMonitorEnabled.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}ComputeLTMEnabled uses Python identifier ComputeLTMEnabled
    __ComputeLTMEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComputeLTMEnabled'), 'ComputeLTMEnabled', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10ComputeLTMEnabled', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 164, 12), )

    
    ComputeLTMEnabled = property(__ComputeLTMEnabled.value, __ComputeLTMEnabled.set, None, None)

    
    # Element {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AssociatedManagedSystem uses Python identifier AssociatedManagedSystem
    __AssociatedManagedSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssociatedManagedSystem'), 'AssociatedManagedSystem', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_ManagedSystemPcmPreference_Type_httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10AssociatedManagedSystem', False, pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 181, 12), )

    
    AssociatedManagedSystem = property(__AssociatedManagedSystem.value, __AssociatedManagedSystem.set, None, None)

    
    # Attribute schemaVersion inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type
    
    # Attribute base inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type
    
    # Attribute lang inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type
    
    # Attribute space inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type
    
    # Attribute id inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractRest.Type
    _ElementMap.update({
        __SystemName.name() : __SystemName,
        __MachineTypeModelSerialNumber.name() : __MachineTypeModelSerialNumber,
        __LongTermMonitorEnabled.name() : __LongTermMonitorEnabled,
        __AggregationEnabled.name() : __AggregationEnabled,
        __ShortTermMonitorEnabled.name() : __ShortTermMonitorEnabled,
        __ComputeLTMEnabled.name() : __ComputeLTMEnabled,
        __AssociatedManagedSystem.name() : __AssociatedManagedSystem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ManagedSystemPcmPreference.Type', ManagedSystemPcmPreference_Type)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (MachineTypeModelSerialNumber_Type):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 97, 16)
    _ElementMap = MachineTypeModelSerialNumber_Type._ElementMap.copy()
    _AttributeMap = MachineTypeModelSerialNumber_Type._AttributeMap.copy()
    # Base type is MachineTypeModelSerialNumber_Type
    
    # Element Metadata ({http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Metadata) inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Element MachineType ({http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineType) inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineTypeModelSerialNumber.Type
    
    # Element Model ({http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}Model) inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineTypeModelSerialNumber.Type
    
    # Element SerialNumber ({http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}SerialNumber) inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}MachineTypeModelSerialNumber.Type
    
    # Attribute schemaVersion inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute kxe uses Python identifier kxe
    __kxe = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kxe'), 'kxe', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_9_kxe', False_Type)
    __kxe._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    __kxe._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ETagBehavior.xsd', 21, 8)
    
    kxe = property(__kxe.value, __kxe.set, None, None)

    
    # Attribute kb uses Python identifier kb
    __kb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kb'), 'kb', '__httpwww_ibm_comxmlnssystemspowerfirmwarepcmmc2012_10_CTD_ANON_9_kb', ROR_Type)
    __kb._DeclarationLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    __kb._UseLocation = pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\RESTStereotypes.xsd', 123, 8)
    
    kb = property(__kb.value, __kb.set, None, None)

    
    # Attribute base inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute lang inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute space inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    
    # Attribute id inherited from {http://www.ibm.com/xmlns/systems/power/firmware/pcm/mc/2012_10/}AbstractNonRest.Type
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kxe.name() : __kxe,
        __kb.name() : __kb
    })



AbstractRest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractRest'), AbstractRest_Type, documentation='\n                \n            ', location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 52, 4))
Namespace.addCategoryObject('elementBinding', AbstractRest.name().localName(), AbstractRest)

AbstractNonRest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AbstractNonRest'), AbstractNonRest_Type, documentation='\n                \n            ', location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 67, 4))
Namespace.addCategoryObject('elementBinding', AbstractNonRest.name().localName(), AbstractNonRest)

MachineTypeModelSerialNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MachineTypeModelSerialNumber'), MachineTypeModelSerialNumber_Type, documentation='\n                \n                \n            ', location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 46, 4))
Namespace.addCategoryObject('elementBinding', MachineTypeModelSerialNumber.name().localName(), MachineTypeModelSerialNumber)

ManagedSystemPcmPreference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ManagedSystemPcmPreference'), ManagedSystemPcmPreference_Type, documentation='\n                \n                \n            ', location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 47, 4))
Namespace.addCategoryObject('elementBinding', ManagedSystemPcmPreference.name().localName(), ManagedSystemPcmPreference)



Metadata_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Atom'), AtomMetadata_Type, scope=Metadata_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 141, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Metadata_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Atom')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 141, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Metadata_Type._Automaton = _BuildAutomaton()




AtomMetadata_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AtomID'), AtomID_Type, scope=AtomMetadata_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 201, 12)))

AtomMetadata_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AtomCreated'), AtomDateTime_Type, scope=AtomMetadata_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 250, 12)))

AtomMetadata_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AtomUpdated'), AtomDateTime_Type, scope=AtomMetadata_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 276, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 167, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 171, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 175, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AtomMetadata_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AtomID')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 201, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AtomMetadata_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AtomCreated')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 250, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AtomMetadata_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AtomUpdated')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 276, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AtomMetadata_Type._Automaton = _BuildAutomaton_()




CommonRESTCollection_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'link'), AtomLink_Type, scope=CommonRESTCollection_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 73, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 167, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 170, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CommonRESTCollection_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'link')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\ietf\\AtomLink.xsd', 73, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CommonRESTCollection_Type._Automaton = _BuildAutomaton_2()




AbstractRest_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), Metadata_Type, scope=AbstractRest_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 117, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractRest_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractRest_Type._Automaton = _BuildAutomaton_3()




AbstractNonRest_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Metadata'), Metadata_Type, scope=AbstractNonRest_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 148, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractNonRest_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractNonRest_Type._Automaton = _BuildAutomaton_4()




MachineTypeModelSerialNumber_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MachineType'), CTD_ANON, scope=MachineTypeModelSerialNumber_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 78, 8)))

MachineTypeModelSerialNumber_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Model'), CTD_ANON_, scope=MachineTypeModelSerialNumber_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 95, 12)))

MachineTypeModelSerialNumber_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SerialNumber'), CTD_ANON_2, scope=MachineTypeModelSerialNumber_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 112, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 148, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 176, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MachineTypeModelSerialNumber_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MachineTypeModelSerialNumber_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MachineType')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 78, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MachineTypeModelSerialNumber_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 95, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MachineTypeModelSerialNumber_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SerialNumber')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 112, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MachineTypeModelSerialNumber_Type._Automaton = _BuildAutomaton_5()




ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SystemName'), CTD_ANON_3, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 79, 8)))

ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MachineTypeModelSerialNumber'), CTD_ANON_9, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 96, 12)))

ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LongTermMonitorEnabled'), CTD_ANON_4, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 113, 12)))

ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AggregationEnabled'), CTD_ANON_5, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 130, 12)))

ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortTermMonitorEnabled'), CTD_ANON_6, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 147, 12)))

ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComputeLTMEnabled'), CTD_ANON_7, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 164, 12)))

ManagedSystemPcmPreference_Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssociatedManagedSystem'), CTD_ANON_8, scope=ManagedSystemPcmPreference_Type, location=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 181, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 117, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 243, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SystemName')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 79, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MachineTypeModelSerialNumber')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 96, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LongTermMonitorEnabled')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 113, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AggregationEnabled')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 130, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortTermMonitorEnabled')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 147, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComputeLTMEnabled')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 164, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ManagedSystemPcmPreference_Type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssociatedManagedSystem')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\ManagedSystemPcmPreference.xsd', 181, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ManagedSystemPcmPreference_Type._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\CommonGlobals.xsd', 148, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 176, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Metadata')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\common\\inc\\CommonMetaData.xsd', 88, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MachineType')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 78, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Model')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 95, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SerialNumber')), pyxb.utils.utility.Location('C:\\Users\\IBM_ADMIN\\Desktop\\pmc.schema.pcm-8.8.2.2\\schema\\pcm\\MachineTypeModelSerialNumber.xsd', 112, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_7()


MachineTypeModelSerialNumber._setSubstitutionGroup(AbstractNonRest)

ManagedSystemPcmPreference._setSubstitutionGroup(AbstractRest)
