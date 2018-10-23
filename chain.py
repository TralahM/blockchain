#!/usr/bin/env python

from block import Block
df={"Author":"TralahM","Title":"chain.py"}
def create_genesis_block(data):
    return Block(None,data)
Chain=[create_genesis_block(df)]
def add_to_chain(block):
    Chain.append(block)
for i in range(6):
    b=Block(Chain[-1].hash,[j for j in range(i+1)])
    add_to_chain(b)

for block in Chain:
    print(block)

class BlockChain(object):
    def __init__(self):
        self.chain=[self.create_genesis_block(),]
    def create_genesis_block(self,data={"Name":"Tcoin","Description":"Tcoin cryptocurrency Transactions."}):
        return Block(None,data)
    def add_block(self,block):
        #TODO
    def proof_of_work(self):
        #TODO
    @property
    def length(self):
        return len(self.chain)

