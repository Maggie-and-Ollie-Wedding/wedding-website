
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
      choirCheck: document.getElementById('choir-check'),
      topButton: document.getElementById('up-to-top'),
      topButtonCheck: document.getElementById('up-to-top-check')
    }
  
    var checkbox = section + 'Check'
    var isChecked = sections[checkbox].checked
  
    if (section == 'topButton') {
      sections.accommodation.style.display = 'none'
      sections.accommodationCheck.checked = false
      sections.gettingThere.style.display = 'none'
      sections.gettingThereCheck.checked = false
      sections.giftRegistry.style.display = 'none'
      sections.choir.style.display = 'none'
      sections.dressCodeCheck.checked = false
      sections.giftRegistry.style.display = 'none'
      sections.giftRegistryCheck.checked = false
      sections.choirCheck.checked = false
    } else {
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
  }
  
  