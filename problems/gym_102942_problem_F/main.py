# src: https://codeforces.com/gym/102942/problem/F

if __name__ == "__main__":
    num_casos = int(input())
    output = []

    for caso in range(0, num_casos):
        aux =  list(map(int, input().split(' ')))
        shop_items = list(map(int, input().split(' ')))
        n = aux[0]
        k = aux[1]
        carrinho = 0
        melhor_carrinho = 0
        indice_inicio = 0
        items_comprados = set()
        i = 0

        while (i < n):
            if (n-indice_inicio <= melhor_carrinho):
                break
            if (shop_items[i] in items_comprados):
                carrinho += 1
                i = i + 1
            elif (shop_items[i] <= k):
                k -= shop_items[i]
                items_comprados.add(shop_items[i])
                carrinho += 1
                i = i + 1
            else:
                melhor_carrinho = carrinho if (carrinho > melhor_carrinho) else melhor_carrinho
                indice_inicio += 1
                i = indice_inicio
                carrinho = 0
                k = aux[1]
                items_comprados.clear()
        output.append(carrinho if (carrinho > melhor_carrinho) else melhor_carrinho)
    
    for out in output:
        print(out)
