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

        echo 
        '<div class="form-inline">

    

            <a class="btn btn-primary btn-theme" href="main_character.php">主要人物</a>

          

         </div>';
        
        
/*
if (isset($_SESSION['uname']))

	{

		echo '<div class="form-inline">

		<label>欢迎您，' . $_SESSION['uname'] . '！&nbsp;&nbsp;  </label>

          <a href="profile.php" class="btn btn-outline-primary mr-2 btn-demo">个人中心</a>

            <a href="logout.php" class="btn btn-primary btn-theme">退出登录</a>

        </div>';

	}

	else

	{

		echo '<div class="form-inline">

          <a href="login.php" class="login mr-4">登录</a>

            <a href="signup.php" class="btn btn-primary btn-theme">注册</a>

        </div>';

	}
*/
        

    echo  '</div>

    </div>

  </nav>

	  </div>';?>
