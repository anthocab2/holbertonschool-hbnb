/**
 * HBnB Places page
 */


let places = [];



/**
 * Get cookie value
 */

function getCookie(name) {


    const cookies =
    document.cookie.split(";");



    for (let cookie of cookies) {


        const [key,value] =
        cookie.trim().split("=");



        if (key === name) {

            return value;

        }

    }


    return null;

}




/**
 * Check authentication
 */

function checkAuthentication() {


    const token =
    getCookie("token");



    const loginLink =
    document.getElementById(
        "login-link"
    );



    if (!token) {


        loginLink.style.display =
        "block";


    } else {


        loginLink.style.display =
        "none";


    }


    loadPlaces(token);


}




/**
 * Fetch and display places
 */

async function loadPlaces(token) {


    try {


        places =
        await getPlaces(token);



        displayPlaces(places);



    } catch(error) {


        console.error(error);


    }

}





/**
 * Display places cards
 */

function displayPlaces(data) {


    const container =
    document.getElementById(
        "places-list"
    );


    container.innerHTML = "";



    data.forEach(place => {



        const card =
        document.createElement(
            "div"
        );


        card.className =
        "place-card";



        card.dataset.price =
        place.price;



        card.innerHTML = `

        <h2>
        ${place.name}
        </h2>


        <p>
        ${place.description || ""}
        </p>


        <p>
        Price:
        $${place.price}
        </p>



        <button class="details-button"
        onclick="viewPlace('${place.id}')">

        View Details

        </button>


        `;



        container.appendChild(card);



    });



}




/**
 * Redirect to place details
 */

function viewPlace(id) {


    window.location.href =
    `place.html?id=${id}`;


}





/**
 * Price filtering
 */

function setupFilter() {


    const filter =
    document.getElementById(
        "price-filter"
    );



    filter.addEventListener(
    "change",
    (event)=>{


        const maxPrice =
        event.target.value;



        const cards =
        document.querySelectorAll(
            ".place-card"
        );



        cards.forEach(card=>{


            const price =
            Number(card.dataset.price);



            if (
                maxPrice === "all" ||
                price <= Number(maxPrice)
            ){


                card.style.display =
                "block";


            } else {


                card.style.display =
                "none";


            }


        });


    });


}




document.addEventListener(
"DOMContentLoaded",
()=>{


    checkAuthentication();


    setupFilter();


});
