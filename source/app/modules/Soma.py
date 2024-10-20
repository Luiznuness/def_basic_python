class ExceptionSoma(Exception):
    ...


class Soma:
    def __init__(self, valor_entra_um: int, valor_entrada_dois:int) -> None:
        """__init__ Essa def é chamada de `Construtor` da classe, aqui recebemos as variaveis e chamamos execuções.

        Args:
            valor_entra_um (int): Inteiro a ser utilizado na soma
            valor_entrada_dois (int): Inteiro a ser utilizado na soma
        """
        self.valor_um =  valor_entra_um
        self.valor_dois = valor_entrada_dois
        self.mensagem_tipagem_forcada = None
        self.__forcar_tipagem()
    
    
    def __forcar_tipagem(self):
        """__forcar_tipagem Função que verifica o tipo do dado, caso não sejam corretos tenta forçar a tipagem

        Raises:
            ValueError: Caso a tipagem não ocorra corretamente retorna um  `ValueError("Verifique os tipo dos dados passados")`
            ExceptionSoma: Para contingencia, estoura uma exeção não mapeada
        """
        try:
            if isinstance(self.valor_um,int) and isinstance(self.valor_dois,int):
                self.mensagem_tipagem_forcada = "Não foi preciso forçar a tipagem."
                return

            self.valor_um = int(self.valor_um)
            self.valor_dois = int(self.valor_dois)
            self.mensagem_tipagem_forcada = "Forçado a tipagem."
            
        except ValueError as err:
            if "invalid literal for int() with base" in err.args[0]:
                raise ValueError("Verifique os tipo dos dados passados")
            
        except Exception as err:
            raise ExceptionSoma(f"Erro não validado: {err}")   
    
    
    def soma(self) -> int:
        return self.valor_um + self.valor_dois
