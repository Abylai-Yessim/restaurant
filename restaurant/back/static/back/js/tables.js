// document.addEventListener('DOMContentLoaded', function() {
//     var modal = document.getElementById("myModal");
//     var btns = document.querySelectorAll(".openModalBtn");
//     var iframe = document.getElementById("modalFrame");
//     var span = document.getElementsByClassName("close")[0];

//     function openModal(e) {
//         e.preventDefault();
//         var tableNumber = this.getAttribute('data-table-number');
//         var time = this.getAttribute('data-time');
//         var bookingUrl = "{% url 'back:booking' %}?table_number=" + tableNumber + "&time=" + time;

//         modal.style.display = "block";
//         iframe.src = bookingUrl;
//     }

//     btns.forEach(function(btn) {
//         btn.onclick = openModal;
//     });

//     if (span) {
//         span.onclick = function() {
//             modal.style.display = "none";
//         }
//     }

//     window.onclick = function(event) {
//         if (event.target == modal) {
//             modal.style.display = "none";
//         }
//     }
// });
