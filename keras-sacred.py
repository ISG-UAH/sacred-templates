import keras
from sacred import Experiment
from sacred.observers import MongoObserver, FileStorageObserver

ex = Experiment("keras-sacred")
# Uncomment to add MongoDB support
#ex.observers.append(MongoObserver(url="mongodb://<user>:<password>@<hostname>:<port>/<auth-db>", db_name="<sacred-db>"))

ex.observers.append(FileStorageObserver("cnn-experiment"))


@ex.config
def cfg():
    batch_size = 64
    num_epochs = 10
    learning_rate = 0.01


class MetricsLoggerCallback(keras.callbacks.Callback):
    def __init__(self, _run):
        super().__init__()
        self._run = _run

    def on_epoch_end(self, _, logs):
        self._run.log_scalar("training.loss", logs.get('loss'))
        self._run.log_scalar("training.acc", logs.get('accuracy'))
        self._run.log_scalar("validation.loss", logs.get('val_loss'))
        self._run.log_scalar("validation.acc", logs.get('val_accuracy'))

@ex.automain
def run(_run, batch_size, num_epochs, learning_rate):
    
    # importing the dataset
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    # normalizing the images to 0 and 1
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # setting up the model
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    # compiling the model
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
                loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    # training the model
    model.fit(train_images, train_labels,
            batch_size=batch_size,
            epochs=num_epochs,
            validation_data=(test_images, test_labels),
            callbacks=[MetricsLoggerCallback(_run)],
            verbose=2)

    # evaluating the model
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    ex.log_scalar("test loss", test_loss)
    ex.log_scalar("test acc", test_acc)
    print('Test loss:', test_loss, ' and Test accuracy:', test_acc)
    
    # We also can store our trained model
    # pickle.dump(model, open("mymodel.p", "wb"))
    # ex.add_artifact("mymodel.p")

    return test_acc
