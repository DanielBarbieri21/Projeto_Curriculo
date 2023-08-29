class Curriculo:
    def __init__(self):
        self.nome = "Adailton Daniel Oliveira Barbieri"
        self.contato = {
            "Localização": "Juiz de Fora",
            "Telefone": "32991186728",
            "E-mail": "[seu e-mail aqui]"
        }
        self.perfil_profissional = "Desenvolvedor Full Stack (Back-End e Front-End) com experiência em Python, Java, HTML, CSS e design web. Analista de Redes. Estudante de Engenharia de Software com habilidades em Microsoft Office, resiliência, liderança, comunicação, trabalho em equipe, pensamento analítico e criativo."
        self.links_sociais = {
            "Facebook": "https://www.facebook.com/dibarbieri",
            "Instagram": "https://www.instagram.com/danielbarbieri21/?hl=pt-br",
            "Linkedin": "https://www.linkedin.com/in/daniel-barbieri-4990462a/"
        }
        self.idiomas = {
            "Inglês": "★★☆☆☆",
            "Espanhol": "★☆☆☆☆"
        }
        self.experiencia_trabalho = [
            {
                "Cargo": "Gerente",
                "Empresa": "ROLAVEDA ROLAMENTOS",
                "Local": "Juiz de Fora",
                "Período": "setembro 2009 – Presente",
                "Descrição": "Vendas, suporte ao cliente e manutenção de páginas web e redes sociais. Responsável pela área de TI."
            },
            {
                "Cargo": "Comprador",
                "Empresa": "Supermercado Bahamas",
                "Local": "Juiz de Fora",
                "Período": "fevereiro 2003 – agosto 2009",
                "Descrição": "Gerente de compras, análise de insumos e planilhas de controle."
            },
            {
                "Cargo": "Garçom",
                "Empresa": "Shayka Comida Árabe",
                "Local": "Juiz de Fora",
                "Período": "janeiro 2001 – janeiro 2003",
                "Descrição": "Atendimento ao cliente e atividades de manutenção."
            }
        ]
        self.formacao_academica = [
            {
                "Curso": "Engenharia de Software",
                "Instituicao": "Faculdade Estácio de Sá",
                "Local": "Juiz de Fora",
                "Período": "junho 2022 – dezembro 2025"
            },
            {
                "Curso": "Ciências Econômicas",
                "Instituicao": "Instituto Vianna Junior",
                "Local": "Juiz de Fora",
                "Período": "janeiro 2006 – dezembro 2009"
            },
            {
                "Curso": "Administração em Sistemas de Informação",
                "Instituicao": "Faculdade Estácio de Sá",
                "Local": "",
                "Período": "janeiro 2004 – dezembro 2007"
            }
        ]
        self.cursos = [
            {
                "Curso": "Java",
                "Instituicao": "Fundação Bradesco",
                "Período": "novembro 2022 – dezembro 2020"
            },
            {
                "Curso": "C# Avançado",
                "Instituicao": "Fundação Bradesco",
                "Período": "outubro 2022 – novembro 2022"
            },
            {
                "Curso": "Introdução a Redes",
                "Instituicao": "Fundação Bradesco",
                "Período": "janeiro 2023 – fevereiro 2023"
            },
            {
                "Curso": "Computação em Nuvem",
                "Instituicao": "Senai/SC",
                "Período": "julho 2023 – agosto 2023"
            },
            {
                "Curso": "Data Science",
                "Instituicao": "Senai/SC",
                "Período": "julho 2023 – agosto 2023"
            },
            {
                "Curso": "Python Avançado",
                "Instituicao": "Fundação Bradesco",
                "Período": "novembro 2022 – dezembro 2022"
            }
        ]
        self.hobbies = "Jogar Futebol e caminhadas"

    def imprimir_curriculo(self):
        print(f"Nome: {self.nome}\n")
        print("Contato:")
        for chave, valor in self.contato.items():
            print(f"- {chave}: {valor}")
        print("\nPerfil Profissional:")
        print(self.perfil_profissional)
        print("\nLinks Sociais:")
        for chave, valor in self.links_sociais.items():
            print(f"- {chave}: {valor}")
        print("\nIdiomas:")
        for idioma, nivel in self.idiomas.items():
            print(f"- {idioma}: {nivel}")
        print("\nExperiência de Trabalho:")
        for experiencia in self.experiencia_trabalho:
            print(f"- Cargo: {experiencia['Cargo']}")
            print(f"  Empresa: {experiencia['Empresa']}")
            print(f"  Local: {experiencia['Local']}")
            print(f"  Período: {experiencia['Período']}")
            print(f"  Descrição: {experiencia['Descrição']}")
        print("\nFormação Acadêmica:")
        for formacao in self.formacao_academica:
            print(f"- Curso: {formacao['Curso']}")
            print(f"  Instituição: {formacao['Instituicao']}")
            print(f"  Local: {formacao['Local']}")
            print(f"  Período: {formacao['Período']}")
        print("\nCursos:")
        for curso in self.cursos:
            print(f"- Curso: {curso['Curso']}")
            print(f"  Instituição: {curso['Instituicao']}")
            print(f"  Período: {curso['Período']}")
        print("\nHobbies:")
        print(self.hobbies)

# Criar instância do currículo
meu_curriculo = Curriculo()

# Imprimir o currículo
meu_curriculo.imprimir_curriculo()
