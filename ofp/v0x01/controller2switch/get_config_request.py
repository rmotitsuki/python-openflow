"""Defines Get Config Request classes and related items"""

# Local source tree imports
from ofp.v0x01.common import header as of_header
from ofp.v0x01.foundation import base

# Classe


class GetConfigRequest(base.GenericStruct):
    """Get Config Request message.

    This message does not contain a body beyond the OpenFlow Header
        :param xid: xid to be used on the message header
    """
    header = of_header.OFPHeader()

    def __init__(self, xid=None):
        self.header.ofp_type = of_header.OFPType.OFPT_GET_CONFIG_REQUEST
        self.header.xid = xid