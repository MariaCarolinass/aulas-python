produtos = ["blusa gola alta", "calça pantalona", "tênis", "regata"]

def adicionarProduto(produto):
	if produto not in produtos:
		produtos.append(produto)
		return f"{produto} adicionado"
	return f"{produto} já existe"

def removerProduto(produto):
	if produto in produtos:
		produtos.remove(produto)
		return f"{produto} removido"
	return f"{produto} inexistente"

def editarProduto(produto, novoproduto):
	for p in produtos:
		if p == produto:
			i = produtos.index(produto)
			produtos[i] = novoproduto
			return f"{produto} editado para {novoproduto}"
	return f"{produto} inexistente"

def exibirProduto(produto):
	if produto in produtos:
		return produto
	return f"{produto} inexistente"

print(adicionarProduto("camisa gola v"))
print(removerProduto("blusa gola alta"))
print(editarProduto("tênis", "tênis de corrida"))
print(exibirProduto("regata"))
print(produtos)
