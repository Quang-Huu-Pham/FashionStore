const collapse = document.querySelector('.navbar-toggler.text-center.bg-light.w-100');
const navItem = document.querySelectorAll('.nav-link.text-dark.menu-title');
const content = document.querySelector('.content .row.mt-4').children;

collapse.addEventListener('click', () => {
    navItem.forEach((item) => {
        collapse.innerHTML = `<i class='bx bxs-chevrons-right h4 m-0'></i>`;
        item.lastElementChild.classList.toggle('d-none');
        item.classList.toggle('justify-content-center');
    });
    content[0].classList.toggle('col-xl-1');
    content[1].classList.toggle('col-xl-11');
});

navItem.forEach((itemLink) => {
    console.log(itemLink.classList.contains('active'));
    itemLink.addEventListener('click', () => {
        document.querySelector('.nav-link.text-dark.menu-title.active').classList.remove('active');

        itemLink.classList.add('active');
    });
});
