const searchYourName = document.getElementById('search-your-name')
const showNamesList = document.getElementById('list-of-invitations-names')
const invitationGroup = document.getElementById('invitation-group')
const selectElement = document.getElementById('list-of-invitations-names')
const RSVPButton = document.getElementById('submit-rsvp-button-section')

function isAndroidMobile() {
  androidBool = /Android/i.test(navigator.userAgent);
  return androidBool
}

window.onload(isAndroidMobile())

function capitalizeNames (input) {
  standard_input = input.toLowerCase()
  capitalized = standard_input.replace(/\b\w/g, match => match.toUpperCase())
  return capitalized
}

function searchableList (listOfInvitations) {
  var listOfInvitationsAndGuests = listOfInvitations.sort()

  var invitations = listOfInvitationsAndGuests.map(str => str.replace(/'/g, ''))

  return invitations
}

function listOfInvitees (listOfInvitations) {
  sorted_listOfInvitations = listOfInvitations.sort()
  var invitees = sorted_listOfInvitations.flatMap(str =>
    str
      .replace(/'/g, '')
      .split(',')
      .map(item => item.trim())
  )
  return invitees
}

function inviteSearch(invitations) {
  var selectedOption = selectElement.value

  searchYourName.addEventListener('input', function () {
    var searchYourNameContent = capitalizeNames(searchYourName.value);
    var filteredInvitations = invitations.filter(option =>
      option.includes(searchYourNameContent)
    );

    showNamesList.innerHTML = '';

    if (searchYourNameContent.length > 2 && filteredInvitations.length > 0) {
      listOfInvitationBullets = filteredInvitations;

      var numberOfOptions = 0

      listOfInvitationBullets.forEach(optionText => {
        var optionElement = document.createElement('option');
        optionElement.value = optionText;
        optionElement.textContent = optionText;
        showNamesList.appendChild(optionElement);
        numberOfOptions +=1
      });

      showNamesList.style.display = 'flex';
      if (window.innerWidth <= 1000) {
        showNamesList.focus()
        if (isAndroidMobile()) {
          showNamesList.focus();
          showNamesList.style.display = 'flex';
        }
      }

      function setDropdownSize() {
        if(numberOfOptions<3){
          maxVisibleOptions = numberOfOptions
        } 
        else {
          maxVisibleOptions = 3;
        }

        var actualSize = Math.max(maxVisibleOptions, 2)

        selectElement.size = actualSize;
      }
      setDropdownSize();

    } else {
      showNamesList.style.display = 'none';
    }
  });

  showNamesList.addEventListener('click', function (e) {
    invitationGroup.textContent = showNamesList.value;
    // showNamesList.style.display = 'none';
    e.preventDefault();
  });

}

function selectInvitation() {
  var selectedOption = selectElement.value;

  RSVPButton.style.display = 'flex';

  if (selectedOption) {


    JSONSTRING = JSON.stringify({ selectedOption: selectedOption })
    if (window.innerWidth <= 1000) {
      


      invitationGroup.textContent = showNamesList.value
      if (isAndroidMobile()) {
        showNamesList.style.display = 'flex';
        
      }
      else
      {
        selectElement.focus()
      }
    }

    fetch('/rsvp_list', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSONSTRING,
    })
      .then(response => response.json())

      .catch(error => {
        console.error('Error:', error);
      });
  }
}