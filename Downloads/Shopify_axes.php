<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Shopify_axes extends CI_Controller { 
	function __Construct(){
		
		//header('Access-Control-Allow-Origin: '.$_SERVER["CONTENT_TYPE"]); 
		//header('Content-Security-Policy: frame-ancestors msghero.com');
		//header('Content-Security-Policy: frame-ancestors 202.221.139.50');
		//header('Content-Security-Policy: frame-ancestors 210.164.6.67');
		//header("Access-Control-Allow-Credentials: true");
		//header('Access-Control-Allow-Origin: *'); 
		//header("Access-Control-Allow-Methods: GET, POST");
		//header("Access-Control-Allow-Headers: Content-Type, *"); 
		
		parent::__Construct();
		$this->load->library('manage_shopify');		
	} 
	public function index(){ 
 
		 echo "dsgdf"; 
	} 
	
	public function payment_success(){
		$fortParams = array_merge($_GET, $_POST);
		$testData = array(
			'data'=>json_encode($fortParams),
		); 
		$this->my_model->insert_data('testnew_tbl' , $testData);
		redirect(base_url("product/checkout_axes_final"));		
 
	}
	public function payment_fail(){ 
		$fortParams = array_merge($_GET, $_POST);
		$testData = array( 
			'data'=>json_encode($fortParams),
		); 
		$this->my_model->insert_data('testnew_tbl' , $testData);
		redirect(base_url("product/checkout_axes_final"));				
		 
	} 
	 	
}


