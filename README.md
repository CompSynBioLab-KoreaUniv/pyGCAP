# pyGCAP: a python Gene Cluster Annotator & Profiler

A Python Package for Probe-based Gene Cluster Finding in Large Microbial Genome Database

- [introduction](#introduction)
- [pipeline-flow](#pipeline-flow)
- [pre-requirement](#pre-requirement)
- [usage](#usage)
- [example](#example)

---

### introduction

Bacterial gene clusters provide insights into metabolism and evolution, and facilitate biotechnological applications. We developed pyGCAP, a Python package for probe-based gene cluster discovery. This pipeline uses sequence search and analysis tools and public databases (e.g. BLAST, MMSeqs2, UniProt, and NCBI) to predict potential gene clusters by user-provided probe genes. We tested the pipeline with the division and cell wall (dcw) gene cluster, crucial for cell division and peptidoglycan biosynthesis.

To evaluate PGCfinder, we used 17 major dcw genes defined by Megrian et al. [1] as a probe set to search for gene clusters in 696 Lactobacillales genomes. The results were integrated to provide detailed information on gene content, gene order, and types of clusters. While PGCfinder examined the completeness of the gene clusters, it could also suggest novel taxa-specific accessory genes related to dcw clusters in Lactobacillales genomes. The package will be freely available on the Python Package Index, Bioconda, and GitHub.

[1] Megrian, D., et al. [Ancient origin and constrained evolution of the division and cell wall gene cluster in Bacteria](https://www.nature.com/articles/s41564-022-01257-y). Nat Microbiol 7, 2114–2127 (2022).

---

### pipeline-flow

<p align="center">
  <img width="801" alt="flowchart" src="https://github.com/jrim42/pyGCAP/assets/90167645/906905ac-5a58-418f-a3c9-3cc422276480">
</p>

---

### pre-requirement

1. `Python`
2. `conda` environment

   - `blast` ([bioconda blast package](https://anaconda.org/bioconda/blast))
     ```
     conda install bioconda::blast
     conda install bioconda/label/cf201901::blast
     ```
   - `datasets` & `dataformat` from NCBI ([conda-forge ncbi-datasets-cli package](https://anaconda.org/conda-forge/ncbi-datasets-cli))

     ```
     conda install conda-forge::ncbi-datasets-cli
     ```

   - `MMseqs2` ([MMseqs2 github](https://github.com/soedinglab/MMseqs2))
     ```
     conda install -c conda-forge -c bioconda mmseqs2
     ```

---

### usage
- pypi pygcap ([link](https://pypi.org/project/pygcap/))

  ```python
  pip install pygcap
  conda activate ncbi_datasets
  pygcap <working_dir> <TAXON> <probe_file_path>
  ```

- input argument description
  ```python
  ### usage example
  pygcap . Facklamia pygcap/data/probe_sample.tsv
  pygcap . 66831 pygcap/data/probe_sample.tsv
  ```
  1.  `working directory`
  2.  `taxon` (both name and taxid are available)
  3.  path of `probe.tsv` ([sample file](https://github.com/jrim42/pyGCAP/blob/main/pygcap/data/probe_sample.tsv))

      - `Probe Name` (user defined)
      - `Prediction` (user defined)
      - `Accession` (UniProt entry)

### options
### (작성중)
```
—-no
  vizualization
  mmseqs2

—-skip 
  datasets
  unzip
  dataformat
  mmseqs2
  uniprot
  parsing
```

---

### example
### (작성중)

- A directory with the following structure will be created in your `working directory` with the name of the `TAXON` provided as input.
  ```
  📦 [TAXON_NAME]
  ├─ data
  │  ├─ assembly_report.tsv
  │  ├─ metadata_target.tsv
  │  └─ ...
  ├─ input
  │  ├─ [GENUS_01]
  │  ├─ [GENUS_02]
  │  └─ ...
  ├─ output
  │  ├─ genus
  │  ├─ img
  │  └─ tsv
  └─ seqlib
     ├─ blast_output.tsv
     ├─ seqlib.tsv
     └─ ...
  ```

- Profiling _dcw_ genes from pan-genomes of Lactobacillales (LAB)

* Cell wall biosynthesis of LAB (eventually we can check and consider using related genes and proteins; for example, [Table 1](https://microbialcellfactories.biomedcentral.com/articles/10.1186/1475-2859-13-S1-S9/tables/1) in this [reveiw paper](https://microbialcellfactories.biomedcentral.com/articles/10.1186/1475-2859-13-S1-S9))
  <br>
  <img width=640 height = 480 src="https://media.springernature.com/lw685/springer-static/image/art%3A10.1186%2F1475-2859-13-S1-S9/MediaObjects/12934_2014_Article_1029_Fig2_HTML.jpg?as=webp">
