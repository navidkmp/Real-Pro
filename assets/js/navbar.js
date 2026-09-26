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

    // Close menu by clicking link
    navList.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navList.classList.remove("is-open");
            menuBtn.classList.remove("is-active");
            menuBtn.setAttribute("aria-expanded", "false");
        });
    });

    // Close menu by clicking outside
    document.addEventListener("click", (e) => {
        if (!navbar.contains(e.target)) {
            navList.classList.remove("is-open");
            menuBtn.classList.remove("is-active");
            menuBtn.setAttribute("aria-expanded", "false");
        }
    });

});


// ------------------------------------------------------------------------------------------------

// LOGOUT ALERT

const logOutBtn = document.querySelector(".btn--logout");

if (logOutBtn) {
    logOutBtn.addEventListener("click", function () {
        alert("you logged out");
    });
}


// ------------------------------------------------------------------------------------------------

// PRELOADER

const preloader = document.querySelector("#preloader");
const percentage = document.querySelector("#loaderPercentage");
const progressCircle = document.querySelector(
    ".preloader__circle-progress"
);

let progress = 0;

const circumference = 2 * Math.PI * 54;


// Circle setup
if (progressCircle) {
    progressCircle.style.strokeDasharray = circumference;
    progressCircle.style.strokeDashoffset = circumference;
}


// Update progress
function updateProgress(value) {

    if (percentage) {
        percentage.textContent = Math.floor(value);
    }

    if (progressCircle) {

        const offset =
            circumference -
            (value / 100) * circumference;

        progressCircle.style.strokeDashoffset = offset;
    }
}


// Loading animation
const loadingAnimation = setInterval(() => {

    progress += 5;

    if (progress >= 90) {
        progress = 90;
        clearInterval(loadingAnimation);
    }

    updateProgress(progress);

}, 40);


// When page is completely loaded
window.addEventListener("load", () => {

    clearInterval(loadingAnimation);

    const finishAnimation = setInterval(() => {

        progress += 5;

        if (progress >= 100) {

            progress = 100;

            clearInterval(finishAnimation);

            updateProgress(100);

            setTimeout(() => {

                if (preloader) {

                    preloader.style.opacity = "0";
                    preloader.style.visibility = "hidden";
                    preloader.style.pointerEvents = "none";
                }

                document.body.classList.add("page-loaded");

                setTimeout(() => {

                    if (preloader) {
                        preloader.remove();
                    }

                }, 500);

            }, 150);
        }

        updateProgress(progress);

    }, 20);

});