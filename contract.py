#!/usr/bin/env python
import json


class SmartContract(object):
    def __init__(self,tx):
        self._=tx
    @property
    def txtype(self):
        return self._["txtype"]
    @property
    def txorigin(self):
        return self._["txorigin"]
    @property
    def txdestin(self):
        return self._["txdestin"]
    @property
    def txvalue(self):
        return self._["txvalue"]
    @property
    def txtime(self):
        return self._["txtime"]
    @property
    def txdate(self):
        return self._["txdate"]
    @property
    def txasset(self):
        return self._["txasset"]
    @property
    def txsummary(self):
        return self._["txsummary"]
    def __str__(self):
        return "Transaction Type: \033[92m "+self.txtype+"\n\033[90m"+"Transaction Date: \033[93m "+self.txdate+"\n\033[90m"+"Transaction Time: \033[93m "+self.txtime+"\n\033[90m\n"+"Transaction Origin: \033[94m "+self.txorigin+"\n\033[90m"+"Transaction Destination: \033[91m "+self.txdestin+"\n\033[90m\n"+"Transaction Asset: \033[92m "+self.txasset+"\n\033[90m"+"Asset Value: \033[95m "+self.txvalue+"\n\033[90m\n"+"\t\033[43m Summary:\033[0m\n"+self.txsummary+"\n"+"___"*21

from datetime import datetime

Example={
        "txtype":"Transfer",
        "txdate":str(datetime.now().date()),
        "txtime":str(datetime.now().time()),
        "txorigin":"TralahTek Inc.",
        "txdestin":"Amazon Aws Inc.",
        "txasset":"Bitcoin",
        "txvalue":"2.67",
        "txsummary":"Payment of Annual AWS cloud services fees for the year 2019.",
        }
example_contract=SmartContract(Example)

