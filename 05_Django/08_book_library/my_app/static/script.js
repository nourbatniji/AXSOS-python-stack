function signup_validation() {
    var first_name = document.querySelector('#first_name')
    var last_name = document.querySelector('#last_name')
    var email = document.querySelector('#email')
    var password = document.querySelector('#password')
    var confirm_pw = document.querySelector('#confirm_pw')

    var result = true

    if (first_name.value == ''){
        alert('Fill First Name')
        result = false
    }
    else if (last_name.value == ''){
        alert('Fill Last Name')
        result = false
    }
    else if (email.value == ''){
        alert('Fill Email')
        result = false
    }
    else if (password.value == ''){
        alert('Fill Password')
        result = false
    }
    else if (confirm_pw.value == ''){
        alert('Fill Password Confirmation')
        result = false
    }

    return result
}


function login_validation() {
    var email = document.querySelector('#login-email')
    var password = document.querySelector('#login-password')

    var result = true

    if (email.value == ''){
        alert('Fill Email')
        result = false
    }
    else if (password.value == ''){
        alert('Fill Password')
        result = false
    }

    return result
}