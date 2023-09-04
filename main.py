from fun import pdb_filter

if __name__ == '__main__':
    input_pdb = input("Please enter the pdb_id, chain by comma separted value")
    pdb_id,chain_id = input_pdb.split(",")
    pdb_filter(pdb_id,chain_id.upper())
