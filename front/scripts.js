/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/avaliacoes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.avaliacoes?.forEach(item => insertList(item.id,
        item.receita_total, 
        item.pedidos_feitos, 
        item.limite,
        item.target,
        item.resultado ? 'Sim' : 'Não',
      ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputReceitaTotal, inputPedidosFeitos, inputLimite, inputTarget) => {
    
  const formData = new FormData();
  formData.append('limite', inputLimite);
  formData.append('pedidos_feitos', inputPedidosFeitos);
  formData.append('receita_total', inputReceitaTotal);
  formData.append('target', inputTarget);

  let url = 'http://127.0.0.1:5000/avaliacao';
  return fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  span.onclick = removeElement;
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = ({target}) => {
  const row = target.parentElement.parentElement;
  const id = row.dataset.id
  if (confirm("Você tem certeza?")) {
    deleteItem(id).then( res => {
      row.remove()
      alert("Removido!")
    })
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = async (id) => {
  let url = 'http://127.0.0.1:5000/avaliacao?id='+id;
  return fetch(url, {
    method: 'delete'
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputReceitaTotal = document.getElementById("newRec").value;
  let inputPedidosFeitos = document.getElementById("newPef").value;
  let inputLimite = document.getElementById("newLim").value;
  let inputTarget = document.getElementById("newTarg").value;

  postItem(inputReceitaTotal, inputPedidosFeitos, inputLimite, inputTarget)
  .then(
    result => {
      insertList(result.id, inputReceitaTotal, inputPedidosFeitos, inputLimite, inputTarget, result.resultado ? 'Sim' : 'Não');
      alert("Item adicionado!");
    }
  );
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (id, receita_total, pedidos_feitos, limite, target, resultado) => {
  
  var item = [receita_total, pedidos_feitos, limite, target, resultado];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  row.dataset.id = id;

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);

  document.getElementById("newRec").value = "";
  document.getElementById("newPef").value = "";
  document.getElementById("newLim").value = "";
  document.getElementById("newTarg").value = "";
}