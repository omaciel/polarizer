import ssl
import suds

from suds.client import Client
from suds.plugin import MessagePlugin
from suds.sax.attribute import Attribute
from suds.transport.https import HttpAuthenticated

from urllib.request import HTTPSHandler

from polarizer.constants import (
    PLAN_WSDL,
    SESSION_WSDL,
    TRACKER_WSDL,
    )


class CustomTransport(HttpAuthenticated):

    def u2handlers(self):

        # use handlers from superclass
        handlers = HttpAuthenticated.u2handlers(self)

        # create custom ssl context, e.g.:
        ctx = ssl._create_unverified_context()
        # configure context as needed...
        ctx.check_hostname = False

        # add a https handler using the custom context
        handlers.append(HTTPSHandler(context=ctx))
        return handlers


class SoapNull(MessagePlugin):
    """Add a xsi:nil=true attribute to any element that is blank.
    Without this plugin, a number of functions that were supposed to accept
    null parameters did not work.
    """
    def marshalled(self, context):
        # Go through every node in the document and check if it is empty and
        # if so set the xsi:nil tag to true
        context.envelope.walk(self.add_nil)

    def add_nil(self, element):
        """Used as a filter function with walk to add xsi:nil to blank attrs.
        """
        if element.isempty() and not element.isnil():
            element.attributes.append(Attribute('xsi:nil', 'true'))


def PlanClient(config):
    client = Client(
        url=URLBuilder(config.server, PLAN_WSDL),
        plugins=[SoapNull()],
        transport=CustomTransport())
    client.set_options(
        soapheaders=SessionClient(
            config.server, config.username, config.password))
    return client


def SessionClient(server, username, password):
    client = Client(
        url=URLBuilder(server, SESSION_WSDL),
        plugins=[SoapNull()],
        transport=CustomTransport())
    client.service.logIn(username, password)
    session = client.last_received().childAtPath(
            'Envelope/Header/sessionID')
    session_id = session.text
    session_ns = session.namespace()
    header = suds.sax.element.Element(
        'sessionID', ns=session_ns).setText(session_id)
    return header


def TrackerClient(config):
    client = Client(
        url=URLBuilder(config.server, TRACKER_WSDL),
        plugins=[SoapNull()],
        transport=CustomTransport())
    client.set_options(
        soapheaders=SessionClient(
            config.server, config.username, config.password))
    return client


def URLBuilder(server, url):
    '''Return full URL for WSDL file.'''
    return url.format(server)
