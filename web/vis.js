"use strict";

/* Boilerplate jQuery */
$(function() {
  $.get("res/uiuc_demographics_undergrad.csv")
   .done(function (csvData) {
     var data = d3.parseCsv(csvData);
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

  var major = _.map(data, "Major Name");
  major = _.uniq(major);
  // opponents can now be used as the domain in your scale

  var enrollment = _.map(data, "Total");
  enrollment = _.uniq(enrollment);
  // years can now be used as the domain in your scale


  var enrollmentScale = d3.scaleLinear()
                    .domain( enrollment )
                    .range( [0, width] )

  var majorScale = d3.scaleLinear()
                    .domain( [d3.min(enrollment), d3.max(enrollment)] )
                    .range( [0, width] )

  var xAxis = d3.axisBottom().scale(enrollmentScale)
  var yAxis = d3.axisLeft().scale(majorScale)

  svg.append("g").call(xAxis)
  svg.append("g").call(yAxis)

  svg.selectAll("circles")
     .data(data)
     .enter()
     .append("circle")
     .attr("r", function (d) {

        return Math.abs(d.Total) * 0.7;
      })
     .attr("cx",function (d) {
        return enrollmentScale(d.enrollment);
     }) // center x pixel
     .attr("cy",function (d) {
        return majorScale(d.major);
     }) // center x pixel
     .attr("fill","purple")
     ;


};
