# CSCI 5527 Final Project

Code to reproduce (most) results for "Weather Prediction using Transformer-based Time-Series Forecasting"

### Description of files:

Scripts

- CustomData, exp, location_ids, original_files, utils, data, img, models, scripts, main_informer.py: These directories/files are from the Informer repository and are used in the Jupyter Notebooks to train the models

- fetch_weather_data.py: This script fetches the weather data of the specified station from the  Local Climatological Data website of all of the years between the given start and end date. It then removes all of the unused columns and cleans the data by removing all rows with NaN values. It outputs a single csv file with all of the formatted weather data in order from the start to end years.

Notebooks
- weather_informer_MS_hours_concat_nearby.ipynb: This notebook contains code for use on Google Colab for reproducing the "Long term prediction + nearby features" experiment. This notebook clones the Informer repository and trains the model on a V100 GPU using weather data from the Local Climatological Data (LCD) for the Minneapolis-Saint Paul airport.
Features from: MINNEAPOLIS FLYING CLOUD AIRPORT, MINNEAPOLIS CRYSTAL AIRPORT, and ST. PAUL DOWNTOWN AIRPORT are also used.
- csci5527_final_plots.ipynb: This notebook contains code for use on Google Colab for plotting Informer test set predictions vs ground truth for both short term and long term prediction tasks

Data

- msp_results: This directory contains serialized numpy arrays of predicted and ground truth wet bulb temperatures on the test set, generated during Informer model training for the "MSP" and "MSP + nearby" experiements.
- station_data.csv: scraped metadata for all 13,400 weather stations available in the 2023 release of LCD
- weather_data_msp_same_timepoints_as_concat.csv, weather_data_msp_with_nearby_concat: The two datasets used for training. First file includes weather features for just MSP, and second file includes MSP features plus (time-matched) nearby station features