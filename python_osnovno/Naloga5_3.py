#   Razdruži, združi

besedilo = input("Vnesite besedo: ")

novo = besedilo.split()
novo[2] = "čuden"

besedilo2 = " ".join(novo)
print(besedilo2)