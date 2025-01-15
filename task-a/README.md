**Architecture Overview**
**Core Components:**
1. Backend (BE):
    - FastAPI for serving corn optimization algorithms.
2. Frontend (FE):
    - Dashboard for real-time crop analytics.
3. Database:
    - PostgreSQL in a container to ensure consistency across deployments.
4. Machine Learning (ML):
    - Serving pre-trained models 
5. Monitoring and Logging:
    - Prometheus for metrics collection.
    - Grafana for dashboards.
    - ELK stack for logging.<br><br>

# Deployment Strategy
## 0. Container images build process before deployment (For All env: on-premise, cloud and hybrid) 
- Let's assume that, Uni-Corn LLC still have no pipeline to automate container image building process, or they have one but still inefficient.
- Set up an Internal CICD pipeline (build pipeline) to automate the container image build process of our in-house software, FE, BE and ML.
  We should not load the ML, FE and BE source code into the container, but rather the binary executable. This approcah is use to protect Uni-Corn LLC intellectual property. If customers can access the source code, it could potentially give negative impact to the company's business in the future.
- Set up a container registry to storage and container images produces by the build pipeline. 
- Set up a automation test pipeline to test the functionality and compatibality between the components. The end result is an archive file containing container images of FE, BE, ML, DB and utility tool like monitoring (Prometheus, Grafana, Etc.), and also `docker-compose.yml` file, and documentation containing instruction for the customer.
- Set up object storage in the cloud such AWS S3, to store archive file produced by automation test pipeline. 

**Here is the diagram for of internal pipelines to produces container image and archive file to be distributed to customers:** [Link to diagram](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&target=blank&highlight=0000ff&edit=https%3A%2F%2Fapp.diagrams.net%2F%23G1clO1_MVE1d_u_N92mE1u4UqUQpk9__W8%23%257B%2522pageId%2522%253A%2522GuBeoLhZzBAxccnSfArH%2522%257D&layers=1&nav=1&title=Design%20exercise.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22GuBeoLhZzBAxccnSfArH%22%3E3Vnfb9s4DP5rAmwPLRLbSdvHNunaw27AsA647l4G2WZsYbIVyHJ%2B3F9%2FpC3FsuOs7q4r0ntJLEoiJfLjRzoZ%2BfNse6fYKv0kYxAjbxxvR%2F5i5HmTq9kYv0iyqyXBxKsFieKxWdQIHvg%2FYIRmX1LyGIrWQi2l0HzVFkYyzyHSLRlTSm7ay5ZStK2uWAIHgoeIiUPpXzzWaS29nI4b%2BT3wJLWWJ2MzkzG72AiKlMVy44j825E%2FV1Lq%2BinbzkGQ86xf6n0fjszuD6Yg10M23C%2B%2Br7993abhI3gfvb8%2FLrPx9zOjZc1EaS488mYC9d2E%2BJDQw03J0WfeeP4H6p4vyCZfgeA52KUo3682d9U760AlyzwGOsMYpzcp1%2FCwYhHNbhAyKEt1JnA02e9272QPCErD1hGZO96BzECrHS7ZtoFj8DYJzHjTRG9iQ5I6kbNAZQYwyV5z41N8MG59hou9p108l7lm6FCF675AwovK7gk617s8Ne8GPd7tOAny%2BJqYAEeRYEXBo7Zf2k6ELdePZoaev5H8fGpGi62zbLEzg6OeLWSpIng6%2FzRTCeinQQRxi60O4%2BTEYdoTBitTIJjm6zbH9cXGWPgsOd5sD4Ng3IaBd9EJb31vs8vlpK6iaUeR11FUO%2BZAUQWV%2FbV%2FHT3TU0APgkbtHt2Bs4uGzbZq9N9R5w1E3ex%2Firoui3UV%2FWbUzZ6uCNellthBcJlTnKDQp152p8GpVYaLAXVXyJJamwctFfWBp%2BjYy5NraK5enDR%2FkQBft1TPBpLmxUmR5tTvkGYXFm%2BlVNs0cGA3OcfxbZ4gJ1at86os0upVMIbqNRE%2F7ri%2BL0Ob2DFf27z2aK99tQl5zqqYwBaiUrNQuFzg7OpR5LuKIqeR51lFKeOlkhkdJwXH0kDlASn%2FbK91qLu6ozuhOm8PofqJ9uOL%2Bg%2FWlXaSHglNt9OcCZ7kxAGYbHg8%2F4Zoj%2BPL9bWZyHgc0%2FZeHm2TxAtQ6dmk20H0cKnfx6X%2B7%2BJS%2B2uIg2oqRtAX7wIf5BI%2FPtyOvDmhznx%2F%2BrP%2BXtzQEXMCYqm54JpXewT%2FQfoymXNUzfPk7UVu3%2Bp1ycctgsGrBs4%2F2l78PKUr0vpad3Q1JyBhQqJss1fHL5LZCiUhBpHcEILeANB0AWrNIyjOD5O3ojTTOJLegq2rYPcyBxol7ljy51KdY6A%2BfqTAnr1CZyyjH6DO6AaygPNdJp5rJxhqp8wQUlb4jufIfGVEw%2FdkUtJ9o7JAPXT1gcanHeMhQlnUfqzPsUmlADdEdiBzPA0l3DsbpPd1XrY9sveGCXVzDyydTWRYBQYVpVT7hzjwrbNzMDvSqTg57l29ao4f%2FrhkybkdmL5s%2FAIs3tkSHVNR5mGpm6K9xyUhBDhii%2BC65swwgsqBKEI20lW6Kyg8pA8IX28vxpcDCvBL8TgOmx%2FX6y60%2BYvCv%2F0X%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
![image](https://github.com/user-attachments/assets/6ae9fab6-dad3-4fa8-8893-eb48ad118388)



## 1. On-Premise for Air-Gapped Farms:
- We pack our product into an archive file, which produce in previous section (`Container images build process before deployment`). This archive file contain FE, BE, ML, DB and utility tools container images, docker-file template and documentation containing instruction for the customer.
- To secure the archive file, we can encrypt it with encryption tool such as `gpg` or `openssl`, send the password or key to the client via SMS (remember, no internet!), or hand over the credential when directly meet the customer, so the physical drive and and credential information is send differetly to the client.

**A. Deployment architecture with Docker Compose**
*Core Services:
1. FastAPI Backend:
    - Containerized FastAPI app running the corn optimization algorithms.
    - Exposed on a local network port (e.g., http://localhost:8000).
    - Scalable by increasing the number of backend replicas in `docker-compose.yml`.
2. Dashboard Frontend:
    - Containerized Dash app running on a separate container.
    - Communicates with the backend using the local Docker network.
    - Served via Nginx or directly exposed (e.g., http://localhost:8050).
3. PostgreSQL:
    - Containerized PostgreSQL instance.
    - Data volume mapped to the host machine for persistence:
    ```
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
    ```
    - Preloaded with required schema and data during initialization.
4. Monitoring:
    - Prometheus:
      - Configured to scrape metrics from the FastAPI backend and PostgreSQL.
      - Uses a prometheus.yml file for static targets.
    - Grafana:
      - Preloaded with dashboards tailored for the system.
      - Mounted as a volume or imported during startup.
5. Logging:
      - ELK stack for log collection and storage.

**B. Docker Compose File `(docker-compose.yml)`**
Here’s an example of a `docker-compose.yml` file for the on-premise setup:
```
version: '3.8'

services:
  backend:
    image: my-corn-backend:latest
    container_name: corn-backend
    build:
      context: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/corn_db
    depends_on:
      - postgres

  frontend:
    image: my-corn-frontend:latest
    container_name: corn-frontend
    build:
      context: ./frontend
    ports:
      - "8050:8050"
    environment:
      - API_URL=http://corn-backend:8000

  postgres:
    image: postgres:14
    container_name: corn-postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: corn_db
    ports:
      - "5432:5432"
    volumes:
      - ./data/postgres:/var/lib/postgresql/data

  prometheus:
    image: prom/prometheus:latest
    container_name: corn-prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana:latest
    container_name: corn-grafana
    ports:
      - "3000:3000"
    volumes:
      - ./grafana:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_USER={saved in .env file}
      - GF_SECURITY_ADMIN_PASSWORD={saved in .env file}

volumes:
  postgres_data:

```

**C. Steps for Deployment**
1. Assume the on-premise environment is ready
2. Extract the archive files from previous step.
3. Given the container image is ready, container image build is no necessary anymore, just start the services:
```
docker-compose up
```
4. Validate the Deployment by access each service's endpoint.<br>

**D. Configuration and Customization**
1. Use `.env` files for environment-specific configurations:
```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name
```
2. Volumes, map volumes for persistence, for example:
    * PostgreSQL: ./data/postgres
    * Grafana: ./grafana
3. Network: Use Docker's internal network for inter-service communication


**Here is the diagram of deployment strategy for on-premise deployment:** [Diagram](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=OnPremise.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%220IWan661LNIZXUq_8_J4%22%3E7Vxbk%2Bo2Ev41U7X7gMvyBeNHmIHkVJ1kqZ3dZPdpSmANKMdYrC0YyK9Py5aML%2BIygIGzx6RyBjfWrfvrVqvV0pP9vNj8FOPl%2FBcWkPDJMoPNk%2F3yZFmua8K%2FgrDNCKjruRllFtNA0naEV%2FonkURZcLaiAUlKL3LGQk6XZeKURRGZ8hINxzH7KL%2F2zsJyq0s8IzXC6xSHdervNODzjNpT4xL0nwmdzVXLyJS%2FLLB6WRKSOQ7YR4FkD5%2Fs55gxnn1bbJ5JKJin%2BJKVG%2B35Ne9YTCJ%2BSgHu%2FjYc%2FfwTG28RX%2F66%2FN3yf2Mdx5Gd41s1YhIAA%2BQji%2FmczViEw%2BGOOojZKgqIqNaEp907XxlbAhEB8Q%2FC%2BVZKE684A9KcL0L5K%2FQ43v5HlDdc9fhfWV368LIpPW3lU9ZX0cG9PJCkhK3iKTkwcGR2JZpwPCP8wJu%2BmwsLUE7YgkCXoGBMQszputwVLOE2y9%2FbSQS%2BSKF8RkBSXdY4XMmmnqxuCB0eTODLjKdsyQjvDLhQlGX3fyumfugkqTT68ALqLTdZMfm7qujfCYkTVRt0N6uw3AiQCw1XsJN8I3w6V8BY8ZBG5DnXTFN25ZmFLE4L2PDfSHBjMItxQMnut4hFAmrvNAyrr78APeEx%2B0YqLwc4meewXJOYU9Djr3hCwjFLKKcsgt8mjHO2KLzQD%2BlM%2FMAFeAdYPk2hLyQuw1b0XWIaWepZDl40iZNlNtB3uhH9GCwZFbUM11BZIisBM7AUBRabmbCYBv5IHGOVMl4xVPSMbA5DvI5HVcA3bUOCRhrdjqNs0MfOhHm9jDQvWC9FuzqK3f0oPhW0lrMHtDV1eCHLkG0XJK33lceYk9k2tf2xHsQH8R7Q9bl6dnqX4S9eCPhFk0T8%2BUfUGcdkQRMC1QyjNY1ZlA3o%2B%2Bj%2FGf0EsqarVWrF3oCa8LKO1vS3quYLGgTpLPYxp5y8LnE6TXyALtZmtmtoo6scmVwXUV0XLeVOFJURKaW9vjZ6Gm2sWvIPughxalYTmCKV3bsaW6wKW5BdZ0vP1LDF6zXGll7zbDkgj73Mspwyr5BbZ1UOsyKr3OZY5TfgleyzNs%2BrBGZsEh8wMscdlb3G8Pr9ZVFnqYx3Ez1Olji6qIO1oYP3sSbHJses2Tsb7ZjA%2BPAkd7lSDytFtzt4coVnKFYbiXTS9jmKRa9Ski7Q3p5ee5W21pUV6exatyld7aLjZk3Dxqove0hc%2BdLWrHrhFf99NOr2TXOfWGqucUgneILfpiFbBQae4%2BQNL5chAEP48m9zYN4bXmMa4gkNKd%2B%2BCRzTaTPizN1rz1BLRylhp2c4rrn7eE5N4l1k%2BF3NXIYM5RlfX%2BxWK%2FbriR2cYaNrl8RuW6bhOAW5uw8hdrsVe6PajjzXMIuf7kOI3bmhQzYaiuKS%2BxdEi34QR0BVY7mG3ytjCZllLKEalnyNq2A35io0EWzch6JBi6KzUGQCigqQKU9Klt3Njcwxj7M5GHVvCKNfvrYwOgNGyC3DqBwxtr2uoRyH%2B8FIF6ZqCkYvgxZG51gj8I9QCTqueeKC9wzcsMkfwk2Ffod4SuYsDNJtk8KADgPKLwxGIrAgul3wt7rZI5514eKClHM%2FOBV5PJVFrapbrJzfkuTAV%2B6mn6faBln2AXoo9rEGePptlvazUp8CWUjeuQZi%2BaZXVguLgXHVHsHQaDT7V7qFa%2B4IYkjK0R9jDhAWFQIsTAeoIDE8DCiXA48Zx7yIYBJTeEXA%2FiUG0eFoFpLxjjiIWLo%2FJ19PezfGQZC1m%2B6phSH76KuNfEGRO%2F2FVshmiSO1BoFmVnFC1%2BSfJNkFZwn0UZZAT%2FWNubSlScLCFSf9XHiopoMD07DAUj6b6f%2BgktZzStTRvDoRiSdVQ5moo3murkqkabtKszREbZWats1KJ1PDc0uv2NEYEMcxTKtuQ3LD8gkjAo%2FSjlzDpnhma1Nam9LalAe3KairXxc9rl1BrV1p7UprVx7MrpRXyaZ%2BlezszM%2BDGRWrNSqtUWmNymMZlZ0LohZAVq9uVLQpYpdblNNCcd5d0sSzNg%2Bmex9M5DqaBK7OIhzNAff2ZGjdJgdcdbPd020qg8OxYCL3d5%2BH2NP1moh%2F70v9H0bxdslB6qISFotTMaqtWL3ztzXMDwvy90vi402fEPD6fYS6%2B%2FD5%2FZ4QyFjfpF7YvmW45d1Ex0YGqu9Je47hOnVd8G2jsQME3im5uZJvdJGe6SrKRS%2FJowDY43ICzN7TD7ySNtZXYtXKWPbnZc65OLTWF5ywRtMgQgYFX%2B6dwiwZG1No0RoF4D3CH0FPBKMwgIPisDNlMSjkyAL5jNJ6OsjqGUvwEpuCg2P6hlcwiX557eN4puGjQ5kLjsZhcT7vr5yID11CcgUfChclE3RoltTMqVXdryq8kjVdgGRGMPuJ0SRTLIT3wqbfQNDJetbo9Kb21dR%2BXD3qJXIE%2FLpwGtvIVWnorXCQ5RtFnVJT%2FC637P7COiFd%2BMcUVq%2FsNGb5n%2FeX1wkJnz%2BIvCqWz7F7Ou9FNy%2FZlvF5z%2BXCYFzPKYzmwYJxw67tmBpnvA3GtcG4%2F%2BtgXOWkXT0Twd6zY%2Bie4dqeFYrrnRAM%2Bu5WQtbRldCEbdKvnZDNmCBYjqBuwk6QTi75ekgTsUIOcnRWbjQyPfvCo5tHjo34teCuBlNdzYzU2HGw3hnJuepWFhU0suvxI5ANxzT67P0RecOa0NX%2Bg4sXZ3serUhb5JNnOZs4lHqCJILC9Qf37ouI6YsYhggrTrZXOA6rP3Cq7%2FVZkDqFwZnBATO1ZMnnkoXbU7OnBiNd51D0SXeoVrdB5jdmRXXxyPYA%2FG0OwF%2B%2FxxHhHyz%2B1upyE%2FdXVJxq5a%2Fe7UA8Qrc8WDKO6RpmQHjly%2FiSjTPly98gbIP%2FXMVEMFmqhVj%2FWqPxahLS6duX8Vs%2FCACFCUkuj%2BgcRo7tV9ZjOufZ1SzGrMagowtlV6DzRbA6wqKyl19fn7JjRfuu16hIuZwzcSTK0xzfu1b1CjHNDWL5BUU30tpejVuPnIMibczxiwgVpI4moUi7da8sFITsBxXAqXc%2B%2Bqem%2B0iZ3IvTvi7E09T8tIqo2F2OjJBNhc06f4a6vu06colYr1c3U7rDQ7e1U5Zuiri93jzAHavOyfqW5WNdoG%2By6Fg4QCWElBNaOrZdcQ2yQchyO9GfUFUtmSEbZq2qFEX5mC4AlqmL3H3vkd%2Bb5cAcuzXVqtkSW3OS%2BaZJLcjS7cU3lQH4Kraq8kgdOK3hOxSbRSnp9VVcszAFFr9Tkb15tzPyt7m103fLC49OHkkqbgV51znVDo%2B7W8Aza7G7S90e%2FgU%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
![image](https://github.com/user-attachments/assets/bd192fd5-7765-4166-8e40-208c3c1443b6)


**E. Data Security**
1. Database Encryption:
   - Use PostgreSQL with encrypted storage (configure host disk encryption or use Docker's volume encryption).
2. Service Authentication:
   - Secure backend endpoints with API keys or JWT.
   - Configure Grafana with admin credentials using environment variables.
3. Transport Security:
   - Use a reverse proxy (e.g., Nginx) to serve HTTPS traffic.
   - Generate self-signed certificates for local use.<br><br>


## 2. Cloud Deployment
Key consideration when design deployment strategy on Cloud environment:
- This infrastrucuture is managed by skeleton team. It means less infrastructure burden is better.
- Development velocity: as a startup, expect high-velocity rollouts on Uni-Corn LLC.
- Deployment high reliability
- Cost effectiveness
- Technical debt implications: how reversible is this decision?

**Design decision:**
Based on above considerations, here is how the Cloud environment looks like:
- First, let's assume the client use their own cloud account to run the workloads, not Uni-Corn LLC account.
- Let's use AWS cloud provider just for example in this exercise. We can also utilize similar services in other cloud provider as per customer request.
- We will utilize the pipelines in `Container images build process before deployment` in previous sections, we will integrate it with our clint cloud environment.
- Setup a VPC in client cloud account. Setup private subnets, for now all the workload will be deployed on private subnets.  
- When comes to running workloads on container, there are 3 options we have: Run on  Basic EC2 instance, EKS clusters and ECS clusters. Lets puts pros and cons of each option:
    * **Basic EC2 instance**
        - Pros:
            * We only pay for the EC2 instances and associated resources, potentially saving on management fees.
            * We have full control over the EC2 instances, OS, and container runtime.
       - Cons:
            * Manual Scaling: We need to manage scaling, load balancing, and failover by ourself.
            * Higher Operational Overhead: Managing the orchestration, scheduling, and monitoring of containers is entirely our responsibility.
            * Complexity: Setting up a resilient and secure container environment requires significant expertise and effort.
            * Limited Observability: Without third-party tools, monitoring and logging may not be as seamless as with managed services.         
   * **EKS (Elastic Kubernetes Service):**
        - Pros:
            * Feature-Rich Orchestration: Leverages Kubernetes' extensive ecosystem for orchestration, monitoring, networking, and scaling.
            * Scalability: EKS can handle thousands of containers across multiple nodes with auto-scaling and load balancing.
            * Portability: Kubernetes is open-source, making it easier to migrate workloads between cloud providers or on-premises.
            * Community Support: Kubernetes has a large community with rich documentation and tooling.
            * Flexibility: Supports both EC2-backed worker nodes and AWS Fargate for serverless containers.
        - Cons:
            * Complex Setup: Even though EKS is managed, configuring Kubernetes clusters can be complex.
            * Cost: EKS incurs an additional fee ($0.10 per hour per cluster), and we still pay for underlying resources (EC2, Fargate, etc.).[1]
            * Learning Curve: Kubernetes has a steep learning curve, which can slow adoption if the team is unfamiliar with it.
            * Overkill for Simple Workloads: May be unnecessarily complex for straightforward applications.
   * **ECS (Elastic Container Service)**:
        - Pros:
            * More automated scaling compare to basic EC2 instances.
            * Lower operational overhead compare to EC2 instances, orchestration and scheduling is managed by ECS.
            * Lower operational overhead: We can use cloud service for monitoring and logging, such as AWS CloudWatch to monitor the infrastructure level and container level.
            * Simpler setup compare to EKS.
            * There are two options for launch type, we can chose EC2-backed for more control or Fargate-backed for serverless and simplified resource management.
            * No additional management fees, we pay for the resources we use (EC2 or Fargate).
            * Easier Learning Curve: Simpler to learn and manage compared to Kubernetes.
        - Cons:
            * AWS Lock-In: ECS is AWS-specific, making migration to another platform more challenging.
            * Less Flexible: Compared to Kubernetes, ECS has fewer customization options and a smaller ecosystem.
            * Scaling Limitations: While ECS can scale automatically, it may lack the fine-grained control and scalability features of Kubernetes.
            
      I made a table to summarize the comparison of these there.
![image](https://github.com/user-attachments/assets/11b056da-6211-466d-be1e-9d349c45142b)
 
    **Based on the requirement and comparison above, I chose to use ECS because of this reasoning:**
    - Scalability: ECS is easy to integrate with AWS autoscaling feature, we only need to setup scaling policy.
    - Simplicity: Elimate the operational overhead for scaling and container scheduling in basic EC2 setup.
    - Deployment velocity: ECS is quick to setup and managed, easy to integrate with CICD tools and other AWS service, so ECS is a great choice for automating deployment with minimal overhead to enable high velocity deployment.
    - Reliability: ECS is highly reliable service, AWS offers an SLA of 99.99% uptime for ECS. [2] 
    - Easier to adopt compare to EKS, which often require complex setup given the EKS flexible nature.
    - Suitable for low number of microservices. Using EKS is overkill since in this case, Uni-Corn LLC only have 3 in-house microservices (FE, BE and ML) to deploy.
    - Cost effective, we only pay for the EC2 machine used to run the workload, no need to pay for management feature like EKS.
      
- We use Load balancers between the services, for this specific case we might need 3 load balancers (LB). 1 LB for users⇔FE communication, 1 LB for FE⇔BE and 1 BE for BE⇔DB connection.
- We need an ECR in customer account to pull container images from Uni-Corn LLC ECR.
- Setup a CD pipeline (eg: Jenkins or AWS CodeDeploy) in customer account to deploy container image from ECR to ECS clusters.
- We will run the database in AWS managed service RDS. Running database in ECS require us to setup persistent storage outside of ECS, which is more challanging than managing RDS. Here are some reason why we should use managed service for DB instead of managing the DB in container by our selves:
    - Data Persistence Challenges: While ECS supports persistent storage via EBS volumes, managing this storage with containers can be complex. If a container with a database crashes, ensuring the data is safely stored and properly recovered can be difficult, especially if multiple containers are used to handle replication, failover, or backups.
    - Data Persistence Challenges: : While ECS supports persistent storage via EBS volumes, managing this storage with containers can be complex. If a container with a database crashes, ensuring the data is safely stored and properly recovered can be difficult, especially if multiple containers are used to handle replication, failover, or backups.
    - Harder to Achieve HA: Achieving high availability (HA) with ECS-managed databases is much harder than using a managed database service like Amazon RDS or Amazon Aurora. Setting up replication, failover, and automated backups manually in ECS can be error-prone and time-consuming.
    - Complicated Backup Solutions: Managing database backups inside ECS requires configuring custom scripts or tools to periodically back up the data, and ensuring that backups are done consistently and safely. With managed services like Amazon RDS, backups, snapshots, and point-in-time recovery are handled automatically, which reduces operational overhead.
    - Security configuration: When running a database in ECS, we'll need to manage IAM roles and permissions for the containers, which increases the risk of misconfigurations. Meanwhile AWS RDS automatically handles IAM integration for database access.
    - Encryption: We’ll have to manually configure encryption at rest and in transit for the database when running in ECS. AWS RDS, on the other hand, provides built-in encryption features and security compliance for databases.
    - Database Patches and Updates: Keeping the containerized database up-to-date with security patches and updates requires manual intervention and regular maintenance. Amazon RDS handles this for you with minimal downtime through managed patching, making it easier to ensure the database remains secure.

- For monitoring and logging, we will use cloud service, for this case is AWS CloudWatch. Chosing monitoring solution is a thread off between operation overhead and cost. But given the condition of Uni-Corn which required high velocity deployment and managed by skeleton team, I opt to use cloud service for monitoring and logging, so we can direct the team effort to focus more on delivering new features with high velocity and quality deployment.<br>
 
**Here is the architecture diagram for deployment strategy on cloud environment:** [Diagram](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=CloudDeployment.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22lF_7-W5QHEBgdZ2kCPPr%22%3E7V3tl6I2F%2F9rPKf9oIdXxY%2BOOrvbzjyd7my7209zImSUDhIeQB371zeBBCEEBQVlt9g9HbhAyMt9%2Bd2bm9BTp%2Bv3Dz7wVo%2FIgk5Pkaz3njrrKYqi6RL%2BQyj7mCKP9FFMWfq2RWkHwrP9D6RE%2BuByY1swyNwYIuSEtpclmsh1oRlmaMD30S572ytysm%2F1wBLmCM8mcPLUr7YVrmKqwdpF6B%2BhvVyxN8sSvbIG7GZKCFbAQrsUSZ331KmPUBgfrd%2Bn0CG9x%2Folfu6%2B4GpSMR%2B6YakHTHmy2FnfPn181r59sB8%2F6duwL9PR2AJnQ1s8%2BfqMCRPTRBtccFz1cM%2F6w0O2G0Z9qt%2Fhf%2FiVU6mn4ytTcjZQdI7An4%2ByBDl%2FRsrIEvjzUZYg88XL3PtlvoIpQu4sU7zEvV9KVRD%2FU%2B%2FQJnRsF04T7pMwcekDy8ajMkUO8jHNRS7uvbtVuHbwmYwPdys7hM8eMEmv7rDoYNorckPK%2F7LCzmnHk1Ixh4cAv8unZUQjAf35FsYDEt%2FjOMAL7EXylA%2FNjR%2FYW%2FgZBnHhhIp50SPH6%2FclkdsB2AXaYOmjjRdV%2FxN%2Bl%2FDqC6BsgYsIffQGWRN7ijqdKcpQIxW3HYdr%2Bhb6oY2FauLYS1JyiMiLAD1z4GtUIu4P210%2BRGczVaJ9IHqFBYIVtGhj8oJAZYO8Fb6nSFQwPkC0hqG%2Fx7fQq9qYCilVU31Zo4TdQehlid21Skm8MdSptqGaZpmUfhBGfEDlsYJsjnOi2VOGDumpBT5YhlHTYwLpp4ycDv%2B%2FQexCPx74Cb5B1rz3%2BDF6nRU03QQhrraPz8GajI27CLzUCxY%2Bu5NxAL2AWxa%2FPFshTE5VktMheFDCrDwwTjAhYWkBw6xtyyKPCyUHc6ZrHWOHo5rvNJNQplAFLKEIOILdVztDkOfLcgQWJlfIEWYsToQb%2FOXiJ6LR8CH783NUhERGqE96t7%2FGJj2%2Bm3a2gHcSxYSLhEs7iNqa8EFck2ztCDtdpW436I6fYgM6n37%2B%2BUQvHBWS4A2G5orytNDqCi2vyPoKLXDeCmdui%2Byi4A08UUQb5Yly%2FjZmSvNEEU2EG%2FinZcHTMvd0sdXmbA3%2B757IZsacYfp8NiIYT2AAX6Mfb52YJnsAC%2Bg8ocAO7ci4LlCINe5J25hoxJS2PIUUQODFzXq130k9xObehwHa%2BCaMjT0GCoHI7EPTb0SnMsOrZOyuOlIGup5TsyMjr2UZrXYtq%2BYh8eV21yiwu38%2BTS%2BxpB0a%2F0%2Bj8a1nKiJNZEy1%2B%2Fv7RqH4ZHI3ujNKQPF69IQqZwG6PhTqiaEAjo3kxvCYCKHzZnxnrx0Q9XwQAp%2FxVIXOUqt3lp7pK1kAXIeKnu8pfdhUT7EaXMWXmU8J%2FjId7NJEDk157RrTLHsrwqu5BzP3tdHFSfizNOf0OTGTb%2B3yqLKAcY4awZkIAB0bhyQuJ%2FHajEN%2B9%2FfDiQD5Ub2aU%2BKOvQAL8GI6aGMNwAoEL8DzHDziBAC%2BrHDnvYAtsB2wsB073L8E0N%2FaZMybG16ZG15F0wasQ9PKQR6MhyJFmujcS8Z5ulE%2FGr99ePvl94n3ZTL7qqi%2FQxbrSI0qtJaQGVzkhyu0RC5w5gcqJxOHex4QMWnRYP8Nw3BPVS7YhCjLChX7OYbLx5iVdiXW80sYHmkt7VzSxKPD5kMHc8s2G4quX8YqhBUuVs73c%2FI4ZfUbxZB8Ar7AAZUJFAjmFQrQ5CKBF2Cr5gR3qA2yRt0QAiBRgLI53axdkW%2FuzuWbdtj075HlDlaAeeeyPhiN8ohAEnCd1hjXDa%2FIdY8PnbaqzjqaPB7o0uEnZ7hI04xyLNSY4tJE3kgHKs9VFCNjoMvjw8%2B4PcYUD7sI53TDfsmwZ6O3sjYYp3%2FGsA2uxTXtxQMCFr6OGQO4ZsXgA8eJwlhm0zMLgkikOkizmoMb%2BLJgzcuztW7o2EAXBl0b5EYu5iWYvx%2BOBYynNKVs9EK2qwOLdrODGVprZgenY0UXgLAfdXbQt4JGgWRWqNXxOGtgtJyMNzVTKLQsLJp23agV7mR%2F%2F408j2HXkBH%2BigiyoTDC7J2%2BIj7bp8%2BeoG%2FjLogmr86IJ6cDYcdMbjoOdhSIXz8QJh7PDiDWaZKl0UBX0%2BKatdD56NUNwKEsimF1Q37mkCvamAtTCiaQmh3lj%2F98m2%2B%2B%2FLl4Nl%2FHnxF4MT71x331Fnq6bqXKBObk7ALTj23RqiIk3IlYbSIWB1hS4Ta1WZFDi7%2FJyODWOcCEK%2BRY0M8usjjODkaqfZR%2FUpxwEDseyxZl6qQYIxn6iEt8kz6q8JzAxpvH6MPol0f78Q%2FTHQLT74D5tozqyZXHJdHw0D3B9HEpyMcdx9cozrv5EqkY6UAgTWK8%2FQRCzPWkQNyTkoapeMTA3LJD2nAfhSBMB4xTaM%2FHQwfcpQNTEPDORZH7QW%2BPavcELCt%2Bb%2BQyOA7aTdhqGpr%2BRJyj1FvguwdcJnbiPCeI60ifKEqZAosAOZsQTpLBS%2B5MObiXu7PnOIfF%2FqvY0RV5xMIiC91aJeuYNqZUjBJmW9EkdlNahySR%2BwoaBJ9SJVLFjIjieJ0ZOXPEdZmfUFYNaSClf60I3irdVE2d8RQMHiTlexh2UdpXF7T%2FwYL2mqafgWXrieJfiGIVrUOxHYrtUGybUKzKzQGqIwGKlW6JYRXjNJpJR6ags0C7dFAqIuALK%2BTb%2F5AVKA4hulbE1cQ8OCAIbDOrTzATbxP7kw1r4Ucpgxq97AIFIxIGOyQTDX0MESLFQQjxRIOqaPT8MM9ATvapE36WIT1x0UtPW%2FSuO2VxNJnx9JwFZaCT0bUU17HdIjKLLSitdBCOvuGJaJFeKmOfmyTTeWaOm04fO%2FBzvqRxtqBk7w5WUNw1uYIw74F96jaq5gprbGhCKT2IWVzgQeiSPm0iGjXu7Hhnxzs73iY7Ps5HuNsXjhImv3eBiXOhm6Fm54q5xPNbBymEs4raUezWVPYHxWQUQ1FAxq6cB8bULBwbSMNWZJEk%2B32dnPC8WRrJ3Oh%2F%2Fft%2FypfN5lfrRXl763%2FceOJIdWHqX%2BHOJGXDV7nA2OfZ87GlMMWbkQhqd5UKvyISdDux79Ds6Pqeko3i5PW%2FtSyDre5m%2BH6kDjQtpXPzsTaR39LYGnGtzVkabBH%2BaT9yXNaPVG6ltI7Wu4u4fz8R9%2Bo7QyjcAvD8SqymkuSFllK5Is9NZ6dtDNlZ9EaLS9vDxybCChV6DtrnGXekj6dR2vtljFt9%2FxfZyDKuOkycxDTzjkQ%2BodEU0FNPu4DtsWByWQvGWpG2YMektz4DJo4XDvlNK3h1VDbAaTAbxwpiPvyJAOfpIGQ5E6tf08TOYgkuUHkXKrei2rLdm1ll1Hy9DvtmXV610i7LJRW212AJg7bWDiuD76Qfo12Z2lm1o0b73Jr%2BQK5mdXOd8zVFe%2BeK1vzLdSz6F1qr4S1sM4vWseM4vsYid2dF6ySJi9Zp0axLU9E6EWw4hgZO%2Br0sbnF9v%2FfR9TfKX%2BbndR893X1b%2FzIcL772m0g0K9rsM94YmG6gHZCiyMQUJK7wYh89W4d1LltNpQg69HskoHq0Khd3xR8BxJcdCIJo7ta3t7YDlzA%2Bdk3bc8hxFBiUNkG0tTSZz8NcgZwSO7GUsxkXt4L01NzFtSS7w0iP95PqxvgmNfVAEOyQT%2FrTQ45t7ltVz5g3YmF5fv4t4QOHqBb816R71ZcAZdfs3ennmFeJbnNNf%2B9F%2Fjnm2zBSZkGJLfOvygwRoODqGnd0dgLh9nVNM8Svj%2BT%2FBPZKa%2BCCiCHm6Sa8wX3tjNEQhuzw4iGLSc8CxqFgcztVtLudUsfuvkJkIApOcoPE4meRj5gdLXEw7mQMryClJ71%2FRPSyCUskEO7oQOszW4Uh%2BUzShHSEcm9arjywsQP%2BamNU6w9M%2FEbMhCAE%2BA%2BhB6SfAGYuGzh9E%2FlYtu4VzOv3UTl9WTEGnrtsjAl0gZNwLHOu9hFvYj%2FDIr02Rev1xqXzBRkouLNx4xXp45cvT9U8ZoF7QzOpmlIjFVkhm6bVS76MVZ5FRipxgNTkl91ZTtEzWSL49ssZRezDlIn8nsjK5RNxqYOX7PCRchWrunZJjkjvMq9TMLwXxJDFrNGubFqV%2Bw6UYnC6pmysOQl4JKxZLpm2rlizds29WZ82pEJdpPnCCsdW%2B0rTj6VAaHtMSKJxeVNRZFUKTYg0UGQlaze0WnQHq2KyWVW2APT6GsBmZL0tm6eXNA5s%2F9eTxkG9WahQPH9XYi1y1%2FFNZIaJlk01Bcz%2FCEpFlopxd2Zrxkp7CRYkVXA5GNHtsyKvvXW7C%2FLrKgryTrTBJur4I%2FxdZesxiV9Z3E8Q2K2%2BK6aXcBqqfS2oarf0OVDalwX7fCTINZP02VjWp14MVAtFWRh9qwLxKgcqd7QviOZYRJ%2BQvouipeXw8R%2Bu3Z8in7j5Dw%2FTKOa6tX3krmGZ76i2%2FjNDehE2OyKfGT4UbAV43a8MCTL2u69gd9%2Fd%2B96%2Fgl2TsHK5HPJI%2BOmZZJFeRmIbsxui6DwHCXm1y7vGU7IALi3kJcBdKxRuoq6qAKK8ihUZ%2BuZUbPF%2B6DkM3327%2Blbd0X27%2Bofenb77dnWtSpX%2F%2FMnwqh%2BvFi9LL2EXa4z7B6tWx%2F2l2pK3a4QBN8%2FOqMzofe6LTpI60NLf91Ly2EL0IeY65u2Fqaej3Pi0NLW3IkY%2FHdClLa9vmvVKAV2WG9Loh7MvjksoY2MgC3CzaN%2BR5gJk19Ton4jywlLQPq0%2B%2FVS8gPN2tfJsDxI0do6JqXHa9oe3WVr1FShKbn9jgSyLMgr5lI%2F6JLnYBb44Zz%2FHzPH6vzjCLD2HPgjhct9jGb4s9DEXBqJFaKiWMPo5DTki9GXr2bYgemX8lcTWksksJR%2FPGYtC5kkcvdp%2BWD4ig5Jc%2B0B8qkdkkUSQ%2Bb8%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E):
![image](https://github.com/user-attachments/assets/2893ec17-4b4e-4d46-8c2d-ede93ffad9f2)


- 

**ECS Detailed Technical Implementation**
- ECS concepts:
  * Task: A unit of execution in an ECS cluster that contains one or more containers.
  * Task definition: task blueprint (template):
  * Service: Responsible for creating task.
- Create separate task-definition for FE, BE and ML.  
- Create multi-task services to run containers across multiple Availability Zones to improve availability.
- Utilize ECS task-definition `revision` feature to roll-out and roll-back application deployment. We can chose `rolling update` or `blue/green` deployment strategy.
- Chose EC2 launch type for compute and cost optimization, or chose Fargate (serverless) launch type for more seamless deployment.
- Security practices: 
  * Implement Security Group (SG) to secure ECS on instance level.
  * Implement Network Access Control List (NACL) to secure ECS on network level (VPC and subnet).
  * Implement authentication on application level
- Automate infrastructure provisioning like network resources (VPC, subnetes, Security Group, etc.) and ECS cluster & ECS resources using Terraform.
 * ECS cluster: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_cluster
 * ECS service: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service.html


## 3. Hybrid Deployment
This architecture is required for farms with intermittent connectivity.

**Cloud environmet**<br>
We use the similar setup in cloud deployment (deployment strategy no.2)
- ECS to run FE, BE, and ML services
- RDS to run database
- Load Balancer to load balanced traffic between service.
- ECR to store container images
- CD tool to deploy container image from ECR to ECS cluster.

**Customer on-premise**<br>
For FE, BE and ML, the deployment strategy is the same as deployment startegy in On-Premise environment (deployment strategy no.2), using Docker Compose to automate the containers deployment, with some additional setup. We have to ensure that the data in on-premise and cloud is synchronized. We also have connectivity challange given the intermitten connection in the customer site.

**Connectivity Challenges:**
- Ensure the system operates completely offline when there is no internet connection.
- Implement a mechanism for data synchronization when the connection is restored.
- Implement a VPN to secure communcation between cloud infrastructure and on-premise infrastructure.

Add a sync service in `docker-compose.yml` file to handle data exchange with the cloud.
```
services:
  frontend:
  .....
  backend:
  .....
  ml_model:
  .....
  database:
  .....
  sync_service:
    image: sync-service-image
    environment:
      CLOUD_DB_URL: cloud-rds-endpoint
      LOCAL_DB_URL: postgres://user:password@database/dbname
    depends_on:
      - database
    networks:
      - internal

networks:
  internal:
    driver: bridge

volumes:
  db_data:
```

**Data Synchronization Strategy**
1. Sync Mechanism:
    - Use a scheduled sync process with retry logic to handle intermittent connections.
    - Sync only delta changes to minimize data transfer when the connection is restored.
2. Conflict Resolution:
    - Decide whether the cloud or on-premise database has higher priority in case of conflicting updates. This one can be decided based on customer data strategy. Let's assume the customer use the cloud database as the higher priority database. 
    - Use timestamps or a versioning system to handle conflicts.
3. Tools:
    - AWS Database Migration Service (DMS): We can set up bi-directional replication between RDS and the on-prem PostgreSQL database (if feasible with intermittent connectivity).
    - Custom Scripts: Use psql commands or Python libraries (e.g., psycopg2) to create a custom synchronization process.

This setup ensures the hybrid model can handle the intermittent internet challenges.


**Load Balancing between cloud on on-premise**<br>
Use AWS Route 53 or a third-party DNS service like Cloudflare with latency-based routing or geo-routing to distribute traffic.
How It Works:
- Route 53 directs users to the on-premise environment when they are in proximity and latency is low.
- If the on-premise setup is down or unreachable, Route 53 automatically routes users to ECS.
- Configure health checks for both ECS and the on-premise environment.
- Example Setup:
    - Create two DNS records (e.g., `app.unicorn.com`):
        - On-premise IP (A/AAAA record or load balancer address).
        - AWS ALB for ECS (A/AAAA record).
    - Use Route 53’s Failover Routing to prefer on-premise when healthy, and ECS as a fallback.

**Hybrid deployment strategy architecture diagram:** [Diagram](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%22lF_7-W5QHEBgdZ2kCPPr%22%3E7V1rd6M2E%2F41OWf7wRzu4I%2BOY%2B9uu9umm227fb%2FkYEwcGmxcwE7cX%2F9KIGEQAwZzMUlw9zRG5iKkmWcuGs1cSdP1y0fP2D5%2BdZeWcyXyy5cr6eZKFIWxxqM%2FuOVAWhSVtKw8e0najg139n8WaaSn7eyl5adODFzXCextutF0NxvLDFJthue5z%2BnTHlwn%2FdStsbIyDXem4WRb%2F7KXwWPUqiv8sf2TZa8e6ZMFnvyyNujJpMF%2FNJbuc6JJml1JU891g%2Bjb%2BmVqOXj06LhE181zfo075lmboMwFgfjj9%2FH9rfnvZPnbvf1y9%2FjrVhwpGulccKBvbC3RAJBD1wse3ZW7MZzZsfXac3ebpYVvy6Oj4zlfXHeLGgXU%2BI8VBAcym8YucFHTY7B2yK%2FxUODrH2zHmbqO66FjB4%2FkaGl4Tx8Cz9j45O3E6ZUo8eHnJ3RF9s3JYPjuzjOtgtcVVUJChrey6LWmMFk8L398%2FnQn%2F%2Fhof%2F2s7IORrEQn4sFIPIKM7EfLXVuBd0AneJZjBPY%2BTS0GIbpVfB65dOJ5xiFxwta1N4GfuPMtbkAnxAwkE%2Boh%2FKOxk8xewNe9QNbV5AXoS9RpepR4%2B2NTSGo5dAoNr0DIbm84OzJ0k7%2FuUMPENBFxBRmiJAOFvivX6B%2Fq8pS%2FUm4wZaAjTlSYBvZYSzcI2SN8j3QDe6ylGwT29gLzfIHtYKIhc5S6Pc88n090EP1DPLcLHHtjTWPQw4y08oyljViCMtPG3Vhpvnt%2BtAPrbmuEPPKMEBuzn7sJCKMKIj0mA4%2FvioA1MNCzPHKPcCYsb7a3ogmJznEcY%2Bvbi%2FgqzzJ3no%2F44pvlRzfnI77f4u%2FrlxUWF5zx7MvcCsHJNuz%2BZ%2FQs8Nd7g5AFukXguU8WfUUEC9MbUVRlBkfIq%2B8tL7ARlk8QruA7Bxifrg1y5FgP4R3ReNib1Zfw6EbiyRhAj1ga%2FmOMe7kohJ9qvVwVoQb5VR6neW8kUGZ8PsoagadnPSYEzZjKUQhrEsxbnTfHGda8ElUHj9QCfVkF4atHDXicUnyq%2Frtz6Q%2BjaOIn6ARB3r5El5Hf6Y2mOz9A3fbQsbHGc7NZ%2BNvEAxYePZNSAPkBvVn08HSHUHOikwyGoEkJ0vxAKcG0MEkDBLO2l8tQ5EGckxaDADkUIt9pIiFEIQEkIQIUIbVFEPj6shSBmGkDUoQZsROmBm%2B1%2BMCHMp2nfyKpzuMZGuHRHa2RJhmdTQYboJ0YmLAUXtl%2B%2BK4xHUQ9SfcOk1MnfbvAcHyIBOhs%2Bu2nE6NQyCT%2BkxWYj4SmQakLSl5I%2BoISOCuFU6eFchF4AtsItWnZRiF7GhWl2UaoDdIb2KsF4GqBuTpfajOyBv03x7yZEmeofXajYdMCEIAP4YeVThTJvhgLy7l1fTuwQ%2BG6cAOEuCdlY4yICbQ8pSkY%2FjZ6rQf7BfcDFveeFWnpkbBHioIPiX3L9FrBVCp4xZTclTSRU5QMzGp6FmVpW%2BMoK2VV4gzK%2Fnk7LcXEg7b8rrXl%2FdYUIaTQp%2FJ8Pm9VVZ5MrrVrvYSq3AwfS0JagVZUkI9VQF3ShNb0JUiDZsXss712jHDk%2FcDwKE1VGCyp%2BmApqbESAMVSFZXsSCmtmRq0B53YGrMp1o9MB5kcocFR3o6I2pb2HtInMxemzuujCRLTZ2nKGTFsJlzaJJEEgHAKheANpKAUzUPKR5lCM0Yzm8%2FVCaCZEVzNgLhjL4yFcW867m7JGY%2BGf29stw6acayg3T%2Biwbs39obtGAvbsYPDvW95exvPeXvTKzDTK8oyRwc0CQ4CN1YhII0xt848T3fSJ%2F23j08%2F%2Fz7Zfp%2Fc%2FCVKv1vUF9Gtd7riOCedzjCxkqFMOp3BtyWD25zPuR6PVTD7a4PzfIYvJ6R%2BIR%2BPh5Uv46iVAQCCaIUoaEIewwO6VXuMq8pcWqjroAIEORDbw2a5Q7q5Ppdu%2BiHTXyPJHaUAtZ4FhdO0rEbAA1Qnt0Z1aodU9%2FXLgFbVSUcWxpzCHz9CiopkWS9HQq0BlwxZI4NSeS5QaDqnCOPjR7%2B8jglPO6TnDNNeZ9rT3lVB5sbJDwkwuLBp0aW8%2BOIaS%2FQ7IgxjY1Z0PjCUCPoy2%2Fb8A55IiUuSmoNe8H5BXy9L1oquIAGd63RtkRoZnxewvq6OAcIT2wIbJZfsmtBFh9W7VFtvVu%2BmY1EBlLC3unrnLf1WFck0U0vjcVrAyBkeb2slD5Qs1JvWrdcKDbJ3%2BIGvR2qXShv%2BDhsEXaQNNy%2FkEdHRIXl0a3k2GoJw8eoMf3LSEVYkck8HX5IB7N4RBs%2FnoCA2KZJ5jVOkJLumJXTWe3UB5VCAfFjDlJ855aI8ZtyUwAJSu7P86b8fs933Pxd35sP4m2vc659H45F0CZxuGlQpw5xcXaD42BdUhTThgcUaY7HIwZJwt0ntspy7%2BAfPDHo7xzCtR9dZWl56700xOeiJ9yP0k6CEI9uxumxepE6CMOKpD6nEM8mlIksJdL5ZHV0NP1ltP%2Fqgdger6deG%2BbQK%2B8ncjwmiYVX3WKeP7uJ6aODYHkVxN99DiOGPDfiVKG3fGgGienxDNJK8jFrRjBmzpR2QF%2FfcwAiSDuOEtuehqTM2K8dKqIDXGzc0P8jpYe9ujeUyem5oMjiO%2Bzyhm6xI%2BBM2jhJPsV62xoayHRznZKE%2BkivyQqaMhe86u8CaxJMXn5kwcOubs%2BcYh%2Fn2K2zoQhYxeMtcs1ZMG6atgYpeQmyLMk9PSmJI7LmvgCDokIBIFTEC%2BfEGMXLmjCsCu6As6TzHJz%2B9cN6Kw1JNk%2F4UpDzw4muYdijsa3DavzGnvSwrZ%2BiyzXjxa2qxojxosYMWO2ixfdJiJWYNUNIALZa%2FpA4r6qe1maRnynIW7nPSKRU2oB8eXc%2F%2BD%2B9AcXDjZhlSNRYPjuH7tpnGE0TE%2B1j%2BpN1a6FJCoPpVeoOCHjKDHeCFhhFSEULgwA3RQoMkyuT4uM6ADw6JA3aVIblwcZVctrjqdsmiMJixuYQRCaqjSURSmy1IW7W8Epm0DiOBWSRTWGKOXp1cdqTn7J3G6RvJCnOjaGgyN6qa6kKXQS49Mw1FXW%2FUeJDjgxwf5Hif5Pg46%2BHunzsKDH4fHBPnqm66lF4rZgLPL%2B2kAFcV5ULdra3oD6KTER2KKGT0l%2FOUMSmtjnG82osokjgN3MkFz4uFkcz00V%2F%2F%2FCp%2B3%2B1%2BWd6LT0%2BjT7st7KnODf3LzRxS1n2VcYx9u7kr2gqTnywE6F0nHb4p3LpTsr8MK76vHRd04zZV3TWdk%2BUEnGbdaEUmSfPBsH0OwKD760%2BbiOOyJqJ4KTwq7PfgTH89zvTqSR9EZm93dpNVW%2FHvoBAUO6S5Kb7mRFo5nEv2QvtG%2B0PHposA1do67iFLuJoynoYR7fUIt3pqF0FPE66kxvZfkng1yNzT29LhpNPWXX8kmFBWgtG3SEqwIu5tOCluxhWosvkoWDgq67vUqYyjN6Lm%2BQnfZVNpbpUuRexNxME5kFcT3PJ6S%2FN1085I2X4dU2LV71ppa6ROh%2B21sbL8vvYOgcErGccw4VI%2Fu1YotM%2Ft6RsyNauL64ytCaWthbbzC03s5wellXoJ2UwdcfR75DqjTrmzHHE8zzji5HBBpS1HHKQ2FGkDJ%2B1e6rfo3u59%2Fvdv54%2F1Hy%2FfgtnN8vf%2FGfLq559HJVKHUS05lATp%2BYVV7pOaes6aXHIDaPiwCV0JALdkkv7cPAYBLn8xwQMhzs3lRuBsJGYfbES7HlLn1xiajMBAf3C7j8fJQIRgG87IdD0LHYsIFefhfUaCqHPbzao1aND4NDSMlCw0yAAyNJErBqwCIV%2Bk6MU5LvoaLFtE%2BydZVuoXy2qQ3VVTjxbz9OgojzbJN%2B%2FjW%2BF1Ygu7rxaH8NomNOra3RyhH%2F%2FwESvzjmX4YaiDZ%2B9tx1pZ0feNaW8d%2FP0BQY3I7%2FwwUzpe%2FkbT5jolEheV08MaeZPZBvUSJ1Piv84n1RXci%2FR0a%2Fj%2Bs%2Bvh8dy6jm0eetXPiDYiYr67%2By2mAwfzPvprktILJQydZheAikd3%2Bi2iVQw%2BG9M7bENJiug2CNHGT1aA6GS96gQxhEo609dooNPrbZfva5IgfvmK%2F49NSX5tbIyQIGbJV3iyDn5TvW%2FZLhtssDhUL641Ros%2F8VlNSxEAVUtsLcWzWMZleiJSlQ1OJZZRnPUiYWNVtYlipeyqnrkGzGkN5ytMD%2F2KMJWY2kWizpBQWSdt7CmgNyoZYNqUk1buMl%2Fp7Q53aHDR1uxwZAh3tG5XStJgriQBqm2Jm5JyI0ZcVm7ERTLJU66SdSghecJzokAvpW69RrCDdjFO4JS%2Bgfvw4Ft1eR22%2FJWLWP5n7nA4X6jQXKpJoQIPyMWSgsDduYzPtsfzI11qfgr73ais1HNkJTJYylini1xMTmVDrJS%2BLyfYgYmNCE%2B%2FydP8e5fQj93KkBMPInO7cOAL6LtCFIfChHGM4pqXlyq0pZSwSKqV56k6KCNG4x0JQGKNWC1ODoramp2m5GvBuYwM2u9V9MfKvq9nMhYYNxZhKe%2Fr0N9STvn%2BY2OPpq6H%2FRtfvkxDr83e9tzN2ipTWLT3dX2UPMUvnzuZsj7Z%2BKpuy%2FoAIfJDWeih0N1rLwvdELMyERaCBtZ6AZdSpfb8e6cVQhZ2Wbt7inecJZm8hGrXC8CN4aoC4AJRMZCgbw9i8xOQZzT4oZjzpYZjKOb8ptPBD8WcGwVVtt6I2mk1Z3gfeAm52OCigv%2FY60UFvrGQ6re0vluZ0EdMCSVe4uRkQS0xq1tAlY%2Bb2M8JBoReNKyuSsBtRR39tDuXvHlza7gduXOhmvO1XGGt%2BCXEsc4JgN4MJfpoz0HWJaJ%2FxuCFuKB%2FqD79nL%2Bt8nK92tpbC2tj54iYBteE37zMkqvvCxEzCYUBXoYK1LLxJM1xcr4JXDvyMkPM0a68yMPM3wWeEVirwxWNEfx0WHg29n3MQE80pA414kc%2F500KuL5sP%2FvmRa%2BsgMXONbpyE0fcJYkZ8pnHjvTG18yFMkKcGG8PjvVCQu3g%2FJChiD8nGA%2FapqRqV81sUyqphtHsCFUi5OA9abSxZpyLoDBBctK5WRgFDSn7IpP%2FTNNTWZFFJqNVc3FzIN2Viexsdx1V0ASWHYG6QrrK8XJ2jhtZSoUHpkRlm0oDUzz85YeLAS89O1hgcLDShMEIvoPURjhJbjoQsuGhY%2B317P66m9HWs9Y2Dttvo8fNJ%2BzCGQFTuX0gvaD8VoK3oUcXQ8Rp5s0vvQKKrvZQbSi00sR00kIrMscni6MzmS1l%2FsKZLeHXLKFpDiRQfj1fZquuiMysa72YdcjxNcx6g7Ou9pLZSxQlGKa9xrQLEo7f6R23d5myaj7Dl5PRrxHo%2FU5UwdirkPYDjBn4KOdebSLCCDbqoNpsbVHQ9UBB51CQrKRJJr0fS%2BR1Tkj%2BLJazPdojqS7rvg2gdB4o8UUkJQHpwLpFJUiLbYuEcObygYSqk1CmDKUMpIrqGHoqxMvWppu7w8YcKKc65cisBpSuJSVjhTmZ9x7Y5wI5vs8gqvJ1p%2BD8XFLiPYe6U0PdqaHu1Pl1p5oSS6LCjdORl5AzXj4a%2BA1XnqqLKcqAKQOmDJjSd0yRwO18PcYVdcCVAVcGXOkXrkCrSwCoHOGnZ6CiDaAygMoAKr0CFSZuUNIVTsvWEROE3moq%2BgAqA6gMoNIrUGEwBcgKBuYeaqOSNwga1Ba7dGm3wvFObomAly%2BIJzy5MxV%2BXYLcPUkEOdRRb5TZND3eA1EsxNuNOIKlc3Zmu8z5OeI5PqzMmti5pAlxQ72dS%2FWYl4Zcn8wSSrmlJ%2BVaWtkqnZcldLbBVQvC8ix%2B4HqJvNDHXbwf9kjCr62f6qyotp1MVJtMhJDs3lgy0Wjo20Q3NhO9pKkcFRfJ%2FC8ypwD7wMYS10QWGJAR5BJ7JoZaY81GAqgIzvP3VQgnQ63bqkQGyz4o2pYhEEoYKQAq0nQAvYjlfJbd6WTbazQ1c6TB4LfxTQPP3o1rPqGZ9verNpk4rkyev8SKF0iAWuVNhP7AYqwE976XydE4WTwylVZq6arz%2BSqxPemdzJckcTJ%2FnC%2Bd2TgOLAl0Plkltpe8j8kS0rylS5mtgJefrEFM0V%2BlMZfctqlpadUTcGM1N1k13eBqj9fWZqok84ARNbjBBzf4O3KDQ1pvTgCQIqrn%2BOTO8oWrZTKavDY7Vjxpxy7cl%2FDryHFXLm7A5a%2FmixdntAyFTWzNAi5jQRZkCOjmc16TznAWVlD%2BGHeIoIDaOZQZtInkEXAB5zM8glVSzJ6T928Buh3z05zU3t1x8kbgJRUzv1woAeMykebu0n3Bzn7sgsIu4cWh%2BhBmng2np4F7fRZJlRngCHEQTm1d%2F5zSh0OOnZPIKSFTjFcT2r3MAKkARuhCRVbHDSApvNSTdUrd7haOjfeNfb7Ntco6MMSM%2F3aehd9uYwXPrveElVhxHnXu%2FvPt%2FWS5RCThW35FG61ynjNJ4tng6hGw%2FZQqNWmlqq1pg3xTQ6azbjKdNd9jQuIDDLeSp5DJ%2Fp1dyus28xldNbxYUVJZZjKrJlKtthGfAKS9L5RFJ%2BMTqCjuSXCRPL7IhNJS83Fxgr8Tv%2BSUmm%2BzMm1hQeDTlWnFfs1plylCdhsbr21vIrfB%2BTElaZo64WLNndMqkdyMbwDpJSXjLltDV1pSuP%2FMWIqp4PWTkjxFAbUvPJXvtanNQlGBs2%2FuLrBwfRA%2BTIcfVgKcOwaOGuFvfs336vSOj8Sy8cvtaSn8a%2BGjCwg1qaxQu1ggZWG%2FuxVqjmuGlWdej1hT2bIMPRBrZ9TTrl4dCIEkhtFM4u1%2BoWVmesA9qd2iZVa03Xr23gisN%2BBHqzxDRx8mnSE6Ppfyl8Wl116TNJO0MWOnS2IzdnppQQds9ymk%2F%2BYEXXjpxPOMQ%2BIEwhLHO2fLmjCERwu45RVCQZcohVegL1EvjsTXQLETMFyt4XXBWKDODdtxQ0CP8B2XEbZxrQbTwC5S3n0IG7AQsPCjl%2B7zJjpr54dXmWFlB8M0EU6gL0Sgo%2FPWRnifBw%2FbreQW4U9ZhybkuSwUK72v3iRoGqsmyIAcghbGW4usgyys14F7NUBKzIIUHB3fCkYBVZpY6ZeZ79JlmniZQSeNCdFprigTOGRtGAx5O6%2Bm7nqNjIZoY2OohZpIc1mG7IS4SeQ%2Fff9%2Be1fHkMAzTwLk2lr8yJJxIZ%2ByYIOwNhWPd0UKwuWCEM%2BJmpgOGh0Rr09NMibJIxOCUU7fwn148K1WqK7ERon3i2KNr320jmIirzGkxFYAaxnF3mK4YTvb5s4wxkVW4wZiIzrdBNdGaMQ7k1l5ZFBZPAn6ONzgIGm6OtZUZqPXqImwJpAG2igEONBAKzQgNFGYGSSCEruMBtg%2F18PHs24ToPxnt3ufW1ixz61mfZLn%2F7z99R1zvCJjjtdVfiyr6pjXxyla0VqjAepruVholSLHHloaWtWxy5Z6YnscRAVPXZnyz8m9oDkZQ3JyMCWm62RAIsJqWZKjKLkMMjsM8GdYsW4WFTAXDJsKZb9fcvvtpiFHJltWHIw%2BKCxsXm3HmOdiMD1aePiVvrpLjHaz%2FwM%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
![image](https://github.com/user-attachments/assets/3641a612-962d-4769-8820-8829d181eae6)<br>


**Hybrid DNS Setup for Failover**<br>
Setup a local DNS server to resolve on-premise private IP for failover when internet down in customer site.<br>
![image](https://github.com/user-attachments/assets/0e08ddfa-1955-45ca-8b05-078acffe7e79)<br><br>



## Reference:
 * [1] https://aws.amazon.com/eks/pricing/
 * [2] https://aws.amazon.com/ecs/sla/
 * [3] https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html
 * [4] https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.Enabling
