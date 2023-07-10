window.addEventListener('load', event => {
  if (window.location.pathname == '/index') {
    carousel_function = function () {
      $('.carousel').carousel({
        interval: 2000
      })
      $('.carousel').carousel('cycle')
    }
    carousel_function()
  }
})

// Get all the links
const links = document.querySelectorAll('a[href^="#"]')

// Attach event listener to each link
links.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault()
    const targetSection = document.querySelector(link.getAttribute('href'))
    targetSection.scrollIntoView({
      behavior: 'smooth'
    })
  })
})

function myFunction () {
  var x = document.getElementById('myLinks')
  if (x.style.display === 'block') {
    x.style.display = 'none'
  } else {
    x.style.display = 'block'
  }
}

function toggleFormSection (row) {
  var RSVP = document.getElementById('RSVPCheck' + row)
  var RSVPDetails = document.getElementById('RSVPDetails' + row)
  var choirCheckbox = document.getElementById('RSVPChoir' + row)
  var choirSection = document.getElementById('dropdownVocalPart' + row)
  var dietCheckbox = document.getElementById('RSVPDiet' + row)
  var dietSection = document.getElementById('dropdownDiet' + row)
  var dietDetail = document.getElementById('dietDetail' + row)
  var selectedDietOption = dietSection.options[dietSection.selectedIndex].value;
  var dietDetailColumn = document.getElementById("diet-detail-column"+row)


  

  if (RSVP.checked) {
    RSVPDetails.style.display = 'flex' // show the section
  } else {
    RSVPDetails.style.display = 'none' // hide the section
  }

  if (choirCheckbox.checked) {
    choirSection.style.display = 'block' // show the section
  } else {
    choirSection.style.display = 'none' // hide the section
    choirSection.value = 'Vocal part'
  }

  if (dietCheckbox.checked) {
    dietSection.style.display = 'block' // show the section
    if ( selectedDietOption === 'Multiple/Other') {
      console.log(selectedDietOption)
      dietDetail.style.display = 'block' // show the section
      dietDetailColumn.style.width= "40vw"
    } else {
      console.log(selectedDietOption)
      dietDetail.style.display = 'none' // hide the section
      dietDetailColumn.style.width= "0%"
      dietSection.value = 'Dietary Requirements'
      dietDetail.value = ''
  
    }
  } else {
    dietSection.style.display = 'none' // hide the section
    dietDetail.style.display = 'none' // hide the section
    dietDetailColumn.style.width= "0%"
    dietSection.value = 'Dietary Requirements'
    dietDetail.value = ''
  }

  
}


