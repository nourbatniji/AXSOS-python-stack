function validate_reg() {
    var first_name = document.querySelector('#first_name')
    var last_name = document.querySelector('#last_name')
    var birthday = document.querySelector('#birthday')
    var email = document.querySelector('#email')
    var password = document.querySelector('#password')
    var confirm_pw = document.querySelector('#confirm_pw')


    var result = true

    if (first_name.value == '') {
        alert("Please fill First Name")
        result = false
    }
    else if (last_name.value == '') {
        alert("Please fill Last Name")
        result = false
    }
    else if (email.value == '') {
        alert("Please fill Email")
        result = false
    }
    else if (birthday.value == 0) {
        alert("Please fill Birthday")
        result = false
    }
    else if (password.value == '') {
        alert("Please fill Password")
        result = false
    }
    else if (confirm_pw.value == '') {
        alert("Please fill Password Confirmation")
        result = false
    }
    return result

}


function validate_login() {
    var email = document.querySelector("#login-email")
    var password = document.querySelector("#login-password")

    var result = true

    if (email.value == '') {
        alert("Email can't be empty")
        result = false
    }
    else if (password.value == '') {
        alert("Password can't be empty")
        result = false
    }
    return result
}
