function reveal (section) {
    var sections = {
      order: document.getElementById('order'),
      seating: document.getElementById('seating'),
      menu: document.getElementById('menu'),
      drinks: document.getElementById('drinks'),
      orderCheck: document.getElementById('order-check'),
      seatingCheck: document.getElementById('seating-check'),
      menuCheck: document.getElementById('menu-check'),
      drinksCheck: document.getElementById('drinks-check'),
      topButton: document.getElementById('up-to-top'),
      topButtonCheck: document.getElementById('up-to-top-check')
    }
  
    var checkbox = section + 'Check'
    var isChecked = sections[checkbox].checked
  
    if (section == 'topButton') {
      sections.order.style.display = 'none'
      sections.menu.style.display = 'none'
      sections.orderCheck.checked = false
      sections.seating.style.display = 'none'
      sections.seatingCheck.checked = false
      sections.menuCheck.checked = false
      sections.drinksCheck.checked = false
      sections.drinks.style.display = 'none'
    } else {
      if (isChecked) {
        sections[section].style.display = 'none'
        sections[checkbox].checked = false
      } else {
        if (section in sections) {
          sections[section].style.display = 'block'
          sections[checkbox].checked = true
  
    
          if (section == 'order') {
            sections.seating.style.display = 'none'
            sections.menu.style.display = 'none'
            sections.seatingCheck.checked = false
            sections.menuCheck.checked = false
            sections.drinksCheck.checked = false
            sections.drinks.style.display = 'none'
          }
  
          if (section == 'seating') {
            sections.order.style.display = 'none'
            sections.orderCheck.checked = false
            sections.menu.style.display = 'none'
            sections.menuCheck.checked = false
            sections.drinksCheck.checked = false
            sections.drinks.style.display = 'none'
          }
  
          if (section == 'menu') {
            sections.order.style.display = 'none'
            sections.orderCheck.checked = false
            sections.seating.style.display = 'none'
            sections.seatingCheck.checked = false
            sections.drinksCheck.checked = false
            sections.drinks.style.display = 'none'
          }

          if (section == 'drinks') {
            sections.order.style.display = 'none'
            sections.orderCheck.checked = false
            sections.seating.style.display = 'none'
            sections.seatingCheck.checked = false
            sections.menu.style.display = 'none'
            sections.menuCheck.checked = false
          }
        }
      }
    }
  }
  
