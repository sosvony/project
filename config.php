<?php
	// this is for SQL setup
	define('DB_SERVER','localhost');
	define('DB_USERNAME', 'root');
	define('DB_PASSWORD', 'raspberry');
	// define('DB_NAME', 'test');
	$link = mysqli_connect( DB_SERVER, DB_USERNAME, DB_PASSWORD);
	mysqli_query($link, 'SET NAMES utf8');
	if($link === false) {
		die("ERROR: Could not connect." . mysqli_connect_error());
	} else {
		return $link;
	}
?>