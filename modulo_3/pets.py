class Animal:
    def falar(self):
        print("Som genérico")


class Cachorro(Animal):
    def falar(self):
        print("Au Au")


class Gato(Animal):
    def falar(self):
        print("Miau")


if __name__ == "__main__":
    cachorro = Cachorro()
    gato = Gato()

    cachorro.falar()
    gato.falar()
