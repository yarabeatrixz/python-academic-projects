populacao_a = 50_000_000
populacao_b = 200_000_000

taxa_a = 0.035
taxa_b = 0.015

anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a do país B.")
