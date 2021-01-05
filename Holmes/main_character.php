<?php

header('Content-Type:text/html;charset=utf-8');

$json_string = file_get_contents("/var/www/html/Holmes/HolmesCompleteSeacrhEngine/data/caches/main_character.json");
$characters = json_decode($json_string,true);


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

        


      
        
		<h1><br/><br/>main characters</h1>
		<?php			
            
            foreach($characters as $character){
                echo "<div class=\"w3l-index-block1\"><div class=\"content py-5\">";
                echo "<div class=\"container\">"."<div class=\"row  py-md-5 py-3\">"."<div>"."<div >"."<p>";
                echo "<table class=\"col-md-5 content-left pt-md-0 pt-5 table table-bordered\"  style=\"table-layout:fixed\">";
                echo "<h2><br/>            ".$character["name"]."<br/></h5><tbody>";
                echo "<h5><br/>subscribe:<br/>".$character["subscribe"]."</h5>";
                echo "<h7>";
                echo "<br/>character appearing:<br/>";
			    $tmparray = $character["chapters"];
			    foreach($tmparray as $c){
				    echo $c."<br/>";
			    }
			    

			    echo "<br/></h7>";
			    echo "</tbody></table></p></div></div>";
			    echo "</div></div>";
                echo "</div></div>";
            }
			
		?>

	
	
		
	


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
