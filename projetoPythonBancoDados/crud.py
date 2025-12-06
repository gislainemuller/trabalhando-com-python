import sqlite3

def readTable(conexao, cursor):
    conexao = sqlite3.connect("python.sqlite")
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
    """)
    tabelas = cursor.fetchall()

    if tabelas:
        for tabela in tabelas:
            print("Tabela:", tabela[0])
    else:
        print("Não há tabelas cadastradas neste banco de dados")


def createTable(cursor, conexao):
    print("Tabela sendo criada...")
    conexao = sqlite3.connect("python.sqlite")

    cursor.execute("DROP TABLE IF EXISTS estoque")
    cursor.execute("DROP TABLE IF EXISTS categorias")
    cursor.execute("DROP TABLE IF EXISTS marcas")
    cursor.execute("DROP TABLE IF EXISTS modelos")
    cursor.execute("DROP TABLE IF EXISTS vendidos")

    cursor.execute("""
    CREATE TABLE estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_item TEXT NOT NULL,
        quantidade INTEGER,
        tamanho TEXT
    );
""")

    cursor.execute("""
    CREATE TABLE categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        setor TEXT
    );
""")

    cursor.execute("""
    CREATE TABLE marcas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        pais TEXT,
        ano_fundacao INTEGER
    );
""")

    cursor.execute("""
    CREATE TABLE modelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL,
        tecido TEXT,
        genero TEXT
    );
""")

    cursor.execute("""
    CREATE TABLE vendidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        quantidade INTEGER,
        data_venda TEXT
    );
""")

    conexao.commit()
    print("Tabelas criadas com sucesso!\n")


def InsertSql(conexao, cursor):
    conexao = sqlite3.connect("python.sqlite")

    print("Inserindo dados...")

    cursor.execute("""
    INSERT INTO estoque_roupas (nome_item, quantidade, tamanho) VALUES
    ('Camiseta Básica', 120, 'M'),
    ('Calça Jeans Skinny', 80, '40'),
    ('Jaqueta de Couro', 25, 'G'),
    ('Saia Midi', 60, 'M'),
    ('Vestido Longo', 40, 'G'),
    ('Camisa Social', 90, 'M'),
    ('Moletom Liso', 110, 'GG'),
    ('Shorts Jeans', 70, '38'),
    ('Blusa de Frio', 50, 'P'),
    ('Regata Algodão', 130, 'M'),
    ('Calça Jogger', 75, 'GG'),
    ('Blazer Feminino', 30, 'M'),
    ('Bermuda Sarja', 95, '42'),
    ('Camiseta Estampada', 150, 'P'),
    ('Top Fitness', 85, 'M'),
    ('Calça Legging', 100, 'G'),
    ('Pijama Algodão', 65, 'M'),
    ('Cardigan Tricot', 55, 'G'),
    ('Macacão Jeans', 45, 'M'),
    ('Cropped Liso', 125, 'P');
""")

    cursor.execute("""
    INSERT INTO categorias_roupas (categoria, descricao, setor) VALUES
    ('Camisetas', 'Roupas para o dia a dia', 'Adulto'),
    ('Calças', 'Vestuário inferior', 'Adulto'),
    ('Vestidos', 'Moda feminina', 'Feminino'),
    ('Jaquetas', 'Peças de frio', 'Adulto'),
    ('Saias', 'Moda feminina', 'Feminino'),
    ('Moda Fitness', 'Roupas para treino', 'Adulto'),
    ('Moda Praia', 'Roupas de banho', 'Adulto'),
    ('Moda Infantil', 'Roupas para crianças', 'Infantil'),
    ('Roupas Sociais', 'Vestuário formal', 'Adulto'),
    ('Acessórios', 'Complemento de look', 'Unissex'),
    ('Pijamas', 'Roupas de dormir', 'Adulto'),
    ('Roupas de Inverno', 'Peças quentes', 'Adulto'),
    ('Roupas de Verão', 'Peças leves', 'Adulto'),
    ('Roupas Jeans', 'Peças em jeans', 'Unissex'),
    ('Moda Streetwear', 'Estilo urbano', 'Adulto'),
    ('Roupas Sustentáveis', 'Eco friendly', 'Adulto'),
    ('Roupas de Festa', 'Para eventos', 'Adulto'),
    ('Tênis e Calçados', 'Calçados em geral', 'Unissex'),
    ('Camisas', 'Moda clássica', 'Adulto'),
    ('Casacos', 'Peças de frio pesadas', 'Adulto');
""")

    
    cursor.execute("""
    INSERT INTO marcas_roupas (marca, pais, ano_fundacao) VALUES
    ('UrbanWear', 'Brasil', 2015),
    ('BlueDenim', 'EUA', 1998),
    ('StyleFit', 'Brasil', 2012),
    ('EleganceFashion', 'França', 1985),
    ('WinterCoats', 'Canadá', 2005),
    ('SunBeach', 'Austrália', 2010),
    ('ClassicModa', 'Itália', 1972),
    ('KidsHappy', 'Brasil', 2018),
    ('StreetKing', 'EUA', 2009),
    ('RoyalWoman', 'França', 1995),
    ('TrendyClub', 'Brasil', 2020),
    ('SoftCotton', 'Índia', 2001),
    ('WalkUrban', 'Inglaterra', 1990),
    ('ModeBelle', 'França', 2003),
    ('FutureWear', 'Japão', 2019),
    ('GreenLife', 'Alemanha', 2014),
    ('LuxBrand', 'Suíça', 1980),
    ('YoungStyle', 'Brasil', 2021),
    ('WarmHouse', 'Noruega', 2007),
    ('OceanFresh', 'Chile', 2013);
""")

    cursor.execute("""
    INSERT INTO modelos_vestuario (modelo, tecido, genero) VALUES
    ('Camiseta Slim Fit', 'Algodão', 'Masculino'),
    ('Regata Dry Fit', 'Poliéster', 'Unissex'),
    ('Calça Cargo', 'Sarja', 'Masculino'),
    ('Vestido Rodado', 'Viscose', 'Feminino'),
    ('Jaqueta Puffer', 'Poliéster', 'Unissex'),
    ('Camisa Xadrez', 'Flanela', 'Masculino'),
    ('Top Esportivo', 'Elastano', 'Feminino'),
    ('Saia Plissada', 'Seda', 'Feminino'),
    ('Cardigan Longo', 'Tricot', 'Feminino'),
    ('Moletom Oversized', 'Algodão', 'Unissex'),
    ('Shorts Tático', 'Poliéster', 'Masculino'),
    ('Blusa Manga Bufante', 'Crepe', 'Feminino'),
    ('Calça Legging Fitness', 'Poliamida', 'Feminino'),
    ('Macacão Social', 'Linho', 'Feminino'),
    ('Blazer Slim', 'Poliéster', 'Masculino'),
    ('Camiseta Oversized', 'Algodão', 'Unissex'),
    ('Jaqueta Jeans', 'Jeans', 'Unissex'),
    ('Saia Jeans', 'Jeans', 'Feminino'),
    ('Vestido Tubinho', 'Poliéster', 'Feminino'),
    ('Regata Básica', 'Algodão', 'Feminino');
""")

    cursor.execute("""
    INSERT INTO roupas_vendidos (item, quantidade, data_venda) VALUES
    ('Camiseta Básica', 3, '2024-01-10'),
    ('Calça Jeans', 1, '2024-01-11'),
    ('Jaqueta Puffer', 2, '2024-01-12'),
    ('Vestido Longo', 1, '2024-01-14'),
    ('Saia Midi', 4, '2024-01-15'),
    ('Camisa Social', 2, '2024-01-17'),
    ('Regata Dry', 5, '2024-01-18'),
    ('Moletom Oversized', 1, '2024-01-19'),
    ('Calça Jogger', 3, '2024-01-22'),
    ('Camiseta Estampada', 6, '2024-01-23'),
    ('Bermuda Sarja', 2, '2024-01-24'),
    ('Jaqueta Jeans', 1, '2024-01-25'),
    ('Top Fitness', 4, '2024-01-26'),
    ('Pijama Algodão', 2, '2024-01-28'),
    ('Blazer Slim', 1, '2024-01-29'),
    ('Shorts Jeans', 3, '2024-02-01'),
    ('Cardigan', 1, '2024-02-02'),
    ('Macacão Jeans', 1, '2024-02-03'),
    ('Saia Futebol', 2, '2024-02-04'),
    ('Cropped Liso', 5, '2024-02-05');
""")

    conexao.commit()

    print("\n Dados inseridos com sucesso!")
    print(" Listando todas as tabelas:\n")


    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
    """)
    tabelas = cursor.fetchall()

    for tabela in tabelas:
        nome = tabela[0]
        print(f"\n Tabela: {nome}")

        cursor.execute(f"SELECT * FROM {nome}")
        linhas = cursor.fetchall()

        if linhas:
            for linha in linhas:
                print("   ➜", linha)
        else:
            print("   (vazia)")

    print("\n Finalizado!\n")


def deleteTable(cursor, conexao, nomeTabela):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = [t[0] for t in cursor.fetchall()]
    
    comando = f"DELETE FROM {nomeTabela} WHERE id IN (1, 2)"
    cursor.execute(comando)
    conexao.commit()

    print(f"✔ Registros da tabela {nomeTabela} foram excluídos!")