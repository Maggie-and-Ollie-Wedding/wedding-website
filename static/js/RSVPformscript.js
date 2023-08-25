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
      })
    } else {
      dietDetail.style.display = 'none' // hide the section
      dietDetailColumn.style.width = '100%'
      dietDetail.style.width = '100%'
      dietOption.innerHTML = selectedDietOption
      dietarySect.style.display = 'none'
      DietResponseDetail = selectedDietOption
      dietDetailText.innerHTML = ''
      dietOption.style.display = 'inline'
      dietOption.innerHTML = selectedDietOption
    }
  } else {
    dietSection.style.display = 'none' // hide the section
    dietDetail.style.display = 'none' // hide the section
    dietDetailColumn.style.width = '100%'
    dietDetailColumn.style.display = 'none'
    dietary.style.display = 'none'
    dietDetail.value = ''
    dietDetailText.innerHTML = ''
    dietary.style.width = '100%'
    dietSection.value = 'Dietary Requirements'
    DietYes.style.display = 'none'
    DietNo.style.display = 'inline'
    DietResponse = 'No'
  }
}

function numberOfInvitees () {
  selectInvitation()

  var numberOfInvitees = 0

  const selectElement = document.getElementById('list-of-invitations-names')
  var selectedOption = selectElement.value

  inviteesList = []

  if (selectedOption.includes(' and ') || selectedOption.includes(', ')) {
    var stringListOfInvitees = selectedOption.replace(' and ', ', ')
    for (const value of stringListOfInvitees.split(', ')) {
      inviteesList.push(value)
    }
  } else {
    var stringListOfInvitees = String(selectedOption)
    inviteesList.push(stringListOfInvitees)
  }

  var numberOfCommas = (stringListOfInvitees.match(/,/g) || []).length
  var numberOfInvitees = 1 + numberOfCommas

  inviteeNumbers = [1, 2, 3, 4, 5, 6]

  for (inviteeNumber of inviteeNumbers) {
    var inviteLine = document.getElementById('person' + inviteeNumber)
    var inviteConfirmation = document.getElementById(
      'rsvpConfirmation' + inviteeNumber
    )

    if (numberOfInvitees < inviteeNumber) {
      inviteLine.style.display = 'none'
      inviteConfirmation.style.display = 'none'
    } else {
      inviteLine.style.display = 'inline'
      inviteConfirmation.style.display = 'inline'

      var fullName = inviteesList[inviteeNumber - 1]
      var nameOnForm = document.getElementById('invitee-form' + inviteeNumber)
      var nameOnFormValue = document.getElementById(
        'invitee-form-value' + inviteeNumber
      )
      var nameSummary = document.getElementById(
        'invitee-summary' + inviteeNumber
      )
      nameOnForm.innerHTML = fullName
      nameSummary.innerHTML = fullName
      nameOnFormValue.value = fullName
    }
  }
}

function submitSwan (event) {
  if (event.key === 'Enter') {
    event.preventDefault() // Prevent the default Enter key behavior
  } else {
    const form = document.getElementById('rsvp-form')
    const gifContainer = document.getElementById('gifContainer')

    event.preventDefault()

    const formValues = new FormData(form)
    for (const value of formValues.values()) {
      const namesToCheck = ['Racher', 'Turner', 'Perry', 'Person4']
      const displayDuration = 20000

      for (const name of namesToCheck) {
        if (value.includes(name)) {
          gifContainer.style.display = 'flex' // Show the container
          var timeout = 10000
          setTimeout(() => {
            gifContainer.style.display = 'none'
          }, displayDuration)

          break
        }
      }
      if (timeout != 10000) {
        var timeout = 0
      }
    }

    setTimeout(function () {
      form.submit()
    }, timeout)
  }
}
