import tensorflow as tf
import numpy as np
from preprocessing import loadData
tMSE = []
for i in range(0, 10):
    inputs, labels, tInputs, tLabels = loadData()
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(14,)),
        tf.keras.layers.Normalization(),
        tf.keras.layers.Dense(8),
        tf.keras.layers.Dense(1)
    ])
    model.compile(tf.keras.optimizers.Adam(learning_rate=0.0002),
                loss='mean_squared_error',
                metrics=[tf.keras.metrics.MeanSquaredError()])
    model.fit(inputs, labels, batch_size=1, epochs=43)
    tMSE.append(model.evaluate(tInputs, tLabels, batch_size=1)[0])
print("Average MSE: " + str(sum(tMSE) / 10))
print("All MSE: " + str(tMSE))
