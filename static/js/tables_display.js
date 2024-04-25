const datatable = document.getElementById('data-table')
const tableslist = document.getElementById('tables_list_per_table')
const viewSwitch = document.getElementById('TableViewSwitch')
const perTableView = document.getElementById('per-table')
const perPersonView = document.getElementById('per-person')

function guestListFunction (guestlist) {


  let list_per_table = {}
  for (var key in guestlist) {
    //table by name
    let table_no = ''
    if (guestlist.hasOwnProperty(key)) {
      var row = datatable.insertRow()
      var cellName = row.insertCell(0)
      var cellValue = row.insertCell(1)

      cellName.appendChild(document.createTextNode(key))

      if (guestlist[key] === 0) {
        table_no = 'Head Table'
      } else {
        table_no = String(guestlist[key])
      }
      cellValue.appendChild(document.createTextNode(table_no))
    }
  }

 

  for (guest in guestlist) {
    let table_no_per_table = String(guestlist[guest])

    if (!list_per_table.hasOwnProperty(table_no_per_table)) {
      list_per_table[table_no_per_table] = []
    }

    list_per_table[table_no_per_table].push(guest)
    list_per_table[table_no_per_table].sort()
  }


  var gridContainer = document.getElementById('gridContainer')
  var headTableContainer = document.getElementById('headTableContainer')

  for (n in list_per_table) {


    var heading = document.createElement('h4')

    if (n === '0') {
      var headTableItem = document.createElement('div')

      headTableItem.className = 'grid-item head-table-item'
      heading.textContent = 'Head Table'
    } else {
      var gridItem = document.createElement('div')
      gridItem.className = 'grid-item'

      heading.textContent = 'Table ' + n
    }

    var ul = document.createElement('ul')

    list_of_names = list_per_table[n]

    for (guest_name in list_of_names) {
      var li = document.createElement('li')
      li.textContent = list_of_names[guest_name]
      ul.appendChild(li)
    }

    if (n === '0') {
      headTableItem.appendChild(heading)
      headTableItem.appendChild(ul)
      headTableContainer.appendChild(headTableItem)
    } else {
      gridItem.appendChild(heading)
      gridItem.appendChild(ul)
      gridContainer.appendChild(gridItem)
    }
  }
}

function changeTableDisplay () {
 
  if (viewSwitch.checked) {
    perTableView.style.display = 'none'
    perPersonView.style.display = 'block'
  } else {
    perTableView.style.display = 'grid'
    perPersonView.style.display = 'none'
  }
}
