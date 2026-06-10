# AI-Powered Legal Document Analysis System (CUAD)

## BRAC University – CSE Project

An AI-powered legal contract analysis system built using the **Contract Understanding Atticus Dataset (CUAD)**. The project combines legal document analysis and Natural Language Processing (NLP) to identify important contractual clauses, assess risk, generate plain-language explanations, and detect potentially conflicting provisions.

---

## Team Members

| Serial | Name | Student ID |
|----------|----------|----------|
| 1 | Shoyeb Hasan Sayem | 22101386 |
| 2 | Afnan Mazumdar | 24141229 |
| 3 | Jerin Aktar | 22101279 |

### Supervisor
**Utsho Kumar Roy**

### Co-Supervisor
**Sifat Tanvir**

Department of Computer Science and Engineering  
BRAC University

---

## Project Overview

Legal contracts often contain complex language that can be difficult for non-lawyers to understand. This project aims to build an intelligent legal document analysis system capable of:

- Extracting important legal clauses from contracts
- Categorizing clauses into predefined legal categories
- Assessing contractual risk levels
- Generating plain-English summaries
- Detecting conflicting contractual provisions
- Supporting future AI-assisted legal review

The project is based on the **CUAD dataset**, which contains expert-annotated commercial contracts.

---

## Dataset Information

### CUAD (Contract Understanding Atticus Dataset)

CUAD is an expert-annotated legal NLP dataset released by **The Atticus Project**.

### Dataset Statistics

| Metric | Value |
|----------|----------|
| Contracts | 510 |
| Clause Categories | 41 |
| Questions | 20,910 |
| Annotation Spans | 13,823 |

License: **Apache-2.0**

---

## System Workflow

```text
CUAD Dataset
      │
      ▼
Data Processing
      │
      ▼
Clause Extraction
      │
      ▼
Risk Classification
      │
      ▼
Plain-Language Summarization
      │
      ▼
Conflict Detection
      │
      ▼
Final Contract Analysis Report
```

---

## Repository Structure

```text
Cuad-Legal-Analysis/
├── Data/
├── Documents/
├── Notebooks/
├── Spreadsheets/
├── Src/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Git & GitHub
- Natural Language Processing (NLP)
- CUAD Dataset

---

## P2 Deliverables

- GitHub Repository
- Dataset Exploration Notebook
- Dataset Statistics Documentation
- Risk Taxonomy Design
- Risk Classification Spreadsheet
- Sample Contract Collection
- Plain-Language Summarization Design
- Conflict Detection Rules
- System Design Documentation

---

## Future Work

- Fine-tune T5 / FLAN-T5 models for legal summarization
- Automate clause extraction using transformer-based models
- Develop a web-based contract review dashboard
- Integrate real-time risk scoring
- Expand conflict detection using semantic analysis

---

## License

CUAD is released under the Apache-2.0 License by The Atticus Project.

This repository was developed as part of academic coursework for the Department of Computer Science and Engineering, BRAC University.
