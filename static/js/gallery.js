document.addEventListener("DOMContentLoaded", function () {
    // CAROUSEL AUTO-SLIDE
    const carousel = document.querySelector("#galleryCarousel");
    if (carousel) {
        let currentIndex = 0;
        const slides = carousel.querySelectorAll(".carousel-item");
        const totalSlides = slides.length;

        function showSlide(index) {
            slides.forEach((slide, i) => slide.classList.remove("active"));
            if (slides[index]) slides[index].classList.add("active");
        }

        setInterval(() => {
            if (totalSlides > 0) {
                currentIndex = (currentIndex + 1) % totalSlides;
                showSlide(currentIndex);
            }
        }, 5000);
    }

    // MODAL IMAGE
    const modal = document.createElement("div");
    modal.id = "imageModal";
    modal.style.display = "none";
    modal.style.position = "fixed";
    modal.style.top = "0";
    modal.style.left = "0";
    modal.style.width = "100%";
    modal.style.height = "100%";
    modal.style.backgroundColor = "rgba(0,0,0,0.8)";
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
            modalImage.src = img.src;
            modal.style.display = "flex";
        });
    });

    closeButton.addEventListener("click", () => modal.style.display = "none");
    modal.addEventListener("click", e => { if (e.target === modal) modal.style.display = "none"; });
});
