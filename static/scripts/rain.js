document.addEventListener("DOMContentLoaded", function() {
    const rainContainer = document.querySelector('.rain');
    
    for (let i = 0; i < 100; i++) {
        let raindrop = document.createElement('div');
        raindrop.classList.add('raindrop');
        raindrop.style.left = `${Math.random() * 100}vw`;
        raindrop.style.animationDuration = `${Math.random() * 1 + 0.5}s`;
        rainContainer.appendChild(raindrop);
    }
});