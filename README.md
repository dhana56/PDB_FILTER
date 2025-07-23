# PDB File Filter

#### For more details and tutorials about PDB files, visit the website: [PDB101.org](https://pdb101.rcsb.org/)

## Overview

This Python program analyzes and filters Protein Data Bank (PDB) files, providing comprehensive tools for structural bioinformatics analysis.

## Features

The program checks for and handles:

1. **Alternate locations** for amino acid residues
2. **Residue numbering** - ensures proper sequential numbering starting from 1
3. **Missing residues** in the PDB files
4. **Insertion residues** present in protein chains
5. **Available chains** in the PDB files
6. **Missing atoms** in the side chains of amino acid residues
7. **Coordinate extraction** for specific atoms
8. **Amino acid sequence** retrieval and analysis

## Installation

1. **Install dependencies** using the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

2. **Navigate to the project directory:**
   ```bash
   cd path/to/pdb_filter
   ```

## Usage

1. **Run the main program:**
   ```bash
   python main.py
   ```

2. **Enter a PDB ID when prompted:**
   ```
   Example: 1mky
   ```

## Available Methods

Once you create a `PDB_FILT` object, you can use these methods:

- `chains()` - Display available chains
- `pdb_filter()` - Filter and clean PDB file for a specific chain
- `miss_res()` - Show missing residues
- `miss_atom()` - Show missing atoms
- `miss_res_csv()` - Export missing residues to CSV
- `amino_seq()` - Display amino acid sequence
- `seq_len()` - Show sequence length
- `cordinate()` - Extract atom coordinates

## Example Usage

```python
from pdbfilter import PDB_FILT

# Initialize with PDB ID
protein = PDB_FILT("1mky")

# View available chains
protein.chains()

# Filter a specific chain
protein.pdb_filter()

# Check for missing residues
protein.miss_res()
```

## Output Files

The program generates:
- Filtered PDB files: `{pdb_id}_{chain}_c.pdb`
- Missing residues CSV: `miss_res_{pdb_id}.csv`

## Requirements

- Python 3.6+
- requests
- pandas
- re (built-in)
- collections (built-in)

## Note

The program automatically downloads PDB files from the RCSB Protein Data Bank database using the provided PDB ID.
