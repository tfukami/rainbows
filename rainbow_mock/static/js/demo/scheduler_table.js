/*
for (var user in schedule_data){
  for (var d in schedule_data[user]) {
    document.write('<tr><td>'+user+'</td><td>'+d+'</td><td>'+schedule_data[user][d]['period']+'</td><td>' + schedule_data[user][d]['status'] + '</td><td>2011/07/25</td><td>$170,750</td></tr>')
  }
}
*/

for (var i = 0; i < schedule_data.length; i++) {
  document.write('<tr><td>'+schedule_data[i][0]+'</td><td>'+schedule_data[i][1]+'</td><td>'+schedule_data[i][2]+'</td><td>'+schedule_data[i][3]+'</td></tr>')
}

