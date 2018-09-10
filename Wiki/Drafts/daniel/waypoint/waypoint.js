var $logo =$(".logo");

$logo.waypoint(function(direction){
  if (direction == "down")
  {
    console.log("Waypoint has been reached!");
    $logo.addClass("logo-activation");
  }
  else
  {
    console.log("Logo has been terminated!");
    $logo.removeClass("logo-activation");
  }
},{
  offset:"33%"
});
