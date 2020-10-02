# sacred-templates

Sacred templates for ISG Machine Learning experiments. 

## Using Sacred

Command-line arguments.

```
python scikit-sacred.py with 'text="Adios"' 'gamma=0.9'
```

From Sacred documentation.

```
./example.py with 'my_list=[1, 2, 3]'
./example.py with 'nested_list=[["a", "b"], [2, 3], False]'
./example.py with 'my_dict={"a":1, "b":[-.2, "two"]}'
./example.py with 'alpha=-.3e-7'
./example.py with 'mask=0b111000'
./example.py with 'message="Hello Bob!"'
```

Configuration can also be stored in a file (not tested).

```
python scikit-sacred.py with configuration.json
```

In case you need to debug your configuration

```
python scikit-sacred.py print_config
```
## Repository files

*scikit-sacred.py*: Scikit-learn with Sacred and MongoDB observer example.

*keras-sacred.py*: Keras with Sacred and MongoDB observer example.

*notebook-keras-sacred.ipynb*: Notebook with a Keras train model.
