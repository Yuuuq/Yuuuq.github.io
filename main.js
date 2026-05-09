const stageShell = document.getElementById("stageShell");
const centerMenuButton = document.getElementById("centerMenuButton");
const dollZone = document.getElementById("dollZone");

if (stageShell && centerMenuButton) {
  const setMenuOpen = (isOpen) => {
    stageShell.classList.toggle("menu-open", isOpen);
    centerMenuButton.setAttribute("aria-expanded", String(isOpen));
  };

  centerMenuButton.addEventListener("click", (event) => {
    event.stopPropagation();
    setMenuOpen(!stageShell.classList.contains("menu-open"));
  });

  document.addEventListener("click", (event) => {
    if (dollZone && !dollZone.contains(event.target)) {
      setMenuOpen(false);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      setMenuOpen(false);
    }
  });
}

document.querySelectorAll(".cv-document img").forEach((image) => {
  const showFallback = () => {
    image.hidden = true;
    const fallback = image.nextElementSibling;
    if (fallback) {
      fallback.hidden = false;
    }
  };

  image.addEventListener("error", showFallback);

  if (image.complete && image.naturalWidth === 0) {
    showFallback();
  }
});
