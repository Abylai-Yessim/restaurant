// document.addEventListener('DOMContentLoaded', function() {
//     var numbers = document.querySelectorAll('.numbers-zal');
//     var form = document.getElementById('booking-form');
    
//     numbers.forEach(function(number) {
//         number.addEventListener('click', function() {
            
//             var tableNumber = this.querySelector('a').innerText;
           
//             var input = document.createElement('input');
//             input.setAttribute('type', 'hidden');
//             input.setAttribute('name', 'table_number');
//             input.setAttribute('value', tableNumber);
//             form.appendChild(input);
            
//             form.style.display = 'block';
//         });
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    // Находим все элементы с классом "place disabled"
    var disabledPlaces = document.querySelectorAll('.place.disabled');

    // Проходимся по найденным элементам
    disabledPlaces.forEach(function(place) {
        // Отменяем действие по умолчанию при клике на элемент
        place.addEventListener('click', function(event) {
            event.preventDefault(); // Отменяем действие по умолчанию (переход по ссылке)
        });
    });
});

