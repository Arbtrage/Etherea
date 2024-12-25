```mermaid


```


// Diagram elements
Users [icon: users] {
  Next.js Frontend [icon: react]
}

Frontend [icon: aws-s3] {
  Hosted on CloudFront [icon: aws-cloudfront]
}

Backend [icon: aws-ec2] {
  FastAPI Service [icon: python]
  
  Data Aggregation [icon: rss] {
    NewsAPI [icon: globe]
    Google News RSS [icon: rss]
    Custom Scrapers [icon: code]
  }
  
  Summarization [icon: brain] {
    Hugging Face Transformers [icon: huggingface]
  }
  
  Task Queue [icon: queue] {
    Redis [icon: redis]
    Celery [icon: celery]
  }
  
  Database [icon: database] {
    PostgreSQL [icon: aws-rds]
  }
  
  Storage [icon: aws-s3] {
    Raw Articles [icon: file-text]
  }
  
  Email Service [icon: aws-ses]
}

Monitoring [icon: monitor] {
  CloudWatch [icon: aws-cloudwatch]
  Prometheus [icon: prometheus]
  Grafana [icon: grafana]
}

// Connections
Next.js Frontend > Hosted on CloudFront
Next.js Frontend > FastAPI Service: REST API

FastAPI Service > Data Aggregation

FastAPI Service > Summarization

FastAPI Service > Task Queue

FastAPI Service > Database

FastAPI Service > Storage

FastAPI Service > Email Service
Email Service > Users: send summaries

Monitoring > Task Queue
FastAPI Service < Monitoring
Email Service < Monitoring
