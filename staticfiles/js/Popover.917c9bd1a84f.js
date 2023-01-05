var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (el) {
    let opts = {
        placement: 'bottom',
        animation: true,
    };
    if (el.hasAttribute('data-bs-content')) {
        opts.content = document.getElementById(el.getAttribute('data-bs-content')).innerHTML;
        opts.html = true;
    }
    return new bootstrap.Popover(el, opts);
});
