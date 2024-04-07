class Node:
    def __init__(self,attribute_index = None, decision = None, children = None):
        self.attribute_index = attribute_index
        self.decision = decision
        self.children = children if children is not None else {}
