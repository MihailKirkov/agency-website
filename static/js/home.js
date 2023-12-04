function observeWithEffect(effect) {
    return new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add(effect);
            } else {
                entry.target.classList.remove(effect);
            }
        });
    });
}

var scaleObserver = observeWithEffect('animation-scale');
var opacityObserver = observeWithEffect('animation-opacity');
var titleObserver = observeWithEffect('animation-title');
var translateXObserver = observeWithEffect('animation-translateX');
var translateXRightObserver = observeWithEffect('animation-translateXRight');

var buttons = document.querySelectorAll('.button-scale');
buttons.forEach((el) => scaleObserver.observe(el));

var title = document.querySelector('.title');
titleObserver.observe(title);

var titleSub = document.querySelector('.title-sub');
opacityObserver.observe(titleSub);

document.querySelectorAll('.services-list a, .services-list button, .services-ul a, .services-title')
    .forEach((el) => translateXObserver.observe(el));

var wrapperContact = document.querySelector('.wrapper-contact');
translateXRightObserver.observe(wrapperContact);

document.querySelectorAll('.icon-element').forEach((el) => {
    opacityObserver.observe(el);
    scaleObserver.observe(el);
});

opacityObserver.observe(document.querySelector('.opacity-effect'));

// document.querySelectorAll('.icon-element-right')
    // .forEach((el) => translateXObserver.observe(el));


document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("wrapper");
    const h2Element = document.getElementById("followCursor");

    container.addEventListener("mousemove", function (event) {
        const containerRect = container.getBoundingClientRect();
        const containerCenterX = containerRect.left + containerRect.width / 2;
        const containerCenterY = containerRect.top + containerRect.height / 2;

        const offsetX = (event.clientX - containerCenterX) * 0.1;
        const offsetY = (event.clientY - containerCenterY) * 0.1;

        h2Element.style.transform = "translate(-50%, -50%) translate(" + offsetX + "px, " + offsetY + "px)";
    });

});

function scrollToDiv(id) {
    console.log('scroll to div')
    const targetDiv = document.getElementById(id);
    console.log(id);
    if (targetDiv) {
        targetDiv.scrollIntoView({
            behavior: "smooth",
            block: "start",
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const animatedDiv = document.getElementById('animatedDiv');
    const h2 = document.querySelector('#animatedDiv h2');

    window.addEventListener('scroll', function() {
        const rect = animatedDiv.getBoundingClientRect();
        const topPosition = rect.top;
        console.log(topPosition, window.innerHeight);

        if (topPosition >= 0 && topPosition <= window.innerHeight-500) {
            // Centered 
            h2.style.top = '50%';
        } else if (topPosition > this.window.innerHeight-500) {
            // Above the viewport
            h2.style.top = '25%';
        } else {
            // Below the viewport
            h2.style.top = '75%';
        }
    });
});