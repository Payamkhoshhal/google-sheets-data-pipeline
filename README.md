# Google Sheets Data Pipeline

An end-to-end data engineering project that extracts data from Google Sheets using Python, loads it into PostgreSQL hosted on AWS RDS, and transforms and tests the data using dbt.

## 🛠️ Tech Stack

- **Python** — Data extraction and loading
- **Google Sheets API** — Source data
- **PostgreSQL** — Data warehouse
- **AWS RDS** — Cloud-hosted PostgreSQL database
- **dbt** — Data transformation and testing

## 🏗️ Architecture

The pipeline follows a simple ELT workflow:

```mermaid
flowchart LR
    A[Google Sheets] -->|Extract| B[Python]
    B -->|Load| C[(PostgreSQL<br/>AWS RDS)]
    C -->|Transform| D[dbt]
    D --> E[(Analytics Models)]
    D --> F[Data Tests]
```

### Data Flow

1. **Extract** — Python retrieves source data from Google Sheets.
2. **Load** — The raw data is loaded into PostgreSQL hosted on AWS RDS.
3. **Transform** — dbt transforms the raw data into structured analytical models.
4. **Test** — dbt tests are used to validate data quality.

## 📊 Dataset

The source data is stored in Google Sheets and contains three main fields:

| Column | Description |
| --- | --- |
| `Date` | Date associated with the recorded value |
| `Dimension` | Category or dimension used to group the data |
| `Value` | Numeric value associated with the dimension |

The pipeline extracts this data from Google Sheets and loads it into PostgreSQL, where dbt is used to transform it into analytical models.

## 📁 Project Structure

```text
google-sheets-data-pipeline/
├── python/          # Python scripts for extracting and loading data
├── models/          # dbt transformation models
├── tests/           # Custom dbt data tests
├── macros/          # Reusable dbt macros
├── seeds/           # Static data files used by dbt
├── snapshots/       # dbt snapshots
├── analyses/        # dbt analytical queries
└── dbt_project.yml  # Main dbt project configuration
```
## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Payamkhoshhal/google-sheets-data-pipeline.git
cd google-sheets-data-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database connection

Create a `.env` file based on `.env.example` and provide your PostgreSQL connection string:

```env
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
```

> Never commit your real `.env` file or database credentials.

### 5. Configure Google Sheets API credentials

Create a Google Cloud service account with access to the Google Sheets API, then download the service account key file.

Save the key file locally as:

```text
Keys.json
```

Make sure the Google Sheet you want to read is shared with the service account email address.

> `Keys.json` is ignored by Git and should never be committed to the repository.


## ⚙️ How It Works

### 1. Extract Data

Python connects to Google Sheets and retrieves the source data using the Google Sheets API.

### 2. Load Data

The extracted data is loaded into a PostgreSQL database hosted on AWS RDS.

### 3. Transform Data

dbt is used to transform the raw data into structured analytical models. The transformation logic is organized inside the `models/` directory.

### 4. Test Data

dbt tests validate the transformed data and help ensure data quality throughout the pipeline.
