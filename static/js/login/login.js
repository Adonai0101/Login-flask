const login = document.getElementById('login').addEventListener('click', (e) => {
    console.log('clcik')
    e.preventDefault()
    loginPost()
})





async function loginPost(){
    showLoader()
    try {
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;

        // Preparar los datos para enviar
        const data = {
            email: email,
            password: password
        };

        const axiosConfig = {
            method: 'post',
            url: '/login',
            data: data
        }

        const response = await axios(axiosConfig)
        window.location.href = '/dashboard'
    }
    catch (error) {
        msjError = ""
        showLoader()
        //msjError = error.response.data.msj
        showToast('Error al ingresar',msjError,'danger') 
    }
}
