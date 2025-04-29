# Importing libraries
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from skimage import io, color, transform, feature
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score

# Defining dataset path and category labels
data_set_path = 'img'
categories = ['car', 'cat', 'dog', 'painting']


def main():
    # Storage lists
    data = []
    labels = []
    file_names = []
    original_images = []

    # Loading preprocessed images
    for label_idx, category in enumerate(categories):
        category_path = os.path.join(data_set_path, category)
        if not os.path.exists(category_path):
            print(f'Folder does not exist: {category_path}')
            continue
        for image_filename in os.listdir(category_path):
            image_path = os.path.join(category_path, image_filename)
            try:
                image = io.imread(image_path)
                original_images.append(image)
                file_names.append(image_filename)

                # Convert to grayscale if RGB
                if image.ndim == 3:
                    image = color.rgb2gray(image)

                # Resize after conversion
                image_resized = transform.resize(image,(128, 64))

                # HOG feature extraction
                hog_features = feature.hog(
                    image_resized,
                    orientations=9,
                    pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2),
                    block_norm='L2-Hys'
                )

                data.append(hog_features)
                labels.append(label_idx)

            except Exception as e:
                print(f'Error scanning image: {image_path}: {e}')

    # Converting data to numpy array for training/testing
    data = np.array(data)
    labels = np.array(labels)
    file_names = np.array(file_names)
    original_images = np.array(original_images, dtype=object)


    # Using StratifiedShuffleSplit for balanced train test split
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.45, random_state=42)
    train_index, test_index = next(sss.split(data, labels))
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = labels[train_index], labels[test_index]
    fn_train, fn_test = file_names[train_index], file_names[test_index]
    orig_train, orig_test = original_images[train_index], original_images[test_index]

    # Training model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')

    # DataFrame with file names and prediction results
    df = pd.DataFrame({
        'FileName': fn_test,
        'TrueCategory': [categories[i] for i in y_test],
        'PredictedCategory': [categories[i] for i in y_pred],
    })
    print('Few rows with results:')
    print(df.head())

    # Visualisation
    n_test = len(orig_test)
    n_cols = int(np.ceil(np.sqrt(n_test)))
    n_rows = int(np.ceil(n_test / n_cols))

    plt.figure(figsize=(n_cols * 3, n_rows * 3))
    for idx in range(n_test):
        plt.subplot(n_rows, n_cols, idx + 1)
        img = orig_test[idx]
        if img.ndim == 2:
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(img)
        plt.axis('off')
        true_label = categories[y_test[idx]]
        prd_label = categories[y_pred[idx]]
        plt.title(f'{fn_test[idx]} \n'
                  f'True label: {true_label} | Predicted label: {prd_label}',
                  fontsize=10)
    plt.show()

if __name__ == '__main__':
    main()