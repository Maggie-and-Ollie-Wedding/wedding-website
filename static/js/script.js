window.addEventListener('load', (event) => {

  if (window.location.pathname =='/index') {
    window.onload (carousel_function = function() {
        ('.carousel').carousel({
              interval: 20
            });
        ('.carousel').carousel('cycle');
      }
    )
          }})



 const rsvpDietSwitch1 = document.getElementById("RSVPDiet1")
 const rsvpDietDropdown1 = document.getElementById("dropdownDiet1")
 const rsvpVocalPartSwitch1 = document.getElementById("RSVPChoir1")
 const rsvpVocalPartDropdown1 = document.getElementById("dropdownVocalPart1")
   
 function rsvpDiet1() {
 if (rsvpDietSwitch1 === true) {
  rsvpDietDropdown1.style.display = "block";
} else {
  rsvpDietDropdown1.style.display = "none";
}
 }

// Get all the links
const links = document.querySelectorAll('a[href^="#"]');

// Attach event listener to each link
links.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const targetSection = document.querySelector(link.getAttribute('href'));
    targetSection.scrollIntoView({
      behavior: 'smooth'
    });
  });
});


function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
