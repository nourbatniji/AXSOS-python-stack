function validate_signup() {
    var email = document.querySelector("#email")
    var first_name = document.querySelector("#first_name")
    var last_name = document.querySelector("#last_name")
    var password = document.querySelector("#password")
    var confirm_pw = document.querySelector("#confirm_pw")

    var result = true
    console.log("DONE");


    if (email.vlaue == '') {
        alert('Please fill the email')
        result = false
    }
    else if (first_name.vlaue == '') {
        alert('Please fill the first name')
        result = false
    }
    else if (last_name.vlaue == '') {
        alert('Please fill the email field')
        result = false
    }
    else if (password.vlaue == '') {
        alert('Please fill the password')
        result = false
    }
    else if (confirm_pw.vlaue == '') {
        alert('Please fill the password confirmation')
        result = false
    }

    console.log(result);

    return result
}



function validate_signin() {
    var email = document.querySelector("#email")
    var password = document.querySelector("#password")

    var result = true
    if (email.vlaue == '') {
        alert('Please fill the email')
        result = false
    }
    else if (password.vlaue == '') {
        alert('Please fill the password')
        result = false
    }
    return result

}