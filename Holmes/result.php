


<?php



$query = $_SERVER["QUERY_STRING"];
$keyword_str = substr($query,9);


$keywords = explode("%20",$keyword_str);
$arrlength=count($keywords);

$para = "";
for($x=0;$x<$arrlength;$x++)
{
	if(x==$arrlength-1)
		$para = $para.$keywords[$x];
	else
	$para = $para.$keywords[$x]." ";
    echo "<br/>";
}

$result1 = "";
$result2 = "";
$socket = socket_create(AF_INET,SOCK_STREAM,SOL_TCP);
socket_set_option($socket,SOL_SOCKET,SO_RECTIMEO,array("sec" => 1, "usec" => 0));
socket_set_option($socket, SOL_SOCKET, SO_SNDTIMEO, array("sec" => 6, "usec" => 0));
if(socket_connect($socket,"127.0.0.1",10000)==false){
    echo "connection error";
}
else{

    if(socket_write($socket,$para,strlen($para))==false){
        echo "write error";
    }
    while(1){
		$tmp = socket_read($socket,1024);
	
		if($tmp[strlen($tmp)-1]=='@'){
			$tmp = substr($tmp,0,-1);
			$result1 = $result1.$tmp;
			break;
		}
		$result1 = $result1.$tmp;
	}
	if(socket_write($socket,"tongbu",strlen($para))==false){
        echo "write error";
	}
	while($tmp = socket_read($socket,1024)){
        $result2 = $result2.$tmp;
	}
    socket_close($socket);
    $data = explode('/',$result1,5);
	$result = array();
	$numresult = array();
    foreach($data as $value){
		$value = explode('$',$value,2);
		array_push($result,$value[1]);
		array_push($numresult,$value[0]);
    }
	$data = explode('@',$result2,2);
	$cpnum = explode(' ',$data[0],2);
	$chapternum = (int)$cpnum[0];
	$paragraghnum = (int)$cpnum[1];
	$content = explode(' ',$data[1]);

}

$json_string = file_get_contents("/var/www/html/Holmes/HolmesCompleteSeacrhEngine/data/caches/summary.json");
$summaries = json_decode($json_string,true);

?>



<!doctype html>
<html>
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="查询结果" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>查询结果</title>
    <!-- web fonts -->
    <link href="http://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900&display=swap" rel="stylesheet">
    <link href="http://fonts.googleapis.com/css?family=Nunito:200,300,400,600,700,800,900&display=swap" rel="stylesheet">
    <!-- //web fonts -->
    <!-- Template CSS -->
    <link rel="stylesheet" href="assets/css/style-starter.css">
	 <script src="assets/js/jquery-3.3.1.min.js" type="text/javascript"></script>
	  
  </head>
  <body>
  <?php
session_start();
echo '<div class="w3l-bootstrap-header fixed-top">

	<nav class="navbar navbar-expand-lg navbar-light p-2">

    <div class="container">

      <a class="navbar-brand" href="home.php">Sherlock Holmes Wikey</a>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"

        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">

        <span class="navbar-toggler-icon"></span>

      </button>



      <div class="collapse navbar-collapse" id="navbarSupportedContent">

        <ul class="navbar-nav mr-auto">

          <li class="nav-item active">

           

          </li>

          <li class="nav-item">

           
          </li>

          <li class="nav-item">

       

          </li>

        </ul>';



	

		echo '<div class="form-inline">

          <a href="home.php" class="btn btn-primary btn-theme">返回</a>

            

        </div>';

	

        

    echo  '</div>

    </div>

  </nav>

	  </div>';?>
<div class="w3l-index-block1">
    <div class="content py-5">

		<h3>chapters：<br/></h3>
		<?php			
			$cnt = 0;
			while ($cnt < count($result))
			{
				$filename = "/var/www/html/Holmes/HolmesCompleteSeacrhEngine/data/".$numresult[$cnt].".txt";
    			$handle = fopen($filename, "r");
    			$ref = fread($handle, filesize ($filename));
				fclose($handle);
				
				echo "<div class=\"container\">"."<div class=\"row align-items-center py-md-5 py-3\">"."<div class=\"col-md-5 content-left pt-md-0 pt-5\">"."<div class=\"form\">"."<p>";
				echo "<table class=\"col-md-5 content-left pt-md-0 pt-5 table table-bordered\" align=\"center\" style=\"table-layout:fixed\">"."<tbody>"."<h5> <a href=\"chapter.php?chapter=".$numresult[$cnt]."&chaptername=".$result[$cnt]."\">" .$result[$cnt]."</a></h5><br/>";
				echo "<h7>summary: <br/>";
				
				$tmparray = $summaries[$numresult[$cnt]]["summary"];
				foreach($tmparray as $asummary){
					echo $asummary."<br/>";
				}

				echo "<br></br></h7>";
				echo "</tbody></table></p></div></div><div class=\"col-md-7 content-photo mt-md-0 mt-5\"><a href = \"".$ref."\"><img src=\"HolmesCompleteSeacrhEngine/data/".$numresult[$cnt].".jpg\" class=\"img-fluid\" alt=\"main image\"/></a></div></div></div>";

				$cnt++;
			}
		?>

		<?php	
				$filename = "/var/www/html/ProKiller/HolmesCompleteSeacrhEngine/data/".$numresult[$cnt].".txt";
    			$handle = fopen($filename, "r");
    			$ref = fread($handle, filesize ($filename));
				fclose($handle);
				echo "<h3>chapter result：chapter ".$chapternum." paragraph ".$paragraghnum."</a><br/></h3>";
				echo "<div class=\"container\">"."<div class=\"row align-items-center py-md-5 py-3\">"."<div class=\"col-md-5 content-left pt-md-0 pt-5\">"."<div class=\"form\">"."<p>";
				echo "<table class=\"col-md-5 content-left pt-md-0 pt-5 table table-bordered\" align=\"center\" style=\"table-layout:fixed\">"."<tbody>"."<h7>";
				
				foreach($content as $value){
					if ($value[0]=='$'){
						echo "<span class=\"red\">".substr($value,1)." </span>";
					}
					else{
						echo $value." ";
					}
				}

				echo "<br></br></h7>";
				echo "</tbody></table></p></div></div><div class=\"col-md-7 content-photo mt-md-0 mt-5\"><a href=\"".$ref."\"><img src=\"HolmesCompleteSeacrhEngine/data/".$chapternum.".jpg\" class=\"img-fluid\" alt=\"main image\"/></a></div></div></div>";

			
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

</body>
</html>
<style> 
 .red{ 
     color:red; 
 } 
  </style>
