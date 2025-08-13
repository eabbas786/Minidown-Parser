# imports
from python_files.parse import read_minidown_file
from python_files.html_renderer import emit_minidown_as_html


if __name__ == "__main__":
    # define paths of input and output files
    input_path = '/Users/elsaabbas/code/minidown_parser/minidown.md'
    output_path = '/Users/elsaabbas/code/minidown_parser/exercise.html'

    # read and parse Minidown file
    print(f"Parsing Minidown file: {input_path}")
    parsed_document = read_minidown_file(input_path)

    # print(f"DEBUG OUTPUT: This is the parsed document object children: {parsed_document.children}")


    # render parsed_document into html file
    print(f"Creating HTML File at path: {output_path}")
    is_success = emit_minidown_as_html(parsed_document, output_path)

    if is_success:
        print(f"The HTML file {output_path} has been created!")
    else:
        print(f"Unable to create the HTML file due to errors.")


    





