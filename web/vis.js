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

var legendRectSize = 18;
var legendSpacing = 4;

/* Visualize the data in the visualize function */
var visualize = function(data) {
  console.log(data);

  // == BOILERPLATE ==
  var margin = { top: 50, right: 50, bottom: 50, left: 50 },
     width = 900 - margin.left - margin.right,
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
  var salary = _.map(data, "Salary75");


  for(var i=0; i<enrollmentIncPer.length; i++) { enrollmentIncPer[i] = +enrollmentIncPer[i]; }
  for(var i=0; i<salary.length; i++) { salary[i] = +salary[i]; }
  console.log(d3.min(enrollmentIncPer));
  var enrollmentScale = d3.scaleLinear()
                    .domain( [-70, 400] )
                    .range( [150, width-100] );

  var majorScale = d3.scaleBand()
                    .domain( majorNames )
                    .range( [height, 0] );

  var xAxis = d3.axisBottom().scale(enrollmentScale);

  var yAxis = d3.axisLeft().scale(majorScale);

  svg.append("g").attr("transform", "translate(0, -20)").call(xAxis);
  svg.append("g").attr("transform", "translate(150, 0)").call(yAxis);
  svg.append("text")
            .attr("text-anchor", "middle")  // this makes it easy to centre the text as the transform is applied to the anchor
            .attr("transform", "translate(" + (width / 2) + " ," + -30 + ")")
            .text("---> Enrollment Growth (%) --->");
  svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x",0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("---> Salary --->");

  var tip = d3.tip().attr("class", "d3-tip").html(function(d){
    return d['Major'] + ": " + 'Current Enrollment: ' + d['Total2015'] + ', 75th pct. Salary: $' + d['Salary75'];
  });
  svg.call(tip);

  var legend = svg.selectAll('.legend')
  .data([1, 2])
  .enter()
  .append('g')
  .attr('class', 'legend')
  .attr('transform', function(d, i) {
    var height = legendRectSize + legendSpacing;
    var horz = -2 * legendRectSize;
    var vert = i * height;
    vert += 30
    horz += 750
    return 'translate(' + horz + ',' + vert + ')';
  });
  legend.append('circle')
  .attr('r', 6)
  .attr('cx', 5 )
  .attr('cy', 10 )
  .style("fill", function (d) {
      if (d == 1) {
          return "purple";
      } else {
          return "#3f51b5";
      }
  });
  legend.append('text')
  .attr('x', legendRectSize + legendSpacing)
  .attr('y', legendRectSize - legendSpacing)
  .text(function(d) {
    if (d == 1) return 'FemaleGrowth';
    return 'MaleGrowth';
  });

  svg.selectAll("circles")
     .data(data)
     .enter()
     .append("circle")
     .on("mouseover", tip.show)
     .on("mouseout", tip.hide)
     .attr("r", function (d) {
        return 6;
      })
     .attr("cx",function (d) {
      return enrollmentScale(Math.max(Math.min(d['TotalIncrPer']*100,400), -70));
     }) // center x pixel
     .attr("cy",function (d) {
      return majorScale(d['Major'])+10;
     }) // center x pixel
     .attr("fill", function (d) {
         if (d.FemaleIncrPer > d.MaleIncrPer) {
             return "purple";
         } else {
             return "#3f51b5";
         }
     })
     .attr("opacity", .7)
     ;
};
