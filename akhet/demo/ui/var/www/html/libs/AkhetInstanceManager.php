<?php

class AkhetInstanceManager
{
  private $base_url;
  function __construct($base_url)
  {
    $this->base_url = $base_url;
  }

  function CreateInstance($data)
  {
    $data_string = json_encode($data);
    $ch = curl_init($this->base_url . '/api/v1/instance');
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json',
        'Content-Length: ' . strlen($data_string)
      )
    );
    $result = curl_exec($ch);
    $result_obj = json_decode($result);
    return $result_obj->_id;
  }

  function GetInstances($status="running"){
    $raw = file_get_contents($this->base_url . "/api/v1/instance");
    $instances_obj = array();
    $instances = json_decode($raw)->_items;
    foreach ($instances as $instance) {
        if ($instance->status==$status) {
            $instances_obj[] = new AkhetInstance($this->base_url, $instance->_id);
        }
    }
    return $instances_obj;
  }
}
