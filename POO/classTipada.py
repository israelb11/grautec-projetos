from dataclasses import dataclass

# Classe tipada mutável (padrão)
@dataclass
class UsuarioMutavel:
    nome: str
    idade: int

p1 = UsuarioMutavel("Ana", 25)
print(p1)
p1.idade = 26  # Permitido!
print(p1)

# Classe tipada imutável (frozen=True)
@dataclass(frozen=True)
class UsuarioImutavel:
    nome: str
    idade: int

p2 = UsuarioImutavel("Bruno", 30)
print(p2)
# p2.idade = 31  # Lança FrozenInstanceError!