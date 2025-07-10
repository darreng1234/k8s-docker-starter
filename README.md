# k8s-docker-starter

## Build and Run Flask Docker Image

1. **Build the Docker image:**
   ```sh
   docker build -t flask-app:v1 .
   ```

2. **Run the Docker image locally:**
   ```sh
   docker run -p 5000:5000 flask-app:v1
   ```

   The Flask app will be available at [http://localhost:5000](http://localhost:5000).

## Deploy to Kubernetes

Make sure that you have a k8s cluster running and connected to your local .kube config

1. **Apply all Kubernetes manifests:**
   ```sh
   kubectl apply -f k8s/
   ```

This will deploy the resources defined in the `k8s` directory to your current Kubernetes cluster.