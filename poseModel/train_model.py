import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
import numpy as np

# Load annotations from file
with open('./data/annotation.txt') as f:
    annotations = [line.strip().split(',') for line in f]

# Define model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu',
                           input_shape=(256, 256, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(34)
])

# Define loss function and optimizer
loss_fn = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam()

# Define training step function


@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        y_pred = model(x)
        loss = loss_fn(y, y_pred)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    accuracy = tf.reduce_mean(tf.keras.metrics.mean_squared_error(y, y_pred))
    return {'mse': loss, 'accuracy': accuracy}


# Prepare data for training
train_images = []
train_labels = []
for annotation in annotations:
    img_path, *keypoints = annotation[0], annotation[1:]
    img = cv2.imread(img_path)
    img = cv2.resize(img, (256, 256))
    train_images.append(img)
    train_labels.append(keypoints)
train_images = np.array(train_images, dtype='float32') / 255.0
train_labels = np.array(train_labels, dtype='float32')

# Split data into training and validation sets
split = int(len(train_images) * 0.8)
train_data = tf.data.Dataset.from_tensor_slices(
    (train_images[:split], train_labels[:split]))
val_data = tf.data.Dataset.from_tensor_slices(
    (train_images[split:], train_labels[split:]))

# Train the model
model.compile(optimizer=optimizer, loss=loss_fn, metrics=['accuracy'])
history = model.fit(train_data.batch(32), epochs=50,
                    validation_data=val_data.batch(32))

# Plot the training and validation loss over time
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Plot the training and validation accuracy over time
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
