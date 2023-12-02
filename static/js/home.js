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
    