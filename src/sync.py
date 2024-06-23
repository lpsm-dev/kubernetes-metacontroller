# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Controller(BaseHTTPRequestHandler):
    def sync(self, parent, children):
        desired_status = {
            "pods": len(children["Pod.v1"]),
            "services": len(children["Service.v1"]),
        }

        image = parent.get("spec", {}).get("image", "nginx:latest")
        port = parent.get("spec", {}).get("port", "80")
        cpu_limit = parent.get("spec", {}).get("cpuLimit", "50m")
        mem_limit = parent.get("spec", {}).get("memLimit", "64Mi")
        cpu_req = parent.get("spec", {}).get("cpuReq", "10m")
        mem_req = parent.get("spec", {}).get("memReq", "32Mi")
        who = parent.get("spec", {}).get("who", "unknown")

        desired_resources = [
            {
              "apiVersion": "v1",
              "kind": "Pod",
              "metadata": {
                "name": parent["metadata"]["name"],
                "labels": {
                    "app.kubernetes.io/name": parent["metadata"]["name"],
                },
              },
              "spec": {
                "restartPolicy": "OnFailure",
                "containers": [
                  {
                    "name": parent["metadata"]["name"],
                    "image": image,
                    "ports": [
                        {
                        "containerPort": port,
                        },
                    ],
                    "resources": {
                        "limits": {
                        "cpu": cpu_limit,
                        "memory": mem_limit,
                        },
                        "requests": {
                        "cpu": cpu_req,
                        "memory": mem_req,
                        },
                    },
                  },
                ],
              },
            },
            {
                "apiVersion": "v1",
                "kind": "Service",
                "metadata": {
                    "name": parent["metadata"]["name"],
                    "labels": {
                        "app.kubernetes.io/name": parent["metadata"]["name"],
                    },
                },
                "spec": {
                    "type": "ClusterIP",
                    "ports": [
                        {
                            "port": port,
                            "targetPort": port,
                            "protocol": "TCP",
                            "name": "http",
                        },
                    ],
                    "selector": {
                        "app.kubernetes.io/name": parent["metadata"]["name"],
                    },
                },
            },
        ]

        return {"status": desired_status, "children": desired_resources}

    def do_POST(self):
        observed = json.loads(self.rfile.read(int(self.headers.get("content-length"))))
        desired = self.sync(observed["parent"], observed["children"])
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(desired).encode())

if __name__ == '__main__':
    HTTPServer(("", 80), Controller).serve_forever()
