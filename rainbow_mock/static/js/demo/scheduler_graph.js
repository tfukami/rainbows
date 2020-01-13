/*
for (var user in test_data){
  for (var d in test_data[user]) {
    ds = d.replace('年', '日').replace('月', '日').split('日')
    document.write(ds[0] + "-" + ds[1] + "-" + ds[2] + " 0:00:00" + test_data[user][d]["period"] + test_data[user][d]["status"])
  }
}
*/

google.charts.load('current', {'packages':['timeline']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var container = document.getElementById('myScheduler');
  var chart = new google.visualization.Timeline(container);
  var dataTable = new google.visualization.DataTable();

s_dat = [];
for (var i = 0; i < schedule_data.length; i++) {
      ds = schedule_data[i][1].replace('年', '日').replace('月', '日').split('日')
      if (schedule_data[i][2] == '午前') {
        s_dat.push([ schedule_data[i][0], schedule_data[i][3], new Date(ds[0],ds[1],ds[2],10,0,0), new Date(ds[0],ds[1],ds[2],11,59,59) ]);
      } else if (schedule_data[i][2] == '正午') {
        s_dat.push([ schedule_data[i][0], schedule_data[i][3], new Date(ds[0],ds[1],ds[2],12,0,0), new Date(ds[0],ds[1],ds[2],14,59,59) ]);
      } else if (schedule_data[i][2] == '午後') {
        s_dat.push([ schedule_data[i][0], schedule_data[i][3], new Date(ds[0],ds[1],ds[2],15,0,0), new Date(ds[0],ds[1],ds[2],17,59,59) ]);
      }
};

  dataTable.addColumn({ type: 'string', id: 'Group' });
  dataTable.addColumn({ type: 'string', id: 'name' });
  dataTable.addColumn({ type: 'date', id: 'Start' });
  dataTable.addColumn({ type: 'date', id: 'End' });
  dataTable.addRows(s_dat)

  var options = {
    timeline: { groupByRowLabel: true }
  };

  chart.draw(dataTable, options);
}


