import pdbfilter

if __name__ == '__main__':
    input_pdb = input("Please enter the pdb_id")
    pdb_gen = pdbfilter.PDB_FILT(input_pdb)
    pdb_gen.chains()#Gives all the chains information in the PDB files.
    pdb_gen.miss_atom() #Missing atoms in the file
    pdb_gen.pdb_filter() #Flterred chain information
    pdb_gen.miss_res_csv() #Store Missing atoms in csv file
    pdb_gen.amino_seq()# Gives seq of PDB chain.
    pdb_gen.seq_len()# Gives length of the chain
    
    





    