# Classe base Pizza
class Pizza:
    def description(self):
        return "Ordered Pizza"

    def cost(self):
        return 5.00

# Classe base para decoradores
class Decorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def description(self):
        return self._pizza.description()

    def cost(self):
        return self._pizza.cost()

# Decorador para adicionar queijo comum
class Cheese(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Cheese"

    def get_ingredient_cost(self):
        return 1.00

# Decorador para adicionar pepperoni
class Pepperoni(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Pepperoni"

    def get_ingredient_cost(self):
        return 1.50

# Decorador para adicionar azeitonas
class Olives(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Olives"

    def get_ingredient_cost(self):
        return 0.75

# Decorador para adicionar cogumelos
class Mushroom(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Mushrooms"

    def get_ingredient_cost(self):
        return 1.25

# Decorador para adicionar chocolate
class Chocolate(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Chocolate"

    def get_ingredient_cost(self):
        return 1.75

# Decorador para adicionar nutella
class Nutella(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Nutella"

    def get_ingredient_cost(self):
        return 2.00

# Decorador para adicionar cheddar
class Cheddar(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Cheddar"

    def get_ingredient_cost(self):
        return 1.50

# Decorador para adicionar provolone
class Provolone(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Provolone"

    def get_ingredient_cost(self):
        return 1.75

# Decorador para adicionar bacon
class Bacon(Decorator):
    def description(self):
        return self._pizza.description() + self.get_ingredient_description()

    def cost(self):
        return self._pizza.cost() + self.get_ingredient_cost()

    def get_ingredient_description(self):
        return ", Bacon"

    def get_ingredient_cost(self):
        return 2.50


# Criando uma pizza simples:

pizza = Pizza()
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona queijo à pizza
pizza = Cheese(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona pepperoni à pizza com queijo
pizza = Pepperoni(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona azeitonas à pizza com queijo e pepperoni
pizza = Olives(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona cogumelos à pizza com queijo, pepperoni e azeitonas
pizza = Mushroom(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona chocolate à pizza com queijo, pepperoni, azeitonas e cogumelos
pizza = Chocolate(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona nutella à pizza com chocolate
pizza = Nutella(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona cheddar à pizza com nutella
pizza = Cheddar(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona provolone à pizza com cheddar
pizza = Provolone(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")

# Adiciona bacon à pizza com provolone
pizza = Bacon(pizza)
print(f"Description: {pizza.description()}, Cost: {pizza.cost()}")
