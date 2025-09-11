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

// Full-size image modal functionality
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.createElement("div");
    modal.id = "imageModal";
    modal.style.display = "none";
    modal.style.position = "fixed";
    modal.style.top = "0";
    modal.style.left = "0";
    modal.style.width = "100%";
    modal.style.height = "100%";
    modal.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
    modal.style.zIndex = "1000";
    modal.style.justifyContent = "center";
    modal.style.alignItems = "center";

    const modalImage = document.createElement("img");
    modalImage.id = "modalImage";
    modalImage.style.maxWidth = "90%";
    modalImage.style.maxHeight = "90%";
    modal.appendChild(modalImage);

    const closeButton = document.createElement("span");
    closeButton.innerHTML = "&times;";
    closeButton.style.position = "absolute";
    closeButton.style.top = "10px";
    closeButton.style.right = "20px";
    closeButton.style.fontSize = "30px";
    closeButton.style.color = "#fff";
    closeButton.style.cursor = "pointer";
    modal.appendChild(closeButton);

    document.body.appendChild(modal);

    document.querySelectorAll(".carousel-item img, .thumbnail img").forEach(img => {
        img.addEventListener("click", () => {
            console.log("Image clicked:", img.src); // Debug log
            modalImage.src = img.src;
            console.log("Modal image source set to:", modalImage.src); // Debug log
            modal.style.display = "flex";
            console.log("Modal display set to flex"); // Debug log
        });
    });

    closeButton.addEventListener("click", () => {
        modal.style.display = "none";
    });

    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});
