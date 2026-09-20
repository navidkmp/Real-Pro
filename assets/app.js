const password = document.querySelector("#password");
const passwordToggle = document.querySelector("#passwordToggle");

passwordToggle.addEventListener("click", () => {

    const isPassword = password.type === "password";

    password.type = isPassword ? "text" : "password";

    passwordToggle.innerHTML = isPassword
        ? '<i class="fa-regular fa-eye-slash"></i>'
        : '<i class="fa-regular fa-eye"></i>';
});