import ssl
import suds

from suds.client import Client
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


def PlanClient(config):
    client = Client(
        URLBuilder(config.server, PLAN_WSDL), transport=CustomTransport())
    client.set_options(
        soapheaders=SessionClient(
            config.server, config.username, config.password))
    return client


def SessionClient(server, username, password):
    client = Client(
        URLBuilder(server, SESSION_WSDL),
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
        URLBuilder(config.server, TRACKER_WSDL), transport=CustomTransport())
    client.set_options(
        soapheaders=SessionClient(
            config.server, config.username, config.password))
    return client


def URLBuilder(server, url):
    '''Return full URL for WSDL file.'''
    return url.format(server)
