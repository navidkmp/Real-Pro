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

// SHOPPING CART
const products = document.querySelectorAll('.product');


products.forEach(function (product) {
    const btnPlus = product.querySelector('.btn--plus');
    const btnMin = product.querySelector('.btn--min');
    const btnDel = product.querySelector('.btn--delete');
    const countElement = product.querySelector('.count');

    let count = 1;

    // add
    btnPlus.addEventListener('click', function () {
        count++
        countElement.textContent = count;
    })

    // min 
    btnMin.addEventListener('click', function () {
        count--
        countElement.textContent = count;
        if (count === 0) {
            product.remove();
        }
    })

    // delete
    btnDel.addEventListener('click', function () {
        product.remove();
    })
})

// PROPERTY DETAILS SLIDER 
const slider = document.querySelector('.property-details-image-box');

let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', function (e) {
    isDown = true;

    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;

    slider.style.cursor = 'grabbing';
});

slider.addEventListener('mouseleave', function () {
    isDown = false;
    slider.style.cursor = 'grab';
});

slider.addEventListener('mouseup', function () {
    isDown = false;
    slider.style.cursor = 'grab';
});

slider.addEventListener('mousemove', function (e) {
    if (!isDown) return;

    e.preventDefault();

    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) * 2;

    slider.scrollLeft = scrollLeft - walk;
});

