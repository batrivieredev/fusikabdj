document.addEventListener("DOMContentLoaded", function () {
    // Initialize the carousel
    const carousel = document.querySelector("#galleryCarousel");
    if (carousel) {
        let currentIndex = 0;
        const slides = carousel.querySelectorAll(".carousel-item");
        const totalSlides = slides.length;

        // Function to show a specific slide
        function showSlide(index) {
            slides.forEach((slide, i) => {
                slide.classList.remove("active");
                if (i === index) {
                    slide.classList.add("active");
                }
            });
        }

        // Auto-slide functionality
        setInterval(() => {
            currentIndex = (currentIndex + 1) % totalSlides;
            showSlide(currentIndex);
        }, 5000); // Change slide every 5 seconds
    }
});
