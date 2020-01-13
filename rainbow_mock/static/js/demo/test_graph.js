/*
  // DOM element where the Timeline will be attached
  var container = document.getElementById('visualization');

  // Create a DataSet (allows two way data-binding)
  var items = new vis.DataSet([
    {id: 1, content: 'item 1', start: '2013-04-20'},
    {id: 2, content: 'item 2', start: '2013-04-14'},
    {id: 3, content: 'item 3', start: '2013-04-18'},
    {id: 4, content: 'item 4', start: '2013-04-16', end: '2013-04-19'},
    {id: 5, content: 'item 5', start: '2013-04-25'},
    {id: 6, content: 'item 6', start: '2013-04-27'}
  ]);

  // Configuration for the Timeline
  var options = {};

  // Create a Timeline
  var timeline = new vis.Timeline(container, items, options);
  */

var group_data = {}
var item_data = []
for (var i = 0; i < schedule_data.length; i++) {
    var tmp_id = schedule_data[i][4] + 1
    if (schedule_data[i][5] == 'user'){
      tmp_id += 1
    }
    group_data[schedule_data[i][4]] = { id: tmp_id, content: schedule_data[i][0]}

    ds = schedule_data[i][1].replace('年', '日').replace('月', '日').split('日')
    if (schedule_data[i][2] == '午前') {
      item_data.push({
        id: i+1,
        content: schedule_data[i][3],
        editable: true,
        start: new Date(ds[0],ds[1],ds[2],10,0,0),
        end: new Date(ds[0],ds[1],ds[2],11,59,59),
        group: tmp_id
        });
    } else if (schedule_data[i][2] == '正午') {
      item_data.push({
        id: i+1,
        content: schedule_data[i][3],
        editable: true,
        start: new Date(ds[0],ds[1],ds[2],12,0,0),
        end: new Date(ds[0],ds[1],ds[2],14,59,59),
        group: tmp_id
        });
    } else if (schedule_data[i][2] == '午後') {
      item_data.push({
        id: i+1,
        content: schedule_data[i][3],
        editable: true,
        start: new Date(ds[0],ds[1],ds[2],15,0,0),
        end: new Date(ds[0],ds[1],ds[2],17,59,59),
        group: tmp_id
        });
    }
}



  // create groups to highlight groupUpdate
  var group_list = []
  for (key in group_data) {
      group_list.push(group_data[key])
  }
  var groups = new vis.DataSet(group_list)
/*var groups = new vis.DataSet([
  { id: 1, content: "Group 1" },
  { id: 2, content: "Group 2" }
]);
*/

// create a DataSet with items
var items = new vis.DataSet(item_data)
/*ds = schedule_data[0][1].replace('年', '日').replace('月', '日').split('日')
var items = new vis.DataSet([
  { id: 1, content: "Editable", editable: true, start: "2010-08-23", group: schedule_data[15][4] },
  {
    id: 2,
    content: schedule_data[0][3],
    editable: true,
    start: new Date(ds[0],ds[1],ds[2],10,0,0),
    end: new Date(ds[0],ds[1],ds[2],15,0,0),
    group: 2
  },
  {
    id: 3,
    content: "Read-only",
    editable: false,
    start: "2010-08-24T16:00:00",
    group: 1
  },
  {
    id: 4,
    content: "Read-only",
    editable: false,
    start: "2010-08-26",
    end: "2010-09-02",
    group: 2
  },
  {
    id: 5,
    content: "Edit Time Only",
    editable: { updateTime: true, updateGroup: false, remove: false },
    start: "2010-08-28",
    group: 1
  },
  {
    id: 6,
    content: "Edit Group Only",
    editable: { updateTime: false, updateGroup: true, remove: false },
    start: "2010-08-29",
    group: 2
  },
  {
    id: 7,
    content: "Remove Only",
    editable: { updateTime: false, updateGroup: false, remove: true },
    start: "2010-08-31",
    end: "2010-09-03",
    group: 1
  },
  { id: 8, content: "Default", start: "2010-09-04T12:00:00", group: 2 }
]);
*/


var container = document.getElementById("visualization");
var options = {
  editable: true // default for all items
};

var timeline = new vis.Timeline(container, items, groups, options);