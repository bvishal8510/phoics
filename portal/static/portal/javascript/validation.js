function validateForm() {
    var x = document.forms["signForm"]["username"].value;
    var y = document.forms["signForm"]["email"].value;
    var z = document.forms["signForm"]["password1"].value;
    var w = document.forms["signForm"]["password2"].value;
    var email_check = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;

    if (x == "") {
        document.getElementById('error_signup_username').innerHTML="Name must be filled out";
        return false;
    }

    else if (y == "") {
        document.getElementById('error_signup_email').innerHTML="Email must be filled out";
        return false;

    }

    else if (z == "") {
        document.getElementById('error_signup_password').innerHTML="Password must be filled out";
        return false;
    }


    else if (w == "") {
        document.getElementById('error_signup_conf_password').innerHTML="confirm password must be filled out";
        return false;
    }

    else if (z != w){
        document.getElementById('error_signup_conf_password').innerHTML="Password are not matching";
        return false;
    }

     else if (!email_check.test(y)){
        document.getElementById('error_signup_email').innerHTML="Email does not contain valid syntax";
        return false;
    }

}

function loginValidate() {

    var x = document.forms["loginForm"]["username"].value;
    var y = document.forms["loginForm"]["password"].value;
    if (x == "") {
      document.getElementById('error_login_username').innerHTML="Name must be filled out";
      return false;
    }

    else if (y == "") {
        document.getElementById('error_login_password').innerHTML="Password must be filled out";
        return false;
    }

}

function forgetValidate() {

    var x = document.forms["forgetForm"]["email"].value;
    var email_check = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;
    if (x == "") {
        document.getElementById('error_forget_email').innerHTML="Email must be filled out";
        return false;
    }

    else if (!email_check.test(x)) {
        document.getElementById('error_forget_email').innerHTML="Email does not contain valid input";
        return false;
    }
}