# Project Context: MicroEndo

## Purpose
The MicroEndo project focuses on integrating the endometrial microbiome and single-cell niche in Asherman's Syndrome. It leverages metagenomic data and scRNA-seq to explore dysbiosis, cellular dysregulation, and tissue repair following CD133+ BMDSC therapy.

## Architecture
- **Language Stack:** R for multi-omics integration (Seurat, MOFA+, mixOmics), Bash for data handling.
- **Directories:**
  - `data/`: All raw and processed datasets (ignored in Git to prevent bloating).
  - `docs/`: Technical specifications, designs, and backlog.
  - `src/`: Analytical R scripts.

## Setup & Conventions
- **Environment:** R scripts, which require significant resources, will be run on the **garnatxa** server. The main working directory on garnatxa is `/home/patienza/cocrea`.
- **Datasets:** Data is stored in `/storage/gge/cocrea_endometrio`. A symlink to this path must be created as the `data/` directory in the repository. The 1.88 GB `.rds` single-cell object and metagenomic tables reside here and are excluded from version control.
- **Credentials:** Any required active credentials (like AWS keys for S3) should be managed via environment variables (e.g. `.Renviron`) and never committed.
- **Workflow:** All actions must adhere to the PRAR (Perceive, Reason, Act, Refine) cycle. Always test changes locally and verify biological coordinate accuracy.
