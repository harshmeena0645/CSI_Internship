# Week 6

# Azure Data Factory Local Simulation
This project simulates ADF pipelines locally using JSON templates.

## Components

- 📂 `linked_services/`: Simulated connections to local SQL and FTP
- 📂 `pipelines/`: Copy pipelines (SHIR to SQL, FTP to SQL, Incremental)
- 📂 `triggers/`: Custom monthly trigger
- 📂 `sample_files/`: FTP input files (like `sales.txt`)
- 📂 `screenshots/`: All required UI captures
- 📂 `README.md`: Project explanation

## Notes
- SHIR is not registered — pipelines are built in JSON for simulation
- FTP and SQL connections are dummy/local
- Pipelines follow ADF structure
