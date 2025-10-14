var $Ancient = $("#Ancient")[0];
$(".box1")
.mouseenter(function() {
	$Ancient.play();
});

$(".box1")
.mouseout(function() {
	$Ancient.pause();
});

var $Blacklight = $("#Blacklight")[0];
$(".box2")
.mouseenter(function() {
	$Blacklight.play();
});

$(".box2")
.mouseout(function() {
	$Blacklight.pause();
});

var $Rift = $("#Rift")[0];
$(".box3")
.mouseenter(function() {
	$Rift.play();
});

$(".box3")
.mouseout(function() {
	$Rift.pause();
});