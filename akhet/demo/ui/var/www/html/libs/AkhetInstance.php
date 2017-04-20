<?php
class AkhetInstance
{
    private $base_url;
    private $instance_id;
    private $data;

    public function __construct($base_url, $instance_id)
    {
        $this->base_url = $base_url;
        $this->instance_id = $instance_id;
        $this->poll();
    }

    public function poll()
    {
        $raw = file_get_contents($this->base_url . '/api/v1/instance/' . $this->instance_id);
        $this->data = json_decode($raw);
    }

    public function get_is_pending()
    {
        return $this->data->status == 'pending';
    }
    public function get_is_assigned()
    {
        return $this->data->status == 'assigned';
    }
    public function get_is_created()
    {
        return $this->data->status == 'created';
    }
    public function get_is_ready()
    {
        return $this->data->status == 'ready';
    }
    public function get_is_running()
    {
        return $this->data->status == 'running';
    }
    public function get_is_stopped()
    {
        return $this->data->status == 'stopped';
    }
    public function get_is_deleted()
    {
        return $this->data->status == 'deleted';
    }

    public function get_instance_id()
    {
        return $this->instance_id;
    }

    public function get_etag()
    {
        return $this->data->_etag;
    }
    public function get_is_shared()
    {
        return $this->data->shared;
    }
    public function get_is_persistent()
    {
        return $this->data->persistent;
    }
    public function get_is_privileged()
    {
        return $this->data->privileged;
    }
    public function get_vnc_password()
    {
        return $this->data->vnc_password;
    }
    public function get_image()
    {
        return $this->data->image;
    }
    public function get_agent_hostname()
    {
        return $this->data->agent_hostname;
    }
    public function get_port_ws_vnc()
    {
        return $this->data->port_ws_vnc;
    }
    public function get_proxies_hostnames()
    {
        return $this->data->proxies_hostnames;
    }

    public function __get($name)
    {
        return $this->data->$name;
    }
}
