class Curriculo:
    def __init__(self):
        self.nome = input("Digite o nome completo: ")
        self.contato = {
            "Localização": input("Digite a localização: "),
            "Telefone": input("Digite o telefone: "),
            "E-mail": input("Digite o e-mail: ")
        }
        self.perfil_profissional = input("Digite o perfil profissional: ")
        self.links_sociais = {
            "Facebook": input("Digite o link do Facebook: "),
            "Instagram": input("Digite o link do Instagram: "),
            "Linkedin": input("Digite o link do Linkedin: ")
        }
        self.idiomas = {}
        idiomas = int(input("Quantos idiomas você deseja adicionar? "))
        for _ in range(idiomas):
            idioma = input("Digite o idioma: ")
            nivel = input("Digite o nível: ")
            self.idiomas[idioma] = nivel
        
        self.experiencia_trabalho = []
        num_experiencias = int(input("Quantas experiências de trabalho você deseja adicionar? "))
        for _ in range(num_experiencias):
            experiencia = {
                "Cargo": input("Digite o cargo: "),
                "Empresa": input("Digite a empresa: "),
                "Local": input("Digite o local: "),
                "Período": input("Digite o período: "),
                "Descrição": input("Digite a descrição: ")
            }
            self.experiencia_trabalho.append(experiencia)
        
        self.formacao_academica = []
        num_formacoes = int(input("Quantas formações acadêmicas você deseja adicionar? "))
        for _ in range(num_formacoes):
            formacao = {
                "Curso": input("Digite o curso: "),
                "Instituição": input("Digite a instituição: "),
                "Local": input("Digite o local: "),
                "Período": input("Digite o período: ")
            }
            self.formacao_academica.append(formacao)
        
        self.cursos = []
        num_cursos = int(input("Quantos cursos você deseja adicionar? "))
        for _ in range(num_cursos):
            curso = {
                "Curso": input("Digite o curso: "),
                "Instituição": input("Digite a instituição: "),
                "Período": input("Digite o período: ")
            }
            self.cursos.append(curso)
        
        self.hobbies = []
        num_hobbies = int(input("Quantos hobbies você deseja adicionar? "))
        for _ in range(num_hobbies):
            hobby = input("Digite o hobby: ")
            self.hobbies.append(hobby)

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
            print(f"  Instituição: {formacao['Instituição']}")
            print(f"  Local: {formacao['Local']}")
            print(f"  Período: {formacao['Período']}")
        print("\nCursos:")
        for curso in self.cursos:
            print(f"- Curso: {curso['Curso']}")
            print(f"  Instituição: {curso['Instituição']}")
            print(f"  Período: {curso['Período']}")
        print("\nHobbies:")
        for hobby in self.hobbies:
            print(f"- {hobby}")

# Criar instância do currículo
meu_curriculo = Curriculo()

# Imprimir o currículo
meu_curriculo.imprimir_curriculo()

