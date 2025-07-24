# codelab-basic

This directory contains basic TensorFlow/Keras code samples for learning and experimentation.

## Files

- **train_code_labs1.py**  
  Trains a simple linear regression model using Keras to fit the equation `y = 3x + 1`.  
  The script:
  - Defines and compiles a model
  - Trains on sample data
  - Exports the model in TensorFlow SavedModel format
  - Prints a prediction for `x = 10.0`

## Usage

1. Install dependencies:
   ```bash
   pip install tensorflow numpy
   ```

2. Run the training script:
   ```bash
   python train_code_labs1.py
   ```

3. The trained model will be saved as `my_model_y_3x` in this directory.

## Notes

- The exported model is in TensorFlow SavedModel format, compatible with Keras 3 inference via `TFSMLayer`.
- For prediction using the exported model, see the corresponding prediction script.

---
```# codelab-basic

This directory contains basic TensorFlow/Keras code samples for learning and experimentation.

## Files

- **train_code_labs1.py**  
  Trains a simple linear regression model using Keras to fit the equation `y = 3x + 1`.  
  The script:
  - Defines and compiles a model
  - Trains on sample data
  - Exports the model in TensorFlow SavedModel format
  - Prints a prediction for `x = 10.0`

## Usage

1. Install dependencies:
   ```bash
   pip install tensorflow numpy
   ```

2. Run the training script:
   ```bash
   python train_code_labs1.py
   ```

3. The trained model will be saved as `my_model_y_3x` in this directory.

## Notes

- The exported model is in TensorFlow SavedModel format, compatible with Keras 3 inference via `TFSMLayer`.
- For prediction using the exported model, see the corresponding prediction script.