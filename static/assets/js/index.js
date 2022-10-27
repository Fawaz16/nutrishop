
const nav = document.getElementsByTagName("nav")[0];
const nightToggler = document.getElementById("night-toggler");

//Check the theme state, if the theme doesn't exist it creates a default state as light
function checkThemeState() {
    if (window.localStorage.getItem("theme") == null) {
        window.localStorage.setItem("theme", "light");
    }
    return window.localStorage.getItem("theme");
}

//save state, so when the DOMContent loads again, it would retrieve the save state
function saveState(theme) {
    window.localStorage.setItem("theme", theme);
}

//Change the state from the saved state, also it could easily be explained as changing the default theme style
function changeThemeState(currentTheme) {
    saveState(currentTheme);
    currentTheme = checkThemeState();
    if (currentTheme == "light") {
        if (nightToggler.classList.contains('bi-toggle-on')) {
            nightToggler.click();
        }
    } else if (currentTheme == "dark") {
        nightToggler.click();
    }
}

//Load the saved state on DOMContentLoaded
window.addEventListener("DOMContentLoaded", () => {
    let currentTheme = checkThemeState();
    changeThemeState(currentTheme);
});



