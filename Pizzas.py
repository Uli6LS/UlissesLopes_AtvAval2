# Importa os módulos necessários para criar classes abstratas
from abc import ABC, abstractmethod

# Define a classe abstrata Pizza que servirá como interface para todos os tipos de pizzas
class Pizza(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# Implementa a classe ConcretePizza que herda de Pizza e representa uma pizza simples
class ConcretePizza(Pizza):
    def description(self):
        return "Plain Pizza"

    def cost(self):
        return 5.00

# Define a classe abstrata ToppingDecorator que também herda de Pizza e contém uma referência a um objeto Pizza
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# Implementa o decorador CheeseDecorator que adiciona queijo à pizza
class CheeseDecorator(ToppingDecorator):
    def description(self):
        return self._pizza.description() + ", Cheese"

    def cost(self):
        return self._pizza.cost() + 1.00

# Implementa o decorador PepperoniDecorator que adiciona pepperoni à pizza
class PepperoniDecorator(ToppingDecorator):
    def description(self):
        return self._pizza.description() + ", Pepperoni"

    def cost(self):
        return self._pizza.cost() + 1.50

# Implementa o decorador OlivesDecorator que adiciona azeitonas à pizza
class OlivesDecorator(ToppingDecorator):
    def description(self):
        return self._pizza.description() + ", Olives"

    def cost(self):
        return self._pizza.cost() + 0.75

# Implementa o decorador MushroomDecorator que adiciona cogumelos à pizza
class MushroomDecorator(ToppingDecorator):
    def description(self):
        return self._pizza.description() + ", Mushrooms"

    def cost(self):
        return self._pizza.cost() + 1.25

# Exemplo de uso do padrão de projeto Decorator
# Cria uma pizza simples
pizza = ConcretePizza()
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona queijo à pizza
pizza = CheeseDecorator(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona pepperoni à pizza com queijo
pizza = PepperoniDecorator(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona azeitonas à pizza com queijo e pepperoni
pizza = OlivesDecorator(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona cogumelos à pizza com queijo, pepperoni e azeitonas
pizza = MushroomDecorator(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")
