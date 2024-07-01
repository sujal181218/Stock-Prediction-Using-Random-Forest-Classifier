# Stock Prediction Using Random Forest Classifier

This project leverages machine learning techniques to predict stock prices using a Random Forest Classifier. The overall workflow is outlined below:

1. **Acquire Historical Fundamental Data** – These are the *features* or *predictors*.
2. **Acquire Historical Stock Price Data** – This will make up the dependent variable.
3. **Preprocess Data** – Clean and prepare the data for modeling.
4. **Model Training** – Use a machine learning model to learn from the data.
5. **Backtest Model Performance** – Evaluate the model's performance on historical data.
6. **Acquire Current Fundamental Data** – Gather up-to-date features for prediction.
7. **Model Verification** – Use a Random Forest Classifier to verify the model's accuracy.
8. **Generate Predictions** – Use current fundamental data to make stock price predictions.

## Random Forest Classifier

The Random Forest Classifier is an ensemble learning method that operates by constructing multiple decision trees during training. Each tree is trained on a random subset of the data, and the final prediction is made by averaging the predictions of all individual trees. Here’s how it works:

- **Bootstrap Aggregation (Bagging)**: The model uses bagging to generate multiple subsets of the original dataset by sampling with replacement. Each subset is used to train a separate decision tree.
- **Random Feature Selection**: At each split in the decision tree, a random subset of features is selected. This randomness helps to create diverse trees and reduces the correlation between them.
- **Voting Mechanism**: For classification tasks, each tree in the forest votes for the predicted class. The class with the majority vote is chosen as the final prediction. For regression tasks, the average prediction of all trees is taken.
- **Reduction of Overfitting**: By averaging the results of multiple trees, Random Forest reduces the risk of overfitting to the training data, leading to more robust predictions.
- **Feature Importance**: Random Forest can calculate the importance of each feature in making predictions, providing insights into which factors are most influential.

Key advantages of using Random Forest in this project include its robustness to overfitting, ability to handle large datasets with mixed feature types, and the provision of feature importance metrics.

## Quickstart

To get started with the project, follow these steps:

1. Open a terminal and navigate to the project's directory:

   ```bash
   cd Users/User/Desktop/Stock-Prediction-Using-Random-Forest-Classifier
   ```
2. Install the required dependencies:
   ```bash
      pip3 install -r requirements.txt
   ```
3. Download historical stock price data:
    ```bash
    python3 download_historical_prices.py
    ```
4. Parse key statistics for model features:
    ```bash
    python3 parsing_keystats.py
    ```  
5. Backtest the model's performance on historical data:
    ```bash
    python3 backtesting.py
    ```
6. Acquire current fundamental data:
    ```bash
    python3 current_data.py
    ```
7. Run tests to ensure everything is working correctly:
    ```bash
    pytest -v
    ```
8. Generate stock price predictions:
    ```bash
    python3 stock_prediction.py
    ```

## Conclusion
This project demonstrates how to use machine learning, specifically the Random Forest Classifier, to predict stock prices. By following the steps outlined above, you can replicate the process and generate your own stock price predictions based on current fundamental data.

For further details and explanations, please refer to the respective Python scripts in the project directory.
    






