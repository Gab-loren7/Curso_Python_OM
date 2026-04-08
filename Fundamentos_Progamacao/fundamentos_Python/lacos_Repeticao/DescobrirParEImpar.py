
# (end="") impede a linha de ser quebrada, concatenando os numeros!

# Contador de Par com For
for i in range(1,101):
    if i == 2:
        print(i, end="")
    elif i % 2 == 0:
        print(f", {i}", end="")
print(".")
        
# Com While
i = 1
while i <= 100:
    i += 1
    if i == 2:
        print(i, end="")
    elif i % 2 == 0:
        print(f", {i}", end="")
print(".")
        