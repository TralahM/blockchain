#!/usr/bin/env python
import hashlib
from datetime import datetime

class Block(object):
    _nums=0
    def __init__(self,prev_hsh,data):
        """
        A Block Represents some Transaction between peers in the network like Asset[money,land,property,media] Transfer/Sale.
        The transaction has a smart contract that is the data and metadata.
        The transaction is accompanied by a timestamp of when it took place.
        """
        Block._nums+=1
        self.prev_hash=prev_hsh
        self.data=data
        self.timestamp=datetime.now()
        self.nonce=0
        self.hash=self.compute_hash()
    def compute_hash(self):
        md5=hashlib.md5()
        md5.update(
            str(str(self.prev_hash)+
            str(self.data)+
            str(self.timestamp)+
            str(self.nonce)).encode('utf-8')
        )
        return md5.hexdigest()
    def __str__(self):
        return "Signature:"+'\033[32m'""+str(self.hash)+'\033[0m\n'+'Index: '+str(self.data)+'\n'
    
