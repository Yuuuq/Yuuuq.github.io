const stageShell = document.getElementById("stageShell");
const centerMenuButton = document.getElementById("centerMenuButton");
const dollZone = document.getElementById("dollZone");
const blackHoleCanvas = document.getElementById("blackHoleCanvas");

if (blackHoleCanvas) {
  const context = blackHoleCanvas.getContext("2d");
  let canvasWidth = 0;
  let canvasHeight = 0;
  let pixelRatio = 1;
  let stars = [];

  const makeStars = () => {
    const count = Math.round(Math.min(260, Math.max(140, canvasWidth / 5)));
    stars = Array.from({ length: count }, () => ({
      x: Math.random() * canvasWidth,
      y: Math.random() * canvasHeight,
      radius: Math.random() * 1.35 + 0.25,
      alpha: Math.random() * 0.7 + 0.18,
      twinkle: Math.random() * Math.PI * 2,
    }));
  };

  const resizeBlackHole = () => {
    pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
    canvasWidth = blackHoleCanvas.clientWidth;
    canvasHeight = blackHoleCanvas.clientHeight;
    blackHoleCanvas.width = Math.floor(canvasWidth * pixelRatio);
    blackHoleCanvas.height = Math.floor(canvasHeight * pixelRatio);
    context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
    makeStars();
  };

  const drawStars = (time) => {
    for (const star of stars) {
      const pulse = 0.72 + Math.sin(time * 0.0016 + star.twinkle) * 0.28;
      context.beginPath();
      context.fillStyle = `rgba(255, 246, 225, ${star.alpha * pulse})`;
      context.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
      context.fill();
    }
  };

  const drawAccretionDisk = (centerX, centerY, horizon, time, frontOnly) => {
    context.save();
    context.translate(centerX, centerY);
    context.rotate(-0.11);
    context.scale(1, 0.34);
    context.lineCap = "round";

    const ringCount = frontOnly ? 26 : 42;
    for (let index = 0; index < ringCount; index += 1) {
      const radius = horizon * (1.12 + index * 0.055);
      const drift = time * 0.00045 + index * 0.21;
      const alpha = frontOnly ? 0.18 - index * 0.003 : 0.15 - index * 0.0022;
      const glow = Math.max(0.025, alpha);
      const hue = 31 + Math.sin(index * 0.5 + time * 0.0004) * 8;
      context.beginPath();
      context.shadowColor = `hsla(${hue}, 100%, 62%, ${glow})`;
      context.shadowBlur = frontOnly ? 22 : 18;
      context.strokeStyle = `hsla(${hue}, 100%, ${frontOnly ? 64 : 56}%, ${glow})`;
      context.lineWidth = Math.max(1.2, horizon * (0.018 + index * 0.0009));

      if (frontOnly) {
        context.arc(0, 0, radius, 0.03 * Math.PI + drift, 0.97 * Math.PI + drift);
      } else {
        context.arc(0, 0, radius, drift, Math.PI * 2 + drift);
      }

      context.stroke();
    }

    context.restore();
  };

  const drawLensedSheet = (centerX, centerY, horizon, time, frontOnly) => {
    context.save();
    context.translate(centerX, centerY);
    context.rotate(-0.08);
    context.lineCap = "round";

    if (!frontOnly) {
      context.save();
      context.scale(1, 0.48);
      for (let index = 0; index < 10; index += 1) {
        const radius = horizon * (1.12 + index * 0.17);
        const alpha = Math.max(0.045, 0.22 - index * 0.015);
        context.beginPath();
        context.shadowColor = `rgba(255, 133, 35, ${alpha})`;
        context.shadowBlur = horizon * 0.34;
        context.strokeStyle = `rgba(255, ${146 + index * 8}, 56, ${alpha})`;
        context.lineWidth = horizon * (0.07 - index * 0.003);
        context.arc(0, 0, radius, Math.PI * 1.04 + time * 0.00008, Math.PI * 1.96 + time * 0.00008);
        context.stroke();
      }
      context.restore();
      context.restore();
      return;
    }

    const plume = context.createLinearGradient(-horizon * 4.8, 0, horizon * 4.2, 0);
    plume.addColorStop(0, "rgba(106, 147, 255, 0)");
    plume.addColorStop(0.16, "rgba(170, 202, 255, 0.3)");
    plume.addColorStop(0.34, "rgba(255, 255, 246, 0.82)");
    plume.addColorStop(0.52, "rgba(255, 236, 184, 0.98)");
    plume.addColorStop(0.72, "rgba(255, 151, 43, 0.82)");
    plume.addColorStop(1, "rgba(143, 48, 8, 0)");

    context.shadowColor = "rgba(255, 202, 112, 0.72)";
    context.shadowBlur = horizon * 0.45;
    context.strokeStyle = plume;
    context.lineWidth = horizon * 0.33;
    context.beginPath();
    context.moveTo(-horizon * 4.7, horizon * 0.16);
    context.bezierCurveTo(-horizon * 2.25, -horizon * 0.22, horizon * 1.7, -horizon * 0.12, horizon * 4.55, -horizon * 0.5);
    context.stroke();

    context.shadowColor = "rgba(255, 255, 245, 0.78)";
    context.shadowBlur = horizon * 0.2;
    context.strokeStyle = "rgba(255, 255, 244, 0.9)";
    context.lineWidth = horizon * 0.08;
    context.beginPath();
    context.moveTo(-horizon * 4.2, horizon * 0.07);
    context.bezierCurveTo(-horizon * 2.0, -horizon * 0.12, horizon * 1.45, -horizon * 0.08, horizon * 3.4, -horizon * 0.33);
    context.stroke();

    const tail = context.createLinearGradient(horizon * 0.7, 0, horizon * 4.8, 0);
    tail.addColorStop(0, "rgba(255, 248, 214, 0.55)");
    tail.addColorStop(0.36, "rgba(255, 147, 37, 0.36)");
    tail.addColorStop(1, "rgba(104, 25, 4, 0)");
    context.fillStyle = tail;
    context.beginPath();
    context.moveTo(horizon * 0.9, -horizon * 0.42);
    context.bezierCurveTo(horizon * 2.1, -horizon * 1.2, horizon * 3.7, -horizon * 1.05, horizon * 5.0, -horizon * 0.78);
    context.bezierCurveTo(horizon * 3.8, -horizon * 0.18, horizon * 2.3, horizon * 0.15, horizon * 0.9, horizon * 0.08);
    context.closePath();
    context.fill();

    context.restore();
  };

  const drawEventHorizon = (centerX, centerY, horizon) => {
    const lensGlow = context.createRadialGradient(centerX, centerY, horizon * 0.84, centerX, centerY, horizon * 2.12);
    lensGlow.addColorStop(0, "rgba(255, 236, 187, 0.52)");
    lensGlow.addColorStop(0.36, "rgba(255, 170, 55, 0.26)");
    lensGlow.addColorStop(0.74, "rgba(109, 58, 255, 0.08)");
    lensGlow.addColorStop(1, "rgba(0, 0, 0, 0)");
    context.fillStyle = lensGlow;
    context.beginPath();
    context.arc(centerX, centerY, horizon * 2.2, 0, Math.PI * 2);
    context.fill();

    context.save();
    context.shadowColor = "rgba(255, 207, 118, 0.48)";
    context.shadowBlur = 22;
    context.strokeStyle = "rgba(255, 231, 177, 0.9)";
    context.lineWidth = 1.2;
    context.beginPath();
    context.arc(centerX, centerY, horizon * 1.05, 0, Math.PI * 2);
    context.stroke();
    context.restore();

    const eventGradient = context.createRadialGradient(centerX - horizon * 0.28, centerY - horizon * 0.32, horizon * 0.08, centerX, centerY, horizon);
    eventGradient.addColorStop(0, "#101015");
    eventGradient.addColorStop(0.42, "#030306");
    eventGradient.addColorStop(1, "#000000");
    context.fillStyle = eventGradient;
    context.beginPath();
    context.arc(centerX, centerY, horizon, 0, Math.PI * 2);
    context.fill();
  };

  const drawBlackHole = (time = 0) => {
    if (!context || !canvasWidth || !canvasHeight) {
      requestAnimationFrame(drawBlackHole);
      return;
    }

    const centerX = canvasWidth * 0.5;
    const centerY = canvasHeight * 0.5;
    const horizon = Math.max(68, Math.min(canvasWidth, canvasHeight) * 0.15);

    context.clearRect(0, 0, canvasWidth, canvasHeight);
    const backdrop = context.createRadialGradient(centerX, centerY, horizon * 0.2, centerX, centerY, Math.max(canvasWidth, canvasHeight) * 0.72);
    backdrop.addColorStop(0, "#050407");
    backdrop.addColorStop(0.48, "#02030a");
    backdrop.addColorStop(1, "#000106");
    context.fillStyle = backdrop;
    context.fillRect(0, 0, canvasWidth, canvasHeight);

    drawStars(time);
    drawAccretionDisk(centerX, centerY, horizon, time, false);
    drawLensedSheet(centerX, centerY, horizon, time, false);
    drawEventHorizon(centerX, centerY, horizon);
    drawLensedSheet(centerX, centerY, horizon, time, true);

    requestAnimationFrame(drawBlackHole);
  };

  window.addEventListener("resize", resizeBlackHole);
  resizeBlackHole();
  requestAnimationFrame(drawBlackHole);
}

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
