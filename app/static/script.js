// *DARK MODE JAVASCRIPT*
function darkMode() {
    var element = document.body;
    const modeBtn = document.getElementsByClassName('mode');
    element.classList.toggle("dark-mode");
}

// *SEARCH BAR JAVASCRIPT*
function searchBar() {
    let searchInput = document.querySelector('.search-bar');
    let images = document.getElementsByClassName('card');
    let searchKeywords = searchInput.value.toLowerCase().split(' ');


    for (var i = 0; i < images.length; i++) {
        let searchVal = images[i].getAttribute("data-alt").toLowerCase();
        let shouldDisplay = searchKeywords.some(keyword => searchVal.includes(keyword));
        images[i].style.display = shouldDisplay ? "block" : "none";
    }
}

// *IMAGE PREVIEW MODAL JAVASCRIPT*
document.addEventListener('DOMContentLoaded', function () {
    // Get references to the modal and image elements
    const imageModal = document.getElementById('imageModal');
    const modalImage = document.getElementById('modalImage');

    // Add a click event listener to all the expand icons
    const expandIcons = document.querySelectorAll('i.fa-expand');
    expandIcons.forEach(icon => {
        icon.addEventListener('click', function () {
            const imageSrc = this.getAttribute('data-image-src');
            modalImage.src = imageSrc;
        });
    });

    // Hide the modal when the close button is clicked
    const closeButton = document.querySelector('button[data-bs-dismiss="modal"]');
    closeButton.addEventListener('click', function () {
        imageModal.style.display = 'none';
    });
});