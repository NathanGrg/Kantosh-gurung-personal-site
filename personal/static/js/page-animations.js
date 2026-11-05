(() => {
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    if (reducedMotion.matches) {
        return;
    }

    const targets = document.querySelectorAll([
        ".program-page__heading",
        ".program-page__section-heading",
        ".program-card",
        ".dental-info-page__heading",
        ".dental-info-card",
        ".contact-page__heading",
        ".contact-card",
        ".news-heading",
        ".news-disclaimer",
        ".news-feature",
        ".news-latest-heading",
        ".news-card",
        ".team-page > .page-section__heading",
        ".team-page > .page-section__intro",
        ".team-page > p",
        ".team-section",
        ".team-card",
    ].join(","));

    if (!targets.length) {
        return;
    }

    const animateTarget = (target, index) => {
        const delay = (index % 5) * 85;

        if (typeof window.anime === "function") {
            window.anime({
                targets: target,
                opacity: [0, 1],
                translateY: [24, 0],
                duration: 720,
                delay,
                easing: "easeOutCubic",
                complete: () => {
                    target.style.removeProperty("opacity");
                    target.style.removeProperty("transform");
                },
            });
            return;
        }

        if (typeof target.animate === "function") {
            const animation = target.animate(
                [
                    { opacity: 0, transform: "translateY(24px)" },
                    { opacity: 1, transform: "translateY(0)" },
                ],
                {
                    duration: 720,
                    delay,
                    easing: "cubic-bezier(0.2, 0.75, 0.25, 1)",
                    fill: "both",
                },
            );
            animation.onfinish = () => {
                target.style.removeProperty("opacity");
                target.style.removeProperty("transform");
                animation.cancel();
            };
            return;
        }

        target.style.removeProperty("opacity");
        target.style.removeProperty("transform");
    };

    targets.forEach((target) => {
        target.style.opacity = "0";
        target.style.transform = "translateY(24px)";
    });

    if (!("IntersectionObserver" in window)) {
        targets.forEach(animateTarget);
        return;
    }

    const observer = new IntersectionObserver((entries, currentObserver) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            const index = Array.prototype.indexOf.call(targets, entry.target);
            animateTarget(entry.target, index);
            currentObserver.unobserve(entry.target);
        });
    }, {
        threshold: 0.12,
        rootMargin: "0px 0px -24px 0px",
    });

    targets.forEach((target) => observer.observe(target));
})();
