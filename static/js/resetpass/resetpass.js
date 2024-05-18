console.log('reset')


const sendEmailReset = document.getElementById('sendEmailReset').addEventListener('click',(e) => {
    e.preventDefault();
    sendRestoreEmailCode();
})


async function sendRestoreEmailCode(){

        try {
            const email = document.getElementById('emailrest').value;
            const data = {email: email};
    
            const axiosConfig = {
                method: 'post',
                url: '/resetpass/sendcode',
                data: data
            }

            moverSlider(1)
            const response = await axios(axiosConfig)
            console.log(response.data)
            
        }
        catch (error) {
    
            moverSlider(-1)
            msjError = error.response.data.msj
            showToast('Email incorrectos',msjError,'danger') 
        }
}



const sendCodeReset = document.getElementById('rescode').addEventListener('click',(e) => {
    console.log("resrardsacw")
    e.preventDefault();
    sendRestorCode();
})


async function sendRestorCode(){

        try {
            const email = document.getElementById('emailrest').value;
            const code = document.getElementById('coderest').value;
            const newPassword = document.getElementById('newpass').value;
            const data = {
                email: email,
                code:code,
                newPassword:newPassword
            };
    
            const axiosConfig = {
                method: 'post',
                url: '/resetpass',
                data: data
            }
            showLoader()
            const response = await axios(axiosConfig)
            console.log(response.data)
            window.location.href = '/login'
            
        }
        catch (error) {
            showLoader()
            msjError = error.response.data.msj
            showToast('Email incorrectos',msjError,'danger') 
        }
}