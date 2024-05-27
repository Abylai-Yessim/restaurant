document.querySelectorAll('.category-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const categoryId = btn.getAttribute('data-category');
        document.querySelectorAll('.menu-category').forEach(cat => {
            cat.style.display = 'none';
        });
        document.getElementById(`category-${categoryId}`).style.display = 'block';
    });
});

function moveComments(direction) {
    const container = document.querySelector('.comments');
    const scrollAmount = 300;
    const step = direction === 'left' ? -scrollAmount : scrollAmount;
    container.scrollLeft += step;
}

function checkCommentsOverflow() {
    const container = document.querySelector('.comments');
    const btnContainer = document.querySelector('.btn-container');

    // Проверяем, переполняется ли контейнер
    if (container.scrollWidth > container.clientWidth) {
        btnContainer.style.display = 'block'; // Показываем кнопки
    } else {
        btnContainer.style.display = 'none'; // Скрываем кнопки
    }
}

// Вызываем функцию при загрузке страницы
document.addEventListener('DOMContentLoaded', checkCommentsOverflow);

// Повторно проверяем при изменении размера окна
window.addEventListener('resize', checkCommentsOverflow);

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.header');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.remove('transparent');
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
            header.classList.add('transparent');
        }
    });
});

var menuToggleIcon = document.getElementById('menu-toggle');

menuToggleIcon.addEventListener('click', function(event) {
    var sideMenu = document.getElementById('side-menu');
    var overlay = document.getElementById('overlay');
    sideMenu.classList.toggle('open');
    overlay.classList.toggle('show');
    menuToggleIcon.classList.toggle('bi-list');
    menuToggleIcon.classList.toggle('bi-x');
    event.stopPropagation();
});

document.addEventListener('click', function(event) {
    var sideMenu = document.getElementById('side-menu');
    var overlay = document.getElementById('overlay');
    var isClickInside = sideMenu.contains(event.target);

    if (!isClickInside) {
        sideMenu.classList.remove('open');
        overlay.classList.remove('show');
        if (menuToggleIcon.classList.contains('bi-x')) {
            menuToggleIcon.classList.remove('bi-x');
            menuToggleIcon.classList.add('bi-list');
        }
    }
});

document.getElementById('side-menu').addEventListener('click', function(event) {
    event.stopPropagation();
});

document.getElementById('overlay').addEventListener('click', function() {
    var sideMenu = document.getElementById('side-menu');
    var overlay = document.getElementById('overlay');
    var menuToggleIcon = document.getElementById('menu-toggle'); 

    sideMenu.classList.remove('open');
    overlay.classList.remove('show');
    if (menuToggleIcon.classList.contains('bi-x')) {
        menuToggleIcon.classList.remove('bi-x');
        menuToggleIcon.classList.add('bi-list');
    }
});

    window.addEventListener('scroll', function() {
        var scrollPosition = window.scrollY;
        var background = document.querySelector('.special-offers-section');
        background.style.transform = 'translateY(' + (scrollPosition * 0.5) + 'px)';
    });


