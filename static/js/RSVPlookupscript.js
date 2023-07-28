function capitalizeNames (input) {
  console.log(input)
  capitalized = input.replace(/\b\w/g, match => match.toUpperCase())
  console.log(capitalized)
  return capitalized
}

function searchableList (listOfInvitations) {
  const listOfInvitationsAndGuests = listOfInvitations

  const invitations = listOfInvitationsAndGuests.map(str =>
    str.replace(/'/g, '')
  )

  console.log('searchableList():')
  return invitations
}

function listOfInvitees (listOfInvitations) {
  const invitees = listOfInvitations.flatMap(str =>
    str
      .replace(/'/g, '')
      .split(',')
      .map(item => item.trim())
  )

  console.log(invitees)
  return invitees
}

function inviteSearch (invitations) {
  const searchYourName = document.getElementById('search-your-name')
  console.log('inviteSearch()')

  searchYourName.addEventListener('input', function () {
    const showNamesList = document.getElementById('list-of-invitations-names')

    showNamesList.innerHTML = ''
    console.log(searchYourName.value.length)
    if (searchYourName.value.length > 2) {
      var searchYourNameContent = capitalizeNames(searchYourName.value)
      listOfInvitationBullets = []
      console.log(searchYourNameContent)
      console.log(invitations)
      console.log(invitations.includes(searchYourNameContent))
      const containsSearchString = invitations.some(option =>
        option.includes(searchYourNameContent)
      )

      console.log(containsSearchString)

      for (var i = 0; i < invitations.length; i++) {
        if (containsSearchString) {
          console.log(invitations[i])
          inviteesNamesBullets = invitations[i]
          // inviteesNamesBullets = '<option>' + invitees[i] + '</option>'
          listOfInvitationBullets.push(inviteesNamesBullets)
        }
      }

      const showNamesList = document.getElementById('list-of-invitations-names')
      console.log(listOfInvitationBullets)
      listOfInvitationBullets.forEach(optionText => {
        const optionElement = document.createElement('option')

        optionElement.value = optionText
        optionElement.textContent = optionText

        showNamesList.appendChild(optionElement)
      })
      console.log(showNamesList)
      if (listOfInvitationBullets.length === 0) {
        showNamesList.style.display = 'none'
        console.log(listOfInvitationBullets.length === 0)
      } else {
        showNamesList.style.display = 'flex'
      }
    } else {
      showNamesList.style.display = 'none'
    }
  })
}

function selectInvitation () {
  const options = listOfInvitationBullets.getElementsByTagName('option')

  for (let i = 0; i < options.length; i++) {
    const optionText = options[i].textContent.toLowerCase()
    const filterValueLowerCase = filterValue.toLowerCase()

    if (optionText.includes(filterValueLowerCase)) {
      options[i].style.display = 'block'
    } else {
      options[i].style.display = 'none'
    }
  }
}

function setDropdownSize () {
  const selectElement = document.getElementById('list-of-invitations-names')
  const optionCount = selectElement.getElementsByTagName('option').length
  const maxVisibleOptions = 4

  selectElement.size = Math.min(maxVisibleOptions, optionCount)
}
