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

    const blogCards =
        document.querySelectorAll(".blog-section .blog");

    if (!blogCards.length) {
        return;
    }


    const blogObserver = new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("is-visible");

                    blogObserver.unobserve(entry.target);
                }

            });

        },
        {
            threshold: 0.2
        }
    );


    blogCards.forEach((card) => {
        blogObserver.observe(card);
    });

});


// SHOPPING CART
const products =
    document.querySelectorAll(".product");


products.forEach((product) => {

    const btnPlus =
        product.querySelector(".btn--plus");

    const btnMin =
        product.querySelector(".btn--min");

    const btnDel =
        product.querySelector(".btn--delete");

    const countElement =
        product.querySelector(".count");


    // اگر اجزای محصول وجود نداشتند،
    // اجرای این محصول را متوقف کن
    if (
        !btnPlus ||
        !btnMin ||
        !btnDel ||
        !countElement
    ) {
        return;
    }


    let count = 1;


    // ADD
    btnPlus.addEventListener("click", () => {

        count++;

        countElement.textContent = count;

    });


    // MIN
    btnMin.addEventListener("click", () => {

        count--;

        if (count <= 0) {

            product.remove();

            return;
        }

        countElement.textContent = count;

    });


    // DELETE
    btnDel.addEventListener("click", () => {

        product.remove();

    });

});


// PROPERTY DETAILS SLIDER
const slider =
    document.querySelector(".property-details-image-box");


if (slider) {

    let isDown = false;
    let startX;
    let scrollLeft;


    // MOUSE DOWN
    slider.addEventListener("mousedown", (e) => {

        isDown = true;

        startX =
            e.pageX - slider.offsetLeft;

        scrollLeft =
            slider.scrollLeft;

        slider.style.cursor =
            "grabbing";

    });


    // MOUSE LEAVE
    slider.addEventListener("mouseleave", () => {

        isDown = false;

        slider.style.cursor =
            "grab";

    });


    // MOUSE UP
    slider.addEventListener("mouseup", () => {

        isDown = false;

        slider.style.cursor =
            "grab";

    });


    // MOUSE MOVE
    slider.addEventListener("mousemove", (e) => {

        if (!isDown) {
            return;
        }

        e.preventDefault();


        const x =
            e.pageX - slider.offsetLeft;


        const walk =
            (x - startX) * 2;


        slider.scrollLeft =
            scrollLeft - walk;

    });

}