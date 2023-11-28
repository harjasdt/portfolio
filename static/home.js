const observer = new IntersectionObserver((entries) => {
	entries.forEach((entry) => {
		console.log(entry.target.getAttribute("data-animation"));

		const animation = entry.target.getAttribute("data-animation");

		if (entry.isIntersecting) {
			entry.target.classList.add("animated", `${animation}`);
		} else {
			entry.target.classList.remove("animated", `${animation}`);
		}
	});
});

const animatedEls = document.querySelectorAll("[data-animation]");
animatedEls.forEach((el) => observer.observe(el));
