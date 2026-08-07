/**
 * Get cookie value by name
 */
function getCookie(name) {

    const cookies = document.cookie.split(';');

    for (let cookie of cookies) {

        const [key, value] =
            cookie.trim().split('=');

        if (key === name) {
            return value;
        }
    }

    return null;
}


/**
 * Verify authentication
 */
function checkAuthentication() {

    const token = getCookie('token');

    if (!token) {

        window.location.href =
            'index.html';

        return null;
    }

    return token;
}


/**
 * Get place id from URL
 */
function getPlaceIdFromURL() {

    const params =
        new URLSearchParams(
            window.location.search
        );

    return params.get('id');
}


/**
 * Submit review to API
 */
async function submitReview(
    token,
    placeId,
    reviewText
) {

    try {

        const response =
            await fetch(
                'http://127.0.0.1:5000/api/v1/reviews/',
                {

                    method: 'POST',

                    headers: {

                        'Content-Type':
                            'application/json',

                        'Authorization':
                            `Bearer ${token}`

                    },

                    body: JSON.stringify({

                        place_id: placeId,

                        text: reviewText

                    })

                }
            );

        return response;

    } catch (error) {

        console.error(error);

        throw error;
    }
}


/**
 * Page loaded
 */
document.addEventListener(
    'DOMContentLoaded',
    () => {

        const token =
            checkAuthentication();

        const placeId =
            getPlaceIdFromURL();

        const reviewForm =
            document.getElementById(
                'review-form'
            );

        const message =
            document.getElementById(
                'message'
            );

        if (reviewForm) {

            reviewForm.addEventListener(
                'submit',
                async (event) => {

                    event.preventDefault();

                    const reviewText =
                        document.getElementById(
                            'review'
                        ).value;

                    try {

                        const response =
                            await submitReview(
                                token,
                                placeId,
                                reviewText
                            );

                        if (response.ok) {

                            message.textContent =
                                'Review submitted successfully!';

                            reviewForm.reset();

                        } else {

                            message.textContent =
                                'Failed to submit review.';

                        }

                    } catch (error) {

                        message.textContent =
                            'An error occurred while submitting the review.';
                    }

                }
            );

        }

    }
);
