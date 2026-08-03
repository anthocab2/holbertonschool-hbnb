/**
 * Handle user authentication
 */


/**
 * Store JWT token in cookie
 *
 * @param {string} token JWT token
 */
function setCookie(token) {

    document.cookie = `token=${token}; path=/`;

}


/**
 * Get JWT token from cookie
 *
 * @returns {string|null}
 */
function getCookie() {

    const cookies = document.cookie.split(";");


    for (let cookie of cookies) {

        const [name, value] = cookie.trim().split("=");


        if (name === "token") {

            return value;

        }

    }


    return null;

}



/**
 * Login user with API
 *
 * @param {string} email User email
 * @param {string} password User password
 */
async function loginUser(email, password) {


    try {


        const response = await fetch(
            "http://127.0.0.1:5000/api/v1/auth/login",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },


                body: JSON.stringify({

                    email: email,

                    password: password

                })

            }

        );



        if (response.ok) {


            const data = await response.json();


            setCookie(data.access_token);


            window.location.href = "index.html";


        } else {


            const error = document.getElementById("error-message");


            if (error) {

                error.textContent =
                "Login failed. Check your email and password.";

            }


        }


    } catch(error) {


        console.error(error);


    }


}




/**
 * Listen for login form submit
 */
document.addEventListener(
"DOMContentLoaded",
() => {


    const loginForm =
    document.getElementById("login-form");



    if (loginForm) {


        loginForm.addEventListener(
        "submit",
        (event) => {


            event.preventDefault();



            const email =
            document.getElementById("email").value;



            const password =
            document.getElementById("password").value;



            loginUser(email,password);



        });


    }


});
