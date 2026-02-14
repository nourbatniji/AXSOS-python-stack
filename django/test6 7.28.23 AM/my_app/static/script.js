function reg_validation() {
    var username = document.querySelector('#username')
    var alias = document.querySelector('#alias')
    var email = document.querySelector('#email')
    var password = document.querySelector('#password')
    var confirm_pw = document.querySelector('#confirm_pw')

    var result = true


    if (username.value == '') {
        alert('Fill Name')
        result = false
    }
    else if (alias.value == '') {
        alert('Fill Alias')
        result = false
    }
    else if (email.value == '') {
        alert('Fill Email')
        result = false
    }
    else if (password.value == '') {
        alert('Fill Password')
        result = false
    }
    else if (confirm_pw.value == '') {
        alert('Fill Password Confirmation')
        result = false
    }
    return result
}
function login_validation() {
    var email = document.querySelector('#login_email')
    var password = document.querySelector('#login_password')

    var result = true

    if (email.value == '') {
        alert('Fill Email')
        result = false
    }
    else if (password.value == '') {
        alert('Fill Password')
        result = false
    }
    return result
}