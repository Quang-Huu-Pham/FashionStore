const slideShow = document.querySelector('#slide-show');
const btnPrev = document.querySelector('.show-prev');
const btnNext = document.querySelector('.show-next');
const favorites = document.querySelectorAll('.favorite');

btnNext.addEventListener('click', () => {
    let cards = document.querySelectorAll('.slide-item');
    slideShow.appendChild(cards[0]);
});

btnPrev.addEventListener('click', () => {
    let cards = document.querySelectorAll('.slide-item');
    slideShow.prepend(cards[cards.length - 1]);
});

favorites.forEach((item) => {
    item.addEventListener('click', () => {
        item.classList.toggle = 'primary';
    });
});
