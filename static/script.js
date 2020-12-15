// DOM Elements
const searchInput = document.querySelector(".search-query");
const submitButton = document.querySelector(".submit-btn");

// Event Listeners
submitButton.addEventListener("click", submitQuery);

function submitQuery(e) {
    e.preventDefault();

    const query = searchInput.value;

    if (!query) return;

    const options = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            query
        }),
    };

    fetch("/api/speed", options)
        .then(res => res.json())
        .then(res => {
            console.log(res);
        })
        .catch(err => {
            console.log(err);
        })
}
