<?php
	// initialize
	session_start();

	// check if user is logged in
	if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
		header("location: welcome.php");
		exit;
	}
?>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>登入介面</title>
	</head>
	<body> 
		<h1>登入</h1>
		<form method = "post" action = "login.php">
			帳號：<input type = "text" name = "username"><br/><br/>
			密碼：<input type = "password" name = "password"><br/><br/>
			<input type = "submit" value="登入" name = "submit"/>
			<a href = "register.html"></a>
		</form>
	</body>
</html>