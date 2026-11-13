🚀 Global EV Charging Infrastructure Power Predictor
📌 Project Overview
This project builds an end-to-end supervised machine learning regression pipeline to analyze and predict the maximum power output capacity (MaxPowerKW) of electric vehicle (EV) charging stations worldwide. Utilizing a large-scale global dataset of over 250,000+ charging stations, this project demonstrates exploratory data analysis (EDA), geospatial data cleaning, feature engineering, and model evaluation using Python.
📂 Dataset & Features
	Source: Global EV Charging Station Network Dataset (Kaggle)
	Total Records Processed: 257,585 stations across multiple global regions.
	Target Variable (Y): MaxPowerKW (Maximum charging power output in kilowatts).
	Independent Features (X):
	Latitude & Longitude (Geospatial coordinates)
	FastChargeCount (Number of fast chargers available at the station)
	YearCreated (Infrastructure establishment year)
🛠️ Data Pipeline & Workflow
	Data Ingestion & Inspection: Loaded large-scale tabular data using pandas, inspected data types, handled missing values, and analyzed statistical distributions.
	Data Preprocessing & Splitting: Dropped null records for target/feature subsets and split the cleaned dataset into an 80% training set and 20% testing set (train_test_split).
	Model Training: Trained a Multiple Linear Regression model using scikit-learn to establish a baseline relationship between geographic/temporal features and station power capacity.
	Evaluation & Visualization: Evaluated performance using regression error metrics and generated an Actual vs. Predicted scatter plot using matplotlib.
📈 Model Evaluation Results
	Mean Absolute Error (MAE): 28.25 kW
	Root Mean Squared Error (RMSE): 52.81 kW
	R-squared (R^2) Score: 0.2284
💡 Key Takeaways & Insights
	Feature Impact: Model coefficients revealed that FastChargeCount has the strongest positive impact on station power output (adding ~29.78 kW per fast charger count), which aligns logically with modern high-capacity DC fast-charging hubs.
	Model Limitations & Interview Talking Points: The R^2score of 0.2284 indicates that a standard linear model captures about 23% of the variance. As visualized in the Actual vs. Predicted plot, infrastructure power output tiers (such as 7 kW AC slow chargers vs. 150–350 kW DC fast chargers) do not scale linearly with coordinates (Latitude/Longitude).
	Next Steps for Improvement: Transitioning from a linear baseline to non-linear tree-based ensembles (such as Random Forest or XGBoost) and incorporating categorical attributes (like ConnectionTypes and Operator via One-Hot Encoding) will significantly improve prediction accuracy.
💻 Tech Stack
	Language: Python
	Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn
	Environment: Jupyter Notebook
