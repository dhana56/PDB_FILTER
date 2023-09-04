import requests

def pdb_file(pdb_id):
    """Function used for retreving the pdbfiles
        :pdb_id, PDB id of the protein
    """
    
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    with open (f"{pdb_id}.pdb", "w") as file:
        file.writelines(requests.get(url).text)
        file.close()  
        
#Function for creating the new file 
def file_creator(new_list, pdb_id):
    with open(f'{pdb_id}_c.pdb', 'w') as cleaned_file:
        cleaned_file.writelines(new_list)
        cleaned_file.close()

# bulding the filetering Function:
def pdb_filter(pdb_id, chain_id):
    """Function that filter the alternate residue & renumberring the residue number with chain_id
    :pdb_id, PDB code for Protein files.
    :chain_id, which chain_id to be filter_out
    """
    
    pdb_file(pdb_id) #Function Download the pdbfile
    value  = 0
    new_lines= []
    for i in open(f'{pdb_id}.pdb'):
        if i.startswith('ATOM') and i[21:22]==chain_id:
            if i[16:17] == 'A' or i[16:17] ==' ':
                if i[12:16].strip() =='N': #Finding the place where it atom_name =='N';nitrogen.
                    value+=1
                    y =i[:22]+f"{str(value): >4}"+i[26:]
                    new_lines.append(y)
                else:
                    y =i[:22]+f"{str(value): >4}"+i[26:]
                    new_lines.append(y)
    
    #Creating the new cleaned pdb file.
    file_creator(new_lines,pdb_id)


        
