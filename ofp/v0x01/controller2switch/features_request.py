"""Defines Features Request classes and related items"""

# Local source tree imports
from ofp.v0x01.common import header as of_header
from ofp.v0x01.foundation import base

# Classes


class FeaturesRequest(base.GenericStruct):
    """Features request message.

    This message does not contain a body beyond the OpenFlow Header
        :param xid: xid to be used on the message header
    """
    header = of_header.OFPHeader()

    def __init__(self, xid=None):
        self.header.ofp_type = of_header.OFPType.OFPT_FEATURES_REPLY
        self.header.xid = xid