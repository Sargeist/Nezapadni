// Smooth fade for messages
document.addEventListener("DOMContentLoaded", () => {
    const msgs = document.querySelectorAll(".messagelist li");
    msgs.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = "0";
        }, 3500);
    });
});
