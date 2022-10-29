//When the night toggler btn is clicked dark mode becomes active

//Since you're in dark theme it changes black to white and white theme changes white to black
nightToggler.onclick = () => {
    const changeBlackToWhite = document.querySelectorAll(".changeBlackToWhite");
    const changeWhiteToBlack = document.querySelectorAll(".changeWhiteToBlack");
    const btnThemeControl = document.querySelectorAll(".btn-theme-control");
    const serviceContact = document.querySelector(".service-contact");

    nightToggler.classList.toggle("bi-toggle-on");
    //dark theme
    if (nightToggler.classList.contains("bi-toggle-on")) {
        nav.style.backgroundColor = "var(--dark-color)";
        document.body.style.backgroundColor = "var(--dark-color)";
        serviceContact.style.backgroundColor = "var(--light-color)";
        serviceContact.style.color = "var(--dark-color)";

        changeBlackToWhite.forEach((element) => {
            element.classList.toggle("changeBlackToWhite");
            element.classList.toggle("changeWhiteToBlack");
        });

        btnThemeControl.forEach((element)=>{
            element.style.backgroundColor = "var(--light-color)";
            element.style.color = "var(--dark-color)";
        });

        saveState("dark");
    }
    //light theme
    else {
        nav.style.backgroundColor = "var(--light-header-color)";
        document.body.style.backgroundColor = "var(--light-color)";
        serviceContact.style.backgroundColor = "var(--light-text-carousel-color)";
        serviceContact.style.color = "var(--dark-color)";

        changeWhiteToBlack.forEach((element) => {
            element.classList.toggle("changeWhiteToBlack");
            element.classList.toggle("changeBlackToWhite");
        });

        btnThemeControl.forEach((element)=>{
            element.style.backgroundColor = "var(--light-header-color)";
            element.style.color = "var(--light-color)";
        });

        saveState("light");

    }
}

