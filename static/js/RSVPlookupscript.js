const searchYourName = document.getElementById('search-your-name')
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

    selectElement.innerHTML = '';

    if (searchYourNameContent.length > 2 && filteredInvitations.length > 0) {
      listOfInvitationBullets = filteredInvitations;

      var numberOfOptions = 0

      listOfInvitationBullets.forEach(optionText => {
        var optionElement = document.createElement('option');
        optionElement.value = optionText;
        optionElement.textContent = optionText;
        selectElement.appendChild(optionElement);
        numberOfOptions +=1
      });

      selectElement.style.display = 'flex';
      // if (window.innerWidth <= 1000) {
      //   selectElement.focus()
      //   if (isAndroidMobile()) {
      //     selectElement.focus();
      //     selectElement.focus();
      //   }
      // }

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
      selectElement.style.display = 'none';
    }
  });

  selectElement.addEventListener('click', function (e) {
    e.preventDefault();
    invitationGroup.textContent = selectElement.value;
    selectElement.style.display = 'none';
    
  });

}

function selectInvitation() {
  var selectedOption = selectElement.value;

  RSVPButton.style.display = 'flex';

  if (selectedOption) {


    JSONSTRING = JSON.stringify({ selectedOption: selectedOption })
    if (window.innerWidth <= 1000) {
      


      invitationGroup.textContent = selectElement.value
      if (isAndroidMobile()) {
        selectElement.display = 'block'; 
        selectElement.focus()
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