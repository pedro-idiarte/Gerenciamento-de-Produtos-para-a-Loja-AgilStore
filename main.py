import json
import os
import uuid

### Caminho para o arquivo JSON onde os dados serão salvos. ###
DATA_FILE = "inventory.json"

### Função para carregar o inventário a partir do arquivo JSON ###
def load_inventory():
    try:
        file = open(DATA_FILE, "r")
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("Arquivo de inventário não encontrado. Criando um novo inventário.")
        return {}
    except json.JSONDecodeError:
        print("Erro ao carregar os dados do inventário. Iniciando com um inventário vazio.")
        return {}

### Função para salvar o inventário no arquivo JSON ###
def save_inventory(inventory):
    try:
        file = open(DATA_FILE, "w")
        json.dump(inventory, file, indent=4)
        file.close()
        print("Inventário salvo com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar o inventário: {e}")

### Função para gerar um ID único ###
def generate_unique_id():
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    short_id = unique_id_str[:8]
    return short_id


### Função para adicionar um produto ao inventário ###
def add_product(inventory):
    while True:
        name = input("Digite o nome do produto (máx. 20 caracteres): ")
        if len(name) <= 20:
            break
        print("O nome do produto deve ter no máximo 20 caracteres. Tente novamente.")

    while True:
        category = input("Digite a categoria do produto (máx. 15 caracteres): ")
        if len(category) <= 15:
            break
        print("A categoria deve ter no máximo 15 caracteres. Tente novamente.")

    quantity = int(input("Digite a quantidade em estoque: "))
    price = float(input("Digite o preço do produto: "))

    product_id = generate_unique_id()
    inventory[product_id] = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    save_inventory(inventory)
    print(f"Produto {name} adicionado com sucesso!")


### Função para listar produtos ###
def list_products(inventory):
    if not inventory:
        print("Nenhum produto no inventário.")
        return

    print(f"{'ID':<10}{'Nome':<20}{'Categoria':<15}{'Quantidade':<10}{'Preço':<10}")
    print("-" * 70)
    for product_id, details in inventory.items():
        print(
            f"{product_id:<10}{details['name']:<20}{details['category']:<15}{details['quantity']:<10}{details['price']:<10.2f}")


### Função para atualizar um produto ###
def update_product(inventory):
    product_id = input("Digite o ID do produto a ser atualizado: ")
    if product_id not in inventory:
        print("Produto não encontrado.")
        return

    print("Deixe o campo em branco para manter o valor atual.")
    name = input(f"Novo nome ({inventory[product_id]['name']}): ") or inventory[product_id]['name']
    category = input(f"Nova categoria ({inventory[product_id]['category']}): ") or inventory[product_id]['category']
    quantity = input(f"Nova quantidade ({inventory[product_id]['quantity']}): ")
    price = input(f"Novo preço ({inventory[product_id]['price']}): ")

    inventory[product_id]['name'] = name
    inventory[product_id]['category'] = category
    inventory[product_id]['quantity'] = int(quantity) if quantity else inventory[product_id]['quantity']
    inventory[product_id]['price'] = float(price) if price else inventory[product_id]['price']

    save_inventory(inventory)
    print("Produto atualizado com sucesso!")


### Função para excluir um produto ###
def delete_product(inventory):
    product_id = input("Digite o ID do produto a ser excluído: ")
    if product_id not in inventory:
        print("Produto não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja excluir o produto {inventory[product_id]['name']}? (s/n): ").lower()
    if confirm == 's':
        del inventory[product_id]
        save_inventory(inventory)
        print("Produto excluído com sucesso!")
    else:
        print("Exclusão cancelada.")


### Função para buscar um produto ###
def search_product(inventory):
    query = input("Digite o ID ou parte do nome do produto: ").lower()

    if query in inventory:
        details = inventory[query]
        print(f"{'ID':<10}{'Nome':<20}{'Categoria':<15}{'Quantidade':<10}{'Preço':<10}")
        print("-" * 70)
        print(
            f"{query:<10}{details['name']:<20}{details['category']:<15}{details['quantity']:<10}{details['price']:<10.2f}")
    else:
        results = {pid: details for pid, details in inventory.items() if query in details['name'].lower()}

        if not results:
            print("Nenhum produto encontrado.")
        else:
            print(f"{'ID':<10}{'Nome':<20}{'Categoria':<15}{'Quantidade':<10}{'Preço':<10}")
            print("-" * 70)
            for product_id, details in results.items():
                print(
                    f"{product_id:<10}{details['name']:<20}{details['category']:<15}{details['quantity']:<10}{details['price']:<10.2f}")


### Menu principal ###
def main():
    inventory = load_inventory()

    while True:
        print("\n--- AgilStore: Gerenciamento de Inventário ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        choice = input("Escolha uma opção: ")
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            list_products(inventory)
        elif choice == '3':
            update_product(inventory)
        elif choice == '4':
            delete_product(inventory)
        elif choice == '5':
            search_product(inventory)
        elif choice == '6':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
