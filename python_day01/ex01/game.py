class GotCharacter:

    def __init__(self, first_name, last_name, attribut):
        self.first_name = first_name
        self.last_name = last_name
        self.attribut = attribut
        self.alive = True

class Alpha(GotCharacter):

    def __init__(self, first_name, last_name, attribut):
        GotCharacter.__init__(self, first_name, last_name, attribut)
        self.caste = "Alpha"

    def print_caste(self, character):
        print("{0} {1} fait partie de la caste {2}".format(character.first_name, character.last_name, character.caste))

    def die(self, character):
        character.alive = False

class Beta(GotCharacter):

    def __init__(self, first_name, last_name, attribut):
        GotCharacter.__init__(self, first_name, last_name, attribut)
        self.caste = "Beta"

    def print_caste(self, character):
        print("{0} {1} fait partie de la caste {2}".format(character.first_name, character.last_name, character.caste))

    def die(self, character):
        character.alive = False


bernard = Alpha("Bernard", "Marx", "Too much alcool")
lenina = Beta("Lenina", "Crowne", "Perfect conditioning")


print(bernard)
print(bernard.first_name)
print(bernard.last_name)
print(bernard.caste)
print(bernard.attribut)
bernard.print_caste(bernard)
print(bernard.alive)
bernard.die(bernard)
print(bernard.alive)

print(lenina)
print(lenina.first_name)
print(lenina.last_name)
print(lenina.caste)
print(lenina.attribut)
lenina.print_caste(lenina)
print(lenina.alive)
lenina.die(lenina)
print(lenina.alive)
