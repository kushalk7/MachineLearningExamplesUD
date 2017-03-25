import IPython.nbformat.current as nbf
nb = nbf.read(open('dt_author_id.py', 'r'), 'py')
nbf.write(nb, open('dt_author_id.ipynb', 'w'), 'ipynb')