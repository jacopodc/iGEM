var $scroll = $(".scrolltext3")

$scroll.waypoint(function(direction){
  if (direction == "down")
  {
    console.log("Waypoint has been reached. Text should now disappear.");
    $scroll.addClass("remove");
  }
  else {
    console.log("Text should now load back up");
    $scroll.removeClass("remove");
  }
},{
  offset:"85%"
});

var $section1 = $(".section-1");

$section1.waypoint(function(direction){
  if (direction == "down")
  {
    console.log("The first section should now load.");
    $section1.addClass("section1animation");
  }
  else {
    console.log("Section 1 should now disappear.");
    $section1.removeClass("section1animation");
  }
},{
  offset:"50%"
})
