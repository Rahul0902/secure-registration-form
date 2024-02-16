//Fade out the alert message when close button is selected
document.addEventListener("DOMContentLoaded", function() {
    var closeButtons = document.querySelectorAll(".close");
    closeButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var alert = this.parentElement;
            alert.style.opacity = 0;
            setTimeout(function() {
                alert.style.display = "none";
            }, 5000); // Adjust the duration of the fade-out effect
        });
    });
});
