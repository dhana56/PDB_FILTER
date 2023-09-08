import pdbfilter

if __name__ == '__main__':
    input_pdb = input("Please enter the pdb_id")
    pdb_gen = pdbfilter.PDB_FILT(input_pdb)
    pdb_gen.chains()
    pdb_gen.miss_atom()
    pdb_gen.pdb_filter()
    pdb_gen.miss_res_csv()




    