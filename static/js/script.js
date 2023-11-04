window.addEventListener('load', event => {
  const pageContent = document.getElementById('page-content')
  pageContent.style.opacity = '1'
})

const links = document.querySelectorAll('a[href^="#"]')

links.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault()
    const targetSection = document.querySelector(link.getAttribute('href'))
    targetSection.scrollIntoView({
      behavior: 'smooth'
    })
  })
})

function expandFunction () {
  var x = document.getElementById('myLinks')
  if (x.style.display === 'block') {
    x.style.display = 'none'
  } else {
    x.style.display = 'block'
  }
}


function revealFromRSVP (section) {
  if (section === 'gettingThere' || section === 'accommodation') {
    window.location.href = '/#getting-there-accommodation'
  } else {
    window.location.href = '/#dress-code-gift-registry-choir'
  }

  reveal(section)
}
