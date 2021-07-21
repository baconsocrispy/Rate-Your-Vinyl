

function sortTable(column) {
  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("myTable");
  switching = true;
  while (switching) {
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      xString = rows[i].getElementsByTagName("TD")[column].innerHTML;
      yString = rows[i + 1].getElementsByTagName("TD")[column].innerHTML;
      console.log(typeof xString);
      x = parseInt(xString);
      y = parseInt(yString);
      //check if the two rows should switch place:
      if (x < y) {
        //if so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}


function savePlayerFunc(rowNum) {
    console.log(rowNum);

    var element_table = document.getElementsByName('brTable');
    var element_tableRows = element_table[0].rows;
    var data = [];
    for(var i = 1 ; i < element_tableRows.length; i++)
    {
        data[i] = element_tableRows[i].getAttribute("name");
    }
    document.getElementById("save-player").innerHTML = data[rowNum];
    console.log(typeof data);
}

function showDiv() {
    var T = document.getElementById("show-div");
    T.style.display = "block";
}