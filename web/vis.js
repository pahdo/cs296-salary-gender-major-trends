"use strict";

/* Boilerplate jQuery */
$(function() {
  $.get("res/uiuc_pretty.csv")
   .done(function (csvData) {
     var data = d3.csvParse(csvData);
     data.sort(function (a, b){
        if (a['Salary75'] < b['Salary75']) {
          return -1;
        }
        if (a['Salary75'] > b['Salary75']) {
          return 1;
        }
        return 0;
     });
     visualize(data);
   })
  .fail(function(e) {
     alert("Failed to load CSV file!");
  });
});

/* Visualize the data in the visualize function */
var visualize = function(data) {
  console.log(data);

  // == BOILERPLATE ==
  var margin = { top: 50, right: 50, bottom: 50, left: 50 },
     width = 800 - margin.left - margin.right,
     height = (data.length * 20);

  var svg = d3.select("#chart")
              .append("svg")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
              .style("width", width + margin.left + margin.right)
              .style("height", height + margin.top + margin.bottom)
              .append("g")
              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");



  // == Your code! :) ==

  var majorNames = _.map(data, "Major");
  majorNames = _.uniq(majorNames);

  var enrollmentIncPer = _.map(data, "TotalIncrPer");

  for(var i=0; i<enrollmentIncPer.length; i++) { enrollmentIncPer[i] = +enrollmentIncPer[i]; }
  console.log(d3.min(enrollmentIncPer));
  var enrollmentScale = d3.scaleLinear()
                    .domain( [d3.min(enrollmentIncPer), d3.max(enrollmentIncPer)] )
                    .range( [0, width] );

  var majorScale = d3.scaleBand()
                    .domain( majorNames )
                    .range( [height, 0] );

  var xAxis = d3.axisBottom().scale(enrollmentScale);

  var yAxis = d3.axisLeft().scale(majorScale);

  svg.append("g").attr("transform", "translate(0, 340)").call(xAxis);
  svg.append("g").attr("transform", "translate(340, 0)").call(yAxis);

  var tip = d3.tip().attr("class", "d3-tip").html(function(d){
    return d['Major'];
  });
  svg.call(tip);

  svg.selectAll("circles")
     .data(data)
     .enter()
     .append("circle")
     .on("mouseover", tip.show)
     .on("mouseout", tip.hide)
     .attr("r", function (d) {
        return 4;
      })
     .attr("cx",function (d) {
       console.log(enrollmentScale(+d['TotalIncrPer']));
      return enrollmentScale(+d['TotalIncrPer']);
     }) // center x pixel
     .attr("cy",function (d) {
      return majorScale(d['Major'])+10;
     }) // center x pixel
     .attr("fill","purple")
     ;
};
