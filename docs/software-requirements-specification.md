# Software Requirements Specification (SRS)

## Objective
Capture the user's needs and goals for the MicroEndo data analysis project.

## Requirements
1. **Multi-Omics Integration**: The system must be capable of processing both host scRNA-seq objects (~123k cells) and microbial taxonomic/functional datasets.
2. **Memory Efficiency**: Given the 1.88 GB size of the input `.rds` file, the analytical workflow must use lightweight metadata extraction and pseudobulk aggregation.
3. **Biomarker Identification**: The system must extract actionable multi-omic panels predictive of AS severity and reproductive success.
