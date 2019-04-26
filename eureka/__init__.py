import py_eureka_client.eureka_client as eureka_client

# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init_registry_client(eureka_server="http://10.0.2.84:8761/eureka",
                                   app_name="access-management-service", instance_port=8000)
