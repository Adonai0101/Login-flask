async function registroPostData() {

    //Mostramos pantalla de carga
    showLoader()
    try {
        const nombre = document.getElementById('registroNombre').value;
        const email = document.getElementById('registroEmail').value;
        const password = document.getElementById('registroPassword').value;

        // Preparar los datos para enviar
        const data = {
            nombre: nombre,
            email: email,
            password: password
        };

        const axiosConfig = {
            method: 'post',
            url: '/login/registro',
            data: data
        }

        const response = await axios(axiosConfig)
        console.log(response.data)
        showLoader()
        moverSlider(1)

    }
    catch (error) {

        showLoader()
        msjError = error.response.data.msj
        showToast('Error con el usuario',msjError,'danger') 
    }
}


const registro = document.getElementById('registro').addEventListener('click', (e) => {
    console.log('clcik')
    e.preventDefault()
    registroPostData()

})

async function loginPostCodigo() {

    try {
        let codigo = document.getElementById('codigo').value;

        const data = {
            codigo: codigo
        }

        const axiosConfig = {
            method: 'post',
            url: '/login/validar',
            data: data
        }

        const response = await axios(axiosConfig)
        window.location.href = '/login/end'

    } catch (error) {
        msjError = error.response.data.msj
        showToast('Fallo el codigo',msjError,'danger') 
    }

}

const validar = document.getElementById('validar').addEventListener('click', (e) => {
    e.preventDefault()
    console.log('Validando')
    loginPostCodigo()
})