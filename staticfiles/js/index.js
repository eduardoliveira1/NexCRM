function filtrarProdutos() {
    let input = document.getElementById("filtro").value.toLowerCase()
    let produtos = document.querySelectorAll(".produto")

    produtos.forEach(produto => {
        let nomeProduto = produto.querySelector(".o_nome_produto").value.toLowerCase()
        
        if (nomeProduto.includes(input)) {
            produto.style.display = "flex"
        } else {
            produto.style.display = "none"
        }
    });
}
