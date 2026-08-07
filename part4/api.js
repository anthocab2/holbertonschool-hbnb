/**
 * API configuration
 */


const API_URL =
"http://127.0.0.1:5000/api/v1";



/**
 * Get places from API
 *
 * @param {string} token JWT token
 * @returns {Array}
 */

async function getPlaces(token) {


    const headers = {
        "Content-Type": "application/json"
    };


    if (token) {

        headers["Authorization"] =
        `Bearer ${token}`;

    }



    const response = await fetch(
        `${API_URL}/places/`,
        {

            method:"GET",

            headers:headers

        }

    );



    if (!response.ok) {

        throw new Error(
        "Failed to fetch places"
        );

    }


    return await response.json();


}
