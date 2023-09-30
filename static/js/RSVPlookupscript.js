function capitalizeNames (input) {
 standard_input = input.toLowerCase()
  capitalized = standard_input.replace(/\b\w/g, match => match.toUpperCase())
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
  sorted_listOfInvitations = listOfInvitations.sort()
  const invitees = sorted_listOfInvitations.flatMap(str =>
    str
      .replace(/'/g, '')
      .split(',')
      .map(item => item.trim())
  )
  return invitees
}



function inviteSearch(invitations) {
  const searchYourName = document.getElementById('search-your-name');
  const showNamesList = document.getElementById('list-of-invitations-names');
  // const showNamesListNames = document.getElementById('list-of-invitations-names-text');
  const invitationGroup = document.getElementById('invitation-group');

  searchYourName.addEventListener('focus', function () {
    showNamesList.style.display = 'block';
  });

  searchYourName.addEventListener('blur', function () {
    showNamesList.style.display = 'none';
  });

  const selectElement = document.getElementById('list-of-invitations-names');
    
  searchYourName.addEventListener('input', function () {
    const searchYourNameContent = capitalizeNames(searchYourName.value);
    const filteredInvitations = invitations.filter(option =>
      option.includes(searchYourNameContent)
    );

    showNamesList.innerHTML = '';

    if (searchYourNameContent.length > 2 && filteredInvitations.length > 0) {
      listOfInvitationBullets = filteredInvitations;
      

      var numberOfOptions=0

      listOfInvitationBullets.forEach(optionText => {
        const optionElement = document.createElement('option');
        optionElement.value = optionText;
        optionElement.textContent = optionText;
        showNamesList.appendChild(optionElement);
        numberOfOptions +=1
      });

      showNamesList.style.display = 'flex';
        
      function setDropdownSize() {
       
        
        if(numberOfOptions<3){
          maxVisibleOptions = numberOfOptions}
        
          else { maxVisibleOptions = 3;}
        
       
        const actualSize = Math.max(maxVisibleOptions, 2)
      
        selectElement.size = actualSize;
      }
      setDropdownSize();
      
      
    } else {
      showNamesList.style.display = 'none';
    }
  });

  showNamesList.addEventListener('change', function (e) {
    invitationGroup.textContent = showNamesList.value;
    showNamesList.style.display = 'none';
    e.preventDefault();
  });
    
  selectElement.addEventListener('touchstart', function(e) {
      e.preventDefault();
      this.focus();
  });

  selectElement.addEventListener('touchend', function(e) {
      e.preventDefault();
      this.selectedIndex = 0; // This will keep the first option selected
      this.blur();
  });

 
}

function selectInvitation() {

          const RSVPButton = document.getElementById('submit-rsvp-button-section')
          const selectElement = document.getElementById('list-of-invitations-names');
          var selectedOption = selectElement.value;

          RSVPButton.style.display = 'flex';

         
          
          if (selectedOption) {
              JSONSTRING = JSON.stringify({ 'selectedOption': selectedOption })
              
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
