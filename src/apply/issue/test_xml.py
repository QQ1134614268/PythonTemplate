# -*- coding:utf-8 -*-
"""
@Time: 2021/7/12
@Description:
"""
import unittest
from io import StringIO
from xml.dom.minidom import parseString
from xml.etree import ElementTree

xml_txt = '<?xml version="1.0" encoding="UTF-8"?><env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:tds="http://www.onvif.org/ver10/device/wsdl" xmlns:trt="http://www.onvif.org/ver10/media/wsdl" xmlns:timg="http://www.onvif.org/ver20/imaging/wsdl" xmlns:tev="http://www.onvif.org/ver10/events/wsdl" xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl" xmlns:tan="http://www.onvif.org/ver20/analytics/wsdl" xmlns:tst="http://www.onvif.org/ver10/storage/wsdl" xmlns:ter="http://www.onvif.org/ver10/error" xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns:tns1="http://www.onvif.org/ver10/topics" xmlns:tmd="http://www.onvif.org/ver10/deviceIO/wsdl" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl" xmlns:wsoap12="http://schemas.xmlsoap.org/wsdl/soap12" xmlns:http="http://schemas.xmlsoap.org/wsdl/http" xmlns:d="http://schemas.xmlsoap.org/ws/2005/04/discovery" xmlns:wsadis="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:wstop="http://docs.oasis-open.org/wsn/t-1" xmlns:wsrf-bf="http://docs.oasis-open.org/wsrf/bf-2" xmlns:wsntw="http://docs.oasis-open.org/wsn/bw-2" xmlns:wsrf-rw="http://docs.oasis-open.org/wsrf/rw-2" xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" xmlns:wsrf-r="http://docs.oasis-open.org/wsrf/r-2" xmlns:trc="http://www.onvif.org/ver10/recording/wsdl" xmlns:tse="http://www.onvif.org/ver10/search/wsdl" xmlns:trp="http://www.onvif.org/ver10/replay/wsdl" xmlns:tnshik="http://www.hikvision.com/2011/event/topics" xmlns:hikwsd="http://www.onvifext.com/onvif/ext/ver10/wsdl" xmlns:hikxsd="http://www.onvifext.com/onvif/ext/ver10/schema" xmlns:tas="http://www.onvif.org/ver10/advancedsecurity/wsdl" xmlns:tr2="http://www.onvif.org/ver20/media/wsdl" xmlns:axt="http://www.onvif.org/ver20/analytics"><env:Header><wsa:To env:mustUnderstand="true">http://44.39.19.14:7080/videoAlarm/pushVideoWarn/44030500101325536071</wsa:To><wsa:Action>http://docs.oasis-open.org/wsn/bw-2/NotificationConsumer/Notify</wsa:Action></env:Header><env:Body><wsnt:Notify><wsnt:NotificationMessage><wsnt:Topic Dialect="http://www.onvif.org/ver10/tev/topicExpression/ConcreteSet">tns1:Monitoring/ProcessorUsage</wsnt:Topic><wsnt:Message><tt:Message UtcTime="2023-05-13T02:27:29Z" PropertyOperation="Changed"><tt:Source><tt:SimpleItem Name="Token" Value="Processor_Usage"/></tt:Source><tt:Data><tt:SimpleItem Name="Value" Value="13"/></tt:Data></tt:Message></wsnt:Message></wsnt:NotificationMessage></wsnt:Notify></env:Body></env:Envelope>'


class TestXml(unittest.TestCase):

    def test_ElementTree_xml(self):
        # tree = ElementTree.parse("tmp.xml")
        # envelop_ele = tree.getroot()
        envelop_ele = ElementTree.XML(xml_txt)
        print(envelop_ele.tag, envelop_ele.attrib, envelop_ele.text, envelop_ele.tail, envelop_ele.getchildren())
        envelop_ele.find('{http://www.w3.org/2003/05/soap-envelope}Header')
        envelop_ele.find('env:Header', namespaces={"env": "http://www.w3.org/2003/05/soap-envelope"})
        namespace = dict([node for _, node in ElementTree.iterparse(StringIO(xml_txt), events=['start-ns'])])
        print(namespace)
        envelop_ele.find('env:Header', namespace)
        body_ele = envelop_ele.find('env:Body', namespace)
        notify_ele = body_ele.find('wsnt:Notify', namespace)
        notify_meg_ele_list = notify_ele.findall('wsnt:NotificationMessage', namespace)
        print(notify_meg_ele_list)

    def test_xml2(self):
        envelop_ele = parseString(xml_txt)
        ele = envelop_ele.documentElement

        print(
            {"nodeName": ele.nodeName,
             "tagName": ele.tagName,
             "localName": ele.localName,
             "childNodes": ele.childNodes,
             "prefix": ele.prefix,
             "namespaceURI": ele.namespaceURI,
             "attributes": ele.attributes,
             "getElementsByTagName": ele.getElementsByTagName("env:Body"),
             "getElementsByTagNameNS": ele.getElementsByTagNameNS('http://www.w3.org/2003/05/soap-envelope', "Body")
             }
        )
