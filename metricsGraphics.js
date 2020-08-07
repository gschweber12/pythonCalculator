<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js'></script>
<script src="https://d3js.org/d3.v5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/metrics-graphics/2.15.6/metricsgraphics.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/metrics-graphics/2.15.6/metricsgraphics.min.css">

<div id="chart"></div>

MG.data_graphic({
  title: "# of downloads",
  data: [{
      'date': new Date('2014-11-01'),
      'value': 12
    },
    {
      'date': new Date('2014-11-02'),
      'value': 9
    }
  ],
  width: 600,
  height: 250,
  color: 'green',
  target: '#chart',
  x_accessor: 'date',
  y_accessor: 'value',
})