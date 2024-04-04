class Node:
    def __init__(self,attribute_index = None, attribute_value = None, decision = None, children = None):
        self.attribute_index = attribute_index
        self.attribute_value = attribute_value
        self.decision = decision
        self.children = children if children is not None else {}
    # def __str__(self):
    #     return f'{self.attribute_value}, {self.decision}, {self.children}'