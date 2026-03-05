function calcular(){

    let numero = document.getElementById("numero").value
    let resultado = document.getElementById("resultado")

    if(numero === ""){
        resultado.innerHTML = "⚠ Ingresa un número"
        return
    }

    numero = parseFloat(numero)

    if(numero < 0){
        resultado.innerHTML = "❌ No se puede calcular raíz de número negativo"
        return
    }

    let raiz = Math.sqrt(numero)

    resultado.innerHTML = "✔ Resultado: " + raiz.toFixed(4)

}