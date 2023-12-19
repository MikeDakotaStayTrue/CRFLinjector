import logging

class CRLFInjector:
    def __init__(self, burp_extender, header_name="Foo", header_value="Bar"):
        self._extender = burp_extender
        self.header_name = header_name
        self.header_value = header_value
        self.mode = False