// (function($) {
//     'use strict';
//     $(function () {
//         //Event carousel
//         $("#events").owlCarousel({
//             loop:true,
//             margin:0,
//             autoPlay: 3000,
//             responsive:{
//                 0:{
//                     items:1
//                 },
//                 768:{
//                     items:2
//                 },
//                 979:{
//                     items:3
//                 },
//                 1199:{
//                     items:4
//                 }
//             },
//             singleItem : false,
//             dots: false,
//             nav: true,
//             navText : ["",""]
//         });
//         $(".btn-event-show").collapse();
//         //Events: Tooltip
//         $('.event-user').tooltip({ boundary: 'window' });
//         feather.replace();
//     });
// })(jQuery);

const gap = 16;

const carousel = document.getElementById("carousel"),
  content = document.getElementById("content"),
  next = document.getElementById("next"),
  prev = document.getElementById("prev");

next.addEventListener("click", e => {
  carousel.scrollBy(width + gap, 0);
  if (carousel.scrollWidth !== 0) {
    prev.style.display = "flex";
  }
  if (content.scrollWidth - width - gap <= carousel.scrollLeft + width) {
    next.style.display = "none";
  }
});
prev.addEventListener("click", e => {
  carousel.scrollBy(-(width + gap), 0);
  if (carousel.scrollLeft - width - gap <= 0) {
    prev.style.display = "none";
  }
  if (!content.scrollWidth - width - gap <= carousel.scrollLeft + width) {
    next.style.display = "flex";
  }
});

let width = carousel.offsetWidth;
window.addEventListener("resize", e => (width = carousel.offsetWidth));
