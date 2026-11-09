const carouselTrack = document.querySelector("[data-carousel-track]");

if (carouselTrack) {
    const carousel = carouselTrack.closest(".home-carousel");
    const slides = Array.from(carouselTrack.querySelectorAll(".home-carousel__slide"));
    const dots = Array.from(document.querySelectorAll("[data-carousel-dot]"));
    const previousButton = document.querySelector("[data-carousel-previous]");
    const nextButton = document.querySelector("[data-carousel-next]");
    const status = carousel.querySelector("[data-carousel-status]");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    let activeIndex = 0;
    let rotationTimer;

    const updateControls = () => {
        slides.forEach((slide, slideIndex) => {
            slide.setAttribute("aria-hidden", String(slideIndex !== activeIndex));
        });
        dots.forEach((dot, dotIndex) => {
            if (dotIndex === activeIndex) {
                dot.setAttribute("aria-current", "true");
            } else {
                dot.removeAttribute("aria-current");
            }
        });
        if (status) {
            status.textContent = `${String(activeIndex + 1).padStart(2, "0")} / ${String(slides.length).padStart(2, "0")}`;
        }
    };

    const showSlide = (index) => {
        activeIndex = (index + slides.length) % slides.length;
        carouselTrack.style.transform = `translateX(-${activeIndex * 100}%)`;
        updateControls();
    };

    const updateRotation = () => {
        window.clearInterval(rotationTimer);
        if (
            slides.length > 1
            && !document.hidden
            && !reducedMotion.matches
            && !carousel.contains(document.activeElement)
        ) {
            rotationTimer = window.setInterval(() => showSlide(activeIndex + 1), 1000);
        }
    };

    previousButton?.addEventListener("click", () => showSlide(activeIndex - 1));
    nextButton?.addEventListener("click", () => showSlide(activeIndex + 1));
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => showSlide(index));
    });

    carousel.addEventListener("focusin", updateRotation);
    carousel.addEventListener("focusout", () => window.setTimeout(updateRotation, 0));
    reducedMotion.addEventListener("change", updateRotation);
    document.addEventListener("visibilitychange", updateRotation);

    updateControls();
    updateRotation();
}
