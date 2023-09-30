function reveal (section) {
    var sections = {
      order: document.getElementById('order'),
      seating: document.getElementById('seating'),
      menu: document.getElementById('menu'),
      orderCheck: document.getElementById('order-check'),
      seatingCheck: document.getElementById('seating-check'),
      menuCheck: document.getElementById('menu-check'),
      topButton: document.getElementById('up-to-top'),
      topButtonCheck: document.getElementById('up-to-top-check')
    }
  
    var checkbox = section + 'Check'
    var isChecked = sections[checkbox].checked
  
    if (section == 'topButton') {
      sections.seating.style.display = 'none'
      sections.menu.style.display = 'none'
      sections.orderCheck.checked = false
      sections.seating.style.display = 'none'
      sections.seatingCheck.checked = false
      sections.menuCheck.checked = false
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
          }
  
          if (section == 'seating') {
            sections.order.style.display = 'none'
            sections.orderCheck.checked = false
            sections.menu.style.display = 'none'
            sections.menuCheck.checked = false
          }
  
          if (section == 'menu') {
            sections.order.style.display = 'none'
            sections.orderCheck.checked = false
            sections.seating.style.display = 'none'
            sections.seatingCheck.checked = false
          }
        }
      }
    }
  }
  

let topButton = document.getElementById('up-to-top')
let pageContent = document.getElementById('page-content')

pageContent.onscroll = function () {
  scrollFunction()
}

function scrollFunction () {
  if (pageContent.scrollTop > 200) {
    topButton.style.display = 'block'
  } else {
    topButton.style.display = 'none'
  }
}

function topFunction () {
  document.body.scrollTop = 0
  document.documentElement.scrollTop = 0
}