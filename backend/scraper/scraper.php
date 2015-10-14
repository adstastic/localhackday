<?php
$html = file_get_contents('https://roombooking.ucl.ac.uk/rb/bookableSpace/viewAllBookableSpace.html?invoker=EFD'); //get the html returned from the following url

$building_doc = new DOMDocument();

libxml_use_internal_errors(TRUE); //disable libxml errors

if(!empty($html)){ //if any html is actually returned

    $building_doc->loadHTML($html);
    libxml_clear_errors(); //remove errors for yucky html

    $building_xpath = new DOMXPath($building_doc);

$link = "https://roombooking.ucl.ac.uk";
$collection = array();
$building_rows = $building_xpath->query("//table[@class='rooms']/tr");
$filename = "data.json";

$counter = 0;
foreach($building_rows as $element){
	if ($counter != 0) {
		$node = $element->childNodes;
		$td_a = $element->childNodes->item(6);
		$a = $td_a->childNodes->item(0);

		$data = array (
			"name" => $node->item(0)->nodeValue,
			"size" => $node->item(2)->nodeValue,
			"type" => $node->item(4)->nodeValue,
			"href" => $link . $a->attributes->item(0)->value
		);
		
		array_push($collection, $data);
	}
	$counter++;
}
echo json_encode($collection);
file_put_contents($filename, json_encode($collection));
}
?>