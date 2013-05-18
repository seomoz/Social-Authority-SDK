<?php 
	$uri = 'https://api.followerwonk.com/social-authority';
	
	// Enter your Access ID and Secret Key from http://followerwonk.com/social-authority below
	$accessID = '';
	$secretKey = '';


	$time = time() + 500;
	$signature = urlencode( base64_encode( hash_hmac( "sha1", "{$accessID}\n{$time}", $secretKey, true ) ) );
	$auth = "AccessID={$accessID};Timestamp={$time};Signature={$signature}";

	// Initialize an array of users. We call the API once for each of the usernames. There are more efficient alternatives.
	$users = array('ebinnion', 'perigrin', 'randfish');

	foreach($users as $user){
		// Fetch the Json object and decode it into an array
		$response = json_decode( file_get_contents( "{$uri}?screen_name={$user};{$auth}" ), true );
		
		// Use the commented API call below to get the result returned as an object
		// $response = json_decode( file_get_contents( "{$uri}?screen_name=randfish;{$auth}" ));
		
		// Uncomment code block below to see entire Json response
		// echo '<pre>';
		// print_r($response);
		// echo '</pre>';

		// Below is an example of how to pull data out of the response array
		$screen_name = $response['_embedded'][0]['screen_name'];
		$user_id = $response['_embedded'][0]['user_id'];
		$social_authority = $response['_embedded'][0]['social_authority'];

		echo $screen_name .'<br>';
		echo $user_id . '<br>';
		echo $social_authority . '<br>';
	}
?>