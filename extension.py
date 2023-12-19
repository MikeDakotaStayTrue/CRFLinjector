from burp import IBurpExtender
from burp import IHttpListener
from burp import IProxyListener
from burp import IScannerListener
from burp import IExtensionStateListener
from burp import ITab

import logging

from gui import GUI
from crlf_injector import CRLFInjector


class BurpExtender(IBurpExtender, IExtensionStateListener, IHttpListener, ITab):

    def registerExtenderCallbacks(self, callbacks):
        print('Registering CRLF Injector ... ')
        self.callbacks = callbacks
        self.helpers = callbacks.helpers
        self._injector = CRLFInjector(self)
        self._ui = GUI(self)
        

        callbacks.setExtensionName("CRLF Injector")
        callbacks.registerExtensionStateListener(self)
        callbacks.registerHttpListener(self)
        callbacks.addSuiteTab(self)

        print('CRLF Injector has been successfully registered')

    def getTabCaption(self):
        return 'CRLF Injector'

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo, macroItems=[]):
        try:
            self.scripts.processHttpMessage(toolFlag, messageIsRequest, messageInfo, macroItems)
        except Exception:
            traceback.print_exc(file=self.callbacks.getStderr())
        return
    
    def getUiComponent(self):
        self._ui.create_gui()
        return self._ui.get_main_panel()


    def get_header_name(self):
        return self._injector.header_name

    def get_header_value(self):
        return self._injector.header_value

    # Create opportunity to set more headers
    def set_header_name(self, header_name):
        self._injector.header_name = header_name

    def set_header_value(self, header_value):
        self._injector.header_name = header_name