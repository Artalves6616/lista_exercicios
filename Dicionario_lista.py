#1.	Crie um dicionário pessoa com as seguintes chaves e valores: "nome" com seu nome, "idade" com sua idade, "cidade" com sua cidade
dicionario={"nome":"Arthur","idade":"22","cidade":"Brasilia"}


#2.	Acesse e imprima o valor associado à chave "nome".
dicionario["nome"]


#3.	Adicione uma nova chave "profissão" com o valor da sua profissão.
dicionario ["profissão"] ="estagiario"


#4.	Modifique o valor da chave "idade" para uma nova idade.
dicionario ["idade"] ="23"


#5.	Remova a chave "cidade" do dicionário.
cidade = dicionario.pop("cidade")


#6. Crie um dicionário contatos com os pares chave-valor: "Alice" - "1234-5678", "Bob" - "8765-4321", "Carol" - "5678-1234"

contatos = {
    "Alice": "1234-5678",
    "Bob": "8765-4321",
    "Carol": "5678-1234"
}

#7. Utilize o método get() para acessar o número de telefone de "Alice"
numero_alice = contatos.get("Alice")
print(f"Número de telefone de Alice: {numero_alice}")

#8. Utilize o método keys() para obter todas as chaves do dicionário

chaves_contatos = contatos.keys()
print(f"Chaves do dicionário: {list(chaves_contatos)}")

#9. Utilize o método values() para obter todos os valores do dicionário

valores_contatos = contatos.values()
print(f"Valores do dicionário: {list(valores_contatos)}")

