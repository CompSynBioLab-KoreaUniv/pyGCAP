# lacto-dcw

- [introduction](#introduction)
- [program-flow](#program-flow)
- [pre-requirement](#pre-requirement)
- [tutorial](#tutorial)
- [result description](#result-description)
- [example](#example)

---

### introduction

- Profiling _dcw_ genes from pan-genomes of Lactobacillales (LAB)

* this repository was built for the guiding 2023-2024 winter URAP student [@jrim42](https://github.com/jrim42)
* based on this paper - [Ancient origin and constrained evolution of the division and cell wall gene cluster in Bacteria](https://www.nature.com/articles/s41564-022-01257-y)
* Cell wall biosynthesis of LAB (eventually we can check and consider using related genes and proteins; for example, [Table 1](https://microbialcellfactories.biomedcentral.com/articles/10.1186/1475-2859-13-S1-S9/tables/1) in this [reveiw paper](https://microbialcellfactories.biomedcentral.com/articles/10.1186/1475-2859-13-S1-S9))
  <br>
  <img width=640 height = 480 src="https://media.springernature.com/lw685/springer-static/image/art%3A10.1186%2F1475-2859-13-S1-S9/MediaObjects/12934_2014_Article_1029_Fig2_HTML.jpg?as=webp">

---
### program-flow

<img width="801" alt="flowchart" src="https://github.com/logcossin/lacto-dcw/assets/90167645/db6e78d4-16b2-4a18-925d-c3dbb6fb3494">

---

### pre-requirement

- 필요한 프로그램

  1. `Python`
  2. `conda` environment
      - `blast`
      - `datasets` & `dataformat` from NCBI
      - `MMseqs2` ([MMseqs2 github](https://github.com/soedinglab/MMseqs2))

- input data
   1. working directory
   2. taxon (both name and taxid are available)
   3. path of `target.tsv`
       - target name (user defined)
       - protein name (user defined)
       - protein entry (UniProt) 
---

### tutorial

---

### result description

1. `output/tsv`
2. `output/img`
3. `output/genus`

---

### exmaple
