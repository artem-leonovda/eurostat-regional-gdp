# Regional Economic Analysis (Eurostat GDP)

End-to-end data analytics project analyzing regional GDP dynamics across European regions using Eurostat data.

## Project Overview

This project builds a reproducible analytics pipeline that:

- Extracts regional GDP data from the Eurostat API
- Stores structured data in PostgreSQL
- Performs analytical computations using Python and Pandas
- Generates an automated analytical report with interactive visualizations

The goal is to evaluate economic performance of European regions by identifying:

- Which regions grow fastest 
- Which regions grow most consistently
- Which regions combine growth and stability

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- Plotly (interactive visualization)
- Jupyter Notebook
- Eurostat API

## Data Source

Eurostat dataset: nama_10r_2gdp — Regional GDP by NUTS regions

[Eurostat API link](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10r_2gdp)

## Project Structure

```
ingestion/        # ETL pipeline scripts
sql/              # schema and analytical SQL
notebooks/        # analysis notebook
reports/          # generated HTML reports
.env.example      # example environment variables
requirements.txt  # project dependencies
run_analysis.sh   # script to execute notebook and generate report
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/artem-leonovda/eurostat-regional-gdp.git
cd eurostat-regional-gdp
```

### 2. Create environment file

```bash
cp .env.example .env
```

Fill in your database credentials.

### 3. Start services

```bash
docker-compose up -d
```

### 4. Run analytics report

```bash
./run_analysis.sh
```

Resulting report:

```
reports/analysis.html
```

## Analysis Performed

- GDP time-series analysis per region
- Year-over-Year growth calculation
- CAGR (Compound Annual Growth Rate)
- Economic volatility (stability) analysis
- Composite economic scoring combining growth, volatility, and average GDP
- Sensitivity analysis to test robustness of ranking against weight changes

## Key Insights

**Which regions grow fastest?**
Regions such as **FIZ, RO11, AT0, RO3, ITT0, CZ02, and PL91** demonstrate the highest CAGR values, indicating rapid economic expansion over the observed period.

**Which regions grow most consistently?**
Regions including **AL01, AT11, and AT22** show smooth and stable GDP trajectories with minimal volatility, suggesting steady and predictable growth.

**Which regions combine growth and stability?**
Regions like **AT0, CZ02, and PL91** achieve a strong balance between above-average growth and relatively stable development patterns.

## Recommendations

- **High growth but risky:** *FIZ, RO11* — strong expansion but likely higher volatility and sensitivity to economic shocks.
- **Stable investment candidate:** *AT11, AT22* — moderate but consistent growth, suitable for long-term stability-focused strategies.
- **Sensitivity analysis** shows that regions remain stable in their positions under various weighting schemes, indicating stable economic indicators that do not depend on model assumptions.

## Author

Artem Leonov
