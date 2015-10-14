var request = require('request'),
    cheerio = require('cheerio'),
    fs      = require('fs');

var DELAY = 200;
var SOURCE = "https://roombooking.ucl.ac.uk";
var SOURCE_URL = SOURCE + "/rb/bookableSpace/viewAllBookableSpace.html?invoker=EFD";

var fields = ['name', 'size', 'type', 'diary', 'info', 'photo', 'location'];

var save = function(json, callback) {
  fs.writeFile('output.json', JSON.stringify(json, null, 4), function(err) {
    if (err) throw err;
    if (callback) callback();
  })
};
var generalData = function(callback) {
  request(SOURCE_URL, function(error, response, html) {
    if (error) {
      throw error;
    }

    var $ = cheerio.load(html);
    var json = [];

    $('.rooms').find('tr').each(function(i, tr) {
      var data = {};

      if (i != 0) {
        $(tr).find('td').each(function(i, td) {
          if (td.children.length > 0) {
            var child = td.children[0];

            if (child.type == 'text') {
              data[fields[i]] = child.data;
            } else if (child.type == 'tag') {
              data[fields[i]] = {
                href: child.attribs.href
              };
            }
          }
        });
      }

      if (Object.keys(data).length == fields.length) {
        json.push(data);
      } else {
        console.log('Ignoring record:', data);
      }
    });

    if (callback) {
      callback(json);
    }
  });
};

var getLocation = function(json, callback) {
  var data = json.location;
  request(data.href, function(error, response, html) {
    if (error) {
      throw error;
    }

    var $ = cheerio.load(html);
    var sibling = $('#lhs').siblings('td[align="left"]')[0];
    var h4 = $(sibling).find('h4');

    data.name = h4.text();
    data.address = h4.next().text();

    if (data.name == 'Temporary Problem Displaying Webpage') {
      console.log(json.name, ':', data.name);
      data.name = '';
      data.address = '';
    }

    if (callback) {
      callback(data);
    }
  });
};

console.log('Reading room list');

generalData(function(records) {
  if (typeof records !== 'object') {
    throw 'Room list is empty';
  }
  console.log('Done.\nReading locations');

  var counter = 0;
  var i = 0;
  var ln = records.length;

  var interval = setInterval(function() {

    if (ln <= i) {
      return clearInterval(interval);
    }

    getLocation(records[i], function(location) {
      process.stdout.write("Reading location #" + (counter + 1) + " out of " + ln + "\r");
      counter++;
      if (counter == ln) {
        console.log('\nDone.\nSaving...');
        save(records, function() {
          console.log('Done.');
        });
      }
    });
    i++;
  }, 200);
});