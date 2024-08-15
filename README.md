# Location-Based Species Presence Prediction

Welcome to the GitHub repository for my Master’s thesis on **Location-Based Species Presence Prediction**, inspired by the GeoLifeCLEF Kaggle competition. This repository contains the code and resources used in my research, aimed at predicting the presence of various species based on geographical and environmental data.

## Overview

This repository is dedicated to benchmarking models for species presence prediction using location-based data. The dataset used in this research is derived entirely from the GeoLifeCLEF Kaggle competition, which provides a rich collection of geographical and environmental features for use in predictive modeling.

## Repository Structure

- **`240605_multimodal_embedding.ipynb`**: This file contains code used for generating multimodal embeddings. These embeddings are created by combining different data modalities (such as environmental, geographical, and species data) to improve the accuracy of species presence prediction models.

- **`240320_raster_preprocessing.ipynb`**: This file includes the preprocessing code for handling raster data for the Top k Binary Classifier approach.

- **`[date]_benchmark_[approach]`**: These files contain the code for benchmarking each approach.

- **`240712_benchmark_analysis.ipynb`**: This file contains the code visualizing the benchmark results.

- **`bench_utils.py`**: Contains helpful functions and classes for the benchmark.

- **`schematics.ipynb`**: This file includes the code for the different architecture schematics of the approaches.

- **`survey_map.ipynb`**: This file includes the code for the different map visualization of the geographic data.

## Data

The data used in this repository is exclusively from the [GeoLifeCLEF Kaggle competition](https://www.kaggle.com/competitions/geolifeclef-2024). Due to the size and licensing constraints of the dataset, it is not included in this repository. To access the data, please refer to the competition page and follow the provided instructions.

## How to Use

1. **Clone the Repository**:
   You can clone this repository and run it locally or fork the respective notebook on Kaggle. If a notebook is available on Kaggle, a      link to it is placed at the top of every file. The GNN approach for example is not, due to package-environment issues in the Kaggle      editor.

2. **Install Dependencies and adjust paths**: 
   Ensure you have Python 3.x and the required dependencies installed. Also make sure that you adjust the paths for loading and storing     data to your environment.

3. **Preprocess Data**: 
   Use the code in the two preprocessing files to preprocess the GeoLifeCLEF dataset. This step is essential for preparing     the data     for model training.

4. **Run Benchmarks**: 
   Use the notebooks to run and evaluate the approaches.


## Contributions

Contributions to this project are welcome. Please feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more details.

## Acknowledgements

Special thanks to the organizers of the GeoLifeCLEF competition for providing the dataset and the inspiration for this research. Additionally, I would like to acknowledge my academic supervisors and peers who provided valuable guidance and feedback throughout this project.

---

For any questions or further information, please contact me at [mathis.jander@web.de].

---

Thank you for visiting the repository and exploring my work on location-based species presence prediction!
