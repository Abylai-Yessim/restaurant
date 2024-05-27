document.addEventListener('DOMContentLoaded', function () {
    const categoryButtons = document.querySelectorAll('.category-btn');
    categoryButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const categoryId = button.getAttribute('data-category-id');
            const categoryElement = document.getElementById('category-' + categoryId);
            if (categoryElement) {
                window.scrollTo({
                    top: categoryElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});
