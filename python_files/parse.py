# import classes as defined AST.py
from python_files.AST import (
    DocumentNode, HeadingNode, ParagraphNode, BulletListNode, InlineCodeNode, 
    DisplayedCodeNode, TextNode, ListItemNode)




def read_file_generator(path):
    ''' 
    This generator reads the file of interest. 
    '''
    try: 
        # open file
        with open(path, 'r') as file:
            for line in file:
                yield line.rstrip('\n') 
    except FileNotFoundError:
        print(f"The file at {path} cannot be found")
        return
    except PermissionError:
        print(f"Error: Permission denied to read the file at path '{path}'.")
        return
    except IOError as e:
        # Catch other potential I/O errors (e.g., disk full, file corrupted)
        print(f"An I/O error occurred while reading the file at path '{path}': {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return

    

def inner_parse(line : str) -> list:
    ''' 
    This function parses a single line and checks
    if there is inline code.
    '''
    
    content, nodes = [], []
    is_code = False # checks which state we are in: text or inline code
    for word in line:
        if word == '`':
            # start or end of inline code
            if not is_code: 
                # start of inline code
                if content: nodes.append(TextNode("".join(content)))
                is_code = True
            else: # end of inline code
                if content: nodes.append(InlineCodeNode("".join(content)))
                is_code = False

            content.clear() # clear content for new state
        else: 
            content.append(word)

    # if contnet is not empty, then it must be of TextNode Object
    if content: nodes.append(TextNode("".join(content)))
     
    return nodes


def get_level(line : str) -> int:
    '''
    This function returns the level of a header
    '''
    idx = 0
    while idx < len(line) and line[idx] == '#': 
        idx += 1
    
    return idx

def is_header(level : int, line : str) -> bool:
    if level > 6 or len(line) < level + 1 or line[level] != ' ':
        # this is not a valid header
        return False
    else:
        return True


def parse_header(level : int, line : str) -> HeadingNode:
    ''' 
    This is a helper function that parses and stores
    header information.
    '''
    # process the actual header
    rem = line[level + 1: ] 

    # further parse line for inline code + create and return Header object
    parsed_line = inner_parse(rem)
    return HeadingNode(level, parsed_line)
    

    

def parse_bullet_list(line : str, gen) -> BulletListNode:
    '''
    This is a helper function that parses and stores
    bullet list information. 
    This expects line to be the first line in a valid
    bulleted list.
    '''
    items = [] # to store all of the list items
    curr_item = [] # to store all content of the current list item

    while True: 
        if line is None or not line.strip():
            # end of bullet list when EOF or an empty line
            if curr_item:
                # add last list item
                items.append(ListItemNode(list(curr_item)))
            return BulletListNode(items)
        
        if line.startswith("* "):
            # new list item: save curr list item and start processing new one
            items.append(ListItemNode(list(curr_item)))
            curr_item.clear() 
            line = line[2:] # only process the line after " *"

        parsed_line = inner_parse(line)  # further parse line for inline code
        curr_item.extend(parsed_line) 
        line = next(gen, None) # get the next line

  

def parse_code_block(line : str, gen) -> DisplayedCodeNode:
    '''
    This is a helper function that parses and stores code bock information.
    It collects code until a valid '```' is reached or EOF i.e. remainder
    of document will be interpreted as a code block. 
    Assumes `initial_fence_line` is the valid opening fence and has been 
    processed by the caller
    '''
    code = [] # all code in code block
    
    while True:
        line = next(gen, None) # get next line
        if line is None or (line.strip() == '```' and line.startswith('```')):
            # reached end of code block
            return DisplayedCodeNode('\n'.join(code))
        code.append(line)
        


            
def read_minidown_file(path) -> DocumentNode:
    '''
    This function passes path to read_file_generator and iterates and parses
    each line of the file in accordance to the rules outlined in mindown.md
    '''
    components = [] # stores all components/ children of document
    paragraph = [] # for processing paragraphs

    # create generator for file of interest
    # if error in reading file, the generator will be empty
    generator = read_file_generator(path)

    # process file
    while True:
        line = next(generator, None) # get next line
        if line is None: break # No more lines to process

        # parsing logic

        # 1) Code Block
        if (line.strip() == '```' and line.startswith('```')):
            # code block is starting
            if paragraph: 
                # end paragraph if in one
                components.append(ParagraphNode(paragraph))
                paragraph.clear()

            components.append(parse_code_block(line, generator)) # get and store code block

        # 2) Header
        elif line.startswith('#') and is_header(get_level(line), line): 
            # this is a header
            if paragraph: 
                # end paragraph if in one
                components.append(ParagraphNode(list(paragraph)))
                paragraph.clear()
            
            level = get_level(line) # get level
            components.append(parse_header(level, line)) # get and store header
            
        # 3) Bullet List   
        elif line.startswith("* "):
            # bullet list is starting
            if paragraph: 
                # end paragraph if in one
                components.append(ParagraphNode(list(paragraph)))
                paragraph.clear()

            components.append(parse_bullet_list(line, generator)) # get and store bullet list

        # 4) Paragraph
        else:
            if not line.strip() and paragraph:
                # curr paragraph comes to an end; start new one
                components.append(ParagraphNode(list(paragraph)))
                paragraph.clear()
                
            else: # there was no current paragraph
                parsed_line = inner_parse(line)
                paragraph.extend(parsed_line) # parse the line for plain text and inline code

            
    # Finish any remaining paragraph
    if paragraph: 
        components.append(ParagraphNode(list(paragraph)))
        
    return DocumentNode(components)

        















    
   


            



    