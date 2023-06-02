"""
Terceiro modelo lumped para discretização do satélite.

Será escrito as classes para cada componentes do satélite, ao todo serão 6:
    - Subtrato do painel;
    - Estrutura do painel;
    - Estrutura do cubesat;
    - PCD's;
    - Parafusos e pressão de conexão;
    - Baterias.

Discretizando os compoenetes será possível calcular a conexão entre eles em radiação e condução

Descrição do cubesat:
    - Tamanho 1U;
    - 4 paineis solares;
    - 4 bases de cobre
    - 4 baes do painel
    - 2 substratos por paienl;
    - 4 PCB's;
    - 5 packs de 4 parafusos;
    - 12 parafusos de 20 mm;
    - 8 parafusos de 14 mm;
    - duas tampas de alumínio no topo;
    - 4 Estruturas verticais;
    - 8 estruturas horizontais.
    - Total: 54 nós.

Dados dos materiais obtidos do livro Spacecraft Thermal Control Handkbook vol. 1
"""

import numpy as np
from fator_gebhart import fator_gebhart as fb
# Criar as classes de cada componente

class Substrato:

    def __init__(self, nome, area, e, a, rho, k, cp):
        self.nome = nome
        self.area = area
        self.e = e
        self.a = a
        self.rho = rho
        self.k = k
        self.cp = cp

class BasePainel:
    def __init__(self, nome, Lx, Ly, Lz, n, e, a, rho, k_in, k_tr,cp):
        self.nome = nome
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.n = n
        self.e = e
        self.a = a
        self.rho = rho
        self.k_in = k_in
        self.k_tr = k_tr
        self.cp = cp

class BaseCobre:
    def __init__(self, nome, Lx, Ly, Lz, n, e, a, rho, k, cp):
        self.nome = nome
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.n = n
        self.e = e
        self.a = a
        self.rho = rho
        self.k = k
        self.cp = cp

class Tampa:
    def __init__(self, nome, Lx, Ly, Lz, n, e, a, rho, k, cp):
        self.nome = nome
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.n = n
        self.e = e
        self.a = a
        self.rho = rho
        self.k = k
        self.cp = cp

class Estrutura:
    def __init__(self, nome, Lx, Ly, Lz, n, e, a, rho, k, cp):
        self.nome = nome
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.n = n
        self.e = e
        self.a = a
        self.rho = rho
        self.k = k
        self.cp = cp

class PCB:
    def __init__(self, nome, Lx, Ly, Lz, n, e, a, rho, k_in, k_tr, cp):
        self.nome = nome
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.n = n
        self.e = e
        self.a = a
        self.rho = rho
        self.k_in = k_in
        self.k_tr = k_tr
        self.cp = cp

class Bateria:
    pass

class Parafusos:
    def __init__(self, nome, Lx, Ly, Lz, rho, k, cp):
        self.nome = nome
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.rho = rho
        self.k = k
        self.cp = cp


# Criar os objetos e a lista de nós

# Paineis solares
"""
Material - Silicio
rho = 2330.0 kg/m^3
k = 148,9 W/m.K
cp = 712,8 J/kg.K
e = 0.899
a = 0.92
"""
substrato1 = Substrato('1', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato2 = Substrato('2', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato3 = Substrato('3', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato4 = Substrato('4', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato5 = Substrato('5', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato6 = Substrato('6', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato7 = Substrato('7', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)
substrato8 = Substrato('8', 0.002696, a = 0.92, e = 0.899, rho =  2330., k=148.9, cp=712.8)

# Base dos substratos
"""
Material - FR-4.0
rho = 1850 kg/m^3
k_in = 0.29 W/m.K
k_tr = 0.81 W/m.K
cp = 1100 J/kg.K

cobertura de Optical solar reflector, indium-tin-oxide (ITO) coated
a = 0.07
e = 0.76
"""
basepainel1 = BasePainel('9', Lx=0.002, Ly=0.084, Lz=0.1,  n='i', e=0.76, a=0.07, rho =1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)
basepainel2 = BasePainel('10', Lx=0.084, Ly=0.002, Lz=0.1,  n='j', e=0.76, a=0.07, rho =1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)
basepainel3 = BasePainel('11', Lx=0.002, Ly=0.084, Lz=0.1,  n='i', e=0.76, a=0.07, rho =1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)
basepainel4 = BasePainel('12', Lx=0.084, Ly=0.002, Lz=0.1,  n='j', e=0.76, a=0.07, rho =1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)

# Base painel de cobre
"""
Material - Cobre C38500
rho = 8580.0 kg/m^3
k = 122.9 W/m.K
cp =  378.0 J/kg.K

superficie - foil tape, plain
a = 0.32
e = 0.02
"""
basecobre1 = BaseCobre('13', Lx=0.001, Ly=0.084, Lz=0.1,  n='i', e=0.02, a=0.32, rho=8580.0, k=122.9, cp=378.0)
basecobre2 = BaseCobre('14', Lx=0.001, Ly=0.084, Lz=0.1,  n='j', e=0.02, a=0.32, rho=8580.0, k=122.9, cp=378.0)
basecobre3 = BaseCobre('15', Lx=0.001, Ly=0.084, Lz=0.1,  n='i', e=0.02, a=0.32, rho=8580.0, k=122.9, cp=378.0)
basecobre4 = BaseCobre('16', Lx=0.001, Ly=0.084, Lz=0.1,  n='j', e=0.02, a=0.32, rho=8580.0, k=122.9, cp=378.0)


# Tampa superior e inferior
"""
Material - Alumínio 7075
rho = 2770.0 kg/m^3
k = 121.2 W/m.K
cp = 961.2 J/kg.K
e = 0.3
a = 0.13
"""
tampa1 = Tampa('17', Lx=0.1, Ly=0.1, Lz=0.003, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
tampa2 = Tampa('18', Lx=0.1, Ly=0.1, Lz=0.003, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)

# PCB's
"""
Material FR-4.0
rho = 1850 kg/m^3
k_in = 0.29 W/m.K
k_tr = 0.81 W/m.K
cp = 1100 J/kg.K

cobertura de Optical solar reflector, indium-tin-oxide (ITO) coated
a = 0.07
e = 0.76
"""
pcb1 = PCB('19', Lx=0.08, Ly=0.08, Lz=0.003, n='k', e=0.76, a = 0.07, rho=1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)
pcb2 = PCB('20', Lx=0.08, Ly=0.08, Lz=0.003, n='k', e=0.76, a = 0.07, rho=1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)
pcb3 = PCB('21', Lx=0.08, Ly=0.08, Lz=0.003, n='k', e=0.76, a = 0.07, rho=1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)
pcb4 = PCB('22', Lx=0.08, Ly=0.08, Lz=0.003, n='k', e=0.76, a = 0.07, rho=1850.0, k_in=0.29, k_tr=0.81, cp=1100.0)

# Estruturas Verticais
"""
Material - Alumínio 7075
rho = 2770.0 kg/m^3
k = 121.2 W/m.K
cp = 961.2 J/kg.K
e = 0.3
a = 0.13
"""
estrutura_vertical1 = Estrutura('23', Lx=0.1, Ly=0.1, Lz=0.003, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical2 = Estrutura('24', Lx=0.1, Ly=0.1, Lz=0.003, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical3 = Estrutura('25', Lx=0.1, Ly=0.1, Lz=0.003, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical4 = Estrutura('26', Lx=0.1, Ly=0.1, Lz=0.003, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical5 = Estrutura('27', Lx=0.1, Ly=0.1, Lz=0.003, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical6 = Estrutura('28', Lx=0.1, Ly=0.1, Lz=0.003, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical7 = Estrutura('29', Lx=0.1, Ly=0.1, Lz=0.003, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_vertical8 = Estrutura('30', Lx=0.1, Ly=0.1, Lz=0.003, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)

# Estruturas Horizontais
"""
Material - Alumínio 7075
rho = 2770.0 kg/m^3
k = 121.2 W/m.K
cp = 961.2 J/kg.K
e = 0.3
a = 0.13
"""
estrutura_horizontal1 = Estrutura('31', Lx=0.002, Ly=0.008, Lz=0.1, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal2 = Estrutura('32', Lx=0.002, Ly=0.008, Lz=0.1, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal3 = Estrutura('33', Lx=0.002, Ly=0.008, Lz=0.1, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal4 = Estrutura('34', Lx=0.002, Ly=0.008, Lz=0.1, n='i', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal5 = Estrutura('35', Lx=0.002, Ly=0.008, Lz=0.1, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal6 = Estrutura('36', Lx=0.002, Ly=0.008, Lz=0.1, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal7 = Estrutura('37', Lx=0.002, Ly=0.008, Lz=0.1, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal8 = Estrutura('38', Lx=0.002, Ly=0.008, Lz=0.1, n='j', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)

estrutura_horizontal9 = Estrutura('39', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal10 = Estrutura('40', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal11 = Estrutura('41', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal12 = Estrutura('42', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal13 = Estrutura('43', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal14 = Estrutura('44', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal15 = Estrutura('45', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)
estrutura_horizontal16 = Estrutura('46', Lx=0.084, Ly=0.008, Lz=0.002, n='k', e=0.3, a = 0.13, rho=2770.0, k=121.2, cp=961.2)

# Parafusos
"""
Material - Alumínio 7075
rho = 2770.0 kg/m^3
k = 121.2 W/m.K
cp = 961.2 J/kg.K
e = 0.3
a = 0.13
"""
parafuso1 = Parafusos('47', Lx=0.005, Ly=0.005, Lz=0.014,  rho=2770.0, k=121.2, cp=961.2)
parafuso2 = Parafusos('48', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso3 = Parafusos('49', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso4 = Parafusos('50', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso5 = Parafusos('51', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso6 = Parafusos('52', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso7 = Parafusos('53', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso8 = Parafusos('54', Lx=0.005, Ly=0.005, Lz=0.014, rho=2770.0, k=121.2, cp=961.2)
parafuso9 = Parafusos('55', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso10 = Parafusos('56', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso11 = Parafusos('57', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso12 = Parafusos('58', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso13 = Parafusos('59', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso14 = Parafusos('60', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso15 = Parafusos('61', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso16 = Parafusos('62', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso17 = Parafusos('63', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso18 = Parafusos('64', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso19 = Parafusos('65', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)
parafuso20 = Parafusos('66', Lx=0.005, Ly=0.005, Lz=0.020, rho=2770.0, k=121.2, cp=961.2)

nos = [substrato1, substrato2, substrato3, substrato4, substrato5, substrato6, substrato7, substrato8,
       basepainel1, basepainel2, basepainel3, basepainel4, basecobre1, basecobre2, basecobre3, basecobre4,
       tampa1, tampa2,
       pcb1, pcb2, pcb3, pcb4,
       estrutura_vertical1,estrutura_vertical2,estrutura_vertical3,estrutura_vertical4,estrutura_vertical5,estrutura_vertical6,estrutura_vertical7,estrutura_vertical8,
       estrutura_horizontal1,estrutura_horizontal2,estrutura_horizontal3,estrutura_horizontal4,estrutura_horizontal5,estrutura_horizontal6,
       estrutura_horizontal7,estrutura_horizontal8,estrutura_horizontal9,estrutura_horizontal10,estrutura_horizontal11,estrutura_horizontal12,
       estrutura_horizontal13,estrutura_horizontal14,estrutura_horizontal15,estrutura_horizontal16,
       parafuso1, parafuso2, parafuso3, parafuso4, parafuso5, parafuso6, parafuso7, parafuso8, parafuso9, parafuso10,
       parafuso11, parafuso12, parafuso13, parafuso14, parafuso15, parafuso16, parafuso17, parafuso18, parafuso19, parafuso20]

# Conexões de condução entre os nós

conduc= {substrato1.nome: [basepainel1.nome],
         substrato2.nome: [basepainel1.nome],
         basepainel1.nome: [substrato1.nome, substrato2.nome, basecobre1.nome],
         basecobre1.nome: [basepainel1.nome, estrutura_horizontal1.nome, estrutura_horizontal2.nome],
         substrato3.nome: [basepainel2.nome],
         substrato4.nome: [basepainel2.nome],
         basepainel2.nome: [substrato3.nome, substrato4.nome, basecobre2.nome],
         basecobre2.nome: [basepainel2.nome, estrutura_horizontal3.nome, estrutura_horizontal4.nome],
         substrato5.nome: [basepainel3.nome],
         substrato6.nome: [basepainel3.nome],
         basepainel3.nome: [substrato5.nome, substrato6.nome, basecobre3.nome],
         basecobre3.nome: [basepainel3.nome, estrutura_horizontal5.nome, estrutura_horizontal6.nome],
         substrato7.nome: [basepainel4.nome],
         substrato8.nome: [basepainel4.nome],
         basepainel4.nome: [substrato7.nome, substrato8.nome, basecobre4.nome],
         basecobre4.nome: [basepainel4.nome, estrutura_horizontal7.nome, estrutura_horizontal8.nome],
         estrutura_horizontal1.nome: [basecobre1.nome, estrutura_horizontal9.nome, estrutura_vertical1.nome, estrutura_vertical2.nome],
         estrutura_horizontal2.nome: [basecobre1.nome, estrutura_horizontal10.nome, estrutura_vertical1.nome, estrutura_vertical2.nome],
         estrutura_horizontal3.nome: [basecobre2.nome, estrutura_horizontal11.nome, estrutura_vertical3.nome, estrutura_vertical4.nome],
         estrutura_horizontal4.nome: [basecobre2.nome, estrutura_horizontal12.nome, estrutura_vertical3.nome, estrutura_vertical4.nome],
         estrutura_horizontal5.nome: [basecobre3.nome, estrutura_horizontal13.nome, estrutura_vertical5.nome, estrutura_vertical6.nome],
         estrutura_horizontal6.nome: [basecobre3.nome, estrutura_horizontal14.nome, estrutura_vertical5.nome, estrutura_vertical6.nome],
         estrutura_horizontal7.nome: [basecobre4.nome, estrutura_horizontal15.nome, estrutura_vertical7.nome, estrutura_vertical8.nome],
         estrutura_horizontal8.nome: [basecobre4.nome, estrutura_horizontal16.nome, estrutura_vertical7.nome, estrutura_vertical8.nome ],
         tampa1.nome: [estrutura_horizontal1.nome, estrutura_horizontal3.nome, estrutura_horizontal5.nome, estrutura_horizontal7.nome, parafuso1.nome, parafuso2.nome, parafuso3.nome, parafuso4.nome],
         tampa2.nome: [estrutura_horizontal2.nome, estrutura_horizontal4.nome, estrutura_horizontal6.nome, estrutura_horizontal8.nome, parafuso5.nome, parafuso6.nome, parafuso7.nome, parafuso8.nome],
         parafuso1.nome: [tampa1.nome, pcb1.nome],
         parafuso2.nome: [tampa1.nome, pcb1.nome],
         parafuso3.nome: [tampa1.nome, pcb1.nome],
         parafuso4.nome: [tampa1.nome, pcb1.nome],
         parafuso5.nome: [tampa2.nome, pcb4.nome],
         parafuso6.nome: [tampa2.nome, pcb4.nome],
         parafuso7.nome: [tampa2.nome, pcb4.nome],
         parafuso8.nome: [tampa2.nome, pcb4.nome],
         parafuso9.nome: [pcb1.nome, pcb2.nome],
         parafuso10.nome: [pcb1.nome, pcb2.nome],
         parafuso11.nome: [pcb1.nome, pcb2.nome],
         parafuso12.nome: [pcb1.nome, pcb2.nome],
         parafuso13.nome: [pcb2.nome, pcb3.nome],
         parafuso14.nome: [pcb2.nome, pcb3.nome],
         parafuso15.nome: [pcb2.nome, pcb3.nome],
         parafuso16.nome: [pcb2.nome, pcb3.nome],
         parafuso17.nome: [pcb3.nome, pcb4.nome],
         parafuso18.nome: [pcb3.nome, pcb4.nome],
         parafuso19.nome: [pcb3.nome, pcb4.nome],
         parafuso20.nome: [pcb3.nome, pcb4.nome],
         pcb1.nome: [parafuso1.nome, parafuso2.nome, parafuso3.nome, parafuso4.nome, parafuso9.nome, parafuso10.nome, parafuso11.nome, parafuso12.nome],
         pcb2.nome: [parafuso9.nome, parafuso10.nome, parafuso11.nome, parafuso12.nome, parafuso13.nome, parafuso14.nome, parafuso15.nome, parafuso16.nome],
         pcb3.nome: [parafuso13.nome, parafuso14.nome, parafuso15.nome, parafuso16.nome, parafuso17.nome, parafuso18.nome, parafuso19.nome, parafuso20.nome],
         pcb4.nome: [parafuso17.nome, parafuso18.nome, parafuso19.nome, parafuso20.nome, parafuso5.nome, parafuso6.nome, parafuso7.nome, parafuso8.nome],
         estrutura_vertical1.nome: [estrutura_horizontal1.nome, estrutura_horizontal2.nome, estrutura_vertical2.nome],
         estrutura_vertical2.nome: [estrutura_horizontal3.nome, estrutura_horizontal4.nome, estrutura_vertical1.nome],
         estrutura_vertical3.nome: [estrutura_horizontal3.nome, estrutura_horizontal4.nome, estrutura_vertical4.nome],
         estrutura_vertical4.nome: [estrutura_horizontal5.nome, estrutura_horizontal6.nome, estrutura_vertical3.nome],
         estrutura_vertical5.nome: [estrutura_horizontal5.nome, estrutura_horizontal6.nome, estrutura_vertical6.nome],
         estrutura_vertical6.nome: [estrutura_horizontal7.nome, estrutura_horizontal8.nome, estrutura_vertical5.nome],
         estrutura_vertical7.nome: [estrutura_horizontal7.nome, estrutura_horizontal8.nome, estrutura_vertical8.nome],
         estrutura_vertical8.nome: [estrutura_horizontal1.nome, estrutura_horizontal2.nome, estrutura_vertical7.nome],
         estrutura_horizontal9.nome: [tampa1.nome, estrutura_vertical1.nome, estrutura_vertical8.nome, estrutura_horizontal1.nome],
         estrutura_horizontal10.nome: [tampa1.nome, estrutura_vertical2.nome, estrutura_vertical3.nome, estrutura_horizontal3.nome],
         estrutura_horizontal11.nome: [tampa1.nome, estrutura_vertical4.nome, estrutura_vertical5.nome, estrutura_horizontal5.nome],
         estrutura_horizontal12.nome: [tampa1.nome, estrutura_vertical6.nome, estrutura_vertical7.nome, estrutura_horizontal7.nome],
         estrutura_horizontal13.nome: [tampa2.nome, estrutura_vertical1.nome, estrutura_vertical8.nome, estrutura_horizontal2.nome],
         estrutura_horizontal14.nome: [tampa2.nome, estrutura_vertical2.nome, estrutura_vertical3.nome, estrutura_horizontal4.nome],
         estrutura_horizontal15.nome: [tampa2.nome, estrutura_vertical4.nome, estrutura_vertical5.nome, estrutura_horizontal6.nome],
         estrutura_horizontal16.nome: [tampa2.nome, estrutura_vertical6.nome, estrutura_vertical7.nome, estrutura_horizontal6.nome]
}
def ordena_nome(lista):
    a = list(lista.keys())
    b = []
    for valor in a:
        b.append(int(valor))
    b.sort()
    lista_nomes = []
    for valor in b:
        lista_nomes.append(str(valor))
    return lista_nomes

lista_nomes = ordena_nome(conduc)

# Define a matriz inicial preenchida por zeros

K_m = np.zeros((len(conduc), len(conduc)))

# Lógica para preencher a matriz com 1 onde existe condução entre nós

for chave in conduc.keys():
    A = (conduc[chave])
    for valor in A:
        K_m[int(chave)-1, int(valor)-1] = 1

# Disntância entre nós

nomes = list(conduc.keys())
valores = list(conduc.values())
L = {}
j = 0
for valor in valores:
    for i in range(len(valor)):
        L[" ".join([nomes[j], valor[i]])] = input(f'Comprimento de {nomes[j]} a {valor[i]}: ')
    j += 1
