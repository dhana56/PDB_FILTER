import requests
import re
import pandas as pd

class PDB_FILT:

    def __init__(self,pdb_id) -> None:
        self.pdb_id = pdb_id
        self.__pdb_file__()
        self.__chain_name__()

    def __pdb_file__(self):
        """Function used for retreving the pdbfiles.
        :pdb_id, PDB id of the protein
        """

        url = f"https://files.rcsb.org/download/{self.pdb_id}.pdb"
        with open (f"{self.pdb_id}.pdb", "w") as file:
            file.writelines(requests.get(url).text)
            file.close()  
            
    #Function for creating the new file 
    def __file_creator__(self,new_list,filter_chain):
        """Function that create the new pdb file.
        :newlist, list that caries changed lines from old pdbfile.
        :pdb_id, pdb_id of protein PDB file.
        """
        with open(f'{self.pdb_id}_{filter_chain}c.pdb', 'w') as cleaned_file:
            cleaned_file.writelines(new_list)
            cleaned_file.close()

    def __chain_name__(self):
        """Function that gives the molecule name and 
        chain values.
        :path, PDB file path
        """
        self.chain= {}
        for i,j in enumerate(open(f"{self.pdb_id}.pdb")):
            pattern=  re.compile("MOL_ID")
            if j.startswith("COMPND"):
                if re.search(pattern,j)  :
                    name = j.strip()[-3:-1]
                if j.startswith("CHAIN",11,17):
                    self.chain[name] =re.sub(r"[,;]",'', j[18:]).split()
        return self.chain
    
    def __miss_fun__(self,which):
        """function that gives inforamtion of residues and atoms
        :file_path, provide the pdb file path
        :which: residue or atoms to calculate in the missing positions in the 
        PDB file.
        """
        #assigning the variable names.
        if which =='residue':
            check ="M RES C SSSEQI"
            start, end = (13,27)
            pivot = "REMARK 465"
        elif which =='atom':
            check = "M RES CSSEQI"
            start, end =(13,25)
            pivot = "REMARK 470"
            
        missing_res = {}
        for i,j in enumerate(open(f"{self.pdb_id}.pdb")):
            need = 0
            if j.startswith(check,start,end):
                need = i
            if j.startswith(pivot) and len(j[11:16].strip())==1:
                atom_vale = j[15:].strip().split()
                sub_miss_res = {}
                sub_miss_res['res'] = atom_vale[0]
                if which =='atom':
                    sub_miss_res['atoms'] = atom_vale[3:]
                sub_miss_res["chain"] = atom_vale[1]

                #updating missing residue info.
                missing_res[atom_vale[2]] = sub_miss_res
            else: pass 
        return missing_res  
    
    # bulding the filetering Function:
    def pdb_filter(self):
        """Function that filter the alternate residue & renumberring the residue number with chain_id.
        :pdb_id, PDB code for Protein files.
        :chain_id, which chain_id to be filter_out
        """
        # self.__pdb_file__() #Function Download the pdbfile
        value  = 0
        new_lines= []
        print("PDB file have the following chains",self.chain)
        filter_chain = input("Please enter one chain name to be filter: ")
        for i in open(f'{self.pdb_id}.pdb'):
            if i.startswith('ATOM') and i[21:22]==filter_chain.upper():
                if i[16:17] == 'A' or i[16:17] ==' ':
                    if i[12:16].strip() =='N': #Finding the place where it atom_name =='N';nitrogen.
                        value+=1
                        y =i[:22]+f"{str(value): >4}"+i[26:]
                        new_lines.append(y)
                    else:
                        y =i[:22]+f"{str(value): >4}"+i[26:]
                        new_lines.append(y)
        
        #Creating the new cleaned pdb file.
        self.__file_creator__(new_lines,filter_chain.upper())
        print(f'{self.pdb_id}_{filter_chain.upper()}_c.pdb is created successfully')
    
    def chains(self):
        print(self.chain)

    def miss_res(self):
        mis_res_val = self.__miss_fun__('residue')
        if len(mis_res_val)!=0:
            print(mis_res_val)
        else:
            print('There is no missing residues')

    def miss_res_csv(self):
        val = self.__miss_fun__('residue')
        df = pd.DataFrame(val.values(), columns=['res','chain'], index= val.keys())
        df.to_csv(f"miss_res_{self.pdb_id}.csv")
    
    def miss_atom(self):
        mis_val_atom = self.__miss_fun__('atom')
        if len(mis_val_atom)!=0:
            print(mis_val_atom)
        else:
            print("There is no missing residue atoms")
