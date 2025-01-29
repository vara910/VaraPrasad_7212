class Example:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

example = Example()
print(example.public_var)
print(example._protected_var)
print(example.get_private_var())
example.set_private_var("New private value")
print(example.get_private_var())