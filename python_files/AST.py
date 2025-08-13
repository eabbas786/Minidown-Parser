# This is an implementation of an Abstract syntax tree (AST) for Minidown.
# It contains class definitions to represent each of the Minidown components
# Each component class is a child of the ASTNode parent class


class ASTNode:
    # parent node: base node for all other nodes
    def __init__(self, children=None):
        self.children = children if children is not None else []


# children nodes

class DocumentNode(ASTNode):
    ''' 
    Represents an entire Minidown document
    Children: everything else in the document
    '''
    def __init__(self, children=None):
        super().__init__(children)


class HeadingNode(ASTNode):
    ''' 
    Represents a Minidown heading
    Children: plain text and/ or inline code
    '''
    def __init__(self, level, children=None):
        super().__init__(children)
        self.level = level 


class ParagraphNode(ASTNode):
    ''' 
    Represents a Paragraph in MiniDown
    Children: plain text and/ or inline code
    '''
    def __init__(self, children=None):
        super().__init__(children)


class BulletListNode(ASTNode):
    ''' 
    Represents a bulleted list in MiniDown
    Children: list item
    '''
    def __init__(self, children=None):
        super().__init__(children)


class ListItemNode(ASTNode):
    ''' 
    Represents a single list item in MiniDown
    Children: plain text and/ or inline code
    '''
    def __init__(self, children=None):
        super().__init__(children)


class InlineCodeNode(ASTNode):
    '''
    Represents inline code in Minidown
    Code is read literally so no children, only content
    Content is string type
    '''
    def __init__(self, content : str):
        super().__init__([])
        self.content = content
        

class DisplayedCodeNode(ASTNode):
    '''
    Represents a block of displayed code in Minidown.
    Code is read literally so no children, only content
    Content is string type
    '''
    def __init__(self, content : str):
        super().__init__([])
        self.content = content


class TextNode(ASTNode):
    '''
    Any other text in the Minidown file
    Plain text has no children, only content
    Content is string type
    '''
    def __init__(self, content : str):
        super().__init__([])
        self.content = content



    
        

  

        