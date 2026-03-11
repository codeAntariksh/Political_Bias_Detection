import nbformat

def clean_notebook_metadata(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Remove the problematic widgets metadata
    if 'widgets' in nb.metadata:
        del nb.metadata['widgets']
        print(f"Successfully cleaned metadata from {input_file}")
    
    with open(input_file, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

clean_notebook_metadata('Additional_Attribute_Features.ipynb')