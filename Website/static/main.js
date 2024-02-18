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

var alerts = document.querySelectorAll(".alert");
alerts.forEach(function(alert) {
    setTimeout(function() {
        if (alert.style.opacity !== "0") {
            alert.style.opacity = 0;
            setTimeout(function() {
                alert.style.display = "none";
            }, 500); // Adjust the duration of the fade-out effect
        }
    }, 3000); // Auto fade out after 3 seconds
});
