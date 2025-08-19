// Highlight active dot on scroll
const sections = document.querySelectorAll('.panel');
const dots = document.querySelectorAll('.dot');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      dots.forEach(dot => dot.classList.remove('active'));
      const activeDot = document.querySelector(`.dots a[href="#${entry.target.id}"]`);
      if (activeDot) activeDot.classList.add('active');
      // add fade effect
      entry.target.classList.add('visible');
    } else {
      entry.target.classList.remove('visible');
    }
  });
}, {
  threshold: 0.5
});

sections.forEach(section => observer.observe(section));
