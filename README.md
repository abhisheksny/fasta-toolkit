# FASTA Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/version-v1.2-green)
![Bioinformatics](https://img.shields.io/badge/domain-bioinformatics-orange)

Python CLI toolkit for FASTA statistics, ORF discovery, Protein translation and CSV reporting.

## Features
- GC/AT composition
- ORF discovery
- Protein translation preview
- Multi-FASTA support
- CSV export for sequence statistics
- Longest ORF reporting (bp)
- Protein length reporting (aa)


## Installation
```bash
git clone https://github.com/abhisheksny/bio_project.git
cd bio_project
pip install -r requirements.txt
```

## Dependencies
- Biopython

## Usage
```bash
python3 fasta_stats.py
```

Place FASTA files inside:

```bash
data/
```

## Example Test Data
- ACTB
- BRCA1
- TP53

## Example Output
- Sequence length
- GC%
- Top ORFs
- Protein preview
- CSV report export
- Protein length reporting (aa)

## Project Structure
```bash
bio_project/
├── data/
├── fasta_stats.py
├── requirements.txt
└── README.md
```

## Release
Current stable release: **v1.2**

## Author
Developed by **Abhishek K.**

## Contact
Use GitHub Issues for suggestions or bugs.
