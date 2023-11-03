const searchYourName = document.getElementById('search-your-name')
const invitationGroup = document.getElementById('invitation-group')
const selectElement = document.getElementById('list-of-invitations-names')
const RSVPButton = document.getElementById('submit-rsvp-button-section')

let androidBool

function isAndroidMobile () {
  console.log('andr')
  androidBool = /Android/i.test(navigator.userAgent)
  console.log(androidBool)
  return androidBool
}

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
      selectElement.style.display = 'none'}
    // }
  })

  selectElement.addEventListener('click', function (e) {
    invitationGroup.textContent = selectElement.value

    
    // if (androidBool) {
    //   console.log("android 2")
    // }
    // else {
    selectElement.style.display = 'none'
    e.preventDefault()
  // }
  })
}

function selectInvitation () {
  let selectedOption = selectElement.value

  RSVPButton.style.display = 'flex'

  if (selectedOption) {
    console.log(selectedOption)

    let JSONSTRING = JSON.stringify({ selectedOption: selectedOption })
    console.log(JSONSTRING)

    if (window.innerWidth <= 1000) {
      selectElement.focus()

      console.log('mobile')

      invitationGroup.textContent = selectElement.value
      if (androidBool){
        selectElement.preventDefault()
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
