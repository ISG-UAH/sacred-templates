# sacred-templates

Sacred templates for ISG Machine Learning and experimental algorithmics experiments. 

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

## Omniboard local execution

To execute Omniboard locally, you hust have docker un your machine, once this precondition is satisfied, running Omniboard is a piece of cake:

```
docker run --name omniboard --net=host -e MONGO_URI=mongodb://<mongo-user>:<mongo-passwd>@<host>:27017/<mongo-db>?authMechanism=SCRAM-SHA-1 vivekratnavel/omniboard
```

There should be now an Omniboard instance running on *localhost:9000*.

## Manage MongoDB database

```
docker run -it --rm --name mongo-express --network host -e ME_CONFIG_BASICAUTH_USERNAME="" -e ME_CONFIG_MONGODB_SERVER="myServer" -e ME_CONFIG_MONGODB_AUTH_DATABASE="myDatabase" -e ME_CONFIG_MONGODB_AUTH_USERNAME="myUser" -e ME_CONFIG_MONGODB_AUTH_PASSWORD="myPassword" mongo-express
```
