### How to hide some legends with CSS code

When two many legends are display above a chart, it's messy.

Consider a timeline X axis with quarters.

<pre>
00:00
00:15
00:30
00:45
01:00
01:15
01:30
01:45
02:00
...
</pre>

You want to only display hours and skip 1 2 and 3 quarter of an hour, just add this CSS code to your page :

```css
@media (max-width: 1200px) {
    #mychart .highcharts-xaxis-labels text:nth-child(4n+2) { display: none; }
    #mychart .highcharts-xaxis-labels text:nth-child(4n+3) { display: none; }
    #mychart .highcharts-xaxis-labels text:nth-child(4n+4) { display: none; }
}
```

`#mychart` the HTML id of my chart.
Child numbering starts at 1, `n` formula variable starts at 0.  
So, it applies a `display: none;` on child 2, 3, 4, 6, 7, 8, 10 etc...
[More about nth-child here] (http://www.w3schools.com/cssref/sel_nth-child.asp, "W3Schoolds nth-child selector")
