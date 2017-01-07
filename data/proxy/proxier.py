import docker

client = docker.from_env()
from quik import Template

temp = Template("""
  server {
    listen 80 default_server;
    #for @worker in @containers:
      location /worker@worker.id {
         proxy_set_header X-Real-IP  $remote_addr;
         proxy_set_header Host $host;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

          proxy_pass http://@worker.ip:8081/;
      }
    #end
      location /static {
        proxy_set_header X-Real-IP  $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_pass http://@worker_static_ip:8081/static;
      }
}
""")

containers = map(lambda item: (item['Names'][0], item['NetworkSettings']['Networks']['bridge']['IPAddress']) ,client.containers())
containers = filter(lambda item: "worker" in item[0], containers)
containers = list(map(lambda item: item[1], containers))
containers = zip(range(0, len(containers)), containers)
containers = map(lambda item: {'id': item[0], 'ip': item[1]}, containers)
worker_static_ip=containers[0]['ip']

conf = temp.render(locals())
with open('default', 'wb') as out:
    out.write(conf)
