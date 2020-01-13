s_dat = [];
for (var i = 0; i < schedule_data.length; i++) {
      ds = schedule_data[i][1].replace('年', '日').replace('月', '日').split('日')
      if (schedule_data[i][2] == '午前') {
        s_dat.push([ schedule_data[i][0], schedule_data[i][3], new Date(ds[0],ds[1],ds[2],10,0,0), new Date(ds[0],ds[1],ds[2],10,59,59) ]);
      } else if (schedule_data[i][2] == '正午') {
        s_dat.push([ schedule_data[i][0], schedule_data[i][3], new Date(ds[0],ds[1],ds[2],11,0,0), new Date(ds[0],ds[1],ds[2],14,59,59) ]);
      } else if (schedule_data[i][2] == '午後') {
        s_dat.push([ schedule_data[i][0], schedule_data[i][3], new Date(ds[0],ds[1],ds[2],15,0,0), new Date(ds[0],ds[1],ds[2],17,59,59) ]);
      }
};

for (var i = 0; i < s_dat.length; i++) {
  document.write('<div>' + s_dat[i][1] + '</div>')
}

