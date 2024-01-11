import pandas as pd

class controler():


    def __init__(self) -> None:
        self.df = None
        self.array_colum = ['Nome', 'idade', 'email', 'senha', 'codigo']

    def iniciar_CSV(self):
        try:
            self.df = pd.read_csv('usuarios.csv', index_col=None)
            print("Já existe")
        except:
            self.df = pd.DataFrame(columns=['Nome', 'idade', 'email', 'senha', 'codigo'])
            self.df.to_csv('usuarios.csv', sep = ',', index=False)
            self.df = pd.read_csv('usuarios.csv',index_col=None)
            print("Criado")
    

    #adicionar linha
    def dict_to_list(self, dic:dict):
        lis = []
        for i in self.array_colum:
            lis.append(dic[i])
        self.add(lis)

    def add(self, array:list):
        df = self.df
        df.loc[len(df.index)] = array
        self.df.to_csv('usuarios.csv', sep = ',', index=False)
        self.iniciar_CSV()

    #remover linha
    def remove(self, int):
        df = self.df
        self.df = df.loc[df["codigo"] != int] 
        self.df.to_csv('usuarios.csv', sep = ',', index=False)
        self.iniciar_CSV()

    
    #alterar linha
    def alterar(self,int ,dic:dict): 
        lis = []
        for i in self.array_colum:
            lis.append(dic[i])
        print(lis)
        self.alt(int, lis)

    def alt(self, int, array):
        print(array)
        df = self.df
        df[df["codigo"] == int] = array
        
        print(df.loc[df["codigo"] == int])
        df.to_csv('usuarios.csv', sep = ',', index=False)
        
        self.iniciar_CSV()
        pass

    #retornar dict de usuario
    def get_array(self, int):
        df = self.df
        array = list(df.loc[df["codigo"] == int].loc[1])
        return array

    def get_dict(self, int):
        array = self.get_array(int)
        dic = {
            'Nome':array[0],
            'idade':array[1],
            'email':array[2],
            'senha':array[3],
            'codigo':array[4]
        }
        return dic
    

    #retornar todos os usuarios
    def get_array_de(self, int):
        df = self.df
        array = list(df.loc[int])
        return array
    
    def get_listDict(self):
        df = self.df
        fi_array =[]
        for i in range(len(df.index)):
            array = self.get_array_de(i)
            dic = {
            'Nome':str(array[0]),
            'idade':str(array[1]),
            'email':str(array[2]),
            'senha':str(array[3]),
            'codigo':str(array[4])
            }
            fi_array.append(dic)
        return fi_array
    
