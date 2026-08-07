/**
 * Place Details Page
 */

let token = null;


/**
 * Get cookie value
 */
function getCookie(name) {

    const cookies = document.cookie.split(";");

    for (let cookie of cookies) {

        const [key, value] =
            cookie.trim().split("=");

        if (key === name) {
            return value;
        }
    }

    return null;
}


/**
 * Extract place id from URL
 */
function getPlaceIdFromURL() {

    const params =
        new URLSearchParams(
            window.location.search
        );

    return params.get("id");
}


/**
 * Authentication check
 */
function checkAuthentication() {

    token = getCookie("token");

    const addReview =
        document.getElementById(
            "add-review"
        );

    if (!token) {

        addReview.style.display =
            "none";

    } else {

        addReview.style.display =
            "block";

    }
}


/**
 * Fetch place details
 */
async function fetchPlaceDetails(
    placeId
) {

    try {

        const headers = {
            "Content-Type":
                "application/json"
        };

        if (token) {

            headers.Authorization =
                `Bearer ${token}`;

        }

        const response =
            await fetch(

                `http://127.0.0.1:5000/api/v1/places/${placeId}`,

                {
                    method: "GET",
                    headers: headers
                }

            );

        if (!response.ok) {

            throw new Error(
                "Failed loading place"
            );

        }

        const place =
            await response.json();

        displayPlaceDetails(place);

    } catch (error) {

        console.error(error);

    }

}


/**
 * Render page
 */
function displayPlaceDetails(place) {

    const details =
        document.getElementById(
            "place-details"
        );

    details.innerHTML = "";



    details.innerHTML = `

        <h1>${place.name}</h1>

        <div class="place-info">

            <p>
                <strong>Description:</strong>
                ${place.description}
            </p>

            <p>
                <strong>Price:</strong>
                $${place.price}
            </p>

            <p>
                <strong>Host:</strong>
                ${place.host}
            </p>

        </div>

    `;


    const amenitiesTitle =
        document.createElement("h2");

    amenitiesTitle.textContent =
        "Amenities";

    details.appendChild(
        amenitiesTitle
    );


    const amenitiesList =
        document.createElement("ul");


    if (place.amenities) {

        place.amenities.forEach(
            amenity => {

                const li =
                    document.createElement(
                        "li"
                    );

                li.textContent =
                    amenity.name;

                amenitiesList.appendChild(
                    li
                );

            }
        );

    }

    details.appendChild(
        amenitiesList
    );



    displayReviews(
        place.reviews || []
    );

}


/**
 * Reviews section
 */
function displayReviews(reviews) {

    const reviewsSection =
        document.getElementById(
            "reviews"
        );

    reviews.forEach(review => {

        const card =
            document.createElement(
                "div"
            );

        card.className =
            "review-card";

        card.innerHTML = `

            <p>
                ${review.text}
            </p>

            <p>
                User:
                ${review.user}
            </p>

            <p>
                Rating:
                ${review.rating}
            </p>

        `;

        reviewsSection.appendChild(
            card
        );

    });

}


/**
 * Page load
 */
document.addEventListener(
    "DOMContentLoaded",
    () => {

        checkAuthentication();

        const placeId =
            getPlaceIdFromURL();

        fetchPlaceDetails(
            placeId
        );

    }
);
