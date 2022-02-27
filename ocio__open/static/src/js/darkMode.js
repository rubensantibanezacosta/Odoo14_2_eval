
window.addEventListener("load", () => {
    const targetNode = document.querySelector("body");
    const config = { childList: true, subtree: true };
    updateLocalStorageDarkmode();

    const callback = function (mutationsList, observer) {
        for (let mutation of mutationsList) {
            if (mutation.type === 'childList') {


/* if(document.getElementsByName("dark_mode_boolean").length>0){
    console.log(document.getElementsByName("dark_mode_boolean")[0].firstChild.checked)
}
 */
                    
                try {
                    if (document.getElementsByName("dark_mode_boolean").length > 0) {
                        document.getElementsByName("dark_mode_boolean")[0].firstChild.addEventListener("change", () => {
                            
                            if (document.getElementsByName("dark_mode_boolean")[0].firstChild.checked) {
                                
                                activateLocalStorageDarkMode()
                                updateLocalStorageDarkmode()
                                console.log("darkMode");

                            } else {
                                deactivateLocalStorageDarkMode()
                                updateLocalStorageDarkmode()
                                console.log("not darkmode");
                            }
                        }

                        )
                    }
                } catch (error) {

                }
            }
        }
    };

    const observer = new MutationObserver(callback);
    observer.observe(targetNode, config);

}
)
function updateLocalStorageDarkmode() {

    if ((localStorage.getItem("DarkMode"))=="true") {
        document.body.classList.add("dark");
        console.log("adding")
    } else {
        document.body.classList.remove("dark");
        document.body.classList.remove("dark");
        document.body.classList.remove("dark");
        document.body.classList.remove("dark");
        console.log("removing")
    }
}

function activateLocalStorageDarkMode() {
    localStorage.setItem("DarkMode", true);
}

function deactivateLocalStorageDarkMode() {
    localStorage.setItem("DarkMode", false);
}