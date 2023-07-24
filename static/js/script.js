window.addEventListener('load', event => {
const pageContent = document.getElementById('page-content')

pageContent.style.opacity='1'

  // if (window.location.pathname == '/index') {
  //   carousel_function = function () {
  //     $('.carousel').carousel({
  //       interval: 2000
  //     })
  //     $('.carousel').carousel('cycle')
  //   }
  //   carousel_function()
  // }
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
  var selectedChoirOption =
    choirSection.options[choirSection.selectedIndex].value
  var dietCheckbox = document.getElementById('RSVPDiet' + row)
  var dietSection = document.getElementById('dropdownDiet' + row)
  var selectedDietOption = dietSection.options[dietSection.selectedIndex].value
  var dietDetailColumn = document.getElementById('diet-detail-column' + row)
  var RSVPNo = document.getElementById('RSVPNo' + row)
  var choirYes = document.getElementById('ChoirYes' + row)
  var dietary = document.getElementById('dietary' + row)
  var dietarySect = document.getElementById('dietary-sect-' + row)
  var DietNo = document.getElementById('DietNo' + row)
  var DietYes = document.getElementById('DietYes' + row)
  var voicePartGuest = document.getElementById('voicePartGuest' + row)
  var dietOption = document.getElementById('dietOption' + row)
  var dietDetail = document.getElementById('dietDetail' + row)
  var dietDetailText = document.getElementById('dietDetailText' + row)

  if (RSVP.checked) {
    RSVPDetails.style.display = 'flex' // show the section
    RSVPNo.style.display = 'none'
    dietary.style.display = 'inline'
    RSVPResponse = 'Yes'
  } else {
    RSVPNo.style.display = 'inline'
    RSVPDetails.style.display = 'none' // hide the section
    choirYes.style.display = 'none'
    dietary.style.display = 'none'
    dietarySect.style.display = 'none'
    dietDetail.style.display = 'none'
    RSVPResponse = 'No'
    dietCheckbox.checked = false
    choirCheckbox.checked = false
  }

  if (choirCheckbox.checked) {
    choirSection.style.display = 'block' // show the section
    choirYes.style.display = 'inline'
    voicePartGuest.innerHTML = selectedChoirOption
    VocalPartRespons = selectedChoirOption
    ChoirResponse = 'Yes'
  } else {
    choirSection.style.display = 'none' // hide the section
    choirSection.value = 'Vocal part'
    choirYes.style.display = 'none'
    ChoirResponse = 'No'
  }

  if (dietCheckbox.checked) {
    dietSection.style.display = 'block' // show the section
    DietYes.style.display = 'inline'
    DietNo.style.display = 'none'
    DietResponse = 'Yes:'

    if (selectedDietOption === 'Multiple/Other') {
      console.log(' multi')
      dietDetail.style.display = 'flex' // show the section
      dietary.style.display = 'inline'
      dietarySect.style.display = 'flex'
      dietDetailColumn.style.display = 'flex'
      dietDetailText.style.display = 'inline'
      dietOption.style.display = 'none'
      dietDetailColumn.style.width = '100%'
      dietOption.value = selectedDietOption
      dietDetail.addEventListener('input', function () {
        dietDetailText.innerHTML = dietDetail.value
        DietResponseDetail = dietDetail.value
        console.log('multi text')
      })
    } else {
      dietDetail.style.display = 'none' // hide the section
      dietDetailColumn.style.width = '0%'
      dietOption.innerHTML = selectedDietOption
      dietarySect.style.display = 'none'
      // dietSection.value = 'Dietary Requirements'
      DietResponseDetail = selectedDietOption
      dietDetailText.innerHTML = ''
      console.log(selectedDietOption)
      dietOption.style.display = 'inline'
      dietOption.innerHTML = selectedDietOption
      console.log('not multi')
    }
  } else {
    dietSection.style.display = 'none' // hide the section
    dietDetail.style.display = 'none' // hide the section
    dietDetailColumn.style.width = '0%'
    dietarySect.style.display = 'none'
    dietDetailColumn.style.display = 'none'
    dietary.style.display = 'none'
    dietDetail.value = ''
    dietDetailText.innerHTML = ''
    dietary.style.width = '0%'
    dietSection.value = 'Dietary Requirements'
    DietYes.style.display = 'none'
    DietNo.style.display = 'inline'
    DietResponse = 'No'
    console.log('no')
  }
}

function reveal (section) {
  var sections = {
    gettingThere: document.getElementById('getting-there'),
    accommodation: document.getElementById('accommodation'),
    dressCode: document.getElementById('dress-code'),
    giftRegistry: document.getElementById('gift-registry'),
    choir: document.getElementById('choir'),
    gettingThereCheck: document.getElementById('getting-there-check'),
    accommodationCheck: document.getElementById('accommodation-check'),
    dressCodeCheck: document.getElementById('dress-code-check'),
    giftRegistryCheck: document.getElementById('gift-registry-check'),
    choirCheck: document.getElementById('choir-check')
  }

  var checkbox = section + 'Check'
  var isChecked = sections[checkbox].checked

  if (isChecked) {
    sections[section].style.display = 'none'
    sections[checkbox].checked = false
  } else {
    if (section in sections) {
      sections[section].style.display = 'block'
      sections[checkbox].checked = true

      if (section == 'gettingThere') {
        sections.accommodation.style.display = 'none'
        sections.accommodationCheck.checked = false
      }

      if (section == 'accommodation') {
        sections.gettingThere.style.display = 'none'
        sections.gettingThereCheck.checked = false
      }

      if (section == 'dressCode') {
        sections.giftRegistry.style.display = 'none'
        sections.choir.style.display = 'none'
        sections.giftRegistryCheck.checked = false
        sections.choirCheck.checked = false
      }

      if (section == 'giftRegistry') {
        sections.dressCode.style.display = 'none'
        sections.dressCodeCheck.checked = false
        sections.choir.style.display = 'none'
        sections.choirCheck.checked = false
      }

      if (section == 'choir') {
        sections.dressCode.style.display = 'none'
        sections.dressCodeCheck.checked = false
        sections.giftRegistry.style.display = 'none'
        sections.giftRegistryCheck.checked = false
      }
    }
  }
}
