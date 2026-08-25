from dataclasses import dataclass

# Classe tipada mutável (padrão)
@dataclass
class UsuarioMutavel:
    nome: str
    idade: int

print(f"""------------------------------\n
USUARIO MUTAVEL-1\n""")
p1 = UsuarioMutavel("Ana", 25)
print(f"O nome do user é: {p1.nome} e a sua idade é {p1.idade} \n")

print(f"""------------------------------\n
USUARIO MUTAVEL-2\n""")
p1 = UsuarioMutavel("Carlos", 32)
print(f"O nome do user é: {p1.nome} e a sua idade é {p1.idade} \n")

# Classe tipada imutável (frozen=True)
@dataclass(frozen=True)
class UsuarioImutavel:
    nome: str
    idade: int

p2 = UsuarioImutavel("Bruno", 30)
print(f"""------------------------------\n
USUARIO IMUTAVEL-1\n""")
print(f"""O nome do user é: {p2.nome} e a sua idade é {p2.idade} \n
------------------------------ \n""")

p2.nome = "Alberto"
p2.idade = 31  # Lança FrozenInstanceError!
