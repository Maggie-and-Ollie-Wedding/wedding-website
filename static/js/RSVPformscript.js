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
    dietDetailColumn.style.width = '100%'
    // dietarySect.style.display = 'none'
    dietDetailColumn.style.display = 'none'
    dietary.style.display = 'none'
    dietDetail.value = ''
    dietDetailText.innerHTML = ''
    dietary.style.width = '100%'
    dietSection.value = 'Dietary Requirements'
    DietYes.style.display = 'none'
    DietNo.style.display = 'inline'
    DietResponse = 'No'
    console.log('no')
  }
}

function numberOfInvitees () {
  var numberOfInvitees = 0

  const selectElement = document.getElementById('list-of-invitations-names')
  var selectedOption = selectElement.value

  console.log(selectedOption)
  inviteesList = [];

  if (selectedOption.includes(' and ') || selectedOption.includes(', ')) {
    var stringListOfInvitees = selectedOption.replace(' and ', ', ');
    for (const value of stringListOfInvitees.split(', ')) {
      inviteesList.push(value);
    }
  } else {
    var stringListOfInvitees = String(selectedOption);
    inviteesList.push(stringListOfInvitees);
  }
  

    console.log("stringListofInvitees ", stringListOfInvitees)
    console.log(inviteesList, " list")

    var numberOfCommas = (stringListOfInvitees.match(/,/g) || []).length
    var numberOfInvitees = 1 + numberOfCommas

    console.log(numberOfInvitees)
    
  
  console.log("invitesList: ", inviteesList)

  inviteeNumbers = [1, 2, 3, 4, 5, 6]
  console.log(numberOfInvitees, " invitees")

  for (inviteeNumber of inviteeNumbers) {
    console.log(inviteeNumber, "inviteeNumber")
    var inviteLine = document.getElementById('person' + inviteeNumber)
    var inviteConfirmation = document.getElementById('rsvpConfirmation' + inviteeNumber)

    if (numberOfInvitees < inviteeNumber) {
      inviteLine.style.display = 'none'
      inviteConfirmation.style.display = 'none'
      console.log("not displaying row number ", numberOfInvitees)

    } else {
      inviteLine.style.display = 'inline'
      inviteConfirmation.style.display = 'inline'

      
      var fullName = inviteesList[inviteeNumber - 1]
      var nameOnForm = document.getElementById('invitee-form' + inviteeNumber)
      var nameOnFormValue = document.getElementById('invitee-form-value' + inviteeNumber)
      var nameSummary = document.getElementById('invitee-summary' + inviteeNumber)
      console.log("name summary ", nameSummary, "name on form ", nameOnForm, "fullname ", fullName, "invite line", inviteLine, "inviteConfirmation", inviteConfirmation)
      nameOnForm.innerHTML = fullName
      nameSummary.innerHTML = fullName
      nameOnFormValue.value = fullName
      console.log(nameOnFormValue, "name on form value")
    }
  } 
}