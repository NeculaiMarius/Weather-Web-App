document.addEventListener("DOMContentLoaded", function() {
    const snowContainer = document.querySelector('.snow');
    
    for (let i = 0; i < 100; i++) {
        let snowflake = document.createElement('span');
        snowflake.classList.add('snowflake');
        snowflake.textContent = '*';
        snowflake.style.left = `${Math.random() * 100}vw`;
        snowflake.style.animationDuration = `${Math.random() * 5 + 5}s`; // Viteza mai lentă
        snowflake.style.animationDelay = `${Math.random() * 5}s`; // Întârziere aleatoare
        snowflake.style.fontSize = `${Math.random() * 10 + 10}px`; // Dimensiune aleatoare
        snowContainer.appendChild(snowflake);
    }
});



function animateSnowball() {
    const snowball = document.getElementById('snowball');
    const directions = [
        'moveTopLeftToBottomRight',
        'moveTopRightToBottomLeft',
        'moveBottomLeftToTopRight',
        'moveBottomRightToTopLeft'
    ];
    const randomDirection = directions[Math.floor(Math.random() * directions.length)];

    snowball.style.animation = `${randomDirection} 3s linear`;
    snowball.style.animationPlayState = 'running';

    snowball.addEventListener('animationend', function() {
        snowball.style.animation = 'none';
        setTimeout(animateSnowball, 1000); 
    }, { once: true });
}


window.onload = animateSnowball;