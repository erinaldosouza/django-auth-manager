import py_eureka_client.eureka_client as eureka_client

# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_servers = "http://eureka-peer1:8761/eureka/, http://eureka-peer2:8762/eureka/, http://eureka-peer3:8763/eureka/, http://eureka-peer4:8764/eureka/"
eureka_client.init_registry_client(eureka_server=eureka_servers,
                                   app_name="access-management-service", instance_port=8000)
