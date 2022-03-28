<?php
	session_start();
	$_SESSION = array();
	session_destory();
	header('location:index.php');
?>
