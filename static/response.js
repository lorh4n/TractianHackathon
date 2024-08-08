document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('uploadForm').addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var formData = new FormData(this); // Create a FormData object from the form

        fetch('/submit', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
          .then(dados => {
            console.log(dados)
            document.getElementById('nome').textContent = `Nome: ${dados.Nome}`;
            document.getElementById('fabricante').textContent = `Fabricante: ${dados.Fabricante}`;
            document.getElementById('tipo').textContent = `Tipo: ${dados.Tipo}`;
            document.getElementById('indetificacao').textContent = `Identificação: ${dados.Identificacao}`;
            document.getElementById('localizacao').textContent = `Localização: ${dados.Localizacao}`;
            document.getElementById('potencia').textContent = `Potência: ${dados.Potencia}`;
            document.getElementById('tensao').textContent = `Tensão: ${dados.Tensao}`;
            document.getElementById('frequencia').textContent = `Frequência: ${dados.Frequencia}`;
            document.getElementById('rotacao').textContent = `Rotação: ${dados.Rotacao}`;
            document.getElementById('protecao').textContent = `Grau de proteção: ${dados.Grau_de_Protecao}`;
            document.getElementById('eficiencia').textContent = `Eficiência: ${dados.Eficiencia}`;
            document.getElementById('estado').textContent = `Estado da peça: ${dados.Estado_Atual}`;
        })
        .catch(error => console.error('Erro ao carregar o JSON:', error));
    });
});
