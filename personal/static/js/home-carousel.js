const carouselTrack = document.querySelector("[data-carousel-track]");

if (carouselTrack) {
    const carousel = carouselTrack.closest(".home-carousel");
    const slides = Array.from(carouselTrack.querySelectorAll(".home-carousel__slide"));
    const dots = Array.from(document.querySelectorAll("[data-carousel-dot]"));
    const previousButton = document.querySelector("[data-carousel-previous]");
    const nextButton = document.querySelector("[data-carousel-next]");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    let activeIndex = 0;
    let rotationTimer;

    const showSlide = (index) => {
        activeIndex = (index + slides.length) % slides.length;
        carouselTrack.scrollTo({
                left: slides[activeIndex].offsetLeft,
                behavior: reducedMotion.matches ? "auto" : "smooth",
        });
        dots.forEach((dot, dotIndex) => {
                if (dotIndex === activeIndex) {
                dot.setAttribute("aria-current", "true");
            } else {
                dot.removeAttribute("aria-current");
            }
        });
    };

    const updateRotation = () => {
        window.clearInterval(rotationTimer);
        if (!reducedMotion.matches && !carousel.matches(":hover") && !carousel.contains(document.activeElement)) {
            rotationTimer = window.setInterval(() => showSlide(activeIndex + 1), 5000);
        }
    };

    previousButton?.addEventListener("click", () => showSlide(activeIndex - 1));
    nextButton?.addEventListener("click", () => showSlide(activeIndex + 1));
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => showSlide(index));
    });

    carousel.addEventListener("mouseenter", updateRotation);
    carousel.addEventListener("mouseleave", updateRotation);
    carousel.addEventListener("focusin", updateRotation);
    carousel.addEventListener("focusout", () => window.setTimeout(updateRotation, 0));
    reducedMotion.addEventListener("change", (event) => {
        if (event.matches) {
            isPaused = true;
        }
        updateRotation();
    });

    let scrollTimer;
    carouselTrack.addEventListener("scroll", () => {
        window.clearTimeout(scrollTimer);
        scrollTimer = window.setTimeout(() => {
            const nearestIndex = slides.reduce((nearest, slide, index) => {
                const nearestDistance = Math.abs(slides[nearest].offsetLeft - carouselTrack.scrollLeft);
                const slideDistance = Math.abs(slide.offsetLeft - carouselTrack.scrollLeft);
                return slideDistance < nearestDistance ? index : nearest;
            }, 0);
            activeIndex = nearestIndex;
            dots.forEach((dot, dotIndex) => {
                if (dotIndex === activeIndex) {
                    dot.setAttribute("aria-current", "true");
                } else {
                    dot.removeAttribute("aria-current");
                }
            });
        }, 80);
    });

    updateRotation();
}
