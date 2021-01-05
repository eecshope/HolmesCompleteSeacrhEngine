<?php

header('Content-Type:text/html;charset=utf-8');
$query = $_SERVER["QUERY_STRING"];
$parameters = explode('&',$query,2);
$chapternum = (int)substr($parameters[0],8);
$chaptername = substr($parameters[1],12);
$chaptername = str_replace("%20"," ",$chaptername);
echo $chapternum;
$json_string = file_get_contents("/var/www/html/Holmes/HolmesCompleteSeacrhEngine/data/caches/chapter_characters.json");
$characters = json_decode($json_string,true);
$json_string = file_get_contents("/var/www/html/Holmes/HolmesCompleteSeacrhEngine/data/caches/summary.json");
$summaries = json_decode($json_string,true);

$socket = socket_create(AF_INET,SOCK_STREAM,SOL_TCP);
socket_set_option($socket,SOL_SOCKET,SO_RECTIMEO,array("sec" => 1, "usec" => 0));
socket_set_option($socket, SOL_SOCKET, SO_SNDTIMEO, array("sec" => 6, "usec" => 0));
if(socket_connect($socket,"127.0.0.1",10001)==false){
    echo "connection error";
}
else{
	if(socket_write($socket,"".$chapternum,strlen("".$chapternum))==false){
        echo "write error";
	}
	$result = "";
	while($tmp = socket_read($socket,2048)){
        $result = $result.$tmp;
	}
	$spoilerarray = explode('@',$result);


}
?>


<!doctype html>
<html>
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="chapter details" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>chapter details</title>
    <!-- web fonts -->
    <link href="http://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900&display=swap" rel="stylesheet">
    <link href="http://fonts.googleapis.com/css?family=Nunito:200,300,400,600,700,800,900&display=swap" rel="stylesheet">
    <!-- //web fonts -->
    <!-- Template CSS -->
    <link rel="stylesheet" href="assets/css/style-starter.css">
	 <script src="assets/js/jquery-3.3.1.min.js" type="text/javascript"></script>
	  
  </head>
  <body>
  <?php include 'navgen.php'; ?>
<div class="w3l-index-block1">
    <div class="content py-5">
        


      

		
		<?php			
			
			echo "<div class=\"container\">"."<div class=\"row  py-md-5 py-3\">"."<h1>".$chaptername." <br/><br/></h1>"."<div class=\"col-md-5 content-left pt-md-0 pt-5\">"."<div class=\"form\">"."<p>";
			echo "<table class=\"col-md-5 content-left pt-md-0 pt-5 table table-bordered\"  style=\"table-layout:fixed\">"."<h5>            main characters：<br/></h5><tbody>";
			echo "<h7 onclick=\"change();\">";
			$tmparray = $characters[$chapternum]["names"];
			foreach($tmparray as $name){
				echo $name."<br/>";
			}
			$filename = "/var/www/html/Holmes/HolmesCompleteSeacrhEngine/data/".$chapternum.".txt";
    		$handle = fopen($filename, "r");
    		$ref = fread($handle, filesize ($filename));
			fclose($handle);

			echo "<br/></h7>";
			echo "</tbody></table></p></div></div>";
			echo "<div class=\"col-md-7 content-photo mt-md-0 mt-5\"><h5>front cover:<br/></h5><a href=\"".$ref."\"><img src=\"HolmesCompleteSeacrhEngine/data/".$chapternum.".jpg\" class=\"img-fluid\" alt=\"main image\"/></a></div>";
			echo "</div></div>";
		?>

	
		<?php			
			
			echo "<div class=\"container\">"."<div class=\"row align-items-center py-md-5 py-3\">";
			echo "<h5>            spoiler：<br/><br/></h5><tbody>";
			echo "<button  class=\"myblack\"  id=\"spoilers\" >";
			
			foreach($spoilerarray as $spoiler){
				echo $spoiler."<br/>";
			}
			
			echo "<br/></button>";
			echo "</tbody></div></div>";
		?>

		<?php			
			
			echo "<div class=\"container\">"."<div class=\"row align-items-center py-md-5 py-3\">";
			echo "<h5>            summary：<br/><br/></h5><tbody>";
			echo "<h7  >";
			
			$tmparray = $summaries[$chapternum]["summary"];
				foreach($tmparray as $asummary){
					echo $asummary."<br/>";
			}
			
			echo "<br/></button>";
			echo "</tbody></div></div>";
		?>
		
	</div>
</div>


<!-- jQuery, Bootstrap JS -->
<script src="assets/js/jquery-3.3.1.min.js"></script>
<script src="assets/js/bootstrap.min.js"></script>

<!-- Template JavaScript -->

<script src="assets/js/owl.carousel.js"></script>

<!-- script for owlcarousel -->
<script>
$(document).ready(function () {
	$('.owl-one').owlCarousel({
	loop: true,
	margin: 0,
	nav: true,
	responsiveClass: true,
	autoplay: false,
	autoplayTimeout: 5000,
	autoplaySpeed: 1000,
	autoplayHoverPause: false,
	responsive: {
		0: {
		items: 1,
		nav: false
		},
		480: {
		items: 1,
		nav: false
		},
		667: {
		items: 1,
		nav: true
		},
		1000: {
		items: 1,
		nav: true
		}
	}
	})
})



</script>
<!-- //script for owlcarousel -->

<!-- disable body scroll which navbar is in active -->
<script>
$(function () {
	$('.navbar-toggler').click(function () {
	$('body').toggleClass('noscroll');
	})
});
</script>
<!-- disable body scroll which navbar is in active -->

<script src="assets/js/jquery.magnific-popup.min.js"></script>
<script>
$(document).ready(function () {
	$('.popup-with-zoom-anim').magnificPopup({
	type: 'inline',

	fixedContentPos: false,
	fixedBgPos: true,

	overflowY: 'auto',

	closeBtnInside: true,
	preloader: false,

	midClick: true,
	removalDelay: 300,
	mainClass: 'my-mfp-zoom-in'
	});

	$('.popup-with-move-anim').magnificPopup({
	type: 'inline',

	fixedContentPos: false,
	fixedBgPos: true,

	overflowY: 'auto',

	closeBtnInside: true,
	preloader: false,

	midClick: true,
	removalDelay: 300,
	mainClass: 'my-mfp-slide-bottom'
	});
});
</script>
<script type="text/javascript">
	var spoilers = document.getElementById('spoilers');
	var change = function(){
		console.log("click");
		if(spoilers.classList.contains("myblack")){
			spoilers.classList.remove("myblack");
		}
		else{
			spoilers.classList.add("myblack");
		}
	}
	spoilers.onclick=change;
</script>
</body>
</html>
<style>


.myblack
{

background-color: #000;
color: #000;

}
</style>
