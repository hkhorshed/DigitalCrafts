
var navigationSelection = "[data-nav-item]";
var imageSelection = "[data-target]";

var navItems = document.querySelectorAll(navigationSelection);
var imgTarget = document.querySelector(imageSelection);

navItems.forEach(function (nav) {
  nav.addEventListener('click', function (event) {
    event.preventDefault();
    imgTarget.setAttribute('src', nav.getAttribute('href'));
  })
});
//  Scroll Bar for target image
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    if (n > x.length) {slideIndex = 1} 
    if (n < 1) {slideIndex = x.length} ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none"; 
    }
    x[slideIndex-1].style.display = "block"; 
}

