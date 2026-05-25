# Technical Design Document

## Implementation Plan

1. **Preprocessing (`src/preprocessing/`)**
   - Write an R script to selectively load `object@meta.data` and compute cell type proportions per sample.
   - Write an R script using `AggregateExpression()` to sum raw counts into pseudobulks.

2. **Integration Setup (`src/mofa/` and `src/mixomics/`)**
   - Prepare formatted matrices for View 1 (Host Proportions), View 2 (Host Genes), View 3 (Microbiome Taxa), and View 4 (Microbiome Pathways).
   - Implement `reticulate` / MOFA Python backend.
   - Configure `block.splsda` parameters for mixOmics.
