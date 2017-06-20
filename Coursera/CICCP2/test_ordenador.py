class Ordenador:
    
    def selecao_direta(self, lista):
        
        fim = len(lista)
        
        for i in range(fim - 1):
            posicao_do_minimo = i
            
            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]: 
                    posicao_do_minimo = j            
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            
    def bolha(self, lista):
        
        fim = len(lista)
        
        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] 
    
    def bolha_curta(self, lista):
        
        fim = len(lista)
        
        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] 
                    trocou = True
            if not trocou:
                return 

import random
import time

class ContaTempos:
    
    def lista_aleatoria(self, n): 
        from random import randrange
        lista = [random.randrange(1000) for x in range(n)] 
        return lista
    
    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)] 
        lista[n//10] = -500 
        return lista        
    
import pytest

class TestaOrdenador:
    
    @pytest.fixture
    def o(self):
        return Ordenador()
    
    @pytest.fixture
    def l_quase(self):
        c = ContaTempos()
        return c.lista_quase_ordenada(100)
    
    @pytest.fixture
    def l_aleatoria(self):
        c = ContaTempos()
        return c.lista_aleatoria(100)
    
    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                return False
        return True                
            
    def test_bolha_curta_aleatoria(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta_aleatoria(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)   
    
    def test_bolha_curta_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selecao_direta_quase(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase) 
