const searchYourName = document.getElementById('search-your-name')
const invitationGroup = document.getElementById('invitation-group')
const selectElement = document.getElementById('list-of-invitations-names')
const RSVPButton = document.getElementById('submit-rsvp-button-section')
const form = document.getElementById('whole-form-input')
const confirmationText = document.getElementById('confirmation-text')

let androidBool
let mobileBool

function isAndroidMobile () {
  androidBool = /Android/i.test(navigator.userAgent)
  return androidBool
}

function isMobile () {
  if (window.innerWidth <= 1000) {
    selectElement.focus()

    mobileBool = true

    isAndroidMobile()
    console.log('android ', androidBool)
  }

  console.log('mobile', mobileBool)
  return mobileBool
}
window.onload(isMobile())
window.onload(isAndroidMobile())

function capitalizeNames (input) {
  let standard_input = input.toLowerCase()
  let capitalized = standard_input.replace(/\b\w/g, match =>
    match.toUpperCase()
  )
  return capitalized
}

function searchableList (listOfInvitations) {
  const listOfInvitationsAndGuests = listOfInvitations.sort()

  const invitations = listOfInvitationsAndGuests.map(str =>
    str.replace(/'/g, '')
  )

  return invitations
}

function listOfInvitees (listOfInvitations) {
  let sorted_listOfInvitations = listOfInvitations.sort()
  const invitees = sorted_listOfInvitations.flatMap(str =>
    str
      .replace(/'/g, '')
      .split(',')
      .map(item => item.trim())
  )
  return invitees
}

function inviteSearch (invitations) {
  let selectedOption = selectElement.value

  searchYourName.addEventListener('input', function () {
    let searchYourNameContent = capitalizeNames(searchYourName.value)
    let filteredInvitations = invitations.filter(option =>
      option.includes(searchYourNameContent)
    )

    selectElement.innerHTML = ''

    console.log(androidBool)

    if (androidBool) {
      console.log('adding search')
      const searchElement = document.createElement('option')
      searchElement.text = 'Search...'
      selectElement.appendChild(searchElement)
    } else {
      console.log('not android')
    }

    if (searchYourNameContent.length > 2 && filteredInvitations.length > 0) {
      let listOfInvitationBullets = filteredInvitations

      let numberOfOptions = 0

      listOfInvitationBullets.forEach(optionText => {
        let optionElement = document.createElement('option')
        optionElement.value = optionText
        optionElement.textContent = optionText
        selectElement.appendChild(optionElement)
        numberOfOptions += 1
      })

      if (isMobile){
        selectElement.value = "Search...";

      }

      selectElement.style.display = 'flex'
      if (window.innerWidth <= 1000) {
        selectElement.focus()
      }

      function setDropdownSize () {
        let maxVisibleOptions
        if (numberOfOptions < 3) {
          maxVisibleOptions = numberOfOptions
        } else {
          maxVisibleOptions = 3
        }

        let actualSize = Math.max(maxVisibleOptions, 2)

        selectElement.size = actualSize
      }

      setDropdownSize()
    } else {
      // if (androidBool) {
      //   console.log("android")
      // }
      // else {
      console.log('set size')
      selectElement.style.display = 'none'
    }
    // }
  })

  selectElement.addEventListener('click', hideFunction())
  selectElement.addEventListener('touch', hideFunction())

  function hideFunction () {
    invitationGroup.textContent = selectElement.value

    console.log('selected')
    console.log(androidBool)
    if (androidBool) {
      console.log('android true')
      selectElement.style.display = 'none'
      const clickEvent = new MouseEvent('click', {
        bubbles: true,
        cancelable: true,
        view: window
      })

      // Dispatch the click event on the element
      selectElement.dispatchEvent(clickEvent)
    } else {
      selectElement.style.display = 'none'
      // e.preventDefault()
    }
  }
}

function selectInvitation () {
  let selectedOption = selectElement.value

  

  RSVPButton.style.display = 'flex'

  if (selectedOption) {
    console.log(selectedOption)

    if (selectedOption == "Search..."){
      form.style.display = 'none';
      confirmationText.style.display = 'none';
    }
  
    else {
      form.style.display = 'block';
      confirmationText.style.display = 'block';
    }

    let JSONSTRING = JSON.stringify({ selectedOption: selectedOption })
    console.log(JSONSTRING)

    if (mobileBool) {
      invitationGroup.textContent = selectElement.value
      if (androidBool) {
        console.log('android')
      } else {
        selectElement.style.display = 'none'
      }
    }

    fetch('/rsvp_list', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSONSTRING
    })
      .then(response => response.json())

      .catch(error => {
        console.error('Error:', error)
      })
  }
}
