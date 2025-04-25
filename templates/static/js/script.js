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

function editar_produto(botao) {
    const div_editar = document.getElementsByClassName('editar')[0]
    if (div_editar.style.display === "flex") {
        div_editar.style.display = "none";
        document.body.style.overflow = 'auto'
    } else {
        div_editar.style.display = "flex";
        document.body.style.overflow = 'hidden'
    }

    // Pegando os dados do botão
    const id = botao.getAttribute("data-produto-id");
    const nome = botao.getAttribute("data-nome");
    const estoque = botao.getAttribute("data-estoque");
    const preco = botao.getAttribute("data-preco");

    // Preenchendo os inputs do modal
    document.getElementById("input_produto_id").value = id;
    document.getElementById("input_nome_produto").value = nome;
    document.getElementById("input_estoque").value = estoque;
    document.getElementById("input_preco").value = preco;

    // console.log(id,nome,estoque,preco)

}

function abrir_mobile_menu() {
    const mobile_menu = document.getElementsByClassName('mobile_menu')[0]

    if (mobile_menu.style.display === "flex") {
        mobile_menu.style.display = "none";
    } else {
        mobile_menu.style.display = "flex";
    }
}
    

function editar_perfil() {
    const div = document.getElementsByClassName('editar')[0]

    if (div.style.display === "flex") {
        div.style.display = "none";
    } else {
        div.style.display = "flex";
    }
}
