from app import adicao
def test_instanciar_adicao():
    valor_um = 1
    valor_dois = 2
    
    ad = adicao(valor_entra_um=valor_um, valor_entrada_dois=valor_dois)
    
    assert ad.mensagem_tipagem_forcada == "Não foi preciso forçar a tipagem."
    assert ad.valor_um == valor_um
    assert ad.valor_dois == valor_dois

def test_soma_ok():
    valor_um = 1
    valor_dois = 2
    
    ad = adicao(valor_entra_um=valor_um, valor_entrada_dois=valor_dois)
    
    assert ad.soma() == 3