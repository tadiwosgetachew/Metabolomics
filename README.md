# Colorectal Cancer Biomarker Discovery Using LC-MS Metabolomics and Machine Learning

This project presents a complete pipeline for **biomarker discovery and validation** in colorectal cancer (CRC) using **targeted LC-MS metabolomics**. By integrating **statistical filtering**, **pathway enrichment**, and **machine learning**, we identify metabolite signatures that differentiate CRC from **polyps** and **healthy** individuals.

---

## Objectives

- Identify metabolic signatures that distinguish CRC from polyp and healthy groups.
- Validate biologically relevant biomarkers using pathway enrichment analysis using Metaboanalst 6.
- Build machine learning models to evaluate the predictive value of the discovered metabolites.

---

## Dataset

- **Source**: [Metabolomics Workbench - Study ST000284](https://www.metabolomicsworkbench.org)
- **Samples**:
  - CRC patients
  - Polyp patients
  - Healthy controls
- **Type**: Targeted metabolomics (LC-MS)

---

## Workflow Overview

```mermaid
graph TD
  A[Data Import & Preprocessing] --> B[PCA & PLS-DA]
  B --> C[Statistical Analysis (VIP, t-test)]
  C --> D[Metabolite Selection (VIP > 1, FDR < 0.05)]
  D --> E[Visualization (Volcano, Heatmap)]
  D --> F[Pathway Enrichment (KEGG & Disease Signatures)]
  D --> G[Network Analysis]
  D --> H[Machine Learning Models]
  ```

## Environment Setup

To replicate the environment, run:

```bash
pip install -r requirements.txt
```


## Key Findings

### Exploratory Data Analysis
- **PCA** showed minimal separation between CRC, polyp, and healthy samples.
- **PLS-DA** revealed clearer group separation, especially between CRC and other groups.
- **CRC vs Polyp** had the best discrimination:
  - CRC vs Polyp: **AUC = 0.855**
  - CRC vs Healthy: **AUC = 0.844**
  - Healthy vs Polyp: **AUC = 0.523**
  - Multiclass (CRC, Polyp, Healthy): **AUC ≈ 0.713**
- **Permutation testing (n = 1000)** validated the statistical significance of all models (p < 0.001).

### Statistically Significant Metabolites
- **Combined VIP > 1 and FDR-adjusted p < 0.05** used to select key metabolites.
- **CRC vs Healthy**: 15 significant metabolites
- **CRC vs Polyp**: 22 significant metabolites
- Several metabolites were **shared** across both comparisons:
  - Methionine, L-Aspartic acid, Lysine, Glutamine, Histidine, Hippuric Acid

### Biological Enrichment (MetaboAnalyst)
- CRC signature was **ranked #1** in both disease signature comparisons:
  - 7 of 54 known CRC metabolites detected in CRC vs Healthy
  - 10 of 54 detected in CRC vs Polyp
- Suggests robust biological relevance and confirms CRC-specific metabolic reprogramming.

### Pathway Enrichment (KEGG)
- **Top enriched pathways (CRC vs Polyp):**
  - **Alanine, Aspartate & Glutamate Metabolism (hsa00250)**
  - **Arginine Biosynthesis (hsa00220)**
- Other enriched pathways:
  - Histidine metabolism
  - Butanoate metabolism
  - Nitrogen metabolism
- Highlights changes in **amino acid turnover**, **TCA cycle intermediates**, **urea cycle**, and **immune signaling**.

### Functional Network Insights
- Key interconnected metabolic modules:
  - Glutamine–Glutamate axis
  - Nitrogen cycling (urea, arginine)
  - Microbiota-derived metabolites (e.g., butanoate)

### Machine Learning Results
- **CRC vs Polyp**:
  - Top 10 features selected via RFE
  - **Test Accuracy**: 83%
  - **AUC**: 0.865
  - **5-Fold CV Accuracy**: 77.5% ± 4.8%
- **CRC vs Healthy**:
  - Top 20 features selected
  - **Test Accuracy**: 88%
  - **AUC**: 0.923
  - **5-Fold CV Accuracy**: 77.8%
- Trade-off observed:
  - Full feature set = higher biological interpretability
  - Reduced feature set = higher ML precision (but fewer known CRC markers)

### Summary
- Distinct CRC-specific metabolic signature identified.
- Evidence of progressive metabolic shift from healthy → polyp → cancer.
- Integrated pipeline supports **non-invasive biomarker discovery** using blood-based targeted metabolomics.

## Conclusion

This project showcases a robust **biomarker discovery pipeline** that integrates **statistical analysis**, **biological pathway enrichment**, and **machine learning**. Through targeted LC-MS metabolomics, we identified metabolite signatures capable of distinguishing colorectal cancer (CRC) from both polyp and healthy groups. 

The findings highlight strong potential for **non-invasive metabolomic biomarkers** in the **early detection**, **risk stratification**, and **monitoring of CRC progression**.

## Future Work

- **Validate on independent, larger datasets**  
  To ensure generalizability and clinical relevance, the metabolite-based models should be tested on external cohorts.

- **Explore multi-omics integration**  
  Combine metabolomics with other omics layers (e.g., transcriptomics, microbiome) to build more comprehensive and mechanistically informative models of CRC.

- **Incorporate clinical and lifestyle metadata**  
  Enhance predictive modeling by integrating key variables such as:  
  `['Age at Consent', 'Gender', 'Height [cm]', 'Weight [kg]', 'BMI [kg/m²]', 'Smoking Status', 'Alcohol Consumption']`  
  These features may improve classification performance and enable personalized risk prediction.  
  - **BMI** is a modifiable CRC risk factor related to systemic metabolism.  
  - **Smoking** and **alcohol consumption** are established lifestyle-related CRC risk factors.  
  - **Gender differences** affect CRC risk, metabolism, and treatment response.  
  Including these covariates can improve both **predictive power** and **biological interpretability**.

- **Apply model interpretability techniques**  
  Use tools such as **SHAP (SHapley Additive exPlanations)** to understand how each metabolite and clinical feature contributes to individual predictions.

- **Benchmark multiple machine learning algorithms**  
  Compare performance of Random Forest with other classifiers such as:
  - XGBoost
  - Support Vector Machines (SVM)
  - Logistic regression with L1/L2 regularization  
  This helps ensure that model performance is not algorithm-dependent.

## References

- **Metabolomics Workbench – ST000284**  
  Public dataset used as the foundation for this study.  
  [https://www.metabolomicsworkbench.org/data/DRCCMetadata.php?Mode=Study&StudyID=ST000284](https://www.metabolomicsworkbench.org/data/DRCCMetadata.php?Mode=Study&StudyID=ST000284)

- **MetaboAnalyst 6.0**  
  Used for pathway enrichment, disease signature analysis, and network interpretation.  
  [https://www.metaboanalyst.ca/](https://www.metaboanalyst.ca/)

- **KEGG Pathway Database**  
  Referenced for functional pathway enrichment and interpretation of metabolic reprogramming.  
  [https://www.genome.jp/kegg/pathway.html](https://www.genome.jp/kegg/pathway.html)



