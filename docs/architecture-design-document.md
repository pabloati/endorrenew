# Architecture Design Document

## Overall System Design

The MicroEndo pipeline follows a sequential, modular architecture:

### 1. Data Ingestion & Transformation Layer
- Reads raw binary `.rds` (Seurat) and `.xlsx` files.
- Scripts in `src/preprocessing/` will collapse the sparse matrices into manageable sample-level data frames (pseudobulks).

### 2. Analytical Layer
- **Univariate**: Standard Spearman correlations (in R).
- **MOFA+ Integration**: Multi-view matrix factorization.
- **mixOmics (DiABLO)**: Partial Least Squares Discriminant Analysis (PLS-DA) across datasets.

### 3. Presentation Layer
- Output will be exported to `results/` in the form of high-resolution images (heatmaps, UMAP projections, circos plots).
