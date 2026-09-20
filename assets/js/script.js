// CTA SECTION LOAD
const cta = document.querySelector(".cta");

if (cta) {
    const ctaObserver = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("is-visible");

                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.25
        }
    );
    ctaObserver.observe(cta);
}

// VISION SECTION LOAD
const visionSection = document.querySelector(".vision-section");

if (visionSection) {

    const visionHeader =
        visionSection.querySelector(".vision__header");

    const visionItems =
        visionSection.querySelectorAll(".vision__item");


    const visionObserver = new IntersectionObserver(
        (entries, observer) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    if (visionHeader) {
                        visionHeader.classList.add("is-visible");
                    }

                    visionItems.forEach((item) => {
                        item.classList.add("is-visible");
                    });

                    observer.unobserve(entry.target);
                }

            });

        },
        {
            threshold: 0.3
        }
    );


    visionObserver.observe(visionSection);
}

// BLOG SECTION LOAD
document.addEventListener("DOMContentLoaded", () => {
    const blogCards = document.querySelectorAll(".blog-section .blog");
    if (!blogCards.length) return;

    const blogObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    blogObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.2 }
    );

    blogCards.forEach((card) => blogObserver.observe(card));
});

// NAVBAR TOGGLE
document.addEventListener("DOMContentLoaded", () => {

    const navbar = document.querySelector(".navbar");
    const menuBtn = document.querySelector(".navbar__menu");
    const navList = document.querySelector(".navbar__list");

    if (!menuBtn || !navList) return;

    menuBtn.addEventListener("click", () => {
        const isOpen = navList.classList.toggle("is-open");
        menuBtn.classList.toggle("is-active", isOpen);
        menuBtn.setAttribute("aria-expanded", isOpen);
    });

    // close menu by clicking to link
    navList.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navList.classList.remove("is-open");
            menuBtn.classList.remove("is-active");
            menuBtn.setAttribute("aria-expanded", "false");
        });
    });

    // close menu by clicking outside
    document.addEventListener("click", (e) => {
        if (!navbar.contains(e.target)) {
            navList.classList.remove("is-open");
            menuBtn.classList.remove("is-active");
            menuBtn.setAttribute("aria-expanded", "false");
        }
    });

});