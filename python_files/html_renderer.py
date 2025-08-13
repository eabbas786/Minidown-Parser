3 # imports
from python_files.AST import (
    DocumentNode, HeadingNode, ParagraphNode, BulletListNode, InlineCodeNode, 
    DisplayedCodeNode, TextNode, ListItemNode
)

import html # for escaping

def emit_minidown_as_html(x : DocumentNode, output_file_path) -> bool:
    """
    Recursively renders an AST node into an HTML string,
    and then writes that string to the specified output file.
    Ensures proper HTML escaping for text content.
    """
    html_output = [] # to help build html string

    # helper function that actually traverses through all nodes starting at DocumentNode
    def render_to_html(node):
        
        if isinstance(node, DocumentNode):
            # DocumentNode is the root node; iterate and recursively process
            # its children
            html_output.append("<html><body>\n\n")
            for child in node.children:
                render_to_html(child)

            html_output.append("</body></html>")


        elif isinstance(node, HeadingNode):
            tag = f"h{node.level}" # h1, h2, ... h6
            html_output.append(f"<{tag}>")

            # process children
            for child in node.children:
                render_to_html(child)
                
                
            html_output.append(f"</{tag}>\n\n")

        elif isinstance(node, ParagraphNode):
            html_output.append("<p>\n")
            # process children
            for child in node.children:
                render_to_html(child)
                html_output.append("\n")

            html_output.append("</p>\n\n")

        elif isinstance(node, BulletListNode):
            html_output.append("<ul>\n")

             # process children
            for child in node.children[1:]:
                render_to_html(child)

            html_output.append("</ul>\n\n")


        elif isinstance(node, DisplayedCodeNode):
            # Get all content stored in code block. DisplayCodeNode.content is a string
            # DisplayedCodeNode has no children     
            # use html.escape to treat &, <, > as part of the code
            html_output.append(f"<pre>\n{html.escape(node.content)}\n</pre>\n\n")
        
        elif isinstance(node, ListItemNode):
            html_output.append("<li> ")
             # process children
            for child in node.children:
                render_to_html(child)
                html_output.append(" ")

            html_output.append(" </li>\n")
            
            
        elif isinstance(node, InlineCodeNode):
            # InlineCodeNode.content is a string
            # # use html.escape with quote=True  to treat `&`, `<`, `>`, `"`, `'` as part of the code
            # InlineCodeNode has no children
            html_output.append(f"<code> {html.escape(node.content, quote=True)} </code>")
            

        elif isinstance(node, TextNode):
            # TextNode.content is a string
            # use html.escape with quote=True to treat `&`, `<`, `>`, `"`, `'` as part of the code
            # TextNode has no children
            html_output.append(html.escape(node.content, quote=True))

        else: # this should not happen if all of the node types have been handled correctly
            print(f"Warning: Unknown AST node type encountered: {type(node).__name__}")


    render_to_html(x) # traverse the AST Node. 
    final_html_string = ''.join(html_output) # convert to string
    
    # open/ create file and write final_html_string to it
    try: 
        with open(output_file_path, "w") as file:
            file.write(final_html_string)
        print(f"HTML file successfully creates at {output_file_path}")
        return True
    
    except IOError as e:
        print(f"Error creating HTML file: {e}")
        return False

    except Exception as e:
        print(f"Unexepected error in creating the file: {e}")
        return False




    

    







    





    




    

