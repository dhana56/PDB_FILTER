#  PDB files Formater
#### For more detials and tutorials about PDB files, visit the website : [PDB101.org](https://pdb101.rcsb.org/)
<br>

> It Programing file takes the PDB files, and checks for:
>    1. Alternate locations for amino acid residues.
>    2. If the residue number is start with 1 or not.
>    3. Checks for the missing residue in the PDB files.
>    4. Check for the insertion residues present in the protein chains.
> <br>
>
<p> By defult it do the work for all the chains in the protein. For the coustomized chain, you have to give the chain id to the funstion it will generate processed file for only the particular chain.<p>

<p>For customized chain, you have to provide the the chain id. Otherwise it will run for the all the chains and produce the new cleaned PDB file contains the data of the all the chains informations.