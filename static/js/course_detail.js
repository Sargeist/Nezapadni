/* ============================================================
   TABS — переключение Overview / Curriculum / Instructor / Reviews
============================================================ */
document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        const tab = btn.dataset.tab;

        document.querySelectorAll(".tab-panel").forEach(panel => {
            panel.classList.remove("active");
            if (panel.id === tab) panel.classList.add("active");
        });
    });
});


/* ============================================================
   CURRICULUM ACCORDION
============================================================ */
document.querySelectorAll(".curriculum-header").forEach(header => {
    header.addEventListener("click", () => {
        header.parentElement.classList.toggle("expanded");
    });
});


/* ============================================================
   ⭐ FIXED STAR RATING — hover работает отдельно, click фиксирует
============================================================ */

const ratingStars = document.querySelectorAll("#ratingStars span");
const ratingValue = document.getElementById("ratingValue");

if (ratingStars.length > 0) {
    let saved = 0; // выбранный рейтинг

    ratingStars.forEach(star => {

        // --- Hover ---
        star.addEventListener("mouseover", () => {
            const value = parseInt(star.dataset.value);

            ratingStars.forEach(s => {
                s.classList.toggle("active", parseInt(s.dataset.value) <= value);
            });
        });

        // --- Убираем hover, возвращаем выбранный рейтинг ---
        star.addEventListener("mouseout", () => {
            ratingStars.forEach(s => {
                s.classList.remove("active");
                s.classList.toggle("selected", parseInt(s.dataset.value) <= saved);
            });
        });

        // --- Click — сохраняем рейтинг ---
        star.addEventListener("click", () => {
            saved = parseInt(star.dataset.value);
            ratingValue.value = saved;

            ratingStars.forEach(s => {
                s.classList.remove("active");
                s.classList.toggle("selected", parseInt(s.dataset.value) <= saved);
            });
        });

    });
}



/* ============================================================
   PREMIUM LOCK
============================================================ */
document.querySelectorAll(".lesson-item.locked").forEach(item => {
    item.addEventListener("click", e => {
        e.preventDefault();

        item.style.transform = "translateX(-4px)";
        setTimeout(() => (item.style.transform = "translateX(0)"), 140);
    });
});
