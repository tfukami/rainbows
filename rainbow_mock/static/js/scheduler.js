google.charts.load('current', {'packages':['timeline']});
google.charts.setOnLoadCallback(drawChart);

function drawChart(data) {
  var container = document.getElementById('myScheduler');
  var chart = new google.visualization.Timeline(container);
  var dataTable = new google.visualization.DataTable();

  dataTable.addColumn({ type: 'string', id: 'Group' });
  dataTable.addColumn({ type: 'string', id: 'name' });
  dataTable.addColumn({ type: 'date', id: 'Start' });
  dataTable.addColumn({ type: 'date', id: 'End' });
  dataTable.addRows([
    [ '', '自分の予定', new Date(2020,1,2,0,0,0), new Date(2020,1,2,23,59,59) ],
    [ 'Group 1', 'friend A', new Date(2020,1,1,16,0,0), new Date(2020,1,1,23,59,59) ],
    [ 'Group 1', 'friend Z', new Date(2020,1,1,11,0,0), new Date(2020,1,2,13,0,0) ],
    [ 'Group 2', 'friend C', new Date(2020,1,1,12,0,0), new Date(2020,1,3,16,0,0) ]
  ]);

  var options = {
    timeline: { groupByRowLabel: true }
  };

  chart.draw(dataTable, options);
}