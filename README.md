# YELPFYP: Mobility-Aware Restaurant Recommendation on Yelp

This repository contains my Final Year Project on **mobility-aware restaurant recommendation** using Yelp data.  
The project studies how users’ movement patterns and activity hubs can be incorporated into the recommendation pipeline, and compares the resulting approach against more traditional baselines.

## Project Overview

Traditional recommender systems often focus mainly on user-item interaction history.  
However, for location-sensitive domains such as restaurants, **where a user usually moves** also matters.

This project explores a recommendation pipeline that combines:

- user visit history
- spatial restaurant information
- user mobility profiling
- candidate retrieval and ranking
- leave-one-out evaluation
- comparison against baseline recommendation models

The core idea is to test whether **mobility-aware filtering and retrieval** can better capture realistic restaurant choices than purely global recommendation methods.

---

## Objectives

The main goals of this project are:

1. Build a structured restaurant recommendation pipeline from Yelp data
2. Construct user visit sequences from check-in, review, tip, and business records
3. Profile user mobility patterns using clustering methods such as DBSCAN
4. Identify user activity centres / hubs
5. Generate recommendation candidates using mobility-aware logic
6. Evaluate recommendation performance with leave-one-out testing
7. Compare the mobility-aware pipeline against baseline models

---

## Repository Structure

```text
YELPFYP/
├─ artifacts/
│  ├─ checkpoints/            # Saved intermediate checkpoints
│  ├─ step1_outputs/          # Outputs from preprocessing / sequence building
│  ├─ step2_outputs/          # Outputs from mobility profiling
│  ├─ step3_outputs/          # Outputs from retrieval / recommendation generation
│  ├─ step4_outputs/          # Outputs from evaluation
│  ├─ export_ui_data/         # Processed outputs for UI/dashboard use
│  └─ lightfm_outputs/        # Baseline LightFM experiment outputs
│
├─ notebooks/
│  ├─ dbscan_work/            # DBSCAN and mobility-related notebooks
│  └─ initial_work/           # Earlier notebooks for preprocessing, modeling, evaluation
│
├─ retrieval_utils.py         # Helper utilities for recommendation / retrieval logic
├─ eligible_users_restaurant.txt
├─ user_ids_10k.txt
├─ user_profiles.json
├─ business_10k_restaurants.csv
├─ checkin_10k.csv
├─ reviews_10k.csv
├─ tips_10k.csv
├─ users_10k.csv
├─ master_10k_user_business.csv
├─ user_activity_centers_eps2km.csv
├─ visits_restaurant_geolocated.csv
├─ report_model_comparison.csv
├─ README.md
└─ LICENSE
```
---

## Data Used

The project uses a reduced / filtered subset of Yelp-related data for experimentation, including:

* **business data** for restaurant metadata
* **check-in data** for temporal visit behaviour
* **review data** for user-business interactions
* **tip data** for additional interaction signals
* **user data** for user-level information

Some files in this repository are intermediate or processed outputs derived from the original Yelp data, such as:

* `master_10k_user_business.csv`
* `visits_restaurant_geolocated.csv`
* `user_activity_centers_eps2km.csv`
* `user_profiles.json`

---

## Methodology

The pipeline is divided into multiple stages.

### 1. Data Exploration and Preparation

Initial notebooks inspect the Yelp subset, clean the data, and construct usable interaction records for downstream experiments.

### 2. User Sequence Construction

User visit histories are transformed into ordered sequences so that later stages can model recent behaviour and candidate prediction more realistically.

### 3. Mobility Profiling

User activity hubs are identified using spatial clustering methods such as **DBSCAN**.
This helps estimate where a user is typically active and how geographically concentrated or spread out their behaviour is.

### 4. Candidate Retrieval

Restaurants are retrieved using recommendation logic that can incorporate:

* historical user interactions
* mobility-centred filtering
* geographic constraints
* profile-based retrieval

### 5. Evaluation

The system is evaluated using a **leave-one-out** style setup, where the model predicts a held-out restaurant interaction from historical user behaviour.

### 6. Baseline Comparison

The mobility-aware approach is compared against baseline methods and model variants.
Relevant comparison outputs are stored in files such as:

* `report_model_comparison.csv`
* `artifacts/lightfm_outputs/`

---

## Main Notebooks

The most relevant notebooks are located under `notebooks/`.

Examples include work related to:

* Yelp dataset inspection
* sequence building
* DBSCAN hub detection
* mobility profiling
* recommendation generation
* model comparison
* evaluation

The repository currently separates notebook work into:

* `notebooks/initial_work/`
* `notebooks/dbscan_work/`

This reflects the development process, where earlier pipeline work and mobility-specific experiments were organized separately.

---

## Key Outputs

Important generated outputs include:

* **checkpoints** for intermediate experiment states
* **step outputs** for each major pipeline stage
* **LightFM outputs** for baseline comparison
* **UI export data** for visualization or dashboard integration
* **model comparison reports** for analysis

---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/bron322/YelpFYP.git
cd YelpFYP
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS / Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

Install the Python packages required by your notebooks and scripts:

```bash
pip install -r requirements.txt
```

If you do not yet have a `requirements.txt`, install the main libraries used in the project manually, such as:

```bash
pip install pandas numpy scikit-learn jupyter matplotlib seaborn
```

Add any other libraries depending on the notebooks you intend to run.

### 4. Launch Jupyter

```bash
jupyter notebook
```

Then open the relevant notebook under `notebooks/`.

---

## Suggested Notebook Execution Flow

A typical workflow for understanding or reproducing the project is:

1. explore the Yelp subset and understand available fields
2. build user visit sequences
3. generate geolocated visit records
4. run DBSCAN-based mobility profiling
5. build user activity centre profiles
6. run recommendation / retrieval notebooks
7. evaluate with leave-one-out testing
8. compare against baselines

---

## Reproducibility Notes

* Some large data files and generated outputs may be excluded from version control
* File paths inside notebooks may need to be adjusted depending on your local environment
* Some notebooks reflect iterative development and experimentation, so there may be overlapping functionality across files
* Generated outputs in `artifacts/` should be interpreted as stage-wise experiment products rather than final polished deliverables only

---

## Results

This project focuses on comparing mobility-aware recommendation with more standard recommendation setups.

Typical outputs include:

* number of evaluated users
* candidate retrieval statistics
* hit rate / recall style ranking metrics
* model comparison summaries
* baseline vs mobility-aware performance differences

You can update this section with your final reported metrics once your experiments are finalized.

Example:

* **Evaluated users:** *[fill in]*
* **Top-K:** *[fill in]*
* **Baseline score:** *[fill in]*
* **Mobility-aware score:** *[fill in]*

---

## Limitations

Some current limitations of the repository include:

* notebooks are still partially research-oriented and may contain development artifacts
* not all experiments are packaged into a single end-to-end script
* some file naming reflects iterative work done during the project
* results depend on the filtered Yelp subset and preprocessing choices

---

## Future Improvements

Possible future extensions include:

* converting notebook logic into reusable Python modules
* adding a full `requirements.txt`
* adding a single end-to-end experiment runner
* improving documentation for each notebook
* integrating the outputs into a dashboard or interactive system
* extending the comparison with more baseline recommenders

---

## Author

**Jing Jie Lim**
Final Year Project on mobility-aware restaurant recommendation using Yelp data.

---

## License

This project is licensed under the terms of the license provided in this repository.

```
